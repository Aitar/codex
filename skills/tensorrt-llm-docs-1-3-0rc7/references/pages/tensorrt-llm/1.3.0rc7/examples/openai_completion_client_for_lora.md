# Openai Completion Client For Lora — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/examples/openai_completion_client_for_lora.html

Openai Completion Client For Lora#

Refer to the trtllm-serve documentation for starting a server.

Source NVIDIA/TensorRT-LLM.

```text
 1### OpenAI Completion Client
 2
 3import os
 4from pathlib import Path
 5
 6from openai import OpenAI
 7
 8client = OpenAI(
 9    base_url="http://localhost:8000/v1",
10    api_key="tensorrt_llm",
11)
12
13lora_path = Path(
14    os.environ.get("LLM_MODELS_ROOT")) / "llama-models" / "luotuo-lora-7b-0.1"
15assert lora_path.exists(), f"Lora path {lora_path} does not exist"
16
17response = client.completions.create(
18    model="llama-7b-hf",
19    prompt="美国的首都在哪里? \n答案:",
20    max_tokens=20,
21    extra_body={
22        "lora_request": {
23            "lora_name": "luotuo-lora-7b-0.1",
24            "lora_int_id": 0,
25            "lora_path": str(lora_path)
26        }
27    },
28)
29
30print(response)
```
