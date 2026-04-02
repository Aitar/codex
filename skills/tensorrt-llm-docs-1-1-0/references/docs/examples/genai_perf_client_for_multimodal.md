Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/examples/genai_perf_client_for_multimodal.md

* [Online Serving Examples](trtllm_serve_examples.md)
* Genai Perf Client For Multimodal

# Genai Perf Client For Multimodal[#](#genai-perf-client-for-multimodal "Link to this heading")

Refer to the [trtllm-serve documentation](https://nvidia.github.io/TensorRT-LLM/commands/trtllm-serve.md) for starting a server.

Source [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM/blob/48b7b5d8b7ed1e6bff57aecc6ff7d1533288bed8/examples/serve/genai_perf_client_for_multimodal.sh).

```
 1#! /usr/bin/env bash
 2
 3genai-perf profile \
 4    -m Qwen2.5-VL-3B-Instruct \
 5    --tokenizer Qwen/Qwen2.5-VL-3B-Instruct \
 6    --endpoint-type multimodal \
 7    --random-seed 123 \
 8    --image-width-mean 64 \
 9    --image-height-mean 64 \
10    --image-format png \
11    --synthetic-input-tokens-mean 128 \
12    --synthetic-input-tokens-stddev 0 \
13    --output-tokens-mean 128 \
14    --output-tokens-stddev 0 \
15    --request-count 5 \
16    --request-rate 1 \
17    --profile-export-file my_profile_export.json \
18    --url localhost:8000 \
19    --streaming
```

[previous

Genai Perf Client](genai_perf_client.md "previous page")
[next

OpenAI Chat Client](openai_chat_client.md "next page")