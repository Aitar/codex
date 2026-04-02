# Aiperf Client For Multimodal — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/examples/aiperf_client_for_multimodal.html

Aiperf Client For Multimodal#

Refer to the trtllm-serve documentation for starting a server.

Source NVIDIA/TensorRT-LLM.

```text
 1#! /usr/bin/env bash
 2
 3aiperf profile \
 4    -m Qwen2.5-VL-3B-Instruct \
 5    --tokenizer ${AIPERF_TOKENIZER_PATH:-Qwen/Qwen2.5-VL-3B-Instruct} \
 6    --endpoint-type chat \
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
