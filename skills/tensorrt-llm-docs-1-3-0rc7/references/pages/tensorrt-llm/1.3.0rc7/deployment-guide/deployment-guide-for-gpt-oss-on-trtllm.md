# Deployment Guide for GPT-OSS on TensorRT-LLM - Blackwell Hardware — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/deployment-guide/deployment-guide-for-gpt-oss-on-trtllm.html

Deployment Guide for GPT-OSS on TensorRT-LLM - Blackwell Hardware#

Introduction#

This deployment guide provides step-by-step instructions for running the GPT-OSS model using TensorRT-LLM, optimized for NVIDIA GPUs. It covers the complete setup required; from accessing model weights and preparing the software environment to configuring TensorRT-LLM parameters, launching the server, and validating inference output.

The guide is intended for developers and practitioners seeking high-throughput or low-latency inference using NVIDIA’s accelerated stack—starting with the PyTorch container from NGC, then installing TensorRT-LLM for model serving.

Prerequisites#

GPU: NVIDIA Blackwell Architecture

OS: Linux

Drivers: CUDA Driver 575 or Later

Docker with NVIDIA Container Toolkit installed

Python3 and python3-pip (Optional, for accuracy evaluation only)

Models#

MXFP4 model: GPT-OSS-120B

MoE Backend Support Matrix#

There are multiple MOE backends inside TensorRT LLM. Here are the support matrix of the MOE backends.

| Device | Activation Type | MoE Weights Type | MoE Backend | Use Case |
| --- | --- | --- | --- | --- |
| B200/GB200/B300/GB300 | MXFP8 | MXFP4 | TRTLLM | Low Latency and Max Throughput |
| H200 | BF16 | MXFP4 | TRITON | Low Latency and Max Throughput |

For Blackwell, the default MoE backend is `TRTLLM`. For Hopper, the default MoE backend is `TRITON`. They are recommended for the best perf. Users don’t need to explicitly set `moe_config.backend`.

Deployment Steps#

Run Docker Container#

Run the docker container using the TensorRT-LLM NVIDIA NGC image.

```text
docker run --rm -it \
--ipc=host \
--gpus all \
-p 8000:8000 \
-v ~/.cache:/root/.cache:rw \
--name tensorrt_llm \
nvcr.io/nvidia/tensorrt-llm/release:1.3.0rc7 \
/bin/bash
```

Note:

The command mounts your user `.cache` directory to save the downloaded model checkpoints which are saved to `~/.cache/huggingface/hub/` by default. This prevents having to redownload the weights each time you rerun the container. If the `~/.cache` directory doesn’t exist please create it using `$mkdir~/.cache`.

You can mount additional directories and paths using the `-v<host_path>:<container_path>` flag if needed, such as mounting the downloaded weight paths.

The command also maps port `8000` from the container to your host so you can access the LLM API endpoint from your host

See the https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tensorrt-llm/containers/release/tags for all the available containers. The containers published in the main branch weekly have `rcN` suffix, while the monthly release with QA tests has no `rcN` suffix. Use the `rc` release to get the latest model and feature support.

If you want to use latest main branch, you can choose to build from source to install TensorRT-LLM, the steps refer to https://nvidia.github.io/TensorRT-LLM/latest/installation/build-from-source-linux.html.

Recommended Performance Settings#

We maintain YAML configuration files with recommended performance settings in the `examples/configs` directory. These config files are present in the TensorRT LLM container at the path `/app/tensorrt_llm/examples/configs`. You can use these out-of-the-box, or adjust them to your specific use case.

For low-latency use cases:

```text
TRTLLM_DIR=/app/tensorrt_llm # change as needed to match your environment
EXTRA_LLM_API_FILE=${TRTLLM_DIR}/examples/configs/curated/gpt-oss-120b-latency.yaml
```

Note: if you don’t have access to the source code locally, you can manually create the YAML config file using the code in the dropdown below.

Show code

```text
EXTRA_LLM_API_FILE=/tmp/config.yml

cat << EOF > ${EXTRA_LLM_API_FILE}

max_batch_size: 64
max_num_tokens: 16384
tensor_parallel_size: 8
moe_expert_parallel_size: 1
trust_remote_code: true
cuda_graph_config:
  enable_padding: true
  max_batch_size: 64
moe_config:
  backend: TRTLLM
stream_interval: 20
num_postprocess_workers: 4
EOF
```

For max-throughput use cases:

```text
TRTLLM_DIR=/app/tensorrt_llm # change as needed to match your environment
EXTRA_LLM_API_FILE=${TRTLLM_DIR}/examples/configs/curated/gpt-oss-120b-throughput.yaml
```

Note: if you don’t have access to the source code locally, you can manually create the YAML config file using the code in the dropdown below.

Show code

```text
EXTRA_LLM_API_FILE=/tmp/config.yml

cat << EOF > ${EXTRA_LLM_API_FILE}

max_batch_size: 720 # Depends on max_sequence_length
max_num_tokens: 16384
tensor_parallel_size: 2
moe_expert_parallel_size: 2
trust_remote_code: true
enable_attention_dp: true
cuda_graph_config:
  enable_padding: true
  max_batch_size: 720
moe_config:
  backend: TRTLLM
stream_interval: 20
num_postprocess_workers: 4
attention_dp_config:
  enable_balance: true
  batching_wait_iters: 50
  timeout_iters: 1
EOF
```

Launch the TensorRT LLM Server#

Below is an example command to launch the TensorRT LLM server with the GPT-OSS model from within the container. The command is specifically configured for the 1024/1024 Input/Output Sequence Length test. The explanation of each flag is shown in the “LLM API Options (YAML Configuration)” section.

```text
trtllm-serve openai/gpt-oss-120b --host 0.0.0.0 --port 8000 --config ${EXTRA_LLM_API_FILE}
```

After the server is set up, the client can now send prompt requests to the server and receive results.

LLM API Options (YAML Configuration)#

These options provide control over TensorRT LLM’s behavior and are set within the YAML file passed to the `trtllm-serve` command via the `--config` argument.

`tensor_parallel_size`#

Description: Sets the tensor-parallel size. This should typically match the number of GPUs you intend to use for a single model instance.

`moe_expert_parallel_size`#

Description: Sets the expert-parallel size for Mixture-of-Experts (MoE) models. Like `tensor_parallel_size`, this should generally match the number of GPUs you’re using. This setting has no effect on non-MoE models.

`kv_cache_free_gpu_memory_fraction`#

Description: A value between `0.0` and `1.0` that specifies the fraction of free GPU memory to reserve for the KV cache after the model is loaded. Since memory usage can fluctuate, this buffer helps prevent out-of-memory (OOM) errors.

Recommendation: If you experience OOM errors, try reducing this value to `0.7` or lower.

`max_batch_size`#

Description: The maximum number of user requests that can be grouped into a single batch for processing. The actual max batch size that can be achieved depends on total sequence length (input + output) and GPU memory available for KV cache.

`max_num_tokens`#

Description: The maximum total number of tokens (across all requests) allowed inside a single scheduled batch. All input tokens (prefill phase) per request and 1 output token per decode request count towards this threshold.

`max_seq_len`#

Description: The maximum possible sequence length for a single request, including both input and generated output tokens. If not set, it will be inferred from model config.

`trust_remote_code`#

Description: Allows TensorRT-LLM to download models and tokenizers from Hugging Face. This flag is passed directly to the Hugging Face API.

`cuda_graph_config`#

Description: A section for configuring CUDA graphs to optimize performance.

Options:

`enable_padding`: If `"true"`, input batches are padded to the nearest `cuda_graph_batch_size`. This can significantly improve performance.

Default: `false`

`max_batch_size`: Sets the maximum batch size for which a CUDA graph will be created.

Default: `0`

Recommendation: Set this to the same value as the `--max_batch_size` command-line option.

`moe_config`#

Description: Configuration for Mixture-of-Experts (MoE) models.

Options:

`backend`: The backend to use for MoE operations.
Default: `CUTLASS`

See the `TorchLlmArgs` class for the full list of options which can be used in the YAML configuration file.

Testing API Endpoint#

Basic Test#

Start a new terminal on the host to test the TensorRT-LLM server you just launched.

You can query the health/readiness of the server using:

```text
curl -s -o /dev/null -w "Status: %{http_code}\n" "http://localhost:8000/health"
```

When the `Status:200` code is returned, the server is ready for queries. Note that the very first query may take longer due to initialization and compilation.

After the TensorRT LLM server is set up and shows Application startup complete, you can send requests to the server.

```text
curl http://localhost:8000/v1/chat/completions -H "Content-Type: application/json"  -d '{
    "model": "openai/gpt-oss-120b",
    "messages": [
        {
            "role": "user",
            "content": "Where is New York?"
        }
    ],
    "max_tokens": 1024,
    "top_p": 1.0
}' -w "\n"
```

Here is an example response, showing that the TensorRT LLM server reasons and answers the questions.

```text
{"id":"chatcmpl-c5bf51b5cab94e10ba5da5266d12ee59","object":"chat.completion","created":1755815898,"model":"openai/gpt-oss-120b","choices":[{"index":0,"message":{"role":"assistant","content":"analysisThe user asks: \"Where is New York?\" Likely they want location info. Provide answer: New York State in northeastern US, New York City on the east coast, coordinates, etc. Provide context.assistantfinal**New York** can refer to two related places in the United States:\n\n| What it is | Where it is | Approx. coordinates | How to picture it |\n|------------|------------|--------------------|-------------------|\n| **New York State** | The northeastern corner of the United States, bordered by **Vermont, Massachusetts, Connecticut, New Jersey, Pennsylvania, and the Canadian provinces of Ontario and Quebec**. | 42.7° N, 75.5° W (roughly the state’s geographic centre) | A roughly rectangular state that stretches from the Atlantic Ocean in the southeast to the Adirondack Mountains and the Great Lakes region in the north. |\n| **New York City (NYC)** | The largest city in the state, located on the **southern tip of the state** where the **Hudson River meets the Atlantic Ocean**. It occupies five boroughs: Manhattan, Brooklyn, Queens, The Bronx, and Staten Island. | 40.7128° N, 74.0060° W | A dense, world‑famous metropolis that sits on a series of islands (Manhattan, Staten Island, parts of the Bronx) and the mainland (Brooklyn and Queens). |\n\n### Quick geographic context\n- **On a map of the United States:** New York State is in the **Northeast** region, just east of the Great Lakes and north of Pennsylvania.  \n- **From Washington, D.C.:** Travel roughly **225 mi (360 km) northeast**.  \n- **From Boston, MA:** Travel about **215 mi (350 km) southwest**.  \n- **From Toronto, Canada:** Travel about **500 mi (800 km) southeast**.\n\n### Travel tips\n- **By air:** Major airports include **John F. Kennedy International (JFK)**, **LaGuardia (LGA)**, and **Newark Liberty International (EWR)** (the latter is actually in New Jersey but serves the NYC metro area).  \n- **By train:** Amtrak’s **Northeast Corridor** runs from **Boston → New York City → Washington, D.C.**  \n- **By car:** Interstates **I‑87** (north‑south) and **I‑90** (east‑west) are the primary highways crossing the state.\n\n### Fun fact\n- The name “**New York**” was given by the English in 1664, honoring the Duke of York (later King James II). The city’s original Dutch name was **“New Amsterdam.”**\n\nIf you need more specific directions (e.g., how to get to a particular neighborhood, landmark, or the state capital **Albany**), just let me know!","reasoning_content":null,"tool_calls":[]},"logprobs":null,"finish_reason":"stop","stop_reason":null,"mm_embedding_handle":null,"disaggregated_params":null,"avg_decoded_tokens_per_iter":1.0}],"usage":{"prompt_tokens":72,"total_tokens":705,"completion_tokens":633},"prompt_token_ids":null}
```

Troubleshooting Tips#

If you encounter CUDA out-of-memory errors, try reducing `max_batch_size` or `max_seq_len`.

Ensure your model checkpoints are compatible with the expected format.

For performance issues, check GPU utilization with nvidia-smi while the server is running.

If the container fails to start, verify that the NVIDIA Container Toolkit is properly installed.

For connection issues, make sure the server port (`8000` in this guide) is not being used by another application.

Running Evaluations to Verify Accuracy (Optional)#

We use OpenAI’s official evaluation tool to test the model’s accuracy. For more information see gpt-oss-eval.
With the added support of Chat Completions and Responses API in `trtllm-serve`, `gpt_oss.evals` works directly without any modifications.

You need to set `enable_attention_dp`, `tp_size`, `ep_size`, `max_batch_size` and `max_num_tokens` when launching the trtllm server and set `reasoning-effort` when launching evaluation in gpt-oss. Below are some reference configurations for accuracy evaluation on B200.

| reasoning-effort | parallel configuration | max_batch_size | max_num_tokens |
| --- | --- | --- | --- |
| low/medium | DEP8 / DEP4 | 128 | 32768 |
| high | DEP8 / DEP4 | 2 | 133120 |
| low/medium | TP8 / TP4 | 1024 | 32768 |
| high | TP8 / TP4 | 720 | 133120 |

Below is an example command for evaluating the accuracy of gpt-oss-120b with low and medium reasoning-effort on GPQA and AIME2025.

```text
# execute this command in gpt-oss
python -m gpt_oss.evals \
  --sampler chat_completions \
  --eval gpqa,aime25 \
  --model gpt-oss-120b \
  --reasoning-effort low,medium
```

Benchmarking Performance#

To benchmark the performance of your TensorRT-LLM server you can leverage the built-in `benchmark_serving.py` script. To do this, first create a wrapper `bench.sh` script.

```text
cat <<'EOF' > bench.sh
#!/usr/bin/env bash
set -euo pipefail

concurrency_list="32 64 128 256 512 1024 2048 4096"
multi_round=5
isl=1024
osl=1024
result_dir=/tmp/gpt_oss_output

for concurrency in ${concurrency_list}; do
    num_prompts=$((concurrency * multi_round))
    python -m tensorrt_llm.serve.scripts.benchmark_serving \
        --model openai/gpt-oss-120b \
        --backend openai \
        --dataset-name "random" \
        --random-input-len ${isl} \
        --random-output-len ${osl} \
        --random-prefix-len 0 \
        --random-ids \
        --num-prompts ${num_prompts} \
        --max-concurrency ${concurrency} \
        --ignore-eos \
        --tokenize-on-client \
        --percentile-metrics "ttft,tpot,itl,e2el"
done
EOF
chmod +x bench.sh
```

To achieve max throughput, with attention DP on, one needs to sweep up to `concurrency=max_batch_size*num_gpus`.

If you want to save the results to a file add the following options.

```text
--save-result \
--result-dir "${result_dir}" \
--result-filename "concurrency_${concurrency}.json"
```

For more benchmarking options see benchmark_serving.py

Run `bench.sh` to begin a serving benchmark. This will take a long time if you run all the concurrencies mentioned in the above `bench.sh` script.

```text
./bench.sh
```

Sample TensorRT-LLM serving benchmark output. Your results may vary due to ongoing software optimizations.

```text
============ Serving Benchmark Result ============
Successful requests:                      16
Benchmark duration (s):                   17.66
Total input tokens:                       16384
Total generated tokens:                   16384
Request throughput (req/s):               [result]
Output token throughput (tok/s):          [result]
Total Token throughput (tok/s):           [result]
User throughput (tok/s):                  [result]
---------------Time to First Token----------------
Mean TTFT (ms):                           [result]
Median TTFT (ms):                         [result]
P99 TTFT (ms):                            [result]
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                           [result]
Median TPOT (ms):                         [result]
P99 TPOT (ms):                            [result]
---------------Inter-token Latency----------------
Mean ITL (ms):                            [result]
Median ITL (ms):                          [result]
P99 ITL (ms):                             [result]
----------------End-to-end Latency----------------
Mean E2EL (ms):                           [result]
Median E2EL (ms):                         [result]
P99 E2EL (ms):                            [result]
==================================================
```

Key Metrics#

Time to First Token (TTFT)#

The typical time elapsed from when a request is sent until the first output token is generated.

Time Per Output Token (TPOT) and Inter-Token Latency (ITL)#

TPOT is the typical time required to generate each token after the first one.

ITL is the typical time delay between the completion of one token and the completion of the next.

Both TPOT and ITL ignore TTFT.

For a single request, ITLs are the time intervals between tokens, while TPOT is the average of those intervals:

\text{TPOT (1 request)} = \text{Avg(ITL)} = \frac{\text{E2E latency} - \text{TTFT}}{\text{Num Output Tokens} - 1}

Across different requests, average TPOT is the mean of each request’s TPOT (all requests weighted equally), while average ITL is token-weighted (all tokens weighted equally):

\text{Avg TPOT (N requests)} = \frac{\text{TPOT}_1 + \text{TPOT}_2 + \cdots + \text{TPOT}_N}{N}

\text{Avg ITL (N requests)} = \frac{\text{Sum of all ITLs across requests}}{\text{Num Output Tokens across requests}}

End-to-End (E2E) Latency#

The typical total time from when a request is submitted until the final token of the response is received.

Total Token Throughput#

The combined rate at which the system processes both input (prompt) tokens and output (generated) tokens.

\text{Total TPS} = \frac{\text{Total input tokens}+\text{Total generated tokens}}{T_{last} - T_{first}}

Tokens Per Second (TPS) or Output Token Throughput#

how many output tokens the system generates each second.

\text{TPS} = \frac{\text{Total generated tokens}}{T_{last} - T_{first}}

Preconfigured Recipes#

The following sections help you pick a known-good `trtllm-serve--config` for your target GPU and traffic pattern.

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
