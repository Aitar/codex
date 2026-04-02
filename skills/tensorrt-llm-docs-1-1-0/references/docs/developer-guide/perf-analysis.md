Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/developer-guide/perf-analysis.md

* Performance Analysis

# Performance Analysis[#](#performance-analysis "Link to this heading")

NVIDIA Nsight Systems reports at the application level are highly informative. Metric sampling capabilities have increased over generations and provide a clean middle-ground between timing analysis and kernel-level deep dives with NVIDIA Nsight Compute.

Given the potential long runtimes of Large Languages Models (LLMs) and the diversity of workloads a model may experience during a single inference pass or binary execution, NVIDIA has added features to TensorRT LLM to get the most out of Nsight Systems capabilities. This document outlines those features as well as provides examples of how to best utilize them to understand your application.

## Feature Descriptions[#](#feature-descriptions "Link to this heading")

The main functionality:

* Relies on toggling the CUDA profiler runtime API on and off.
* (PyTorch workflow only) Toggling the PyTorch profiler on and off.
* Provides a means to understand which regions a user may want to focus on.

Toggling the CUDA profiler runtime API on and off:

* Allows users to know specifically what the profiled region corresponds to.
* Results in smaller files to post-process (for metric extraction or similar).

(PyTorch workflow only) Toggling the PyTorch profiler on and off:

* Help users to analysis the performance breakdown in the model.
* Results in smaller files to post-process (for metric extraction or similar).

## Coordinating with NVIDIA Nsight Systems Launch[#](#coordinating-with-nvidia-nsight-systems-launch "Link to this heading")

Consult the Nsight Systems User Guide for full overview of options.

On the PyTorch workflow, basic NVTX markers are by default provided. On the C++/TensorRT workflow, append `--nvtx` when calling `scripts/build_wheel.py` script to compile, and clean build the code.

### Only collect specific iterations[#](#only-collect-specific-iterations "Link to this heading")

To reduce the Nsight Systems profile size, and ensure that only specific iterations are collected, set environment variable `TLLM_PROFILE_START_STOP=A-B`, and append `-c cudaProfilerApi` to `nsys profile` command.

### Enable more NVTX markers for debugging[#](#enable-more-nvtx-markers-for-debugging "Link to this heading")

Set environment variable `TLLM_NVTX_DEBUG=1`.

### Enable garbage collection (GC) NVTX markers[#](#enable-garbage-collection-gc-nvtx-markers "Link to this heading")

Set environment variable `TLLM_PROFILE_RECORD_GC=1`.

### Enable GIL information in NVTX markers[#](#enable-gil-information-in-nvtx-markers "Link to this heading")

Append “python-gil” to Nsys “-t” option.

## Coordinating with PyTorch profiler (PyTorch workflow only)[#](#coordinating-with-pytorch-profiler-pytorch-workflow-only "Link to this heading")

### Collect PyTorch profiler results[#](#collect-pytorch-profiler-results "Link to this heading")

1. Set environment variable `TLLM_PROFILE_START_STOP=A-B` to specify the range of the iterations to be collected.
2. Set environment variable `TLLM_TORCH_PROFILE_TRACE=<path>`, and the results will be saved to `<path>`.

### Visualize the PyTorch profiler results[#](#visualize-the-pytorch-profiler-results "Link to this heading")

Use [chrome://tracing/](#chrome://tracing/) to inspect the saved profile.

## Examples[#](#examples "Link to this heading")

Consult the Nsight Systems User Guide for full overview of MPI-related options.

### Profiling specific iterations on a `trtllm-bench`/`trtllm-serve` run[#](#profiling-specific-iterations-on-a-trtllm-bench-trtllm-serve-run "Link to this heading")

Say we want to profile iterations 100 to 150 on a `trtllm-bench`/`trtllm-serve` run, we want to collect as much information as possible for debugging, such as GIL, debugging NVTX markers, etc:

```
#!/bin/bash

# Prepare dataset for the benchmark
python3 benchmarks/cpp/prepare_dataset.py \
    --tokenizer=${MODEL_PATH} \
    --stdout token-norm-dist --num-requests=${NUM_SAMPLES} \
    --input-mean=1000 --output-mean=1000 --input-stdev=0 --output-stdev=0 > /tmp/dataset.txt

# Benchmark and profile
TLLM_PROFILE_START_STOP=100-150 nsys profile \
  -o trace -f true \
  -t 'cuda,nvtx,python-gil' -c cudaProfilerApi \
  --cuda-graph-trace node \
  -e TLLM_PROFILE_RECORD_GC=1,TLLM_LLMAPI_ENABLE_NVTX=1,TLLM_TORCH_PROFILE_TRACE=trace.json \
  --trace-fork-before-exec=true \
  trtllm-bench \ # or trtllm-serve command
    --model deepseek-ai/DeepSeek-V3 \
    --model_path ${MODEL_PATH} \
    throughput \
    --dataset /tmp/dataset.txt --warmup 0 \
    --backend pytorch \
    --streaming
```

The Nsight Systems reports will be saved to `trace.nsys-rep`. Use NVIDIA Nsight Systems application to open it.

The PyTorch profiler results will be saved to `trace.json`. Use [chrome://tracing/](#chrome://tracing/) to inspect the saved profile.

[previous

Architecture Overview](overview.md "previous page")
[next

TensorRT LLM Benchmarking](perf-benchmarking.md "next page")

On this page

* [Feature Descriptions](#feature-descriptions)
* [Coordinating with NVIDIA Nsight Systems Launch](#coordinating-with-nvidia-nsight-systems-launch)
  + [Only collect specific iterations](#only-collect-specific-iterations)
  + [Enable more NVTX markers for debugging](#enable-more-nvtx-markers-for-debugging)
  + [Enable garbage collection (GC) NVTX markers](#enable-garbage-collection-gc-nvtx-markers)
  + [Enable GIL information in NVTX markers](#enable-gil-information-in-nvtx-markers)
* [Coordinating with PyTorch profiler (PyTorch workflow only)](#coordinating-with-pytorch-profiler-pytorch-workflow-only)
  + [Collect PyTorch profiler results](#collect-pytorch-profiler-results)
  + [Visualize the PyTorch profiler results](#visualize-the-pytorch-profiler-results)
* [Examples](#examples)
  + [Profiling specific iterations on a `trtllm-bench`/`trtllm-serve` run](#profiling-specific-iterations-on-a-trtllm-bench-trtllm-serve-run)