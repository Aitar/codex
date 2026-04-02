# Curl Completion Client — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/examples/curl_completion_client.html

Curl Completion Client#

Refer to the trtllm-serve documentation for starting a server.

Source NVIDIA/TensorRT-LLM.

```text
 1#! /usr/bin/env bash
 2
 3curl http://localhost:8000/v1/completions \
 4    -H "Content-Type: application/json" \
 5    -d '{
 6        "model": "TinyLlama-1.1B-Chat-v1.0",
 7        "prompt": "Where is New York?",
 8        "max_tokens": 16,
 9        "temperature": 0
10    }'
```
