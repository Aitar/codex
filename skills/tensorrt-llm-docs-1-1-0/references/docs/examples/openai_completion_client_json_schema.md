Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/examples/openai_completion_client_json_schema.md

* [Online Serving Examples](trtllm_serve_examples.md)
* OpenAI Completion Client with JSON Schema

# OpenAI Completion Client with JSON Schema[#](#openai-completion-client-with-json-schema "Link to this heading")

Refer to the [trtllm-serve documentation](https://nvidia.github.io/TensorRT-LLM/commands/trtllm-serve.md) for starting a server.

Source [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM/blob/48b7b5d8b7ed1e6bff57aecc6ff7d1533288bed8/examples/serve/openai_completion_client_json_schema.py).

```
 1
 2# This example requires to specify `guided_decoding_backend` as
 3# `xgrammar` or `llguidance` in the extra_llm_api_options.yaml file.
 4import json
 5
 6from openai import OpenAI
 7
 8client = OpenAI(
 9    base_url="http://localhost:8000/v1",
10    api_key="tensorrt_llm",
11)
12
13response = client.chat.completions.create(
14    model="TinyLlama-1.1B-Chat-v1.0",
15    messages=[{
16        "role": "system",
17        "content": "you are a helpful assistant"
18    }, {
19        "role":
20        "user",
21        "content":
22        f"Give me the information of the biggest city of China in the JSON format.",
23    }],
24    temperature=0,
25    response_format={
26        "type": "json",
27        "schema": {
28            "type": "object",
29            "properties": {
30                "name": {
31                    "type": "string"
32                },
33                "population": {
34                    "type": "integer"
35                },
36            },
37            "required": ["name", "population"],
38            "chat_template_kwargs": {
39                "enable_thinking": False
40            }
41        }
42    },
43)
44
45content = response.choices[0].message.content
46try:
47    response_json = json.loads(content)
48    assert "name" in response_json and "population" in response_json
49    print(content)
50except json.JSONDecodeError:
51    print("Failed to decode JSON response")
```

[previous

Openai Completion Client For Lora](openai_completion_client_for_lora.md "previous page")
[next

Dynamo K8s Example](dynamo_k8s_example.md "next page")