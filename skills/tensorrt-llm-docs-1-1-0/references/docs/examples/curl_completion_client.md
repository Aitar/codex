Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/examples/curl_completion_client.md

* [Online Serving Examples](trtllm_serve_examples.md)
* Curl Completion Client

# Curl Completion Client[#](#curl-completion-client "Link to this heading")

Refer to the [trtllm-serve documentation](https://nvidia.github.io/TensorRT-LLM/commands/trtllm-serve.md) for starting a server.

Source [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM/blob/48b7b5d8b7ed1e6bff57aecc6ff7d1533288bed8/examples/serve/curl_completion_client.sh).

```
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

[previous

Curl Chat Client For Multimodal](curl_chat_client_for_multimodal.md "previous page")
[next

Deepseek R1 Reasoning Parser](deepseek_r1_reasoning_parser.md "next page")