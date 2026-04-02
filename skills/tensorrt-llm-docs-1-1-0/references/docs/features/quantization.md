Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/features/quantization.md

* Quantization

# Quantization[#](#quantization "Link to this heading")

## Quantization in TensorRT LLM[#](#quantization-in-tensorrt-llm "Link to this heading")

Quantization is a technique used to reduce memory footprint and computational cost by converting the model’s weights and/or activations from high-precision floating-point numbers (like BF16) to lower-precision data types, such as INT8, FP8, or FP4.

TensorRT LLM offers a variety of quantization recipes to optimize LLM inference. These recipes can be broadly categorized as follows:

* FP4
* FP8 Per Tensor
* FP8 Block Scaling
* FP8 Rowwise
* FP8 KV Cache
* W4A16 GPTQ
* W4A8 GPTQ
* W4A16 AWQ
* W4A8 AWQ

## Usage[#](#usage "Link to this heading")

The default PyTorch backend supports FP4 and FP8 quantization on the latest Blackwell and Hopper GPUs.

### Running Pre-quantized Models[#](#running-pre-quantized-models "Link to this heading")

TensorRT LLM can directly run [pre-quantized models](https://huggingface.co/collections/nvidia/model-optimizer-66aa84f7966b3150262481a4) generated with the [NVIDIA Model Optimizer](https://github.com/NVIDIA/Model-Optimizer).

```
from tensorrt_llm import LLM
llm = LLM(model='nvidia/Llama-3.1-8B-Instruct-FP8')
llm.generate("Hello, my name is")
```

#### FP8 KV Cache[#](#fp8-kv-cache "Link to this heading")

Note

TensorRT LLM allows you to enable the FP8 KV cache manually, even for checkpoints that do not have it enabled by default.

Here is an example of how to set the FP8 KV Cache option:

```
from tensorrt_llm import LLM
from tensorrt_llm.llmapi import KvCacheConfig
llm = LLM(model='/path/to/model',
          kv_cache_config=KvCacheConfig(dtype='fp8'))
llm.generate("Hello, my name is")
```

### Offline Quantization with ModelOpt[#](#offline-quantization-with-modelopt "Link to this heading")

If a pre-quantized model is not available on the [Hugging Face Hub](https://huggingface.co/collections/nvidia/model-optimizer-66aa84f7966b3150262481a4), you can quantize it offline using ModelOpt.

Follow this step-by-step guide to quantize a model:

```
git clone https://github.com/NVIDIA/TensorRT-Model-Optimizer.git
cd TensorRT-Model-Optimizer/examples/llm_ptq
scripts/huggingface_example.sh --model <huggingface_model_card> --quant fp8 --export_fmt hf
```

## Model Supported Matrix[#](#model-supported-matrix "Link to this heading")

| Model | NVFP4 | MXFP4 | FP8(per tensor) | FP8(block scaling) | FP8(rowwise) | FP8 KV Cache | W4A8 AWQ | W4A16 AWQ | W4A8 GPTQ | W4A16 GPTQ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BERT | . | . | . | . | . | Y | . | . | . | . |
| DeepSeek-R1 | Y | . | . | Y | . | Y | . | . | . | . |
| EXAONE | . | . | Y | . | . | Y | Y | Y | . | . |
| Gemma 3 | . | . | Y | . | . | Y | Y | Y | . | . |
| GPT-OSS | . | Y | . | . | . | Y | . | . | . | . |
| LLaMA | Y | . | Y | . | . | Y | . | Y | . | Y |
| LLaMA-v2 | Y | . | Y | . | . | Y | Y | Y | . | Y |
| LLaMA 3 | . | . | . | . | Y | Y | Y | . | . | . |
| LLaMA 4 | Y | . | Y | . | . | Y | . | . | . | . |
| Mistral | . | . | Y | . | . | Y | . | Y | . | . |
| Mixtral | Y | . | Y | . | . | Y | . | . | . | . |
| Phi | . | . | . | . | . | Y | Y | . | . | . |
| Qwen | . | . | . | . | . | Y | Y | Y | . | Y |
| Qwen-2/2.5 | Y | . | Y | . | . | Y | Y | Y | . | Y |
| Qwen-3 | Y | . | Y | . | . | Y | . | Y | . | Y |
| BLIP2-OPT | . | . | . | . | . | Y | . | . | . | . |
| BLIP2-T5 | . | . | . | . | . | Y | . | . | . | . |
| LLaVA | . | . | Y | . | . | Y | . | Y | . | Y |
| VILA | . | . | Y | . | . | Y | . | Y | . | Y |
| Nougat | . | . | . | . | . | Y | . | . | . | . |

Note

The vision component of multi-modal models(BLIP2-OPT/BLIP2-T5/LLaVA/VILA/Nougat) uses FP16 by default.
The language component decides which quantization methods are supported by a given multi-modal model.

## Hardware Support Matrix[#](#hardware-support-matrix "Link to this heading")

| Model | NVFP4 | MXFP4 | FP8(per tensor) | FP8(block scaling) | FP8(rowwise) | FP8 KV Cache | W4A8 AWQ | W4A16 AWQ | W4A8 GPTQ | W4A16 GPTQ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Blackwell(sm120) | Y | Y | Y | . | . | Y | . | . | . | . |
| Blackwell(sm100/103) | Y | Y | Y | Y | . | Y | . | . | . | . |
| Hopper | . | . | Y | Y | Y | Y | Y | Y | Y | Y |
| Ada Lovelace | . | . | Y | . | . | Y | Y | Y | Y | Y |
| Ampere | . | . | . | . | . | Y | . | Y | . | Y |

Note

FP8 block wise scaling GEMM kernels for sm100/103 are using MXFP8 recipe (E4M3 act/weight and UE8M0 act/weight scale), which is slightly different from SM90 FP8 recipe (E4M3 act/weight and FP32 act/weight scale).

## Quick Links[#](#quick-links "Link to this heading")

* [Pre-quantized Models by ModelOpt](https://huggingface.co/collections/nvidia/model-optimizer-66aa84f7966b3150262481a4)
* [ModelOpt Support Matrix](https://nvidia.github.io/Model-Optimizer/guides/0_support_matrix.md)

[previous

Parallelism in TensorRT LLM](parallel-strategy.md "previous page")
[next

Sampling](sampling.md "next page")

On this page

* [Quantization in TensorRT LLM](#quantization-in-tensorrt-llm)
* [Usage](#usage)
  + [Running Pre-quantized Models](#running-pre-quantized-models)
    - [FP8 KV Cache](#fp8-kv-cache)
  + [Offline Quantization with ModelOpt](#offline-quantization-with-modelopt)
* [Model Supported Matrix](#model-supported-matrix)
* [Hardware Support Matrix](#hardware-support-matrix)
* [Quick Links](#quick-links)