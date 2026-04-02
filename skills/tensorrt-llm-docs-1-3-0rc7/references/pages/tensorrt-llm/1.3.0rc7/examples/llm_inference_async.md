# Generate text asynchronously — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/examples/llm_inference_async.html

Generate text asynchronously#

Source NVIDIA/TensorRT-LLM.

```text
 1import asyncio
 2
 3from tensorrt_llm import LLM, SamplingParams
 4
 5
 6def main():
 7    # model could accept HF model name or a path to local HF model.
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
20    # Async based on Python coroutines
21    async def task(prompt: str):
22        output = await llm.generate_async(prompt, sampling_params)
23        print(
24            f"Prompt: {output.prompt!r}, Generated text: {output.outputs[0].text!r}"
25        )
26
27    async def main():
28        tasks = [task(prompt) for prompt in prompts]
29        await asyncio.gather(*tasks)
30
31    asyncio.run(main())
32
33    # Got output like follows:
34    # Prompt: 'Hello, my name is', Generated text: '\n\nJane Smith. I am a student pursuing my degree in Computer Science at [university]. I enjoy learning new things, especially technology and programming'
35    # Prompt: 'The capital of France is', Generated text: 'Paris.'
36    # Prompt: 'The future of AI is', Generated text: 'an exciting time for us. We are constantly researching, developing, and improving our platform to create the most advanced and efficient model available. We are'
37
38
39if __name__ == '__main__':
40    main()
```
