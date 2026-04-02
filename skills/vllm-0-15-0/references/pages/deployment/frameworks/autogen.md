# AutoGen - vLLM

Source: https://docs.vllm.ai/en/v0.15.0/deployment/frameworks/autogen/

AutoGen¶

AutoGen is a framework for creating multi-agent AI applications that can act autonomously or work alongside humans.

Prerequisites¶

Set up the vLLM and AutoGen environment:

```text
pip install vllm

# Install AgentChat and OpenAI client from Extensions
# AutoGen requires Python 3.10 or later.
pip install -U "autogen-agentchat" "autogen-ext[openai]"
```

Deploy¶

Start the vLLM server with the supported chat completion model, e.g.

```text
vllm serve mistralai/Mistral-7B-Instruct-v0.2
```

Call it with AutoGen:

Code

```text
import asyncio
from autogen_core.models import UserMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelFamily


async def main() -> None:
    # Create a model client
    model_client = OpenAIChatCompletionClient(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        base_url="http://{your-vllm-host-ip}:{your-vllm-host-port}/v1",
        api_key="EMPTY",
        model_info={
            "vision": False,
            "function_calling": False,
            "json_output": False,
            "family": ModelFamily.MISTRAL,
            "structured_output": True,
        },
    )

    messages = [UserMessage(content="Write a very short story about a dragon.", source="user")]

    # Create a stream.
    stream = model_client.create_stream(messages=messages)

    # Iterate over the stream and print the responses.
    print("Streamed responses:")
    async for response in stream:
        if isinstance(response, str):
            # A partial response is a string.
            print(response, flush=True, end="")
        else:
            # The last response is a CreateResult object with the complete message.
            print("\n\n------------\n")
            print("The complete response:", flush=True)
            print(response.content, flush=True)

    # Close the client when done.
    await model_client.close()


asyncio.run(main())
```

For details, see the tutorial:

Using vLLM in AutoGen

OpenAI-compatible API examples
