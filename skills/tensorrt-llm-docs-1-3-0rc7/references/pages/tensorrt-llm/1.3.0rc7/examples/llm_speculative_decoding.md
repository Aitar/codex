# Speculative Decoding — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/examples/llm_speculative_decoding.html

Speculative Decoding#

Source NVIDIA/TensorRT-LLM.

```text
 1from typing import Optional
 2
 3import click
 4
 5from tensorrt_llm import LLM, SamplingParams
 6from tensorrt_llm.llmapi import (Eagle3DecodingConfig, KvCacheConfig,
 7                                 MTPDecodingConfig, NGramDecodingConfig)
 8
 9prompts = [
10    "What is the capital of France?",
11    "What is the future of AI?",
12]
13
14
15def run_MTP(model: Optional[str] = None):
16    spec_config = MTPDecodingConfig(num_nextn_predict_layers=1,
17                                    use_relaxed_acceptance_for_thinking=True,
18                                    relaxed_topk=10,
19                                    relaxed_delta=0.01)
20
21    llm = LLM(
22        # You can change this to a local model path if you have the model downloaded
23        model=model or "nvidia/DeepSeek-R1-FP4",
24        speculative_config=spec_config,
25    )
26
27    for prompt in prompts:
28        response = llm.generate(prompt, SamplingParams(max_tokens=10))
29        print(response.outputs[0].text)
30
31
32def run_Eagle3():
33    spec_config = Eagle3DecodingConfig(
34        max_draft_len=3,
35        speculative_model="yuhuili/EAGLE3-LLaMA3.1-Instruct-8B",
36        eagle3_one_model=True)
37
38    kv_cache_config = KvCacheConfig(free_gpu_memory_fraction=0.8)
39
40    llm = LLM(
41        model="meta-llama/Llama-3.1-8B-Instruct",
42        speculative_config=spec_config,
43        kv_cache_config=kv_cache_config,
44    )
45
46    for prompt in prompts:
47        response = llm.generate(prompt, SamplingParams(max_tokens=10))
48        print(response.outputs[0].text)
49
50
51def run_ngram():
52    spec_config = NGramDecodingConfig(
53        max_draft_len=3,
54        max_matching_ngram_size=3,
55        is_keep_all=True,
56        is_use_oldest=True,
57        is_public_pool=True,
58    )
59
60    llm = LLM(
61        model="meta-llama/Llama-3.1-8B-Instruct",
62        speculative_config=spec_config,
63        # ngram doesn't work with overlap_scheduler
64        disable_overlap_scheduler=True,
65    )
66
67    for prompt in prompts:
68        response = llm.generate(prompt, SamplingParams(max_tokens=10))
69        print(response.outputs[0].text)
70
71
72@click.command()
73@click.argument("algo",
74                type=click.Choice(["MTP", "EAGLE3", "DRAFT_TARGET", "NGRAM"]))
75@click.option("--model",
76              type=str,
77              default=None,
78              help="Path to the model or model name.")
79def main(algo: str, model: Optional[str] = None):
80    algo = algo.upper()
81    if algo == "MTP":
82        run_MTP(model)
83    elif algo == "EAGLE3":
84        run_Eagle3()
85    elif algo == "NGRAM":
86        run_ngram()
87    else:
88        raise ValueError(f"Invalid algorithm: {algo}")
89
90
91if __name__ == "__main__":
92    main()
```
