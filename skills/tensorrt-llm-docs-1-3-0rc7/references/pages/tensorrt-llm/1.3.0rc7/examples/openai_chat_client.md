# OpenAI Chat Client — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/examples/openai_chat_client.html

OpenAI Chat Client#

Refer to the trtllm-serve documentation for starting a server.

Source NVIDIA/TensorRT-LLM.

```text
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
