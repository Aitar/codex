# Welcome to LMDeploy’s tutorials! — lmdeploy

Source: https://lmdeploy.readthedocs.io/en/latest/

Welcome to LMDeploy’s tutorials!

Welcome to LMDeploy’s tutorials!#

LMDeploy is a toolkit for compressing, deploying, and serving LLM.

StarWatchFork

LMDeploy has the following core features:

Efficient Inference: LMDeploy delivers up to 1.8x higher request throughput than vLLM, by introducing key features like persistent batch(a.k.a. continuous batching), blocked KV cache, dynamic split&fuse, tensor parallelism, high-performance CUDA kernels and so on.

Effective Quantization: LMDeploy supports weight-only and k/v quantization, and the 4-bit inference performance is 2.4x higher than FP16. The quantization quality has been confirmed via OpenCompass evaluation.

Effortless Distribution Server: Leveraging the request distribution service, LMDeploy facilitates an easy and efficient deployment of multi-model services across multiple machines and cards.

Excellent Compatibility: LMDeploy supports KV Cache Quant, AWQ and Automatic Prefix Caching to be used simultaneously.

Documentation#

Indices and tables#

Search Page

HTTP Routing Table
