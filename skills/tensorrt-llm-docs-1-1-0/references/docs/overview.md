Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/overview.md

* Overview

# Overview[#](#overview "Link to this heading")

## About TensorRT LLM[#](#about-tensorrt-llm "Link to this heading")

[TensorRT LLM](https://developer.nvidia.com/tensorrt) is NVIDIA’s comprehensive open-source library for accelerating and optimizing inference performance of the latest large language models (LLMs) on NVIDIA GPUs.

## Key Capabilities[#](#key-capabilities "Link to this heading")

### 🔥 **Architected on Pytorch**[#](#architected-on-pytorch "Link to this heading")

TensorRT LLM provides a high-level Python [LLM API](quick-start-guide.md#run-offline-inference-with-llm-api) that supports a wide range of inference setups - from single-GPU to multi-GPU or multi-node deployments. It includes built-in support for various parallelism strategies and advanced features. The LLM API integrates seamlessly with the broader inference ecosystem, including NVIDIA [Dynamo](https://github.com/ai-dynamo/dynamo) and the [Triton Inference Server](https://github.com/triton-inference-server/server).

TensorRT LLM is designed to be modular and easy to modify. Its PyTorch-native architecture allows developers to experiment with the runtime or extend functionality. Several popular models are also pre-defined and can be customized using [native PyTorch code](https://github.com/NVIDIA/TensorRT-LLM/tree/48b7b5d/tensorrt_llm/_torch/models/modeling_deepseekv3.py), making it easy to adapt the system to specific needs.

### ⚡ **State-of-the-Art Performance**[#](#state-of-the-art-performance "Link to this heading")

TensorRT LLM delivers breakthrough performance on the latest NVIDIA GPUs:

* **DeepSeek R1**: [World-record inference performance on Blackwell GPUs](https://developer.nvidia.com/blog/nvidia-blackwell-delivers-world-record-deepseek-r1-inference-performance/)
* **Llama 4 Maverick**: [Breaks the 1,000 TPS/User Barrier on B200 GPUs](https://developer.nvidia.com/blog/blackwell-breaks-the-1000-tps-user-barrier-with-metas-llama-4-maverick/)

### 🎯 **Comprehensive Model Support**[#](#comprehensive-model-support "Link to this heading")

TensorRT LLM supports the latest and most popular LLM [architectures](https://nvidia.github.io/TensorRT-LLM/models/supported-models.md).

### FP4 Support[#](#fp4-support "Link to this heading")

[NVIDIA B200 GPUs](https://www.nvidia.com/en-us/data-center/dgx-b200/) , when used with TensorRT LLM, enable seamless loading of model weights in the new [FP4 format](https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/#what_is_nvfp4), allowing you to automatically leverage optimized FP4 kernels for efficient and accurate low-precision inference.

### FP8 Support[#](#fp8-support "Link to this heading")

TensorRT LLM strives to support the most popular models on **Day 0**.

### 🚀 **Advanced Optimization & Production Features**[#](#advanced-optimization-production-features "Link to this heading")

* **[In-Flight Batching & Paged Attention](features/paged-attention-ifb-scheduler.md)**: In-flight batching eliminates wait times by dynamically managing request execution, processing context and generation phases together for maximum GPU utilization and reduced latency.
* **[Multi-GPU Multi-Node Inference](features/parallel-strategy.md)**: Seamless distributed inference with tensor, pipeline, and expert parallelism across multiple GPUs and nodes through the Model Definition API.
* **[Advanced Quantization](features/quantization.md)**:

  + **FP4 Quantization**: Native support on NVIDIA B200 GPUs with optimized FP4 kernels
  + **FP8 Quantization**: Automatic conversion on NVIDIA H100 GPUs leveraging Hopper architecture
* **[Speculative Decoding](features/speculative-decoding.md)**: Multiple algorithms including EAGLE, MTP and NGram
* **[KV Cache Management](features/kvcache.md)**: Paged KV cache with intelligent block reuse and memory optimization
* **[Chunked Prefill](features/paged-attention-ifb-scheduler.m d)**: Efficient handling of long sequences by splitting context into manageable chunks
* **[LoRA Support](features/lora.md)**: Multi-adapter support with HuggingFace and NeMo formats, efficient fine-tuning and adaptation
* **[Checkpoint Loading](features/checkpoint-loading.md)**: Flexible model loading from various formats (HuggingFace, NeMo, custom)
* **[Guided Decoding](features/guided-decoding.md)**: Advanced sampling with stop words, bad words, and custom constraints
* **[Disaggregated Serving (Beta)](features/disagg-serving.md)**: Separate context and generation phases across different GPUs for optimal resource utilization

### 🔧 **Latest GPU Architecture Support**[#](#latest-gpu-architecture-support "Link to this heading")

TensorRT LLM supports the full spectrum of NVIDIA GPU architectures:

* **NVIDIA Blackwell**: B200, B300, GB200, GB300, RTX Pro 6000 SE with FP4 optimization
* **NVIDIA Hopper**: H100, H200, GH200 with FP8 acceleration
* **NVIDIA Ada Lovelace**: L40/L40S, RTX 40 series with FP8 acceleration
* **NVIDIA Ampere**: A100, RTX 30 series for production workloads

## What Can You Do With TensorRT LLM?[#](#what-can-you-do-with-tensorrt-llm "Link to this heading")

Whether you’re building the next generation of AI applications, optimizing existing LLM deployments, or exploring the frontiers of large language model technology, TensorRT LLM provides the tools, performance, and flexibility you need to succeed in the era of generative AI.To get started, refer to the [Quick Start Guide](quick-start-guide.md#quick-start-guide).