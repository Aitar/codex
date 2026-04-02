# Generate text in streaming — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/examples/llm_inference_async_streaming.html

Generate text in streaming#

Source NVIDIA/TensorRT-LLM.

```text
 1import asyncio
 2
 3from tensorrt_llm import LLM, SamplingParams
 4
 5
 6def main():
 7
 8    # model could accept HF model name or a path to local HF model.
 9    llm = LLM(model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
10
11    # Sample prompts.
12    prompts = [
13        "Hello, my name is",
14        "The capital of France is",
15        "The future of AI is",
16    ]
17
18    # Create a sampling params.
19    sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
20
21    # Async based on Python coroutines
22    async def task(id: int, prompt: str):
23
24        # streaming=True is used to enable streaming generation.
25        async for output in llm.generate_async(prompt,
26                                               sampling_params,
27                                               streaming=True):
28            print(f"Generation for prompt-{id}: {output.outputs[0].text!r}")
29
30    async def main():
31        tasks = [task(id, prompt) for id, prompt in enumerate(prompts)]
32        await asyncio.gather(*tasks)
33
34    asyncio.run(main())
35
36    # Got output like follows:
37    # Generation for prompt-0: '\n'
38    # Generation for prompt-3: 'an'
39    # Generation for prompt-2: 'Paris'
40    # Generation for prompt-1: 'likely'
41    # Generation for prompt-0: '\n\n'
42    # Generation for prompt-3: 'an exc'
43    # Generation for prompt-2: 'Paris.'
44    # Generation for prompt-1: 'likely to'
45    # Generation for prompt-0: '\n\nJ'
46    # Generation for prompt-3: 'an exciting'
47    # Generation for prompt-2: 'Paris.'
48    # Generation for prompt-1: 'likely to nomin'
49    # Generation for prompt-0: '\n\nJane'
50    # Generation for prompt-3: 'an exciting time'
51    # Generation for prompt-1: 'likely to nominate'
52    # Generation for prompt-0: '\n\nJane Smith'
53    # Generation for prompt-3: 'an exciting time for'
54    # Generation for prompt-1: 'likely to nominate a'
55    # Generation for prompt-0: '\n\nJane Smith.'
56    # Generation for prompt-3: 'an exciting time for us'
57    # Generation for prompt-1: 'likely to nominate a new'
58
59
60if __name__ == '__main__':
61    main()
```
