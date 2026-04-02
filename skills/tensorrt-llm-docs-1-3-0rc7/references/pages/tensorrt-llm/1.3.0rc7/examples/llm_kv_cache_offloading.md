# KV Cache Offloading — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/examples/llm_kv_cache_offloading.html

KV Cache Offloading#

Source NVIDIA/TensorRT-LLM.

```text
  1'''
  2This script demonstrates the effectiveness of KV cache host offloading in TensorRT-LLM.
  3
  4**Scenario:**
  5The script simulates a scenario where the GPU's KV cache is severely limited,
  6while multiple requests with recurring prompts (like system prompts) are processed.
  7
  81.  **Constrained GPU Cache:** The GPU KV cache is configured to be very small,
  9    only large enough to hold the state for a single request.
 102.  **Alternating Prompts:** Four requests are sent sequentially (batch size of 1)
 11    with two distinct prompts in an A, B, A, B pattern.
 123.  **Cache Eviction:** Due to the small GPU cache, processing prompt B will
 13    force the eviction of the cache generated for prompt A.
 14
 15**Demonstration:**
 16
 17* **Without Offloading (Default):**
 18    - When the first prompt 'A' is processed, its KV cache is stored on the GPU.
 19    - When prompt 'B' arrives, the cache manager needs space and discards the cache for 'A'.
 20    - When prompt 'A' is sent again, its cache must be recomputed from scratch.
 21    - **Expected Outcome:** The log will show `reused blocks: 0` and `cache hit rate: 0`.
 22
 23* **With Offloading (`--enable_offloading`):**
 24    - When prompt 'B' arrives, the cache for 'A' is not discarded but is instead
 25      *offloaded* from the fast GPU VRAM to the slower (but larger) host CPU RAM.
 26    - When prompt 'A' is sent again, its KV cache is loaded back from host RAM
 27      to the GPU, which is significantly faster than recomputing it.
 28    - **Expected Outcome:** The log will show positive values for `reused blocks`
 29      and a non-zero `cache hit rate`, confirming that the cache was successfully
 30      reused from the host.
 31
 32**How to Run & Verify:**
 33
 341.  **Without Offloading:**
 35    ```bash
 36    TLLM_LOG_LEVEL=DEBUG python llm_kv_cache_offloading.py 2>&1 | tee offloading_disabled.log
 37    ```
 38    (Check the log for zero reuse)
 39
 402.  **With Offloading:**
 41    ```bash
 42    TLLM_LOG_LEVEL=DEBUG python llm_kv_cache_offloading.py --enable_offloading 2>&1 | tee offloading_enabled.log
 43    ```
 44    (Check the log for non-zero reuse)
 45'''
 46
 47import argparse
 48
 49from tensorrt_llm import LLM, SamplingParams
 50from tensorrt_llm.llmapi import KvCacheConfig
 51
 52
 53def main(args):
 54    # Define two distinct prompts to simulate different requests or system prompts.
 55    prompt_a = (
 56        "Returns the per-iterations statistics computed since last call to this method. "
 57        "Contains at most iter_stats_max_iterations iterations.")
 58    prompt_b = ("Use for skipping decoding step for non generation model, "
 59                "and return the batch_output (such as mm_embeddings)")
 60
 61    # Use a batch size of 1 to process requests sequentially, making the cache
 62    # eviction and reuse cycle easy to observe.
 63    max_batch_size = 1
 64    max_seq_len = 256
 65
 66    # --- KV Cache Configuration ---
 67    # Set a small GPU KV cache size (in number of tokens). This is crucial for the demo,
 68    # as it's only large enough to hold the KV cache for a single request.
 69    kv_cache_max_tokens = 256
 70    # Define the size of a single cache block.
 71    kv_cache_page_size = 16
 72    # Enable a 1 GB host cache if offloading is requested, otherwise disable it (size 0).
 73    # This is the key toggle for the experiment.
 74    kv_cache_host_size = 1024**3 if args.enable_offloading else 0
 75
 76    sampling_params = SamplingParams(max_tokens=max_seq_len)
 77
 78    llm = LLM(
 79        model="Qwen/Qwen3-8B",
 80        max_batch_size=max_batch_size,
 81        max_seq_len=max_seq_len,
 82        kv_cache_config=KvCacheConfig(
 83            enable_block_reuse=True,  # Enable reuse of cached blocks
 84            max_tokens=kv_cache_max_tokens,  # Max tokens in GPU cache
 85            tokens_per_block=kv_cache_page_size,
 86            host_cache_size=kv_cache_host_size  # Host cache size for offloading
 87        ))
 88
 89    # Process four requests sequentially using two distinct prompts (A, B, A, B).
 90    # This pattern is designed to showcase the cache eviction and reuse behavior.
 91    print("--- First Round ---")
 92    # 1. Process prompt A. Its cache is stored on the GPU.
 93    output_a = llm.generate(prompt_a, sampling_params)
 94    print(
 95        f"Prompt: {output_a.prompt!r}, Generated text: {output_a.outputs[0].text!r}"
 96    )
 97    # 2. Process prompt B. Its cache replaces/offloads A's cache.
 98    output_b = llm.generate(prompt_b, sampling_params)
 99    print(
100        f"Prompt: {output_b.prompt!r}, Generated text: {output_b.outputs[0].text!r}"
101    )
102
103    print("\n--- Second Round ---")
104    # 3. Process prompt A again.
105    #    - Without offloading: Must recompute from scratch.
106    #    - With offloading: Recovers cache from host RAM.
107    output_a = llm.generate(prompt_a, sampling_params)
108    print(
109        f"Prompt: {output_a.prompt!r}, Generated text: {output_a.outputs[0].text!r}"
110    )
111    # 4. Process prompt B again.
112    #    - Without offloading: Must recompute from scratch.
113    #    - With offloading: Recovers cache from host RAM.
114    output_b = llm.generate(prompt_b, sampling_params)
115    print(
116        f"Prompt: {output_b.prompt!r}, Generated text: {output_b.outputs[0].text!r}"
117    )
118
119    llm.shutdown()
120
121
122if __name__ == "__main__":
123    parser = argparse.ArgumentParser(
124        description=
125        "A script to demonstrate the effectiveness of KV cache host offloading."
126    )
127    parser.add_argument('--enable_offloading',
128                        action='store_true',
129                        help='Enable host RAM for KV cache offloading.')
130    args = parser.parse_args()
131    main(args)
```
