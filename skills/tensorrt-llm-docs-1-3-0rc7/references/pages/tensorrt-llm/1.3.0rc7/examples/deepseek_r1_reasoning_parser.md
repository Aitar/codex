# Deepseek R1 Reasoning Parser — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/examples/deepseek_r1_reasoning_parser.html

Deepseek R1 Reasoning Parser#

Refer to the trtllm-serve documentation for starting a server.

Source NVIDIA/TensorRT-LLM.

```text
 1#! /usr/bin/env bash
 2
 3cat >./config.yml <<EOF
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
22    --config ./config.yml \
23    --reasoning_parser deepseek-r1
```
