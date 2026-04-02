Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/examples/openai_completion_client.md

* [Online Serving Examples](trtllm_serve_examples.md)
* OpenAI Completion Client

# OpenAI Completion Client[#](#openai-completion-client "Link to this heading")

Refer to the [trtllm-serve documentation](https://nvidia.github.io/TensorRT-LLM/commands/trtllm-serve.md) for starting a server.

Source [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM/blob/48b7b5d8b7ed1e6bff57aecc6ff7d1533288bed8/examples/serve/openai_completion_client.py).

```
 1
 2from openai import OpenAI
 3
 4client = OpenAI(
 5    base_url="http://localhost:8000/v1",
 6    api_key="tensorrt_llm",
 7)
 8
 9response = client.completions.create(
10    model="TinyLlama-1.1B-Chat-v1.0",
11    prompt="Where is New York?",
12    max_tokens=20,
13)
14print(response)
```

[previous

OpenAI Chat Client for Multimodal](openai_chat_client_for_multimodal.md "previous page")
[next

Openai Completion Client For Lora](openai_completion_client_for_lora.md "next page")