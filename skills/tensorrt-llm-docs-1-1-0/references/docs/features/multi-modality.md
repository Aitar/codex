Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/features/multi-modality.md

* Multimodal Support in TensorRT LLM

# Multimodal Support in TensorRT LLM[#](#multimodal-support-in-tensorrt-llm "Link to this heading")

TensorRT LLM supports a variety of multimodal models, enabling efficient inference with inputs beyond just text.

---

## Background[#](#background "Link to this heading")

Multimodal LLMs typically handle non-text inputs by combining a multimodal encoder with an LLM decoder. The encoder first transforms non-text modality input into embeddings, which are then fused with text embeddings and fed into the LLM decoder for downstream inference. Compared to standard LLM inference, multimodal LLM inference involves three additional stages to support non-text modalities.

* **Multimodal Input Processor**: Preprocess raw multimodal input into a format suitable for the multimodal encoder, such as pixel values for vision models.
* **Multimodal Encoder**: Encodes the processed input into embeddings that are aligned with the LLM’s embedding space.
* **Integration with LLM Decoder**: Fuses multimodal embeddings with text embeddings as the input to the LLM decoder.

## Optimizations[#](#optimizations "Link to this heading")

TensorRT LLM incorporates some key optimizations to enhance the performance of multimodal inference:

* **In-Flight Batching**: Batches multimodal requests within the GPU executor to improve GPU utilization and throughput.
* **CPU/GPU Concurrency**: Asynchronously overlaps data preprocessing on the CPU with image encoding on the GPU.
* **Raw data hashing**: Leverages image hashes and token chunk information to improve KV cache reuse and minimize collisions.

Further optimizations are under development and will be updated as they become available.

## Model Support Matrix[#](#model-support-matrix "Link to this heading")

Please refer to the latest multimodal [support matrix](../models/supported-models.md#multimodal-feature-support-matrix-pytorch-backend).

## Examples[#](#examples "Link to this heading")

The following examples demonstrate how to use TensorRT LLM’s multimodal support in various scenarios, including quick run examples, serving endpoints, and performance benchmarking.

### Quick start[#](#quick-start "Link to this heading")

Quickly try out TensorRT LLM’s multimodal support using our `LLM-API` and a ready-to-run [example](https://github.com/NVIDIA/TensorRT-LLM/tree/48b7b5d/examples/llm-api/quickstart_multimodal.py):

```
python3 quickstart_multimodal.py --model_dir Efficient-Large-Model/NVILA-8B --modality image
```

### OpenAI-Compatible Server via [`trtllm-serve`](../commands/trtllm-serve/trtllm-serve.md)[#](#openai-compatible-server-via-trtllm-serve "Link to this heading")

Launch an OpenAI-compatible server with multimodal support using the `trtllm-serve` command, for example:

```
trtllm-serve Qwen/Qwen2-VL-7B-Instruct  --backend pytorch
```

You can then send OpenAI-compatible requests, such as via curl or API clients, to the server endpoint. See [curl chat client for multimodal script](https://github.com/NVIDIA/TensorRT-LLM/tree/48b7b5d/examples/serve/curl_chat_client_for_multimodal.sh) as an example.

### Run with [`trtllm-bench`](../commands/trtllm-bench.md)[#](#run-with-trtllm-bench "Link to this heading")

Evaluate offline inference performance with multimodal inputs using the `trtllm-bench` tool. For detailed instructions, see the [benchmarking guide](#../../source/performance/perf-benchmarking.md).

[previous

LoRA (Low-Rank Adaptation)](lora.md "previous page")
[next

Overlap Scheduler](overlap-scheduler.md "next page")

On this page

* [Background](#background)
* [Optimizations](#optimizations)
* [Model Support Matrix](#model-support-matrix)
* [Examples](#examples)
  + [Quick start](#quick-start)
  + [OpenAI-Compatible Server via `trtllm-serve`](#openai-compatible-server-via-trtllm-serve)
  + [Run with `trtllm-bench`](#run-with-trtllm-bench)