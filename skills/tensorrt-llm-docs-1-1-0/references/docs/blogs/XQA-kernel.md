Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/blogs/XQA-kernel.md

* New XQA-kernel provides 2.4x more Llama-70B throughput within the same latency budget

# New XQA-kernel provides 2.4x more Llama-70B throughput within the same latency budget[#](#new-xqa-kernel-provides-2-4x-more-llama-70b-throughput-within-the-same-latency-budget "Link to this heading")

XQA kernel provides optimization for [MQA](https://arxiv.org/abs/1911.02150) and [GQA](https://arxiv.org/abs/2305.13245v3) during generation phase. It also provides optimization for beam search. Using tensor cores for acceleration, reducing data loading and conversion, it delivers increased throughput within the same latency budget. Increased throughput allows serving greater number of user requests while providing the same experience.

Support matrix and usage flags are described in [docs/source/advanced/gpt\_attention](#/docs/source/advanced/gpt-attention.md#xqa-optimization).

**Increased Throughput:**
Looking at the Throughput-Latency curves below, we see that the enabling of XQA optimization increases throughput. Higher throughput equates to serving more users, and we can see that TPOT on the Y-axis flattens out when XQA gets enabled.

![XQA increased throughput within same latency budget](https://github.com/NVIDIA/TensorRT-LLM/blob/rel/docs/source/blogs/media/XQA_ThroughputvsLatency.png?raw=true)

Preliminary measured Performance, subject to change. TPOT lower is better. FP8, 8xH100 GPUs, Single Engine, ISL/OSL: 512/2048, BS: 1 - 256, TensorRT LLM v0.8a

## Llama-70B on H200 up to 2.4x increased throughput with XQA within same latency budget[#](#llama-70b-on-h200-up-to-2-4x-increased-throughput-with-xqa-within-same-latency-budget "Link to this heading")

**H200 2.4x with XQA**

| Model | GPUs | Input Length | Output Length | Throughput w/o XQA (tok/s/GPU) | Throughput w/ XQA (tok/s/GPU) | Speedup |
| --- | --- | --- | --- | --- | --- | --- |
| Llama-70B | 1 | 128 | 2048 | 1,227 | 2,941 | 2.4x |
|  | 8 | 128 | 2048 | 13,232 | 25,300 | 1.9x |

### Closing[#](#closing "Link to this heading")

These improvements will be published in the `main` branch soon, and will be
included in the v0.8 releases.

For more information about H200, please see the [H200 announcement blog](H200launch.md).

Throughput is calculated as output tokens per second per gpu.
`out_tps=output_seqlen*batch_size/total_latency/tp`

**Glossary:**
| DP = Data Parallel
ISL = Input Sequence Length
| PP = Pipeline Parallel
| OSL = Output Sequence Length
| OOM = Out of Memory
| TP = Tensor Parallel

[previous

H200 achieves nearly 12,000 tokens/sec on Llama2-13B with TensorRT LLM](H200launch.md "previous page")
[next

H100 has 4.6x A100 Performance in TensorRT LLM, achieving 10,000 tok/s at 100ms to first token](H100vsA100.md "next page")

On this page

* [Llama-70B on H200 up to 2.4x increased throughput with XQA within same latency budget](#llama-70b-on-h200-up-to-2-4x-increased-throughput-with-xqa-within-same-latency-budget)
  + [Closing](#closing)