# AutoDeploy (Beta) — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/features/auto_deploy/auto-deploy.html

AutoDeploy (Beta)#

Note

This project is under active development and is currently released as beta feature. The code is
subject to change, and may include backward-incompatible updates.

Seamless Model Deployment from PyTorch to TensorRT LLM#

AutoDeploy is designed to simplify and accelerate the deployment of PyTorch models, including off-the-shelf models such as those from the Hugging Face Transformers library, to TensorRT LLM.

AutoDeploy overview and relation with TensorRT LLM’s LLM API

AutoDeploy provides an alternative method for deploying models using the LLM API without requiring code changes to the source model (for example, Hugging Face Transformers models) or manual implementation of inference optimizations, such as KV-caches, multi-GPU parallelism, or quantization. Instead, AutoDeploy extracts a computation graph from the source model and applies inference optimizations through a series of automated graph transformations. AutoDeploy generates an inference-optimized graph that can be directly executed in the TensorRT LLM PyTorch runtime and leverages various runtime optimizations including in-flight batching, paging, and overlap scheduling.

Key Features#

Seamless Model Translation: Automatically converts PyTorch/Hugging Face models to TensorRT LLM without manual rewrites.

Unified Model Definition: Maintain a single source of truth with your original PyTorch/Hugging Face model.

Optimized Inference: Built-in transformations for sharding, quantization, KV-cache integration, MHA fusion, and CudaGraph optimization.

Immediate Deployment: Day-0 support for models with continuous performance enhancements.

Quick Setup & Prototyping: Lightweight pip package for easy installation with a demo environment for fast testing.

Get Started#

Install AutoDeploy:

AutoDeploy is included with the TRT-LLM installation.

```text
sudo apt-get -y install libopenmpi-dev && pip3 install --upgrade pip setuptools && pip3 install tensorrt_llm
```

You can refer to TRT-LLM installation guide for more information.

Run Llama Example:

You are now ready to run an in-framework Llama Demo.

The general entry point for running the AutoDeploy demo is the `build_and_run_ad.py` script. Checkpoints are loaded directly from Huggingface (HF) or a local HF-like directory:

```text
cd examples/auto_deploy
python build_and_run_ad.py --model "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
```

Support Matrix#

AutoDeploy streamlines the model deployment process through an automated workflow designed for efficiency and performance. The workflow begins with a PyTorch model, which is exported using `torch.export` to generate a standard Torch graph. This graph contains core PyTorch ATen operations alongside custom attention operations, determined by the attention backend specified in the configuration.

The exported graph then undergoes a series of automated transformations, including graph sharding, KV-cache insertion, and GEMM fusion, to optimize model performance. After these transformations, the graph is compiled using one of the supported compile backends (like `torch-opt`), followed by deploying it via the TensorRT LLM runtime.

Support Matrix

Advanced Usage#

Example Run Script

Logging Level

Incorporating AutoDeploy into Your Own Workflow

Expert Configurations

Performance Benchmarking

KV Cache Architecture

Export ONNX for EdgeLLM

Testing Strategy

Roadmap#

We are actively expanding AutoDeploy to support a broader range of model architectures and inference features.

Upcoming Model Support:

Vision-Language Models (VLMs)

Structured State Space Models (SSMs) and Linear Attention architectures

Planned Features:

Low-Rank Adaptation (LoRA)

Speculative Decoding for accelerated generation

To track development progress and contribute, visit our Github Project Board.
We welcome community contributions, see `examples/auto_deploy/CONTRIBUTING.md` for guidelines.
