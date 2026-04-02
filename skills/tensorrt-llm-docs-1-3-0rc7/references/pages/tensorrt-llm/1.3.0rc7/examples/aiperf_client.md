# Aiperf Client — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/examples/aiperf_client.html

Aiperf Client#

Refer to the trtllm-serve documentation for starting a server.

Source NVIDIA/TensorRT-LLM.

```text
 1#! /usr/bin/env bash
 2
 3aiperf profile \
 4    -m TinyLlama-1.1B-Chat-v1.0 \
 5    --tokenizer ${AIPERF_TOKENIZER_PATH:-TinyLlama/TinyLlama-1.1B-Chat-v1.0} \
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
