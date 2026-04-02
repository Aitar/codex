# Curl Chat Client — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/examples/curl_chat_client.html

Curl Chat Client#

Refer to the trtllm-serve documentation for starting a server.

Source NVIDIA/TensorRT-LLM.

```text
 1#! /usr/bin/env bash
 2
 3curl http://localhost:8000/v1/chat/completions \
 4    -H "Content-Type: application/json" \
 5    -d '{
 6        "model": "TinyLlama-1.1B-Chat-v1.0",
 7        "messages":[{"role": "system", "content": "You are a helpful assistant."},
 8                    {"role": "user", "content": "Where is New York?"}],
 9        "max_tokens": 16,
10        "temperature": 0
11    }'
```
