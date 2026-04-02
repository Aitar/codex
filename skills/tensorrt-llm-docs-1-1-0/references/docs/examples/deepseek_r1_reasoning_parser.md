Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/examples/deepseek_r1_reasoning_parser.md

* [Online Serving Examples](trtllm_serve_examples.md)
* Deepseek R1 Reasoning Parser

# Deepseek R1 Reasoning Parser[#](#deepseek-r1-reasoning-parser "Link to this heading")

Refer to the [trtllm-serve documentation](https://nvidia.github.io/TensorRT-LLM/commands/trtllm-serve.md) for starting a server.

Source [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM/blob/48b7b5d8b7ed1e6bff57aecc6ff7d1533288bed8/examples/serve/deepseek_r1_reasoning_parser.sh).

```
 1#! /usr/bin/env bash
 2
 3cat >./extra-llm-api-config.yml <<EOF
 4cuda_graph_config:
 5    enable_padding: true
 6    max_batch_size: 512
 7enable_attention_dp: true
 8kv_cache_config:
 9    dtype: fp8
10    free_gpu_memory_fraction: 0.8
11stream_interval: 10
12moe_config:
13    backend: DEEPGEMM
14EOF
15
16trtllm-serve \
17    deepseek-ai/DeepSeek-R1 \
18    --host localhost --port 8000 \
19    --trust_remote_code \
20    --max_batch_size 1024 --max_num_tokens 8192 \
21    --tp_size 8 --ep_size 8 --pp_size 1 \
22    --extra_llm_api_options ./extra-llm-api-config.yml \
23    --reasoning_parser deepseek-r1
```

[previous

Curl Completion Client](curl_completion_client.md "previous page")
[next

Genai Perf Client](genai_perf_client.md "next page")