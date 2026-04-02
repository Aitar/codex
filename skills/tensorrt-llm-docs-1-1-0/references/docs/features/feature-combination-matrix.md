Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/features/feature-combination-matrix.md

* Feature Combination Matrix

# Feature Combination Matrix[#](#feature-combination-matrix "Link to this heading")

| Feature | Overlap Scheduler | CUDA Graph | Attention Data Parallelism | Disaggregated Serving | Chunked Prefill | MTP | EAGLE-3(One Model Engine) | EAGLE-3(Two Model Engine) | Torch Sampler | TLLM C++ Sampler | KV Cache Reuse | Slide Window Attention | Logits Post Processor | Guided Decoding | LoRA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Overlap Scheduler | — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| CUDA Graph | Yes | — |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Attention Data Parallelism | Yes | Yes | — |  |  |  |  |  |  |  |  |  |  |  |  |
| Disaggregated Serving | Yes | Yes | Yes | — |  |  |  |  |  |  |  |  |  |  |  |
| Chunked Prefill | Yes | Yes | Yes | Yes | — |  |  |  |  |  |  |  |  |  |  |
| MTP | Yes | Yes | Yes | Yes | Yes | — |  |  |  |  |  |  |  |  |  |
| EAGLE-3(One Model Engine) | Yes | Yes | Yes | Yes | Yes | No | — |  |  |  |  |  |  |  |  |
| EAGLE-3(Two Model Engine) | No | Yes | Yes | Yes | Yes | No | No | — |  |  |  |  |  |  |  |
| Torch Sampler | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |  |  |  |  |  |  |
| TLLM C++ Sampler | Yes | Yes | Yes | Yes | Yes | No | No | No | No | — |  |  |  |  |  |
| KV Cache Reuse | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | — |  |  |  |  |
| Slide Window Attention | Yes | Yes | Yes | Yes | Yes | No | Untested | Untested | Yes | Yes | WIP | — |  |  |  |
| Logits Post Processor | Yes | Yes | Yes | No | Yes | No | No | No | Yes | Yes | Yes | Yes | — |  |  |
| Guided Decoding | Yes | Yes | Yes | Yes | Yes | No | No | Yes | Yes | Yes | Yes | Yes | Yes | — |  |
| LoRA | Yes | No | Untested | Untested | Untested | Untested | Untested | Untested | Yes | Yes | Yes | Yes | Yes | Untested | — |

[previous

API Reference](../llm-api/reference.md "previous page")
[next

Multi-Head, Multi-Query, and Group-Query Attention](attention.md "next page")