Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/examples/llm_speculative_decoding.md

* [LLM Examples](llm_api_examples.md)
* Speculative Decoding

# Speculative Decoding[#](#speculative-decoding "Link to this heading")

Source [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM/blob/48b7b5d8b7ed1e6bff57aecc6ff7d1533288bed8/examples/llm-api/llm_speculative_decoding.py).

```
 1from typing import Optional
 2
 3import click
 4
 5from tensorrt_llm import LLM, SamplingParams
 6from tensorrt_llm.llmapi import (EagleDecodingConfig, MTPDecodingConfig,
 7                                 NGramDecodingConfig)
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
33    spec_config = EagleDecodingConfig(
34        max_draft_len=3,
35        speculative_model_dir="yuhuili/EAGLE3-LLaMA3.1-Instruct-8B",
36        eagle3_one_model=True)
37
38    llm = LLM(
39        model="meta-llama/Llama-3.1-8B-Instruct",
40        speculative_config=spec_config,
41    )
42
43    for prompt in prompts:
44        response = llm.generate(prompt, SamplingParams(max_tokens=10))
45        print(response.outputs[0].text)
46
47
48def run_ngram():
49    spec_config = NGramDecodingConfig(
50        max_draft_len=3,
51        max_matching_ngram_size=3,
52        is_keep_all=True,
53        is_use_oldest=True,
54        is_public_pool=True,
55    )
56
57    llm = LLM(
58        model="meta-llama/Llama-3.1-8B-Instruct",
59        speculative_config=spec_config,
60        # ngram doesn't work with overlap_scheduler
61        disable_overlap_scheduler=True,
62    )
63
64    for prompt in prompts:
65        response = llm.generate(prompt, SamplingParams(max_tokens=10))
66        print(response.outputs[0].text)
67
68
69@click.command()
70@click.argument("algo",
71                type=click.Choice(["MTP", "EAGLE3", "DRAFT_TARGET", "NGRAM"]))
72@click.option("--model",
73              type=str,
74              default=None,
75              help="Path to the model or model name.")
76def main(algo: str, model: Optional[str] = None):
77    algo = algo.upper()
78    if algo == "MTP":
79        run_MTP(model)
80    elif algo == "EAGLE3":
81        run_Eagle3()
82    elif algo == "NGRAM":
83        run_ngram()
84    else:
85        raise ValueError(f"Invalid algorithm: {algo}")
86
87
88if __name__ == "__main__":
89    main()
```

[previous

Generate text with multiple LoRA adapters](llm_multilora.md "previous page")
[next

KV Cache Connector](llm_kv_cache_connector.md "next page")