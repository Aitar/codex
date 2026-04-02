# Model Recipes — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/deployment-guide/index.html

Model Recipes#

Quick Start for Popular Models#

The table below contains `trtllm-serve` commands that can be used to easily deploy popular models including DeepSeek-R1, gpt-oss, Llama 4, Qwen3, and more.

We maintain LLM API configuration files for these models containing recommended performance settings in two locations:

Curated Examples: examples/configs/curated - Hand-picked configurations for common scenarios.

Comprehensive Database: examples/configs/database - A more comprehensive set of known-good configurations for various GPUs and traffic patterns.

The TensorRT LLM Docker container makes these config files available at `/app/tensorrt_llm/examples/configs/curated` and `/app/tensorrt_llm/examples/configs/database` respectively. You can reference them as needed:

```text
export TRTLLM_DIR="/app/tensorrt_llm" # path to the TensorRT LLM repo in your local environment
```

Note

The configs here are specifically optimized for a target ISL/OSL (Input/Output Sequence Length) of 1024/1024. If your traffic pattern is different, refer to the Preconfigured Recipes section below which covers a larger set of traffic patterns and performance profiles.

This table is designed to provide a straightforward starting point; for detailed model-specific deployment guides, check out the guides below.

| Model Name | GPU | Inference Scenario | Config | Command |
| --- | --- | --- | --- | --- |
| DeepSeek-R1 | H100, H200 | Max Throughput | deepseek-r1-throughput.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/curated/deepseek-r1-throughput.yaml` |
| DeepSeek-R1 | B200, GB200 | Max Throughput | deepseek-r1-deepgemm.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/curated/deepseek-r1-deepgemm.yaml` |
| DeepSeek-R1 (NVFP4) | B200, GB200 | Max Throughput | deepseek-r1-throughput.yaml | `trtllm-servenvidia/DeepSeek-R1-FP4--config${TRTLLM_DIR}/examples/configs/curated/deepseek-r1-throughput.yaml` |
| DeepSeek-R1 (NVFP4) | B200, GB200 | Min Latency | deepseek-r1-latency.yaml | `trtllm-servenvidia/DeepSeek-R1-FP4-v2--config${TRTLLM_DIR}/examples/configs/curated/deepseek-r1-latency.yaml` |
| gpt-oss-120b | Any | Max Throughput | gpt-oss-120b-throughput.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/curated/gpt-oss-120b-throughput.yaml` |
| gpt-oss-120b | Any | Min Latency | gpt-oss-120b-latency.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/curated/gpt-oss-120b-latency.yaml` |
| Qwen3-Next-80B-A3B-Thinking | Any | Max Throughput | qwen3-next.yaml | `trtllm-serveQwen/Qwen3-Next-80B-A3B-Thinking--config${TRTLLM_DIR}/examples/configs/curated/qwen3-next.yaml` |
| Qwen3 family (e.g. Qwen3-30B-A3B) | Any | Max Throughput | qwen3.yaml | `trtllm-serveQwen/Qwen3-30B-A3B--config${TRTLLM_DIR}/examples/configs/curated/qwen3.yaml` (swap to another Qwen3 model name as needed) |
| Llama-3.3-70B (FP8) | Any | Max Throughput | llama-3.3-70b.yaml | `trtllm-servenvidia/Llama-3.3-70B-Instruct-FP8--config${TRTLLM_DIR}/examples/configs/curated/llama-3.3-70b.yaml` |
| Llama 4 Scout (FP8) | Any | Max Throughput | llama-4-scout.yaml | `trtllm-servenvidia/Llama-4-Scout-17B-16E-Instruct-FP8--config${TRTLLM_DIR}/examples/configs/curated/llama-4-scout.yaml` |
| Kimi-K2-Thinking (NVFP4) | B200, GB200 | Max Throughput | kimi-k2-thinking.yaml | `trtllm-servenvidia/Kimi-K2-Thinking-NVFP4--config${TRTLLM_DIR}/examples/configs/curated/kimi-k2-thinking.yaml` |

Model-Specific Deployment Guides#

The deployment guides below provide more detailed instructions for serving specific models with TensorRT LLM.

Preconfigured Recipes#

Recipe selector#

Note

Traffic Patterns: The ISL (Input Sequence Length) and OSL (Output Sequence Length)
values in each configuration represent the maximum supported values for that config.
Requests exceeding these limits may result in errors.

To handle requests with input sequences longer than the configured ISL, add the following
to your config file:

```text
enable_chunked_prefill: true
```

This enables chunked prefill, which processes long input sequences in chunks rather than
requiring them to fit within a single prefill operation. Note that enabling chunked prefill
does not guarantee optimal performance—these configs are tuned for the specified ISL/OSL.

Recipe database#

The table below lists all available pre-configured model scenarios in the TensorRT LLM configuration database. Each row represents a specific model, GPU, and performance profile combination with recommended request settings.

DeepSeek-R1#

| GPU | Performance Profile | ISL / OSL | Concurrency | Config | Command |
| --- | --- | --- | --- | --- | --- |
| 8xB200_NVL | Min Latency | 1024 / 1024 | 1 | 1k1k_tp8_conc1.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k1k_tp8_conc1.yaml` |
| 8xB200_NVL | Low Latency | 1024 / 1024 | 2 | 1k1k_tp8_conc2.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k1k_tp8_conc2.yaml` |
| 8xB200_NVL | Low Latency | 1024 / 1024 | 4 | 1k1k_tp8_conc4.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k1k_tp8_conc4.yaml` |
| 8xB200_NVL | Low Latency | 1024 / 1024 | 8 | 1k1k_tp8_conc8.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k1k_tp8_conc8.yaml` |
| 8xB200_NVL | Low Latency | 1024 / 1024 | 16 | 1k1k_tp8_conc16.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k1k_tp8_conc16.yaml` |
| 8xB200_NVL | Balanced | 1024 / 1024 | 32 | 1k1k_tp8_conc32.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k1k_tp8_conc32.yaml` |
| 8xB200_NVL | Balanced | 1024 / 1024 | 64 | 1k1k_tp8_conc64.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k1k_tp8_conc64.yaml` |
| 8xB200_NVL | High Throughput | 1024 / 1024 | 128 | 1k1k_tp8_conc128.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k1k_tp8_conc128.yaml` |
| 8xB200_NVL | High Throughput | 1024 / 1024 | 256 | 1k1k_tp8_conc256.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k1k_tp8_conc256.yaml` |
| 8xB200_NVL | High Throughput | 1024 / 1024 | 512 | 1k1k_tp8_conc512.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k1k_tp8_conc512.yaml` |
| 8xB200_NVL | High Throughput | 1024 / 1024 | 1024 | 1k1k_tp8_conc1024.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k1k_tp8_conc1024.yaml` |
| 8xB200_NVL | Max Throughput | 1024 / 1024 | 2048 | 1k1k_tp8_conc2048.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k1k_tp8_conc2048.yaml` |
| 8xB200_NVL | Min Latency | 1024 / 8192 | 1 | 1k8k_tp8_conc1.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k8k_tp8_conc1.yaml` |
| 8xB200_NVL | Low Latency | 1024 / 8192 | 2 | 1k8k_tp8_conc2.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k8k_tp8_conc2.yaml` |
| 8xB200_NVL | Low Latency | 1024 / 8192 | 4 | 1k8k_tp8_conc4.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k8k_tp8_conc4.yaml` |
| 8xB200_NVL | Low Latency | 1024 / 8192 | 8 | 1k8k_tp8_conc8.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k8k_tp8_conc8.yaml` |
| 8xB200_NVL | Low Latency | 1024 / 8192 | 16 | 1k8k_tp8_conc16.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k8k_tp8_conc16.yaml` |
| 8xB200_NVL | Balanced | 1024 / 8192 | 32 | 1k8k_tp8_conc32.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k8k_tp8_conc32.yaml` |
| 8xB200_NVL | Balanced | 1024 / 8192 | 64 | 1k8k_tp8_conc64.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k8k_tp8_conc64.yaml` |
| 8xB200_NVL | High Throughput | 1024 / 8192 | 128 | 1k8k_tp8_conc128.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k8k_tp8_conc128.yaml` |
| 8xB200_NVL | High Throughput | 1024 / 8192 | 256 | 1k8k_tp8_conc256.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k8k_tp8_conc256.yaml` |
| 8xB200_NVL | High Throughput | 1024 / 8192 | 512 | 1k8k_tp8_conc512.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k8k_tp8_conc512.yaml` |
| 8xB200_NVL | High Throughput | 1024 / 8192 | 1024 | 1k8k_tp8_conc1024.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k8k_tp8_conc1024.yaml` |
| 8xB200_NVL | Max Throughput | 1024 / 8192 | 2048 | 1k8k_tp8_conc2048.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k8k_tp8_conc2048.yaml` |
| 8xB200_NVL | Min Latency | 8192 / 1024 | 1 | 8k1k_tp8_conc1.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/8k1k_tp8_conc1.yaml` |
| 8xB200_NVL | Low Latency | 8192 / 1024 | 2 | 8k1k_tp8_conc2.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/8k1k_tp8_conc2.yaml` |
| 8xB200_NVL | Low Latency | 8192 / 1024 | 4 | 8k1k_tp8_conc4.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/8k1k_tp8_conc4.yaml` |
| 8xB200_NVL | Low Latency | 8192 / 1024 | 8 | 8k1k_tp8_conc8.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/8k1k_tp8_conc8.yaml` |
| 8xB200_NVL | Low Latency | 8192 / 1024 | 16 | 8k1k_tp8_conc16.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/8k1k_tp8_conc16.yaml` |
| 8xB200_NVL | Balanced | 8192 / 1024 | 32 | 8k1k_tp8_conc32.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/8k1k_tp8_conc32.yaml` |
| 8xB200_NVL | Balanced | 8192 / 1024 | 64 | 8k1k_tp8_conc64.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/8k1k_tp8_conc64.yaml` |
| 8xB200_NVL | High Throughput | 8192 / 1024 | 128 | 8k1k_tp8_conc128.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/8k1k_tp8_conc128.yaml` |
| 8xB200_NVL | High Throughput | 8192 / 1024 | 256 | 8k1k_tp8_conc256.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/8k1k_tp8_conc256.yaml` |
| 8xB200_NVL | High Throughput | 8192 / 1024 | 512 | 8k1k_tp8_conc512.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/8k1k_tp8_conc512.yaml` |
| 8xB200_NVL | High Throughput | 8192 / 1024 | 1024 | 8k1k_tp8_conc1024.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/8k1k_tp8_conc1024.yaml` |
| 8xB200_NVL | Max Throughput | 8192 / 1024 | 2048 | 8k1k_tp8_conc2048.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/8k1k_tp8_conc2048.yaml` |
| 8xH200_SXM | Min Latency | 1024 / 1024 | 1 | 1k1k_tp8_conc1.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/1k1k_tp8_conc1.yaml` |
| 8xH200_SXM | Low Latency | 1024 / 1024 | 2 | 1k1k_tp8_conc2.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/1k1k_tp8_conc2.yaml` |
| 8xH200_SXM | Low Latency | 1024 / 1024 | 4 | 1k1k_tp8_conc4.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/1k1k_tp8_conc4.yaml` |
| 8xH200_SXM | Low Latency | 1024 / 1024 | 8 | 1k1k_tp8_conc8.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/1k1k_tp8_conc8.yaml` |
| 8xH200_SXM | Low Latency | 1024 / 1024 | 16 | 1k1k_tp8_conc16.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/1k1k_tp8_conc16.yaml` |
| 8xH200_SXM | Balanced | 1024 / 1024 | 32 | 1k1k_tp8_conc32.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/1k1k_tp8_conc32.yaml` |
| 8xH200_SXM | Balanced | 1024 / 1024 | 64 | 1k1k_tp8_conc64.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/1k1k_tp8_conc64.yaml` |
| 8xH200_SXM | High Throughput | 1024 / 1024 | 128 | 1k1k_tp8_conc128.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/1k1k_tp8_conc128.yaml` |
| 8xH200_SXM | High Throughput | 1024 / 1024 | 256 | 1k1k_tp8_conc256.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/1k1k_tp8_conc256.yaml` |
| 8xH200_SXM | High Throughput | 1024 / 1024 | 512 | 1k1k_tp8_conc512.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/1k1k_tp8_conc512.yaml` |
| 8xH200_SXM | High Throughput | 1024 / 1024 | 1024 | 1k1k_tp8_conc1024.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/1k1k_tp8_conc1024.yaml` |
| 8xH200_SXM | Max Throughput | 1024 / 1024 | 2048 | 1k1k_tp8_conc2048.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/1k1k_tp8_conc2048.yaml` |
| 8xH200_SXM | Min Latency | 1024 / 8192 | 1 | 1k8k_tp8_conc1.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/1k8k_tp8_conc1.yaml` |
| 8xH200_SXM | Low Latency | 1024 / 8192 | 2 | 1k8k_tp8_conc2.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/1k8k_tp8_conc2.yaml` |
| 8xH200_SXM | Low Latency | 1024 / 8192 | 4 | 1k8k_tp8_conc4.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/1k8k_tp8_conc4.yaml` |
| 8xH200_SXM | Low Latency | 1024 / 8192 | 8 | 1k8k_tp8_conc8.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/1k8k_tp8_conc8.yaml` |
| 8xH200_SXM | Balanced | 1024 / 8192 | 16 | 1k8k_tp8_conc16.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/1k8k_tp8_conc16.yaml` |
| 8xH200_SXM | Balanced | 1024 / 8192 | 32 | 1k8k_tp8_conc32.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/1k8k_tp8_conc32.yaml` |
| 8xH200_SXM | High Throughput | 1024 / 8192 | 64 | 1k8k_tp8_conc64.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/1k8k_tp8_conc64.yaml` |
| 8xH200_SXM | High Throughput | 1024 / 8192 | 128 | 1k8k_tp8_conc128.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/1k8k_tp8_conc128.yaml` |
| 8xH200_SXM | High Throughput | 1024 / 8192 | 256 | 1k8k_tp8_conc256.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/1k8k_tp8_conc256.yaml` |
| 8xH200_SXM | Max Throughput | 1024 / 8192 | 512 | 1k8k_tp8_conc512.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/1k8k_tp8_conc512.yaml` |
| 8xH200_SXM | Min Latency | 8192 / 1024 | 1 | 8k1k_tp8_conc1.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/8k1k_tp8_conc1.yaml` |
| 8xH200_SXM | Low Latency | 8192 / 1024 | 2 | 8k1k_tp8_conc2.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/8k1k_tp8_conc2.yaml` |
| 8xH200_SXM | Low Latency | 8192 / 1024 | 4 | 8k1k_tp8_conc4.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/8k1k_tp8_conc4.yaml` |
| 8xH200_SXM | Low Latency | 8192 / 1024 | 8 | 8k1k_tp8_conc8.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/8k1k_tp8_conc8.yaml` |
| 8xH200_SXM | Balanced | 8192 / 1024 | 16 | 8k1k_tp8_conc16.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/8k1k_tp8_conc16.yaml` |
| 8xH200_SXM | High Throughput | 8192 / 1024 | 32 | 8k1k_tp8_conc32.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/8k1k_tp8_conc32.yaml` |
| 8xH200_SXM | High Throughput | 8192 / 1024 | 64 | 8k1k_tp8_conc64.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/8k1k_tp8_conc64.yaml` |
| 8xH200_SXM | High Throughput | 8192 / 1024 | 128 | 8k1k_tp8_conc128.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/8k1k_tp8_conc128.yaml` |
| 8xH200_SXM | Max Throughput | 8192 / 1024 | 256 | 8k1k_tp8_conc256.yaml | `trtllm-servedeepseek-ai/DeepSeek-R1-0528--config${TRTLLM_DIR}/examples/configs/database/deepseek-ai/DeepSeek-R1-0528/H200/8k1k_tp8_conc256.yaml` |

DeepSeek-R1 (NVFP4)#

| GPU | Performance Profile | ISL / OSL | Concurrency | Config | Command |
| --- | --- | --- | --- | --- | --- |
| 4xB200_NVL | High Throughput | 1024 / 8192 | 2048 | 1k8k_tp4_conc2048.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/1k8k_tp4_conc2048.yaml` |
| 4xB200_NVL | Min Latency | 8192 / 1024 | 1024 | 8k1k_tp4_conc1024.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/8k1k_tp4_conc1024.yaml` |
| 4xB200_NVL | Max Throughput | 8192 / 1024 | 2048 | 8k1k_tp4_conc2048.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/8k1k_tp4_conc2048.yaml` |
| 8xB200_NVL | Min Latency | 1024 / 1024 | 1 | 1k1k_tp8_conc1.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/1k1k_tp8_conc1.yaml` |
| 8xB200_NVL | Low Latency | 1024 / 1024 | 2 | 1k1k_tp8_conc2.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/1k1k_tp8_conc2.yaml` |
| 8xB200_NVL | Low Latency | 1024 / 1024 | 4 | 1k1k_tp8_conc4.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/1k1k_tp8_conc4.yaml` |
| 8xB200_NVL | Low Latency | 1024 / 1024 | 8 | 1k1k_tp8_conc8.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/1k1k_tp8_conc8.yaml` |
| 8xB200_NVL | Low Latency | 1024 / 1024 | 16 | 1k1k_tp8_conc16.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/1k1k_tp8_conc16.yaml` |
| 8xB200_NVL | Balanced | 1024 / 1024 | 32 | 1k1k_tp8_conc32.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/1k1k_tp8_conc32.yaml` |
| 8xB200_NVL | Balanced | 1024 / 1024 | 64 | 1k1k_tp8_conc64.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/1k1k_tp8_conc64.yaml` |
| 8xB200_NVL | High Throughput | 1024 / 1024 | 128 | 1k1k_tp8_conc128.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/1k1k_tp8_conc128.yaml` |
| 8xB200_NVL | High Throughput | 1024 / 1024 | 256 | 1k1k_tp8_conc256.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/1k1k_tp8_conc256.yaml` |
| 8xB200_NVL | High Throughput | 1024 / 1024 | 512 | 1k1k_tp8_conc512.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/1k1k_tp8_conc512.yaml` |
| 8xB200_NVL | High Throughput | 1024 / 1024 | 1024 | 1k1k_tp8_conc1024.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/1k1k_tp8_conc1024.yaml` |
| 8xB200_NVL | Max Throughput | 1024 / 1024 | 2048 | 1k1k_tp8_conc2048.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/1k1k_tp8_conc2048.yaml` |
| 8xB200_NVL | Min Latency | 1024 / 8192 | 1 | 1k8k_tp8_conc1.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/1k8k_tp8_conc1.yaml` |
| 8xB200_NVL | Low Latency | 1024 / 8192 | 2 | 1k8k_tp8_conc2.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/1k8k_tp8_conc2.yaml` |
| 8xB200_NVL | Low Latency | 1024 / 8192 | 4 | 1k8k_tp8_conc4.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/1k8k_tp8_conc4.yaml` |
| 8xB200_NVL | Low Latency | 1024 / 8192 | 8 | 1k8k_tp8_conc8.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/1k8k_tp8_conc8.yaml` |
| 8xB200_NVL | Low Latency | 1024 / 8192 | 16 | 1k8k_tp8_conc16.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/1k8k_tp8_conc16.yaml` |
| 8xB200_NVL | Balanced | 1024 / 8192 | 32 | 1k8k_tp8_conc32.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/1k8k_tp8_conc32.yaml` |
| 8xB200_NVL | High Throughput | 1024 / 8192 | 64 | 1k8k_tp8_conc64.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/1k8k_tp8_conc64.yaml` |
| 8xB200_NVL | High Throughput | 1024 / 8192 | 128 | 1k8k_tp8_conc128.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/1k8k_tp8_conc128.yaml` |
| 8xB200_NVL | High Throughput | 1024 / 8192 | 256 | 1k8k_tp8_conc256.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/1k8k_tp8_conc256.yaml` |
| 8xB200_NVL | High Throughput | 1024 / 8192 | 512 | 1k8k_tp8_conc512.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/1k8k_tp8_conc512.yaml` |
| 8xB200_NVL | Max Throughput | 1024 / 8192 | 1024 | 1k8k_tp8_conc1024.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/1k8k_tp8_conc1024.yaml` |
| 8xB200_NVL | Min Latency | 8192 / 1024 | 1 | 8k1k_tp8_conc1.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/8k1k_tp8_conc1.yaml` |
| 8xB200_NVL | Low Latency | 8192 / 1024 | 2 | 8k1k_tp8_conc2.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/8k1k_tp8_conc2.yaml` |
| 8xB200_NVL | Low Latency | 8192 / 1024 | 4 | 8k1k_tp8_conc4.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/8k1k_tp8_conc4.yaml` |
| 8xB200_NVL | Low Latency | 8192 / 1024 | 8 | 8k1k_tp8_conc8.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/8k1k_tp8_conc8.yaml` |
| 8xB200_NVL | Balanced | 8192 / 1024 | 16 | 8k1k_tp8_conc16.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/8k1k_tp8_conc16.yaml` |
| 8xB200_NVL | Balanced | 8192 / 1024 | 32 | 8k1k_tp8_conc32.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/8k1k_tp8_conc32.yaml` |
| 8xB200_NVL | High Throughput | 8192 / 1024 | 64 | 8k1k_tp8_conc64.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/8k1k_tp8_conc64.yaml` |
| 8xB200_NVL | High Throughput | 8192 / 1024 | 128 | 8k1k_tp8_conc128.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/8k1k_tp8_conc128.yaml` |
| 8xB200_NVL | High Throughput | 8192 / 1024 | 256 | 8k1k_tp8_conc256.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/8k1k_tp8_conc256.yaml` |
| 8xB200_NVL | Max Throughput | 8192 / 1024 | 512 | 8k1k_tp8_conc512.yaml | `trtllm-servenvidia/DeepSeek-R1-0528-FP4-v2--config${TRTLLM_DIR}/examples/configs/database/nvidia/DeepSeek-R1-0528-FP4-v2/B200/8k1k_tp8_conc512.yaml` |

gpt-oss-120b#

| GPU | Performance Profile | ISL / OSL | Concurrency | Config | Command |
| --- | --- | --- | --- | --- | --- |
| 2xB200_NVL | Min Latency | 1024 / 8192 | 4 | 1k8k_tp2_conc4.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k8k_tp2_conc4.yaml` |
| 2xB200_NVL | Max Throughput | 1024 / 8192 | 256 | 1k8k_tp2_conc256.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k8k_tp2_conc256.yaml` |
| 2xB200_NVL | Min Latency | 8192 / 1024 | 768 | 8k1k_tp2_conc768.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/8k1k_tp2_conc768.yaml` |
| 2xB200_NVL | Max Throughput | 8192 / 1024 | 1280 | 8k1k_tp2_conc1280.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/8k1k_tp2_conc1280.yaml` |
| 4xB200_NVL | Min Latency | 1024 / 1024 | 8 | 1k1k_tp4_conc8.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k1k_tp4_conc8.yaml` |
| 4xB200_NVL | Low Latency | 1024 / 1024 | 128 | 1k1k_tp4_conc128.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k1k_tp4_conc128.yaml` |
| 4xB200_NVL | Balanced | 1024 / 1024 | 256 | 1k1k_tp4_conc256.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k1k_tp4_conc256.yaml` |
| 4xB200_NVL | High Throughput | 1024 / 1024 | 1280 | 1k1k_tp4_conc1280.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k1k_tp4_conc1280.yaml` |
| 4xB200_NVL | Max Throughput | 1024 / 1024 | 1536 | 1k1k_tp4_conc1536.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k1k_tp4_conc1536.yaml` |
| 4xB200_NVL | Min Latency | 1024 / 8192 | 10 | 1k8k_tp4_conc10.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k8k_tp4_conc10.yaml` |
| 4xB200_NVL | Low Latency | 1024 / 8192 | 64 | 1k8k_tp4_conc64.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k8k_tp4_conc64.yaml` |
| 4xB200_NVL | Balanced | 1024 / 8192 | 128 | 1k8k_tp4_conc128.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k8k_tp4_conc128.yaml` |
| 4xB200_NVL | Balanced | 1024 / 8192 | 384 | 1k8k_tp4_conc384.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k8k_tp4_conc384.yaml` |
| 4xB200_NVL | High Throughput | 1024 / 8192 | 640 | 1k8k_tp4_conc640.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k8k_tp4_conc640.yaml` |
| 4xB200_NVL | Max Throughput | 1024 / 8192 | 896 | 1k8k_tp4_conc896.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k8k_tp4_conc896.yaml` |
| 4xB200_NVL | Min Latency | 8192 / 1024 | 1 | 8k1k_tp4_conc1.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/8k1k_tp4_conc1.yaml` |
| 4xB200_NVL | Low Latency | 8192 / 1024 | 2 | 8k1k_tp4_conc2.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/8k1k_tp4_conc2.yaml` |
| 4xB200_NVL | Low Latency | 8192 / 1024 | 4 | 8k1k_tp4_conc4.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/8k1k_tp4_conc4.yaml` |
| 4xB200_NVL | Low Latency | 8192 / 1024 | 10 | 8k1k_tp4_conc10.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/8k1k_tp4_conc10.yaml` |
| 4xB200_NVL | Balanced | 8192 / 1024 | 32 | 8k1k_tp4_conc32.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/8k1k_tp4_conc32.yaml` |
| 4xB200_NVL | High Throughput | 8192 / 1024 | 64 | 8k1k_tp4_conc64.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/8k1k_tp4_conc64.yaml` |
| 4xB200_NVL | High Throughput | 8192 / 1024 | 256 | 8k1k_tp4_conc256.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/8k1k_tp4_conc256.yaml` |
| 4xB200_NVL | High Throughput | 8192 / 1024 | 1536 | 8k1k_tp4_conc1536.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/8k1k_tp4_conc1536.yaml` |
| 4xB200_NVL | Max Throughput | 8192 / 1024 | 1792 | 8k1k_tp4_conc1792.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/8k1k_tp4_conc1792.yaml` |
| 8xB200_NVL | Min Latency | 1024 / 1024 | 1 | 1k1k_tp8_conc1.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k1k_tp8_conc1.yaml` |
| 8xB200_NVL | Low Latency | 1024 / 1024 | 2 | 1k1k_tp8_conc2.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k1k_tp8_conc2.yaml` |
| 8xB200_NVL | Low Latency | 1024 / 1024 | 4 | 1k1k_tp8_conc4.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k1k_tp8_conc4.yaml` |
| 8xB200_NVL | Low Latency | 1024 / 1024 | 16 | 1k1k_tp8_conc16.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k1k_tp8_conc16.yaml` |
| 8xB200_NVL | Low Latency | 1024 / 1024 | 32 | 1k1k_tp8_conc32.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k1k_tp8_conc32.yaml` |
| 8xB200_NVL | Low Latency | 1024 / 1024 | 64 | 1k1k_tp8_conc64.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k1k_tp8_conc64.yaml` |
| 8xB200_NVL | Balanced | 1024 / 1024 | 384 | 1k1k_tp8_conc384.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k1k_tp8_conc384.yaml` |
| 8xB200_NVL | High Throughput | 1024 / 1024 | 512 | 1k1k_tp8_conc512.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k1k_tp8_conc512.yaml` |
| 8xB200_NVL | High Throughput | 1024 / 1024 | 640 | 1k1k_tp8_conc640.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k1k_tp8_conc640.yaml` |
| 8xB200_NVL | High Throughput | 1024 / 1024 | 768 | 1k1k_tp8_conc768.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k1k_tp8_conc768.yaml` |
| 8xB200_NVL | High Throughput | 1024 / 1024 | 896 | 1k1k_tp8_conc896.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k1k_tp8_conc896.yaml` |
| 8xB200_NVL | High Throughput | 1024 / 1024 | 1792 | 1k1k_tp8_conc1792.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k1k_tp8_conc1792.yaml` |
| 8xB200_NVL | Max Throughput | 1024 / 1024 | 2048 | 1k1k_tp8_conc2048.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k1k_tp8_conc2048.yaml` |
| 8xB200_NVL | Min Latency | 1024 / 8192 | 1 | 1k8k_tp8_conc1.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k8k_tp8_conc1.yaml` |
| 8xB200_NVL | Low Latency | 1024 / 8192 | 2 | 1k8k_tp8_conc2.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k8k_tp8_conc2.yaml` |
| 8xB200_NVL | Low Latency | 1024 / 8192 | 8 | 1k8k_tp8_conc8.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k8k_tp8_conc8.yaml` |
| 8xB200_NVL | Low Latency | 1024 / 8192 | 16 | 1k8k_tp8_conc16.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k8k_tp8_conc16.yaml` |
| 8xB200_NVL | Balanced | 1024 / 8192 | 32 | 1k8k_tp8_conc32.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k8k_tp8_conc32.yaml` |
| 8xB200_NVL | Balanced | 1024 / 8192 | 768 | 1k8k_tp8_conc768.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k8k_tp8_conc768.yaml` |
| 8xB200_NVL | High Throughput | 1024 / 8192 | 1024 | 1k8k_tp8_conc1024.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k8k_tp8_conc1024.yaml` |
| 8xB200_NVL | High Throughput | 1024 / 8192 | 1280 | 1k8k_tp8_conc1280.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k8k_tp8_conc1280.yaml` |
| 8xB200_NVL | High Throughput | 1024 / 8192 | 1792 | 1k8k_tp8_conc1792.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k8k_tp8_conc1792.yaml` |
| 8xB200_NVL | Max Throughput | 1024 / 8192 | 2048 | 1k8k_tp8_conc2048.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/1k8k_tp8_conc2048.yaml` |
| 8xB200_NVL | Min Latency | 8192 / 1024 | 8 | 8k1k_tp8_conc8.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/8k1k_tp8_conc8.yaml` |
| 8xB200_NVL | Low Latency | 8192 / 1024 | 16 | 8k1k_tp8_conc16.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/8k1k_tp8_conc16.yaml` |
| 8xB200_NVL | Balanced | 8192 / 1024 | 128 | 8k1k_tp8_conc128.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/8k1k_tp8_conc128.yaml` |
| 8xB200_NVL | Balanced | 8192 / 1024 | 384 | 8k1k_tp8_conc384.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/8k1k_tp8_conc384.yaml` |
| 8xB200_NVL | High Throughput | 8192 / 1024 | 640 | 8k1k_tp8_conc640.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/8k1k_tp8_conc640.yaml` |
| 8xB200_NVL | Max Throughput | 8192 / 1024 | 2048 | 8k1k_tp8_conc2048.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/B200/8k1k_tp8_conc2048.yaml` |
| 2xH200_SXM | Min Latency | 8192 / 1024 | 16 | 8k1k_tp2_conc16.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/8k1k_tp2_conc16.yaml` |
| 2xH200_SXM | Balanced | 8192 / 1024 | 256 | 8k1k_tp2_conc256.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/8k1k_tp2_conc256.yaml` |
| 2xH200_SXM | Max Throughput | 8192 / 1024 | 384 | 8k1k_tp2_conc384.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/8k1k_tp2_conc384.yaml` |
| 4xH200_SXM | Min Latency | 1024 / 1024 | 128 | 1k1k_tp4_conc128.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k1k_tp4_conc128.yaml` |
| 4xH200_SXM | Balanced | 1024 / 1024 | 384 | 1k1k_tp4_conc384.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k1k_tp4_conc384.yaml` |
| 4xH200_SXM | Max Throughput | 1024 / 1024 | 1024 | 1k1k_tp4_conc1024.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k1k_tp4_conc1024.yaml` |
| 4xH200_SXM | High Throughput | 1024 / 8192 | 512 | 1k8k_tp4_conc512.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k8k_tp4_conc512.yaml` |
| 4xH200_SXM | Min Latency | 8192 / 1024 | 2 | 8k1k_tp4_conc2.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/8k1k_tp4_conc2.yaml` |
| 4xH200_SXM | Balanced | 8192 / 1024 | 4 | 8k1k_tp4_conc4.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/8k1k_tp4_conc4.yaml` |
| 4xH200_SXM | Max Throughput | 8192 / 1024 | 768 | 8k1k_tp4_conc768.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/8k1k_tp4_conc768.yaml` |
| 8xH200_SXM | Min Latency | 1024 / 1024 | 4 | 1k1k_tp8_conc4.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k1k_tp8_conc4.yaml` |
| 8xH200_SXM | Low Latency | 1024 / 1024 | 8 | 1k1k_tp8_conc8.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k1k_tp8_conc8.yaml` |
| 8xH200_SXM | Low Latency | 1024 / 1024 | 16 | 1k1k_tp8_conc16.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k1k_tp8_conc16.yaml` |
| 8xH200_SXM | Low Latency | 1024 / 1024 | 32 | 1k1k_tp8_conc32.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k1k_tp8_conc32.yaml` |
| 8xH200_SXM | Balanced | 1024 / 1024 | 64 | 1k1k_tp8_conc64.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k1k_tp8_conc64.yaml` |
| 8xH200_SXM | High Throughput | 1024 / 1024 | 512 | 1k1k_tp8_conc512.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k1k_tp8_conc512.yaml` |
| 8xH200_SXM | High Throughput | 1024 / 1024 | 768 | 1k1k_tp8_conc768.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k1k_tp8_conc768.yaml` |
| 8xH200_SXM | High Throughput | 1024 / 1024 | 896 | 1k1k_tp8_conc896.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k1k_tp8_conc896.yaml` |
| 8xH200_SXM | Max Throughput | 1024 / 1024 | 2048 | 1k1k_tp8_conc2048.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k1k_tp8_conc2048.yaml` |
| 8xH200_SXM | Min Latency | 1024 / 8192 | 1 | 1k8k_tp8_conc1.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k8k_tp8_conc1.yaml` |
| 8xH200_SXM | Low Latency | 1024 / 8192 | 2 | 1k8k_tp8_conc2.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k8k_tp8_conc2.yaml` |
| 8xH200_SXM | Low Latency | 1024 / 8192 | 4 | 1k8k_tp8_conc4.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k8k_tp8_conc4.yaml` |
| 8xH200_SXM | Low Latency | 1024 / 8192 | 8 | 1k8k_tp8_conc8.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k8k_tp8_conc8.yaml` |
| 8xH200_SXM | Low Latency | 1024 / 8192 | 16 | 1k8k_tp8_conc16.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k8k_tp8_conc16.yaml` |
| 8xH200_SXM | Low Latency | 1024 / 8192 | 32 | 1k8k_tp8_conc32.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k8k_tp8_conc32.yaml` |
| 8xH200_SXM | Balanced | 1024 / 8192 | 64 | 1k8k_tp8_conc64.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k8k_tp8_conc64.yaml` |
| 8xH200_SXM | High Throughput | 1024 / 8192 | 128 | 1k8k_tp8_conc128.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k8k_tp8_conc128.yaml` |
| 8xH200_SXM | High Throughput | 1024 / 8192 | 256 | 1k8k_tp8_conc256.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k8k_tp8_conc256.yaml` |
| 8xH200_SXM | High Throughput | 1024 / 8192 | 768 | 1k8k_tp8_conc768.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k8k_tp8_conc768.yaml` |
| 8xH200_SXM | High Throughput | 1024 / 8192 | 896 | 1k8k_tp8_conc896.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k8k_tp8_conc896.yaml` |
| 8xH200_SXM | High Throughput | 1024 / 8192 | 1024 | 1k8k_tp8_conc1024.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k8k_tp8_conc1024.yaml` |
| 8xH200_SXM | Max Throughput | 1024 / 8192 | 1280 | 1k8k_tp8_conc1280.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/1k8k_tp8_conc1280.yaml` |
| 8xH200_SXM | Min Latency | 8192 / 1024 | 1 | 8k1k_tp8_conc1.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/8k1k_tp8_conc1.yaml` |
| 8xH200_SXM | Low Latency | 8192 / 1024 | 8 | 8k1k_tp8_conc8.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/8k1k_tp8_conc8.yaml` |
| 8xH200_SXM | Low Latency | 8192 / 1024 | 32 | 8k1k_tp8_conc32.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/8k1k_tp8_conc32.yaml` |
| 8xH200_SXM | Balanced | 8192 / 1024 | 64 | 8k1k_tp8_conc64.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/8k1k_tp8_conc64.yaml` |
| 8xH200_SXM | Balanced | 8192 / 1024 | 128 | 8k1k_tp8_conc128.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/8k1k_tp8_conc128.yaml` |
| 8xH200_SXM | High Throughput | 8192 / 1024 | 512 | 8k1k_tp8_conc512.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/8k1k_tp8_conc512.yaml` |
| 8xH200_SXM | High Throughput | 8192 / 1024 | 640 | 8k1k_tp8_conc640.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/8k1k_tp8_conc640.yaml` |
| 8xH200_SXM | Max Throughput | 8192 / 1024 | 1536 | 8k1k_tp8_conc1536.yaml | `trtllm-serveopenai/gpt-oss-120b--config${TRTLLM_DIR}/examples/configs/database/openai/gpt-oss-120b/H200/8k1k_tp8_conc1536.yaml` |
