Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/quick-start-guide.md

* Quick Start Guide

# Quick Start Guide[#](#quick-start-guide "Link to this heading")

This is the starting point to try out TensorRT LLM. Specifically, this Quick Start Guide enables you to quickly get set up and send HTTP requests using TensorRT LLM.

## Launch Docker on a node with NVIDIA GPUs deployed[#](#launch-docker-on-a-node-with-nvidia-gpus-deployed "Link to this heading")

```
docker run --rm -it --ipc host --gpus all --ulimit memlock=-1 --ulimit stack=67108864 -p 8000:8000 nvcr.io/nvidia/tensorrt-llm/release:1.1.0
```

## Deploy online serving with trtllm-serve[#](#deploy-online-serving-with-trtllm-serve "Link to this heading")

You can use the `trtllm-serve` command to start an OpenAI compatible server to interact with a model.
To start the server, you can run a command like the following example inside a Docker container:

```
trtllm-serve "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
```

You may also deploy pre-quantized models to improve performance.
Ensure your GPU supports FP8 quantization before running the following:

```
trtllm-serve "nvidia/Qwen3-8B-FP8"
```

For more options, browse the full [collection of generative models](https://huggingface.co/collections/nvidia/inference-optimized-checkpoints-with-model-optimizer) that have been quantized and optimized for inference with the TensorRT Model Optimizer.

Note

If you are running trtllm-server inside a Docker container, you have two options for sending API requests:

1. Expose a port (e.g., 8000) to allow external access to the server from outside the container.
2. Open a new terminal and use the following command to directly attach to the running container:

```
docker exec -it <container_id> bash
```

After the server has started, you can access well-known OpenAI endpoints such as `v1/chat/completions`.
Inference can then be performed using examples similar to the one provided below, from a separate terminal.

```
curl -X POST http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    -d '{
        "model": "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        "messages":[{"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "Where is New York? Tell me in a single sentence."}],
        "max_tokens": 32,
        "temperature": 0
    }'
```

*Example Output*

```
{
  "id": "chatcmpl-ef648e7489c040679d87ed12db5d3214",
  "object": "chat.completion",
  "created": 1741966075,
  "model": "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "New York is a city in the northeastern United States, located on the eastern coast of the state of New York.",
        "tool_calls": []
      },
      "logprobs": null,
      "finish_reason": "stop",
      "stop_reason": null
    }
  ],
  "usage": {
    "prompt_tokens": 43,
    "total_tokens": 69,
    "completion_tokens": 26
  }
}
```

For detailed examples and command syntax, refer to the [trtllm-serve](commands/trtllm-serve/trtllm-serve.md) section.

## Run Offline inference with LLM API[#](#run-offline-inference-with-llm-api "Link to this heading")

The LLM API is a Python API designed to facilitate setup and inference with TensorRT LLM directly within Python. It enables model optimization by simply specifying a HuggingFace repository name or a model checkpoint. The LLM API streamlines the process by managing model loading, optimization, and inference, all through a single `LLM` instance.

Here is a simple example to show how to use the LLM API with TinyLlama.

```
 1from tensorrt_llm import LLM, SamplingParams
 2
 3
 4def main():
 5
 6    # Model could accept HF model name, a path to local HF model,
 7    # or TensorRT Model Optimizer's quantized checkpoints like nvidia/Llama-3.1-8B-Instruct-FP8 on HF.
 8    llm = LLM(model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
 9
10    # Sample prompts.
11    prompts = [
12        "Hello, my name is",
13        "The capital of France is",
14        "The future of AI is",
15    ]
16
17    # Create a sampling params.
18    sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
19
20    for output in llm.generate(prompts, sampling_params):
21        print(
22            f"Prompt: {output.prompt!r}, Generated text: {output.outputs[0].text!r}"
23        )
24
25    # Got output like
26    # Prompt: 'Hello, my name is', Generated text: '\n\nJane Smith. I am a student pursuing my degree in Computer Science at [university]. I enjoy learning new things, especially technology and programming'
27    # Prompt: 'The president of the United States is', Generated text: 'likely to nominate a new Supreme Court justice to fill the seat vacated by the death of Antonin Scalia. The Senate should vote to confirm the'
28    # Prompt: 'The capital of France is', Generated text: 'Paris.'
29    # Prompt: 'The future of AI is', Generated text: 'an exciting time for us. We are constantly researching, developing, and improving our platform to create the most advanced and efficient model available. We are'
30
31
32if __name__ == '__main__':
33    main()
```

You can also directly load pre-quantized models [quantized checkpoints on Hugging Face](https://huggingface.co/collections/nvidia/model-optimizer-66aa84f7966b3150262481a4) in the LLM constructor.
To learn more about the LLM API, check out the [LLM API Introduction](llm-api/index.md) and [LLM Examples](examples/llm_api_examples.md).

## Next Steps[#](#next-steps "Link to this heading")

In this Quick Start Guide, you have:

* Learned how to deploy a model with `trtllm-serve` for online serving
* Explored the LLM API for offline inference with TensorRT LLM

To continue your journey with TensorRT LLM, explore these resources:

* **[Installation Guide](installation/index.md)** - Detailed installation instructions for different platforms
* **[Deployment Guide](examples/llm_api_examples.md)** - Comprehensive examples for deploying LLM inference in various scenarios
* **[Model Support](models/supported-models.md)** - Check which models are supported and how to add new ones
* **CLI Reference** - Explore TensorRT LLM command-line tools:

  + [`trtllm-serve`](commands/trtllm-serve/trtllm-serve.md) - Deploy models for online serving
  + [`trtllm-bench`](commands/trtllm-bench.md) - Benchmark model performance
  + [`trtllm-eval`](commands/trtllm-eval.md) - Evaluate model accuracy

[previous

Overview](overview.md "previous page")
[next

Installation](installation/index.md "next page")

On this page

* [Launch Docker on a node with NVIDIA GPUs deployed](#launch-docker-on-a-node-with-nvidia-gpus-deployed)
* [Deploy online serving with trtllm-serve](#deploy-online-serving-with-trtllm-serve)
* [Run Offline inference with LLM API](#run-offline-inference-with-llm-api)
* [Next Steps](#next-steps)