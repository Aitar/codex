# OpenAI Responses Client — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/examples/openai_responses_client.html

OpenAI Responses Client#

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
 9response = client.responses.create(
10    model="TinyLlama-1.1B-Chat-v1.0",
11    input="Where is New York?",
12    max_output_tokens=20,
13)
14print(response)
```
