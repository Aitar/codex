Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/examples/llm_inference.md

* [LLM Examples](llm_api_examples.md)
* Generate text

# Generate text[#](#generate-text "Link to this heading")

Source [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM/blob/48b7b5d8b7ed1e6bff57aecc6ff7d1533288bed8/examples/llm-api/llm_inference.py).

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
27    # Prompt: 'The capital of France is', Generated text: 'Paris.'
28    # Prompt: 'The future of AI is', Generated text: 'an exciting time for us. We are constantly researching, developing, and improving our platform to create the most advanced and efficient model available. We are'
29
30
31if __name__ == '__main__':
32    main()
```

[previous

LLM Examples](llm_api_examples.md "previous page")
[next

Generate text asynchronously](llm_inference_async.md "next page")