# LiteLLM - vLLM

Source: https://docs.vllm.ai/en/v0.15.0/deployment/frameworks/litellm/

LiteLLM¶

LiteLLM call all LLM APIs using the OpenAI format [Bedrock, Huggingface, VertexAI, TogetherAI, Azure, OpenAI, Groq etc.]

LiteLLM manages:

Translate inputs to provider's `completion`, `embedding`, and `image_generation` endpoints

Consistent output, text responses will always be available at `['choices'][0]['message']['content']`

Retry/fallback logic across multiple deployments (e.g. Azure/OpenAI) - Router

Set Budgets & Rate limits per project, api key, model LiteLLM Proxy Server (LLM Gateway)

And LiteLLM supports all models on VLLM.

Prerequisites¶

Set up the vLLM and litellm environment:

```text
pip install vllm litellm
```

Deploy¶

Chat completion¶

Start the vLLM server with the supported chat completion model, e.g.

```text
vllm serve qwen/Qwen1.5-0.5B-Chat
```

Call it with litellm:

Code

```text
import litellm

messages = [{"content": "Hello, how are you?", "role": "user"}]

# hosted_vllm is prefix key word and necessary
response = litellm.completion(
    model="hosted_vllm/qwen/Qwen1.5-0.5B-Chat", # pass the vllm model name
    messages=messages,
    api_base="http://{your-vllm-server-host}:{your-vllm-server-port}/v1",
    temperature=0.2,
    max_tokens=80,
)

print(response)
```

Embeddings¶

Start the vLLM server with the supported embedding model, e.g.

```text
vllm serve BAAI/bge-base-en-v1.5
```

Call it with litellm:

```text
from litellm import embedding
import os

os.environ["HOSTED_VLLM_API_BASE"] = "http://{your-vllm-server-host}:{your-vllm-server-port}/v1"

# hosted_vllm is prefix key word and necessary
# pass the vllm model name
embedding = embedding(model="hosted_vllm/BAAI/bge-base-en-v1.5", input=["Hello world"])

print(embedding)
```

For details, see the tutorial Using vLLM in LiteLLM.
