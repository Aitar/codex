Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/examples/genai_perf_client.md

* [Online Serving Examples](trtllm_serve_examples.md)
* Genai Perf Client

# Genai Perf Client[#](#genai-perf-client "Link to this heading")

Refer to the [trtllm-serve documentation](https://nvidia.github.io/TensorRT-LLM/commands/trtllm-serve.md) for starting a server.

Source [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM/blob/48b7b5d8b7ed1e6bff57aecc6ff7d1533288bed8/examples/serve/genai_perf_client.sh).

```
 1#! /usr/bin/env bash
 2
 3genai-perf profile \
 4    -m TinyLlama-1.1B-Chat-v1.0 \
 5    --tokenizer TinyLlama/TinyLlama-1.1B-Chat-v1.0 \
 6    --endpoint-type chat \
 7    --random-seed 123 \
 8    --synthetic-input-tokens-mean 128 \
 9    --synthetic-input-tokens-stddev 0 \
10    --output-tokens-mean 128 \
11    --output-tokens-stddev 0 \
12    --request-count 100 \
13    --request-rate 10 \
14    --profile-export-file my_profile_export.json \
15    --url localhost:8000 \
16    --streaming
```

[previous

Deepseek R1 Reasoning Parser](deepseek_r1_reasoning_parser.md "previous page")
[next

Genai Perf Client For Multimodal](genai_perf_client_for_multimodal.md "next page")