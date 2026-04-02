# Runtime Configuration Examples — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/examples/llm_runtime.html

Runtime Configuration Examples#

Source NVIDIA/TensorRT-LLM.

```text
  1'''
  2This script demonstrates various runtime configuration options in TensorRT-LLM,
  3including KV cache management and CUDA graph optimizations.
  4
  5**KV Cache Configuration:**
  6
  7The KV cache (key-value cache) stores attention keys and values during inference,
  8which is crucial for efficient autoregressive generation. Proper KV cache configuration helps with:
  9
 101. **Memory Management**: Control GPU memory allocation for the key-value cache through
 11   `free_gpu_memory_fraction`, balancing memory between model weights and cache storage.
 12
 132. **Block Reuse Optimization**: Enable `enable_block_reuse` to optimize memory usage
 14   for shared prefixes across multiple requests, improving throughput for common prompts.
 15
 163. **Performance Tuning**: Configure cache block sizes and total capacity to match
 17   your workload characteristics (batch size, sequence length, and request patterns).
 18
 19Please refer to the `KvCacheConfig` API reference for more details.
 20
 21**CUDA Graph Configuration:**
 22
 23CUDA graphs help reduce kernel launch overhead and improve GPU utilization by capturing
 24and replaying GPU operations. Benefits include:
 25
 26- Reduced kernel launch overhead for repeated operations
 27- Better GPU utilization through optimized execution
 28- Improved throughput for inference workloads
 29
 30Please refer to the `CudaGraphConfig` API reference for more details.
 31
 32**How to Run:**
 33
 34Run all examples:
 35```bash
 36python llm_runtime.py
 37```
 38
 39Run specific example:
 40```bash
 41python llm_runtime.py --example kv_cache
 42python llm_runtime.py --example cuda_graph
 43```
 44'''
 45
 46import argparse
 47
 48from tensorrt_llm import LLM, SamplingParams
 49from tensorrt_llm.llmapi import CudaGraphConfig, KvCacheConfig
 50
 51
 52def example_cuda_graph_config():
 53    """
 54    Example demonstrating CUDA graph configuration for performance optimization.
 55
 56    CUDA graphs help with:
 57    - Reduced kernel launch overhead
 58    - Better GPU utilization
 59    - Improved throughput for repeated operations
 60    """
 61    print("\n=== CUDA Graph Configuration Example ===")
 62
 63    cuda_graph_config = CudaGraphConfig(
 64        batch_sizes=[1, 2, 4],
 65        enable_padding=True,
 66    )
 67
 68    llm = LLM(
 69        model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
 70        cuda_graph_config=cuda_graph_config,  # Enable CUDA graphs
 71        max_batch_size=4,
 72        max_seq_len=512,
 73        kv_cache_config=KvCacheConfig(free_gpu_memory_fraction=0.5))
 74
 75    prompts = [
 76        "Hello, my name is",
 77        "The capital of France is",
 78        "The future of AI is",
 79    ]
 80
 81    sampling_params = SamplingParams(max_tokens=50, temperature=0.8, top_p=0.95)
 82
 83    # This should benefit from CUDA graphs
 84    outputs = llm.generate(prompts, sampling_params)
 85    for output in outputs:
 86        print(f"Prompt: {output.prompt}")
 87        print(f"Generated: {output.outputs[0].text}")
 88        print()
 89
 90
 91def example_kv_cache_config():
 92    """Example demonstrating KV cache configuration for memory management and performance."""
 93    print("\n=== KV Cache Configuration Example ===")
 94    print("\n1. KV Cache Configuration:")
 95
 96    llm_advanced = LLM(
 97        model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
 98        max_batch_size=8,
 99        max_seq_len=1024,
100        kv_cache_config=KvCacheConfig(
101            # free_gpu_memory_fraction: the fraction of free GPU memory to allocate to the KV cache
102            free_gpu_memory_fraction=0.5,
103            # enable_block_reuse: whether to enable block reuse
104            enable_block_reuse=True))
105
106    prompts = [
107        "Hello, my name is",
108        "The capital of France is",
109        "The future of AI is",
110    ]
111
112    outputs = llm_advanced.generate(prompts)
113    for i, output in enumerate(outputs):
114        print(f"Query {i+1}: {output.prompt}")
115        print(f"Answer: {output.outputs[0].text[:100]}...")
116        print()
117
118
119def main():
120    """
121    Main function to run all runtime configuration examples.
122    """
123    parser = argparse.ArgumentParser(
124        description="Runtime Configuration Examples")
125    parser.add_argument("--example",
126                        type=str,
127                        choices=["kv_cache", "cuda_graph", "all"],
128                        default="all",
129                        help="Which example to run")
130
131    args = parser.parse_args()
132
133    if args.example == "kv_cache" or args.example == "all":
134        example_kv_cache_config()
135
136    if args.example == "cuda_graph" or args.example == "all":
137        example_cuda_graph_config()
138
139
140if __name__ == "__main__":
141    main()
```
