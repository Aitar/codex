# Benchmarking with trtllm-bench — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/features/auto_deploy/advanced/benchmarking_with_trtllm_bench.html

Benchmarking with trtllm-bench#

AutoDeploy is integrated with the `trtllm-bench` performance benchmarking utility, enabling you to measure comprehensive performance metrics such as token throughput, request throughput, and latency for your AutoDeploy-optimized models.

Getting Started#

Before benchmarking with AutoDeploy, review the TensorRT LLM benchmarking guide to familiarize yourself with the standard trtllm-bench workflow and best practices.

Basic Usage#

Invoke the AutoDeploy backend by specifying `--backend_autodeploy` in your `trtllm-bench` command:

```text
trtllm-bench \
  --model meta-llama/Llama-3.1-8B \
  throughput \
  --dataset /tmp/synthetic_128_128.txt \
  --backend _autodeploy
```

Note

As in the PyTorch workflow, AutoDeploy does not require a separate `trtllm-benchbuild` step. The model is automatically optimized during benchmark initialization.

Advanced Configuration#

For more granular control over AutoDeploy’s behavior during benchmarking, use the `--config` flag with a YAML configuration file:

Note

Non-breaking: `--config<file.yaml>` is the preferred flag for passing a YAML configuration file.
Existing workflows using `--extra_llm_api_options<file.yaml>` continue to work; it is an equivalent alias.

```text
trtllm-bench \
  --model meta-llama/Llama-3.1-8B \
  throughput \
  --dataset /tmp/synthetic_128_128.txt \
  --backend _autodeploy \
  --config autodeploy_config.yaml
```

Configuration Examples#

Basic Performance Configuration (`autodeploy_config.yaml`)#

```text
# runtime engine
runtime: trtllm

# model loading
skip_loading_weights: false

# Sequence configuration
max_batch_size: 256

# transform options
# KV cache configuration
kv_cache_config:
  # fraction of free memory to use for kv-caches
  free_gpu_memory_fraction: 0.8

# transform options
transforms:
  insert_cached_attention:
    # attention backend
    backend: flashinfer
  compile_model:
    # compilation backend
    backend: torch-opt
    # CUDA Graph optimization
    cuda_graph_batch_sizes: [1, 2, 4, 8, 16, 32, 64, 128, 256]
```

Enable multi-GPU execution by specifying `--tpn`, where `n` is the number of GPUs.

Configuration Options Reference#

Core Performance Settings#

| Parameter | Default | Description |
| --- | --- | --- |
| `compile_backend` | `torch-compile` | Compilation backend: `torch-simple`, `torch-compile`, `torch-cudagraph`, `torch-opt` |
| `runtime` | `trtllm` | Runtime engine: `trtllm`, `demollm` |
| `kv_cache_config.free_gpu_memory_fraction` | `0.9` | Fraction of available GPU memory for KV cache (0.0-1.0) |
| `skip_loading_weights` | `false` | Skip weight loading for architecture-only benchmarks |

CUDA Graph Optimization#

| Parameter | Default | Description |
| --- | --- | --- |
| `cuda_graph_batch_sizes` | `null` | List of batch sizes for CUDA graph creation |

Tip

For optimal CUDA graph performance, specify batch sizes that match your expected workload patterns. For example: `[1,2,4,8,16,32,64,128]`

Performance Optimization Tips#

Memory Management: Set `kv_cache_config.free_gpu_memory_fraction` to 0.8-0.9 for optimal KV cache utilization

Compilation Backend: Use `torch-opt` for production workloads

Attention Backend: `flashinfer` generally provides the best performance for most models

CUDA Graphs: Enable CUDA graphs for batch sizes that match your production traffic patterns.
