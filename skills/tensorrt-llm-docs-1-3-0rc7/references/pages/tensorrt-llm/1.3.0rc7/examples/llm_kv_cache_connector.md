# KV Cache Connector — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/examples/llm_kv_cache_connector.html

KV Cache Connector#

Source NVIDIA/TensorRT-LLM.

```text
  1'''
  2This script demonstrates the KV cache connector feature in TensorRT-LLM, which enables
  3custom persistence and reuse of KV cache blocks across different LLM instances.
  4
  5**Scenario:**
  6The script implements a persistent KV cache connector that saves computed KV cache blocks
  7to disk and loads them back in subsequent runs, eliminating redundant computation for
  8recurring prompts.
  9
 10**What is a KV Cache Connector?**
 11
 12A KV cache connector is a customizable interface that allows you to:
 131.  **Save KV Cache:** Persist computed KV cache blocks to an external storage
 14    (disk, database, distributed cache, etc.)
 152.  **Load KV Cache:** Retrieve previously computed cache blocks instead of recomputing them
 163.  **Share Cache Across Instances:** Reuse cache blocks across different LLM instances
 17    or sessions, unlike regular block reuse which is limited to a single instance
 18
 19**How It Works:**
 20
 21This example implements a `PersistentKvCacheConnector` with two key components:
 22
 23* **PersistentKvCacheConnectorLeader (Scheduler):**
 24    - Hashes token sequences to create unique identifiers for each cache block
 25    - Checks if cached blocks exist on disk for incoming requests
 26    - Schedules load operations for cache hits
 27    - Schedules save operations for newly computed blocks
 28
 29* **PersistentKvCacheConnectorWorker:**
 30    - Executes the actual load/save operations between GPU and disk
 31    - Loads cached blocks from disk files into GPU memory
 32    - Saves newly computed blocks from GPU to disk files
 33
 34**Demonstration:**
 35
 36The script processes the same prompt twice using two separate LLM instances:
 37
 381.  **First Run (Instance 1):**
 39    - The LLM computes the KV cache for the input prompt
 40    - The connector saves the computed cache blocks to disk (as .pt files)
 41    - The generation completes and the LLM instance is destroyed
 42
 432.  **Second Run (Instance 2):**
 44    - A new LLM instance is created with the same connector configuration
 45    - When processing the same prompt, the connector finds matching cache blocks on disk
 46    - The cache is loaded from disk instead of being recomputed
 47    - **Expected Outcome:** Faster prefill as cache blocks are loaded rather than computed
 48    - Both outputs should be identical, demonstrating deterministic cache reuse
 49
 50**Key Benefits:**
 51
 52- **Cross-Instance Cache Sharing:** Share computed caches across multiple LLM instances
 53- **Persistent Storage:** Cache survives beyond the lifetime of a single LLM instance
 54- **Custom Storage Backends:** Implement any storage mechanism (shown here: disk files)
 55- **Reduced Computation:** Eliminate redundant KV cache computation for repeated prompts
 56
 57**How to Run:**
 58
 59```bash
 60python llm_kv_cache_connector.py <model_path>
 61```
 62
 63Example:
 64```bash
 65python llm_kv_cache_connector.py meta-llama/Llama-3.1-8B-Instruct
 66```
 67
 68**Implementation Notes:**
 69
 70- This example uses content-based hashing to identify cache blocks
 71- Cache files are stored in a temporary directory (cleaned up after the demo)
 72- The implementation is simplified and not optimized for production use
 73- Does not support chunked prefill in this example
 74- See `tensorrt_llm/_torch/pyexecutor/kv_cache_connector.py` for the full connector interface
 75
 76**NOTE:** This example connector implementation is designed for demonstration purposes
 77and is NOT suitable for production use without additional optimizations and error handling.
 78'''
 79
 80import os
 81import sys
 82from dataclasses import dataclass, field
 83from pathlib import Path
 84from tempfile import TemporaryDirectory
 85
 86import click
 87import torch
 88
 89from tensorrt_llm import LLM, SamplingParams, logger
 90from tensorrt_llm._torch.pyexecutor.kv_cache_connector import (
 91    KvCacheConnectorScheduler, KvCacheConnectorWorker, SchedulerOutput)
 92from tensorrt_llm.bindings.internal.batch_manager import LlmRequest
 93from tensorrt_llm.llmapi.llm_args import KvCacheConnectorConfig, TorchLlmArgs
 94
 95CONNECTOR_CACHE_FOLDER_KEY = "CONNECTOR_CACHE_FOLDER"
 96
 97
 98@dataclass
 99class PersistentKvCacheConnectorMetadata:
100    load: list[tuple[str, int]] = field(default_factory=list)
101    save: list[tuple[str, int]] = field(default_factory=list)
102
103
104class PersistentKvCacheConnectorWorker(KvCacheConnectorWorker):
105
106    def __init__(self, llm_args: TorchLlmArgs):
107        super().__init__(llm_args)
108
109        self.kv_cache_tensor = None
110
111    def register_kv_caches(self, kv_cache_tensor: torch.Tensor):
112        assert self.kv_cache_tensor is None, "KV cache tensor already registered"
113        self.kv_cache_tensor = kv_cache_tensor
114
115    def start_load_kv(self, stream: torch.cuda.Stream):
116        # Do all loads synchronously, and blockwise.
117        for path, block_id in self._metadata.load:
118            cpu_tensor = torch.load(path, map_location="cpu")
119
120            # Copy into the device block.
121            self.kv_cache_tensor[block_id].copy_(cpu_tensor, non_blocking=False)
122
123    def wait_for_layer_load(self, layer_idx: int, stream: torch.cuda.Stream):
124        pass
125
126    def save_kv_layer(self, layer_idx: int, stream: torch.cuda.Stream):
127        pass
128
129    def wait_for_save(self, stream: torch.cuda.Stream):
130
131        # Make sure the forward pass is complete before beginning our save.
132        stream.synchronize()
133
134        for path, block_id in self._metadata.save:
135            cpu_tensor = self.kv_cache_tensor[block_id].cpu()
136
137            # Don't write anything if this specific block already exists.
138            if Path(path).exists():
139                continue
140
141            # Do a blocking save to the file. This way, we only return once all saves are complete.
142            torch.save(cpu_tensor, path)
143
144    def get_finished(
145            self, finished_gen_req_ids: list[int],
146            started_loading_req_ids: list[int]) -> tuple[list[int], list[int]]:
147
148        return [], []
149
150
151class PersistentKvCacheConnectorLeader(KvCacheConnectorScheduler):
152
153    def __init__(self, llm_args: TorchLlmArgs):
154        super().__init__(llm_args)
155
156        self.block_size = self._llm_args.kv_cache_config.tokens_per_block
157        self.pending_loads = {}
158
159        self.cache_folder = os.environ.get(CONNECTOR_CACHE_FOLDER_KEY,
160                                           "./connector_cache")
161
162        os.makedirs(self.cache_folder, exist_ok=True)
163
164    def build_connector_meta(self, scheduler_output: SchedulerOutput):
165        # NOTE: This is a simplified implementation, and does not work with chunked prefill.
166
167        metadata = PersistentKvCacheConnectorMetadata()
168
169        for req in scheduler_output.new_requests:
170            # If we don't have any pending loads for this request, we can skip it.
171            if req.request_id not in self.pending_loads:
172                continue
173
174            num_computed_blocks = req.computed_position // self.block_size
175            block_ids = req.new_block_ids
176
177            pending_load = self.pending_loads[req.request_id]
178
179            for file_path, block_pos in zip(
180                    pending_load, range(num_computed_blocks, len(block_ids))):
181                metadata.load.append((file_path, block_ids[block_pos]))
182
183            # Break up the remainder of the token sequence into chunks.
184            chunks = self._chunk_tokens(req.new_tokens)
185
186            # For each chunk that isn't already on device, and isn't in our connector cache, we need to save it.
187            for block_pos in range(num_computed_blocks + len(pending_load),
188                                   len(block_ids)):
189                if len(chunks[block_pos]) == self.block_size:
190                    hashed_tokens = self._hash_tokens(chunks[block_pos])
191
192                    file_path = self._file_path(hashed_tokens)
193
194                    metadata.save.append((file_path, block_ids[block_pos]))
195
196        self.pending_loads = {}
197
198        return metadata
199
200    def _hash_tokens(self, tokens: list[int]) -> int:
201        return abs(hash(tuple(tokens)))
202
203    def _file_path(self, hash_value: int) -> Path:
204        return Path(self.cache_folder) / f"{hash_value}.pt"
205
206    def _chunk_tokens(self, tokens: list[int]) -> list[list[int]]:
207        return [
208            tokens[i:i + self.block_size]
209            for i in range(0, len(tokens), self.block_size)
210        ]
211
212    def get_num_new_matched_tokens(
213            self, request: LlmRequest,
214            num_computed_tokens: int) -> tuple[int, bool]:
215        self.pending_loads[request.request_id] = []
216
217        # Don't bother with sequences with partial matches.
218        if (num_computed_tokens % self.block_size) != 0:
219            return 0, False
220
221        computed_blocks = num_computed_tokens // self.block_size
222
223        # Get all the tokens that don't have a cache hit on device.
224        remaining_tokens = request.get_tokens(0)[computed_blocks *
225                                                 self.block_size:]
226
227        remaining_chunks = self._chunk_tokens(remaining_tokens)
228
229        # For each chunk, check if it exists in our cache.
230        for chunk in remaining_chunks:
231            # Only do full blocks.
232            if len(chunk) == self.block_size:
233                hashed_tokens = self._hash_tokens(chunk)
234
235                file_path = self._file_path(hashed_tokens)
236
237                # If we get a cache hit, we want to load it into device.
238                # Otherwise, we can stop looking.
239                if file_path.exists():
240                    self.pending_loads[request.request_id].append(file_path)
241                else:
242                    break
243
244        logger.info(
245            f"KV CONNECTOR: Matched {len(self.pending_loads[request.request_id])} blocks for request {request.request_id}"
246        )
247
248        return len(
249            self.pending_loads[request.request_id]) * self.block_size, False
250
251    def request_finished(self, request: LlmRequest,
252                         cache_block_ids: list[int]) -> bool:
253        # We don't do any asynchronous saving, so always return False
254        return False
255
256    def update_state_after_alloc(self, request: LlmRequest,
257                                 block_ids: list[int]):
258        pass
259
260
261@click.command()
262@click.argument("model", type=str)
263def main(model: str):
264    sys.path.append(os.path.join(
265        os.path.dirname(__file__),
266        "..",
267    ))
268
269    this_module = __file__[__file__.rfind("/") + 1:__file__.rfind(".py")]
270
271    # --- KV Cache Connector Config ---
272    kv_connector_config = KvCacheConnectorConfig(
273        connector_module=this_module,
274        connector_scheduler_class="PersistentKvCacheConnectorLeader",
275        connector_worker_class="PersistentKvCacheConnectorWorker",
276    )
277
278    connector_cache_dir = TemporaryDirectory()
279    os.environ[CONNECTOR_CACHE_FOLDER_KEY] = connector_cache_dir.name
280
281    # Create LLM instance with KV Cache Connector
282    llm = LLM(model=model,
283              backend="pytorch",
284              cuda_graph_config=None,
285              kv_connector_config=kv_connector_config)
286
287    test_text = (
288        "Nvidia Corporation is an American technology company headquartered in Santa Clara, California."
289        "Founded in 1993 by Jensen Huang, Chris Malachowsky, and Curtis Priem, it develops graphics processing units (GPUs), "
290        "system on a chips (SoCs), and application programming interfaces (APIs) for data science, high-performance computing, "
291        "and mobile and automotive applications. Tell me about the company.")
292
293    sampling_params = SamplingParams(max_tokens=32)
294
295    # Generate text with the first LLM instance and save the kv cache blocks by the connector.
296    output = llm.generate([test_text], sampling_params)
297    text0 = output[0].outputs[0].text
298
299    print("First output: ", text0)
300    print("Loading new LLM instance...")
301
302    del llm
303
304    # Create a new LLM instance with the same connector configuration
305    llm = LLM(model=model,
306              backend="pytorch",
307              cuda_graph_config=None,
308              kv_connector_config=kv_connector_config)
309
310    # Generate text with the second LLM instance and it should reuse the kv cache blocks from the connector.
311    output = llm.generate([test_text], sampling_params)
312    text1 = output[0].outputs[0].text
313
314    print("Second output (using connector cache): ", text1)
315
316    # Verify that the two outputs are identical
317    assert text0 == text1
318
319    connector_cache_dir.cleanup()
320
321
322if __name__ == "__main__":
323    main()
```
