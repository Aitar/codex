Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/features/auto_deploy/advanced/benchmarking_with_trtllm_bench.md

* Benchmarking with trtllm-bench

# Benchmarking with trtllm-bench[#](#benchmarking-with-trtllm-bench "Link to this heading")

AutoDeploy is integrated with the `trtllm-bench` performance benchmarking utility, enabling you to measure comprehensive performance metrics such as token throughput, request throughput, and latency for your AutoDeploy-optimized models.

## Getting Started[#](#getting-started "Link to this heading")

Before benchmarking with AutoDeploy, review the [TensorRT LLM benchmarking guide](#../../performance/perf-benchmarking.md#running-with-the-pytorch-workflow) to familiarize yourself with the standard trtllm-bench workflow and best practices.

## Basic Usage[#](#basic-usage "Link to this heading")

Invoke the AutoDeploy backend by specifying `--backend _autodeploy` in your `trtllm-bench` command:

```
trtllm-bench \
  --model meta-llama/Llama-3.1-8B \
  throughput \
  --dataset /tmp/synthetic_128_128.txt \
  --backend _autodeploy
```

Note

As in the PyTorch workflow, AutoDeploy does not require a separate `trtllm-bench build` step. The model is automatically optimized during benchmark initialization.

## Advanced Configuration[#](#advanced-configuration "Link to this heading")

For more granular control over AutoDeploy’s behavior during benchmarking, use the `--extra_llm_api_options` flag with a YAML configuration file:

```
trtllm-bench \
  --model meta-llama/Llama-3.1-8B \
  throughput \
  --dataset /tmp/synthetic_128_128.txt \
  --backend _autodeploy \
  --extra_llm_api_options autodeploy_config.yaml
```

### Configuration Examples[#](#configuration-examples "Link to this heading")

#### Basic Performance Configuration (`autodeploy_config.yaml`)[#](#basic-performance-configuration-autodeploy-config-yaml "Link to this heading")

```
# Compilation backend
compile_backend: torch-opt

# Runtime engine
runtime: trtllm

# Model loading
skip_loading_weights: false

# Fraction of free memory to use for kv-caches
free_mem_ratio: 0.8

# CUDA Graph optimization
cuda_graph_batch_sizes: [1, 2, 4, 8, 16, 32, 64, 128, 256]

# Attention backend
attn_backend: flashinfer

# Sequence configuration
max_batch_size: 256
```

Enable multi-GPU execution by specifying `--tp n`, where `n` is the number of GPUs

## Configuration Options Reference[#](#configuration-options-reference "Link to this heading")

### Core Performance Settings[#](#core-performance-settings "Link to this heading")

| Parameter | Default | Description |
| --- | --- | --- |
| `compile_backend` | `torch-compile` | Compilation backend: `torch-simple`, `torch-compile`, `torch-cudagraph`, `torch-opt` |
| `runtime` | `trtllm` | Runtime engine: `trtllm`, `demollm` |
| `free_mem_ratio` | `0.0` | Fraction of available GPU memory for KV cache (0.0-1.0) |
| `skip_loading_weights` | `false` | Skip weight loading for architecture-only benchmarks |

### CUDA Graph Optimization[#](#cuda-graph-optimization "Link to this heading")

| Parameter | Default | Description |
| --- | --- | --- |
| `cuda_graph_batch_sizes` | `null` | List of batch sizes for CUDA graph creation |

Tip

For optimal CUDA graph performance, specify batch sizes that match your expected workload patterns. For example: `[1, 2, 4, 8, 16, 32, 64, 128]`

## Performance Optimization Tips[#](#performance-optimization-tips "Link to this heading")

1. **Memory Management**: Set `free_mem_ratio` to 0.8-0.9 for optimal KV cache utilization
2. **Compilation Backend**: Use `torch-opt` for production workloads
3. **Attention Backend**: `flashinfer` generally provides the best performance for most models
4. **CUDA Graphs**: Enable CUDA graphs for batch sizes that match your production traffic patterns.

On this page

* [Getting Started](#getting-started)
* [Basic Usage](#basic-usage)
* [Advanced Configuration](#advanced-configuration)
  + [Configuration Examples](#configuration-examples)
    - [Basic Performance Configuration (`autodeploy_config.yaml`)](#basic-performance-configuration-autodeploy-config-yaml)
* [Configuration Options Reference](#configuration-options-reference)
  + [Core Performance Settings](#core-performance-settings)
  + [CUDA Graph Optimization](#cuda-graph-optimization)
* [Performance Optimization Tips](#performance-optimization-tips)