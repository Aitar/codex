Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/examples/openai_chat_client.md

* [Online Serving Examples](trtllm_serve_examples.md)
* OpenAI Chat Client

# OpenAI Chat Client[#](#openai-chat-client "Link to this heading")

Refer to the [trtllm-serve documentation](https://nvidia.github.io/TensorRT-LLM/commands/trtllm-serve.md) for starting a server.

Source [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM/blob/48b7b5d8b7ed1e6bff57aecc6ff7d1533288bed8/examples/serve/openai_chat_client.py).

```
 1
 2from openai import OpenAI
 3
 4client = OpenAI(
 5    base_url="http://localhost:8000/v1",
 6    api_key="tensorrt_llm",
 7)
 8
 9response = client.chat.completions.create(
10    model="TinyLlama-1.1B-Chat-v1.0",
11    messages=[{
12        "role": "system",
13        "content": "you are a helpful assistant"
14    }, {
15        "role": "user",
16        "content": "Where is New York?"
17    }],
18    max_tokens=20,
19)
20print(response)
```

[previous

Genai Perf Client For Multimodal](genai_perf_client_for_multimodal.md "previous page")
[next

OpenAI Chat Client for Multimodal](openai_chat_client_for_multimodal.md "next page")