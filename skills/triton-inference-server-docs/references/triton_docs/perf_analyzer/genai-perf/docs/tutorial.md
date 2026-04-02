* [GenAI Performance Analyzer](../../../perf_benchmark/genai_perf.md)
* Profile...

# Profile Large Language Models with GenAI-Perf[#](#profile-large-language-models-with-genai-perf "Link to this heading")

This tutorial will demonstrate how you can use GenAI-Perf to measure the performance of
various inference endpoints such as
[KServe inference protocol](https://github.com/kserve/kserve/tree/master/docs/predict-api/v2)
and [OpenAI API](https://platform.openai.com/docs/api-reference/introduction)
that are widely used across the industry.

## Table of Contents[#](#table-of-contents "Link to this heading")

* [Profile GPT2 running on Triton + TensorRT-LLM Backend](#tensorrt-llm)
* [Profile GPT2 running on Triton + vLLM Backend](#triton-vllm)
* [Profile Zephyr-7B-Beta running on OpenAI Chat Completions API-Compatible Server](#openai-chat)
* [Profile GPT2 running on OpenAI Completions API-Compatible Server](#openai-completions)

## Profile GPT-2 running on Triton + TensorRT-LLM [#](#profile-gpt-2-running-on-triton-tensorrt-llm "Link to this heading")

You can follow the [quickstart guide](https://github.com/triton-inference-server/triton_cli?tab=readme-ov-file#serving-a-trt-llm-model)
in the Triton CLI Github repository to serve GPT-2 on the Triton server with the TensorRT-LLM backend.

### Run GenAI-Perf[#](#run-genai-perf "Link to this heading")

Run GenAI-Perf inside the Triton Inference Server SDK container:

```
genai-perf profile \
  -m gpt2 \
  --backend tensorrtllm \
  --synthetic-input-tokens-mean 200 \
  --synthetic-input-tokens-stddev 0 \
  --output-tokens-mean 100 \
  --output-tokens-stddev 0 \
  --output-tokens-mean-deterministic \
  --streaming \
  --request-count 50 \
  --warmup-request-count 10
```

Example output:

```
                              NVIDIA GenAI-Perf | LLM Metrics
âââââââââââââââââââââââââââââââââââââ³âââââââââ³âââââââââ³âââââââââ³âââââââââ³âââââââââ³âââââââââ
â                         Statistic â    avg â    min â    max â    p99 â    p90 â    p75 â
â¡ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ©
â          Time to first token (ms) â  13.68 â  11.07 â  21.50 â  18.81 â  14.29 â  13.97 â
â          Inter token latency (ms) â   1.86 â   1.28 â   2.11 â   2.11 â   2.01 â   1.95 â
â              Request latency (ms) â 203.70 â 180.33 â 228.30 â 225.45 â 216.48 â 211.72 â
â            Output sequence length â 103.46 â  95.00 â 134.00 â 122.96 â 108.00 â 104.75 â
â             Input sequence length â 200.00 â 200.00 â 200.00 â 200.00 â 200.00 â 200.00 â
â Output token throughput (per sec) â 504.02 â    N/A â    N/A â    N/A â    N/A â    N/A â
â      Request throughput (per sec) â   4.87 â    N/A â    N/A â    N/A â    N/A â    N/A â
âââââââââââââââââââââââââââââââââââââ´âââââââââ´âââââââââ´âââââââââ´âââââââââ´âââââââââ´âââââââââ
```

## Profile GPT-2 running on Triton + vLLM [#](#profile-gpt-2-running-on-triton-vllm "Link to this heading")

You can follow the [quickstart guide](https://github.com/triton-inference-server/triton_cli?tab=readme-ov-file#serving-a-vllm-model)
in the Triton CLI Github repository to serve GPT-2 on the Triton server with the vLLM backend.

### Run GenAI-Perf[#](#id1 "Link to this heading")

Run GenAI-Perf inside the Triton Inference Server SDK container:

```
genai-perf profile \
  -m gpt2 \
  --backend vllm \
  --synthetic-input-tokens-mean 200 \
  --synthetic-input-tokens-stddev 0 \
  --output-tokens-mean 100 \
  --output-tokens-stddev 0 \
  --output-tokens-mean-deterministic \
  --streaming \
  --request-count 50 \
  --warmup-request-count 10
```

Example output:

```
                              NVIDIA GenAI-Perf | LLM Metrics
âââââââââââââââââââââââââââââââââââââ³âââââââââ³âââââââââ³âââââââââ³âââââââââ³âââââââââ³âââââââââ
â                         Statistic â    avg â    min â    max â    p99 â    p90 â    p75 â
â¡ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ©
â          Time to first token (ms) â  22.04 â  14.00 â  26.02 â  25.73 â  24.41 â  24.06 â
â          Inter token latency (ms) â   4.58 â   3.45 â   5.34 â   5.33 â   5.11 â   4.86 â
â              Request latency (ms) â 542.48 â 468.10 â 622.39 â 615.67 â 584.73 â 555.90 â
â            Output sequence length â 115.15 â 103.00 â 143.00 â 138.00 â 120.00 â 118.50 â
â             Input sequence length â 200.00 â 200.00 â 200.00 â 200.00 â 200.00 â 200.00 â
â Output token throughput (per sec) â 212.04 â    N/A â    N/A â    N/A â    N/A â    N/A â
â      Request throughput (per sec) â   1.84 â    N/A â    N/A â    N/A â    N/A â    N/A â
âââââââââââââââââââââââââââââââââââââ´âââââââââ´âââââââââ´âââââââââ´âââââââââ´âââââââââ´âââââââââ
```

## Profile Zephyr-7B-Beta running on OpenAI Chat API-Compatible Server [#](#profile-zephyr-7b-beta-running-on-openai-chat-api-compatible-server "Link to this heading")

Serve the model on the vLLM server with [OpenAI Chat Completions API](https://platform.openai.com/docs/api-reference/chat) endpoint:

```
docker run -it --net=host --gpus=all vllm/vllm-openai:latest --model HuggingFaceH4/zephyr-7b-beta --dtype float16
```

### Run GenAI-Perf[#](#id2 "Link to this heading")

Run GenAI-Perf inside the Triton Inference Server SDK container:

```
genai-perf profile \
  -m HuggingFaceH4/zephyr-7b-beta \
  --endpoint-type chat \
  --synthetic-input-tokens-mean 200 \
  --synthetic-input-tokens-stddev 0 \
  --output-tokens-mean 100 \
  --output-tokens-stddev 0 \
  --streaming \
  --request-count 50 \
  --warmup-request-count 10
```

Example output:

```
                                    NVIDIA GenAI-Perf | LLM Metrics
âââââââââââââââââââââââââââââââââââââ³âââââââââââ³âââââââââââ³âââââââââââ³âââââââââââ³âââââââââââ³âââââââââââ
â                         Statistic â      avg â      min â      max â      p99 â      p90 â      p75 â
â¡ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ©
â          Time to first token (ms) â    37.99 â    32.65 â    45.89 â    45.85 â    44.69 â    37.49 â
â          Inter token latency (ms) â    19.19 â    18.78 â    20.11 â    20.00 â    19.39 â    19.23 â
â              Request latency (ms) â 1,915.41 â 1,574.73 â 2,027.20 â 2,016.50 â 1,961.22 â 1,931.45 â
â            Output sequence length â    98.83 â    81.00 â   101.00 â   100.83 â   100.00 â   100.00 â
â             Input sequence length â   200.00 â   200.00 â   200.00 â   200.00 â   200.00 â   200.00 â
â Output token throughput (per sec) â    51.55 â      N/A â      N/A â      N/A â      N/A â      N/A â
â      Request throughput (per sec) â     0.52 â      N/A â      N/A â      N/A â      N/A â      N/A â
âââââââââââââââââââââââââââââââââââââ´âââââââââââ´âââââââââââ´âââââââââââ´âââââââââââ´âââââââââââ´âââââââââââ
```

## Profile GPT-2 running on OpenAI Completions API-Compatible Server [#](#profile-gpt-2-running-on-openai-completions-api-compatible-server "Link to this heading")

Serve the model on the vLLM server with [OpenAI Completions API](https://platform.openai.com/docs/api-reference/completions) endpoint:

```
docker run -it --net=host --gpus=all vllm/vllm-openai:latest --model gpt2 --dtype float16 --max-model-len 1024
```

### Run GenAI-Perf[#](#id3 "Link to this heading")

Run GenAI-Perf inside the Triton Inference Server SDK container:

```
genai-perf profile \
  -m gpt2 \
  --endpoint-type completions \
  --synthetic-input-tokens-mean 200 \
  --synthetic-input-tokens-stddev 0 \
  --output-tokens-mean 100 \
  --output-tokens-stddev 0 \
  --request-count 50 \
  --warmup-request-count 10
```

Example output:

```
                             NVIDIA GenAI-Perf | LLM Metrics
âââââââââââââââââââââââââââââââââââââ³âââââââââ³âââââââââ³âââââââââ³âââââââââ³âââââââââ³âââââââââ
â                         Statistic â    avg â    min â    max â    p99 â    p90 â    p75 â
â¡ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ©
â              Request latency (ms) â 437.85 â 328.10 â 497.05 â 495.28 â 485.68 â 460.91 â
â            Output sequence length â 112.66 â  83.00 â 123.00 â 122.69 â 119.90 â 116.25 â
â             Input sequence length â 200.00 â 200.00 â 200.00 â 200.00 â 200.00 â 200.00 â
â Output token throughput (per sec) â 257.21 â    N/A â    N/A â    N/A â    N/A â    N/A â
â      Request throughput (per sec) â   2.28 â    N/A â    N/A â    N/A â    N/A â    N/A â
âââââââââââââââââââââââââââââââââââââ´âââââââââ´âââââââââ´âââââââââ´âââââââââ´âââââââââ´âââââââââ
```

