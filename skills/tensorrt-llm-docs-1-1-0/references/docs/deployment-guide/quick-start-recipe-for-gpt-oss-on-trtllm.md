Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/deployment-guide/quick-start-recipe-for-gpt-oss-on-trtllm.md

* [Model Recipes](index.md)
* Quick Start Recipe for GPT-OSS on TensorRT-LLM - Blackwell Hardware

# Quick Start Recipe for GPT-OSS on TensorRT-LLM - Blackwell Hardware[#](#quick-start-recipe-for-gpt-oss-on-tensorrt-llm-blackwell-hardware "Link to this heading")

## Introduction[#](#introduction "Link to this heading")

This deployment guide provides step-by-step instructions for running the GPT-OSS model using TensorRT-LLM, optimized for NVIDIA GPUs. It covers the complete setup required; from accessing model weights and preparing the software environment to configuring TensorRT-LLM parameters, launching the server, and validating inference output.

The guide is intended for developers and practitioners seeking high-throughput or low-latency inference using NVIDIA’s accelerated stack—starting with the PyTorch container from NGC, then installing TensorRT-LLM for model serving.

## Prerequisites[#](#prerequisites "Link to this heading")

* GPU: NVIDIA Blackwell Architecture
* OS: Linux
* Drivers: CUDA Driver 575 or Later
* Docker with NVIDIA Container Toolkit installed
* Python3 and python3-pip (Optional, for accuracy evaluation only)

## Models[#](#models "Link to this heading")

* MXFP4 model: [GPT-OSS-120B](https://huggingface.co/openai/gpt-oss-120b)

## MoE Backend Support Matrix[#](#moe-backend-support-matrix "Link to this heading")

There are multiple MOE backends inside TRT-LLM. Here are the support matrix of the MOE backends.

| Device | Activation Type | MoE Weights Type | MoE Backend | Use Case |
| --- | --- | --- | --- | --- |
| B200/GB200 | MXFP8 | MXFP4 | TRTLLM | Low Latency |
| B200/GB200 | MXFP8 | MXFP4 | CUTLASS | Max Throughput |

The default moe backend is `CUTLASS`, so for the combination which is not supported by `CUTLASS`, one must set the `moe_config.backend` explicitly to run the model.

## Deployment Steps[#](#deployment-steps "Link to this heading")

### Run Docker Container[#](#run-docker-container "Link to this heading")

Run the docker container using the TensorRT-LLM NVIDIA NGC image.

```
docker run --rm -it \
--ipc=host \
--gpus all \
-p 8000:8000 \
-v ~/.cache:/root/.cache:rw \
--name tensorrt_llm \
nvcr.io/nvidia/tensorrt-llm/release:1.0.0rc6 \
/bin/bash
```

Note:

* The command mounts your user `.cache` directory to save the downloaded model checkpoints which are saved to `~/.cache/huggingface/hub/` by default. This prevents having to redownload the weights each time you rerun the container. If the `~/.cache` directory doesn’t exist please create it using `$ mkdir ~/.cache`.
* You can mount additional directories and paths using the `-v <host_path>:<container_path>` flag if needed, such as mounting the downloaded weight paths.
* The command also maps port `8000` from the container to your host so you can access the LLM API endpoint from your host
* See the <https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tensorrt-llm/containers/release/tags> for all the available containers. The containers published in the main branch weekly have `rcN` suffix, while the monthly release with QA tests has no `rcN` suffix. Use the `rc` release to get the latest model and feature support.

If you want to use latest main branch, you can choose to build from source to install TensorRT-LLM, the steps refer to <https://nvidia.github.io/TensorRT-LLM/latest/installation/build-from-source-linux.md>.

### Creating the TRT-LLM Server config[#](#creating-the-trt-llm-server-config "Link to this heading")

We create a YAML configuration file `/tmp/config.yml` for the TensorRT-LLM Server and populate it with the following recommended performance settings.

For low-latency with `TRTLLM` MOE backend:

```
EXTRA_LLM_API_FILE=/tmp/config.yml

cat << EOF > ${EXTRA_LLM_API_FILE}
enable_attention_dp: false
cuda_graph_config:
  enable_padding: true
  max_batch_size: 720
moe_config:
    backend: TRTLLM
stream_interval: 20
num_postprocess_workers: 4
EOF
```

For max-throughput with `CUTLASS` MOE backend:

```
EXTRA_LLM_API_FILE=/tmp/config.yml

cat << EOF > ${EXTRA_LLM_API_FILE}
enable_attention_dp: true
cuda_graph_config:
  enable_padding: true
  max_batch_size: 720
moe_config:
    backend: CUTLASS
stream_interval: 20
num_postprocess_workers: 4
attention_dp_config:
    enable_balance: true
    batching_wait_iters: 50
    timeout_iters: 1
EOF
```

### Launch the TRT-LLM Server[#](#launch-the-trt-llm-server "Link to this heading")

Below is an example command to launch the TRT-LLM server with the GPT-OSS model from within the container. The command is specifically configured for the 1024/1024 Input/Output Sequence Length test. The explanation of each flag is shown in the “Configs and Parameters” section.

```
trtllm-serve openai/gpt-oss-120b \
    --host 0.0.0.0 \
    --port 8000 \
    --backend pytorch \
    --max_batch_size 720 \
    --max_num_tokens 16384 \
    --kv_cache_free_gpu_memory_fraction 0.9 \
    --tp_size 8 \
    --ep_size 8 \
    --trust_remote_code \
    --extra_llm_api_options ${EXTRA_LLM_API_FILE}
```

After the server is set up, the client can now send prompt requests to the server and receive results.

### Configs and Parameters[#](#configs-and-parameters "Link to this heading")

These options are used directly on the command line when you start the `trtllm-serve` process.

#### `--tp_size`[#](#tp-size "Link to this heading")

* **Description:** Sets the **tensor-parallel size**. This should typically match the number of GPUs you intend to use for a single model instance.

#### `--ep_size`[#](#ep-size "Link to this heading")

* **Description:** Sets the **expert-parallel size** for Mixture-of-Experts (MoE) models. Like `tp_size`, this should generally match the number of GPUs you’re using. This setting has no effect on non-MoE models.

#### `--kv_cache_free_gpu_memory_fraction`[#](#kv-cache-free-gpu-memory-fraction "Link to this heading")

* **Description:** A value between `0.0` and `1.0` that specifies the fraction of free GPU memory to reserve for the KV cache after the model is loaded. Since memory usage can fluctuate, this buffer helps prevent out-of-memory (OOM) errors.
* **Recommendation:** If you experience OOM errors, try reducing this value to `0.7` or lower.

#### `--backend pytorch`[#](#backend-pytorch "Link to this heading")

* **Description:** Tells TensorRT-LLM to use the **pytorch** backend.

#### `--max_batch_size`[#](#max-batch-size "Link to this heading")

* **Description:** The maximum number of user requests that can be grouped into a single batch for processing. The actual max batch size that can be achieved depends on total sequence length (input + output).

#### `--max_num_tokens`[#](#max-num-tokens "Link to this heading")

* **Description:** The maximum total number of tokens (across all requests) allowed inside a single scheduled batch.

#### `--max_seq_len`[#](#max-seq-len "Link to this heading")

* **Description:** The maximum possible sequence length for a single request, including both input and generated output tokens. We won’t specifically set it. It will be inferred from model config.

#### `--trust_remote_code`[#](#trust-remote-code "Link to this heading")

* **Description:** Allows TensorRT-LLM to download models and tokenizers from Hugging Face. This flag is passed directly to the Hugging Face API.

#### Extra LLM API Options (YAML Configuration)[#](#extra-llm-api-options-yaml-configuration "Link to this heading")

These options provide finer control over performance and are set within a YAML file passed to the `trtllm-serve` command via the `--extra_llm_api_options` argument.

#### `cuda_graph_config`[#](#cuda-graph-config "Link to this heading")

* **Description**: A section for configuring CUDA graphs to optimize performance.
* **Options**:

  + `enable_padding`: If `"true"`, input batches are padded to the nearest `cuda_graph_batch_size`. This can significantly improve performance.

    **Default**: `false`
  + `max_batch_size`: Sets the maximum batch size for which a CUDA graph will be created.

    **Default**: `0`

    **Recommendation**: Set this to the same value as the `--max_batch_size` command-line option.

#### `moe_config`[#](#moe-config "Link to this heading")

* **Description**: Configuration for Mixture-of-Experts (MoE) models.
* **Options**:

  + `backend`: The backend to use for MoE operations.
    **Default**: `CUTLASS`

See the [`TorchLlmArgs` class](https://nvidia.github.io/TensorRT-LLM/llm-api/reference.md#tensorrt_llm.llmapi.TorchLlmArgs) for the full list of options which can be used in the `extra_llm_api_options`.

## Testing API Endpoint[#](#testing-api-endpoint "Link to this heading")

### Basic Test[#](#basic-test "Link to this heading")

Start a new terminal on the host to test the TensorRT-LLM server you just launched.

You can query the health/readiness of the server using:

```
curl -s -o /dev/null -w "Status: %{http_code}\n" "http://localhost:8000/health"
```

When the `Status: 200` code is returned, the server is ready for queries. Note that the very first query may take longer due to initialization and compilation.

After the TRT-LLM server is set up and shows Application startup complete, you can send requests to the server.

```
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

Here is an example response, showing that the TRT-LLM server reasons and answers the questions.

```
{"id":"chatcmpl-c5bf51b5cab94e10ba5da5266d12ee59","object":"chat.completion","created":1755815898,"model":"openai/gpt-oss-120b","choices":[{"index":0,"message":{"role":"assistant","content":"analysisThe user asks: \"Where is New York?\" Likely they want location info. Provide answer: New York State in northeastern US, New York City on the east coast, coordinates, etc. Provide context.assistantfinal**New York** can refer to two related places in the United States:\n\n| What it is | Where it is | Approx. coordinates | How to picture it |\n|------------|------------|--------------------|-------------------|\n| **New York State** | The northeastern corner of the United States, bordered by **Vermont, Massachusetts, Connecticut, New Jersey, Pennsylvania, and the Canadian provinces of Ontario and Quebec**. | 42.7° N, 75.5° W (roughly the state’s geographic centre) | A roughly rectangular state that stretches from the Atlantic Ocean in the southeast to the Adirondack Mountains and the Great Lakes region in the north. |\n| **New York City (NYC)** | The largest city in the state, located on the **southern tip of the state** where the **Hudson River meets the Atlantic Ocean**. It occupies five boroughs: Manhattan, Brooklyn, Queens, The Bronx, and Staten Island. | 40.7128° N, 74.0060° W | A dense, world‑famous metropolis that sits on a series of islands (Manhattan, Staten Island, parts of the Bronx) and the mainland (Brooklyn and Queens). |\n\n### Quick geographic context\n- **On a map of the United States:** New York State is in the **Northeast** region, just east of the Great Lakes and north of Pennsylvania.  \n- **From Washington, D.C.:** Travel roughly **225 mi (360 km) northeast**.  \n- **From Boston, MA:** Travel about **215 mi (350 km) southwest**.  \n- **From Toronto, Canada:** Travel about **500 mi (800 km) southeast**.\n\n### Travel tips\n- **By air:** Major airports include **John F. Kennedy International (JFK)**, **LaGuardia (LGA)**, and **Newark Liberty International (EWR)** (the latter is actually in New Jersey but serves the NYC metro area).  \n- **By train:** Amtrak’s **Northeast Corridor** runs from **Boston → New York City → Washington, D.C.**  \n- **By car:** Interstates **I‑87** (north‑south) and **I‑90** (east‑west) are the primary highways crossing the state.\n\n### Fun fact\n- The name “**New York**” was given by the English in 1664, honoring the Duke of York (later King James II). The city’s original Dutch name was **“New Amsterdam.”**\n\nIf you need more specific directions (e.g., how to get to a particular neighborhood, landmark, or the state capital **Albany**), just let me know!","reasoning_content":null,"tool_calls":[]},"logprobs":null,"finish_reason":"stop","stop_reason":null,"mm_embedding_handle":null,"disaggregated_params":null,"avg_decoded_tokens_per_iter":1.0}],"usage":{"prompt_tokens":72,"total_tokens":705,"completion_tokens":633},"prompt_token_ids":null}
```

### Troubleshooting Tips[#](#troubleshooting-tips "Link to this heading")

* If you encounter CUDA out-of-memory errors, try reducing `max_batch_size` or `max_seq_len`.
* Ensure your model checkpoints are compatible with the expected format.
* For performance issues, check GPU utilization with nvidia-smi while the server is running.
* If the container fails to start, verify that the NVIDIA Container Toolkit is properly installed.
* For connection issues, make sure the server port (`8000` in this guide) is not being used by another application.

### Running Evaluations to Verify Accuracy (Optional)[#](#running-evaluations-to-verify-accuracy-optional "Link to this heading")

We use OpenAI’s official evaluation tool to test the model’s accuracy. For more information see [https://github.com/openai/gpt-oss/tree/main/gpt\_oss/evals](#gpt-oss-eval).
With the added support of Chat Completions and Responses API in `trtllm-serve,` `gpt_oss.evals` works directly without any modifications.

You need to set `enable_attention_dp`, `tp_size`, `ep_size`, `max_batch_size` and `max_num_tokens` when launching the trtllm server and set `reasoning-effort` when launching evaluation in gpt-oss. Below are some reference configurations for accuracy evaluation on B200.

| **reasoning-effort** | **parallel configuration** | **max\_batch\_size** | **max\_num\_tokens** |
| --- | --- | --- | --- |
| low/medium | DEP8 / DEP4 | 128 | 32768 |
| high | DEP8 / DEP4 | 2 | 133120 |
| low/medium | TP8 / TP4 | 1024 | 32768 |
| high | TP8 / TP4 | 720 | 133120 |

Below is an example command for evaluating the accuracy of gpt-oss-120b with low and medium reasoning-effort on GPQA and AIME2025.

```
# execute this command in gpt-oss
python -m gpt_oss.evals \
  --sampler chat_completions \
  --eval gpqa,aime25 \
  --model gpt-oss-120b \
  --reasoning-effort low,medium
```

## Benchmarking Performance[#](#benchmarking-performance "Link to this heading")

To benchmark the performance of your TensorRT-LLM server you can leverage the built-in `benchmark_serving.py` script. To do this first creating a wrapper `bench.sh` script.

```
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

To achieve max through-put, with attention DP on, one needs to sweep up to `concurrency = max_batch_size * num_gpus`.

If you want to save the results to a file add the following options.

```
--save-result \
--result-dir "${result_dir}" \
--result-filename "concurrency_${concurrency}.json"
```

For more benchmarking options see [https://github.com/NVIDIA/TensorRT-LLM/blob/main/tensorrt\\_llm/serve/scripts/benchmark\\_serving.py](https://github.com/NVIDIA/TensorRT-LLM/blob/main/tensorrt%5C_llm/serve/scripts/benchmark%5C_serving.py).

Run `bench.sh` to begin a serving benchmark. This will take a long time if you run all the concurrencies mentioned in the above `bench.sh` script.

```
./bench.sh
```

Sample TensorRT-LLM serving benchmark output. Your results may vary due to ongoing software optimizations.

```
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

### Key Metrics[#](#key-metrics "Link to this heading")

* Median Time to First Token (TTFT)

  + The typical time elapsed from when a request is sent until the first output token is generated.
* Median Time Per Output Token (TPOT)

  + The typical time required to generate each token *after* the first one.
* Median Inter-Token Latency (ITL)

  + The typical time delay between the completion of one token and the completion of the next.
* Median End-to-End Latency (E2EL)

  + The typical total time from when a request is submitted until the final token of the response is received.
* Total Token Throughput

  + The combined rate at which the system processes both input (prompt) tokens and output (generated) tokens.

[previous

Quick Start Recipe for Llama4 Scout 17B on TensorRT LLM - Blackwell & Hopper Hardware](quick-start-recipe-for-llama4-scout-on-trtllm.md "previous page")
[next

Supported Models](../models/supported-models.md "next page")

On this page

* [Introduction](#introduction)
* [Prerequisites](#prerequisites)
* [Models](#models)
* [MoE Backend Support Matrix](#moe-backend-support-matrix)
* [Deployment Steps](#deployment-steps)
  + [Run Docker Container](#run-docker-container)
  + [Creating the TRT-LLM Server config](#creating-the-trt-llm-server-config)
  + [Launch the TRT-LLM Server](#launch-the-trt-llm-server)
  + [Configs and Parameters](#configs-and-parameters)
    - [`--tp_size`](#tp-size)
    - [`--ep_size`](#ep-size)
    - [`--kv_cache_free_gpu_memory_fraction`](#kv-cache-free-gpu-memory-fraction)
    - [`--backend pytorch`](#backend-pytorch)
    - [`--max_batch_size`](#max-batch-size)
    - [`--max_num_tokens`](#max-num-tokens)
    - [`--max_seq_len`](#max-seq-len)
    - [`--trust_remote_code`](#trust-remote-code)
    - [Extra LLM API Options (YAML Configuration)](#extra-llm-api-options-yaml-configuration)
    - [`cuda_graph_config`](#cuda-graph-config)
    - [`moe_config`](#moe-config)
* [Testing API Endpoint](#testing-api-endpoint)
  + [Basic Test](#basic-test)
  + [Troubleshooting Tips](#troubleshooting-tips)
  + [Running Evaluations to Verify Accuracy (Optional)](#running-evaluations-to-verify-accuracy-optional)
* [Benchmarking Performance](#benchmarking-performance)
  + [Key Metrics](#key-metrics)