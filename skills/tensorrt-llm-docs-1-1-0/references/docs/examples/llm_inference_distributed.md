Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/examples/llm_inference_distributed.md

* [LLM Examples](llm_api_examples.md)
* Distributed LLM Generation

# Distributed LLM Generation[#](#distributed-llm-generation "Link to this heading")

Source [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM/blob/48b7b5d8b7ed1e6bff57aecc6ff7d1533288bed8/examples/llm-api/llm_inference_distributed.py).

```
 1from tensorrt_llm import LLM, SamplingParams
 2
 3
 4def main():
 5    # model could accept HF model name or a path to local HF model.
 6    llm = LLM(
 7        model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
 8        # Enable 2-way tensor parallelism
 9        tensor_parallel_size=2
10        # Enable 2-way pipeline parallelism if needed
11        # pipeline_parallel_size=2
12        # Enable 2-way expert parallelism for MoE model's expert weights
13        # moe_expert_parallel_size=2
14        # Enable 2-way tensor parallelism for MoE model's expert weights
15        # moe_tensor_parallel_size=2
16    )
17
18    # Sample prompts.
19    prompts = [
20        "Hello, my name is",
21        "The capital of France is",
22        "The future of AI is",
23    ]
24
25    # Create a sampling params.
26    sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
27
28    for output in llm.generate(prompts, sampling_params):
29        print(
30            f"Prompt: {output.prompt!r}, Generated text: {output.outputs[0].text!r}"
31        )
32
33    # Got output like
34    # Prompt: 'Hello, my name is', Generated text: '\n\nJane Smith. I am a student pursuing my degree in Computer Science at [university]. I enjoy learning new things, especially technology and programming'
35    # Prompt: 'The capital of France is', Generated text: 'Paris.'
36    # Prompt: 'The future of AI is', Generated text: 'an exciting time for us. We are constantly researching, developing, and improving our platform to create the most advanced and efficient model available. We are'
37
38
39# The entry point of the program need to be protected for spawning processes.
40if __name__ == '__main__':
41    main()
```

[previous

Generate text in streaming](llm_inference_async_streaming.md "previous page")
[next

Generate text with guided decoding](llm_guided_decoding.md "next page")