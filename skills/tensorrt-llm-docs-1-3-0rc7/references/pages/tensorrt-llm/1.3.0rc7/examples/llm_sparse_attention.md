# Sparse Attention — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/examples/llm_sparse_attention.html

Sparse Attention#

Source NVIDIA/TensorRT-LLM.

```text
  1"""
  2This example demonstrates how to use sparse attention with TensorRT-LLM.
  3
  4Supported sparse attention algorithms:
  5- RocketKV
  6- DSA
  7
  8Usage:
  9```bash
 10python llm_sparse_attention.py --algo ROCKETKV --attention_backend TRTLLM --window_size 32 --kernel_size 63 --prompt_budget 2048
 11```
 12"""
 13import argparse
 14import json
 15
 16from tensorrt_llm import LLM, SamplingParams
 17from tensorrt_llm.llmapi import (CudaGraphConfig, DeepSeekSparseAttentionConfig,
 18                                 KvCacheConfig, MoeConfig,
 19                                 RocketSparseAttentionConfig)
 20
 21
 22def read_input(input_file):
 23    results = []
 24    with open(input_file, 'r') as f:
 25        for line in f:
 26            ret = json.loads(line)
 27            results.append(ret)
 28    return results
 29
 30
 31def parse_arguments():
 32    parser = argparse.ArgumentParser()
 33    parser.add_argument(
 34        '--model_path',
 35        type=str,
 36        default=
 37        "/home/scratch.trt_llm_data_ci/llm-models/llama-3.1-model/Llama-3.1-8B-Instruct"
 38    )
 39    parser.add_argument(
 40        '--input_file',
 41        type=str,
 42        default="tests/unittest/_torch/multi_gpu/NIAH_simple_data.jsonl")
 43
 44    # Build config
 45    parser.add_argument('--algo',
 46                        type=str,
 47                        default='ROCKETKV',
 48                        choices=['ROCKETKV', 'DSA'])
 49    parser.add_argument('--attention_backend',
 50                        type=str,
 51                        default='TRTLLM',
 52                        choices=['VANILLA', 'TRTLLM'])
 53
 54    # RocketKV config
 55    parser.add_argument('--window_size',
 56                        type=int,
 57                        default=32,
 58                        help="The window size for RocketKV.")
 59    parser.add_argument('--kernel_size',
 60                        type=int,
 61                        default=63,
 62                        help="The kernel size for RocketKV.")
 63    parser.add_argument('--prompt_budget',
 64                        type=int,
 65                        default=2048,
 66                        help="The prompt budget for RocketKV.")
 67    parser.add_argument('--topk',
 68                        type=int,
 69                        default=64,
 70                        help='Top-k for RocketKV')
 71    parser.add_argument('--kt_cache_dtype',
 72                        type=str,
 73                        default='float8_e5m2',
 74                        choices=['bfloat16', 'float8_e5m2'])
 75    parser.add_argument('--index_max_chunk_size',
 76                        type=int,
 77                        default=32768,
 78                        help="The maximum chunk size for the indexer.")
 79    parser.add_argument("--max_seq_len",
 80                        type=int,
 81                        default=10240,
 82                        help="The maximum sequence length.")
 83    parser.add_argument("--max_batch_size",
 84                        type=int,
 85                        default=256,
 86                        help="The maximum batch size.")
 87    parser.add_argument("--max_new_tokens",
 88                        type=int,
 89                        default=128,
 90                        help="The maximum new tokens.")
 91    parser.add_argument(
 92        "--max_num_tokens",
 93        type=int,
 94        default=81920,
 95        help=
 96        "The maximum total tokens (context + generation) across all sequences in a batch."
 97    )
 98
 99    # Parallelism
100    parser.add_argument('--moe_backend',
101                        type=str,
102                        default='CUTLASS',
103                        choices=[
104                            'CUTLASS', 'TRTLLM', 'VANILLA', 'WIDEEP',
105                            'DEEPGEMM', 'CUTEDSL', 'TRITON'
106                        ])
107    parser.add_argument('--tp_size', type=int, default=1)
108    parser.add_argument('--moe_ep_size', type=int, default=-1)
109    parser.add_argument('--enable_attention_dp',
110                        default=False,
111                        action='store_true')
112
113    # KV cache
114    parser.add_argument('--kv_cache_dtype', type=str, default='auto')
115    parser.add_argument("--kv_cache_fraction", type=float, default=0.7)
116    parser.add_argument('--tokens_per_block', type=int, default=32)
117    parser.add_argument('--num_samples', type=int, default=10)
118
119    # Runtime
120    parser.add_argument('--print_iter_log',
121                        default=False,
122                        action='store_true',
123                        help='Print iteration logs during execution')
124    parser.add_argument('--use_cuda_graph', default=False, action='store_true')
125    parser.add_argument('--cuda_graph_padding_enabled',
126                        default=False,
127                        action='store_true')
128    parser.add_argument('--cuda_graph_batch_sizes',
129                        nargs='+',
130                        type=int,
131                        default=None)
132    parser.add_argument('--enable_chunked_prefill',
133                        default=False,
134                        action='store_true',
135                        help='Enable chunked prefill')
136    args = parser.parse_args()
137    return args
138
139
140def run_llm(args, sparse_attention_config):
141    data = read_input(args.input_file)
142    num_samples = args.num_samples if args.num_samples is not None else len(
143        data)
144    data = data[:num_samples]
145
146    kv_cache_config = KvCacheConfig(
147        enable_block_reuse=
148        False,  # sparse attention does not support kv cache reuse now
149        free_gpu_memory_fraction=args.kv_cache_fraction,
150        tokens_per_block=args.tokens_per_block,
151        dtype=args.kv_cache_dtype,
152    )
153
154    cuda_graph_config = CudaGraphConfig(
155        batch_sizes=args.cuda_graph_batch_sizes,
156        enable_padding=args.cuda_graph_padding_enabled,
157    ) if args.use_cuda_graph else None
158
159    llm = LLM(
160        model=args.model_path,
161        backend='pytorch',
162        kv_cache_config=kv_cache_config,
163        attn_backend=args.attention_backend,
164        sparse_attention_config=sparse_attention_config,
165        max_batch_size=args.max_batch_size,
166        max_seq_len=args.max_seq_len,
167        max_num_tokens=args.max_num_tokens,
168        tensor_parallel_size=args.tp_size,
169        moe_expert_parallel_size=args.moe_ep_size,
170        enable_attention_dp=args.enable_attention_dp,
171        cuda_graph_config=cuda_graph_config,
172        print_iter_log=args.print_iter_log,
173        enable_iter_perf_stats=args.print_iter_log,
174        moe_config=MoeConfig(backend=args.moe_backend),
175        enable_chunked_prefill=args.enable_chunked_prefill,
176    )
177
178    prompts = []
179    reference = []
180    for sample in data:
181        prompts.append(
182            {'prompt': sample['input_context'] + sample['input_query']})
183        reference.append(sample['outputs'])
184
185    sampling_params = SamplingParams(add_special_tokens=False,
186                                     max_tokens=args.max_new_tokens,
187                                     temperature=0.8,
188                                     top_p=0.95)
189
190    outputs = llm.generate(prompts, sampling_params)
191    for idx, output in enumerate(outputs):
192        print(
193            f'Generated text: {output.outputs[0].text!r}, ref: {reference[idx]}'
194        )
195
196
197def run_RocketKV(args):
198    sparse_attention_config = RocketSparseAttentionConfig(
199        window_size=args.window_size,
200        kernel_size=args.kernel_size,
201        prompt_budget=args.prompt_budget,
202        topk=args.topk,
203        kt_cache_dtype=args.kt_cache_dtype,
204    )
205    run_llm(args, sparse_attention_config)
206
207
208def run_DSA(args):
209    sparse_attention_config = DeepSeekSparseAttentionConfig(
210        indexer_max_chunk_size=args.index_max_chunk_size, )
211    run_llm(args, sparse_attention_config)
212
213
214def main():
215    args = parse_arguments()
216    if args.algo == 'ROCKETKV':
217        run_RocketKV(args)
218    elif args.algo == 'DSA':
219        run_DSA(args)
220    else:
221        raise ValueError(f"Invalid algorithm: {args.algo}")
222
223
224if __name__ == "__main__":
225    main()
```
