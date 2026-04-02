Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/deployment-guide/quick-start-recipe-for-deepseek-r1-on-trtllm.md

* [Model Recipes](index.md)
* Quick Start Recipe for DeepSeek R1 on TensorRT LLM - Blackwell & Hopper Hardware

# Quick Start Recipe for DeepSeek R1 on TensorRT LLM - Blackwell & Hopper Hardware[#](#quick-start-recipe-for-deepseek-r1-on-tensorrt-llm-blackwell-hopper-hardware "Link to this heading")

## Introduction[#](#introduction "Link to this heading")

This deployment guide provides step-by-step instructions for running the DeepSeek R1 model using TensorRT LLM with FP8 and NVFP4 quantization, optimized for NVIDIA GPUs. It covers the complete setup required; from accessing model weights and preparing the software environment to configuring TensorRT LLM parameters, launching the server, and validating inference output.

The guide is intended for developers and practitioners seeking high-throughput or low-latency inference using NVIDIA’s accelerated stack—starting with the PyTorch container from NGC, then installing TensorRT LLM for model serving, FlashInfer for optimized CUDA kernels, and ModelOpt to enable FP8 and NVFP4 quantized execution.

## Prerequisites[#](#prerequisites "Link to this heading")

* GPU: NVIDIA Blackwell or Hopper Architecture
* OS: Linux
* Drivers: CUDA Driver 575 or Later
* Docker with NVIDIA Container Toolkit installed
* Python3 and python3-pip (Optional, for accuracy evaluation only)

## Models[#](#models "Link to this heading")

* FP8 model: [DeepSeek-R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528)
* NVFP4 model: [DeepSeek-R1-0528-FP4](https://huggingface.co/nvidia/DeepSeek-R1-0528-FP4)

## MoE Backend Support Matrix[#](#moe-backend-support-matrix "Link to this heading")

There are multiple MOE backends inside TRT-LLM, not all of them supporting every precision on every GPUs. Here are the support matrix of the MOE backends.

| device | Checkpoint | Supported moe\_backend |
| --- | --- | --- |
| H100/H200 | FP8 | CUTLASS |
| B200/GB200 EP<=8 | NVFP4 | CUTLASS, TRTLLM |
| B200/GB200 EP<=8 | FP8 | DEEPGEMM |
| GB200 NVL72 EP>8 | NVFP4 | WIDEEP |
| GB200 NVL72 EP>8 | FP8 | WIDEEP without EPLB |

The default moe backend is `CUTLASS`, so for the combination which is not supported by `CUTLASS`, one must set the `moe_config.backend` explicitly to run the model.

## Deployment Steps[#](#deployment-steps "Link to this heading")

### Run Docker Container[#](#run-docker-container "Link to this heading")

Run the docker container using the TensorRT LLM NVIDIA NGC image.

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

If you want to use latest main branch, you can choose to build from source to install TensorRT LLM, the steps refer to <https://nvidia.github.io/TensorRT-LLM/latest/installation/build-from-source-linux.md>

### Creating the TRT-LLM Server config[#](#creating-the-trt-llm-server-config "Link to this heading")

We create a YAML configuration file /tmp/config.yml for the TensorRT LLM Server and populate it with the following recommended performance settings.

```
EXTRA_LLM_API_FILE=/tmp/config.yml

cat << EOF > ${EXTRA_LLM_API_FILE}
enable_attention_dp: true
cuda_graph_config:
  enable_padding: true
  max_batch_size: 128
kv_cache_config:
  dtype: fp8
stream_interval: 10
speculative_config:
  decoding_type: MTP
  num_nextn_predict_layers: 1
EOF
```

For FP8 model, we need extra `moe_config`:

```
EXTRA_LLM_API_FILE=/tmp/config.yml

cat << EOF > ${EXTRA_LLM_API_FILE}
enable_attention_dp: true
cuda_graph_config:
  enable_padding: true
  max_batch_size: 128
kv_cache_config:
  dtype: fp8
stream_interval: 10
speculative_config:
  decoding_type: MTP
  num_nextn_predict_layers: 1
moe_config:
  backend: DEEPGEMM
  max_num_tokens: 3200
EOF
```

### Launch the TRT-LLM Server[#](#launch-the-trt-llm-server "Link to this heading")

Below is an example command to launch the TRT-LLM server with the DeepSeek-R1 model from within the container. The command is specifically configured for the 1024/1024 Input/Output Sequence Length test. The explanation of each flag is shown in the “Configs and Parameters” section.

```
trtllm-serve deepseek-ai/DeepSeek-R1-0528 \
    --host 0.0.0.0 \
    --port 8000 \
    --backend pytorch \
    --max_batch_size 1024 \
    --max_num_tokens 3200 \
    --max_seq_len 2048 \
    --kv_cache_free_gpu_memory_fraction 0.8 \
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

**Description:** Tells TensorRT LLM to use the **pytorch** backend.

#### `--max_batch_size`[#](#max-batch-size "Link to this heading")

* **Description:** The maximum number of user requests that can be grouped into a single batch for processing.

#### `--max_num_tokens`[#](#max-num-tokens "Link to this heading")

* **Description:** The maximum total number of tokens (across all requests) allowed inside a single scheduled batch.

#### `--max_seq_len`[#](#max-seq-len "Link to this heading")

* **Description:** The maximum possible sequence length for a single request, including both input and generated output tokens.

#### `--trust_remote_code`[#](#trust-remote-code "Link to this heading")

**Description:** Allows TensorRT LLM to download models and tokenizers from Hugging Face. This flag is passed directly to the Hugging Face API.

#### Extra LLM API Options (YAML Configuration)[#](#extra-llm-api-options-yaml-configuration "Link to this heading")

These options provide finer control over performance and are set within a YAML file passed to the `trtllm-serve` command via the `--extra_llm_api_options` argument.

#### `kv_cache_config`[#](#kv-cache-config "Link to this heading")

* **Description**: A section for configuring the Key-Value (KV) cache.
* **Options**:

  + `dtype`: Sets the data type for the KV cache.
    **Default**: `"auto"` (uses the data type specified in the model checkpoint).

#### `cuda_graph_config`[#](#cuda-graph-config "Link to this heading")

* **Description**: A section for configuring CUDA graphs to optimize performance.
* **Options**:

  + `enable_padding`: If `"true"`, input batches are padded to the nearest `cuda_graph_batch_size`. This can significantly improve performance.

    **Default**: `false`
  + `max_batch_size`: Sets the maximum batch size for which a CUDA graph will be created.

    **Default**: `0`

    **Recommendation**: Set this to the same value as the `--max_batch_size` command-line option.
  + `batch_sizes`: A specific list of batch sizes to create CUDA graphs for.

    **Default**: `None`

#### `moe_config`[#](#moe-config "Link to this heading")

* **Description**: Configuration for Mixture-of-Experts (MoE) models.
* **Options**:

  + `backend`: The backend to use for MoE operations.
    **Default**: `CUTLASS`

#### `attention_backend`[#](#attention-backend "Link to this heading")

* **Description**: The backend to use for attention calculations.
* **Default**: `TRTLLM`

See the [`TorchLlmArgs` class](https://nvidia.github.io/TensorRT-LLM/llm-api/reference.md#tensorrt_llm.llmapi.TorchLlmArgs) for the full list of options which can be used in the `extra_llm_api_options`.

### Wide Expert Parallelism[#](#wide-expert-parallelism "Link to this heading")

Add the following fields to the YAML configuration file `/tmp/config.yml` to enable wide EP:

```
moe_config:
    backend: WIDEEP
    max_num_tokens: 9216
    load_balancer:  # configure online EP balancer
      num_slots: 288
      layer_updates_per_iter: 1
```

Refer to the wide EP [examples](https://github.com/NVIDIA/TensorRT-LLM/tree/main/examples/wide_ep) for more details.

## Testing API Endpoint[#](#testing-api-endpoint "Link to this heading")

### Basic Test[#](#basic-test "Link to this heading")

Start a new terminal on the host to test the TensorRT LLM server you just launched.

You can query the health/readiness of the server using:

```
curl -s -o /dev/null -w "Status: %{http_code}\n" "http://localhost:8000/health"
```

When the `Status: 200` code is returned, the server is ready for queries. Note that the very first query may take longer due to initialization and compilation.

After the TRT-LLM server is set up and shows Application startup complete, you can send requests to the server.

```
curl http://localhost:8000/v1/completions -H "Content-Type: application/json"  -d '{
      "model": "deepseek-ai/DeepSeek-R1-0528",
      "prompt": "Where is New York?",
      "max_tokens": 16,
      "temperature": 0
}'
```

Here is an example response, showing that the TRT-LLM server returns “New York is a state located in the northeastern United States. It is bordered by”, completing the input sequence.

```
{"id":"cmpl-e728f08114c042309efeae4df86a50ca","object":"text_completion","created":1754294810,"model":"deepseek-ai/DeepSeek-R1-0528","choices":[{"index":0,"text":" / by Megan Stine ; illustrated by John Hinderliter.\n\nBook | Gross","token_ids":null,"logprobs":null,"context_logits":null,"finish_reason":"length","stop_reason":null,"disaggregated_params":null}],"usage":{"prompt_tokens":6,"total_tokens":22,"completion_tokens":16},"prompt_token_ids":null}
```

### Troubleshooting Tips[#](#troubleshooting-tips "Link to this heading")

* If you encounter CUDA out-of-memory errors, try reducing `max_batch_size` or `max_seq_len`.

  + For running input/output sequence lengths of 8K/1K on H200, there is a known CUDA Out-Of-Memory issue caused by the PyTorch CUDA Caching Allocator fragmenting memory. As a workaround, you can set the environment variable `PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:8192`. For more details, please refer to the [PyTorch documentation on optimizing memory usage](https://docs.pytorch.org/docs/stable/notes/cuda.md#optimizing-memory-usage-with-pytorch-cuda-alloc-conf).
* Ensure your model checkpoints are compatible with the expected format.
* For performance issues, check GPU utilization with nvidia-smi while the server is running.
* If the container fails to start, verify that the NVIDIA Container Toolkit is properly installed.
* For connection issues, make sure the server port (`8000` in this guide) is not being used by another application.

### Running Evaluations to Verify Accuracy (Optional)[#](#running-evaluations-to-verify-accuracy-optional "Link to this heading")

We use the `lm-eval` tool to test the model’s accuracy. For more information see [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness).

To run the evaluation harness exec into the running TensorRT LLM container and install with this command:

```
docker exec -it tensorrt_llm /bin/bash

pip install -U lm-eval
```

FP8 command for GSM8K:

* Note: The tokenizer will add BOS (beginning of sentence token) before input prompt by default which leads to accuracy regression on GSM8K task for DeepSeek R1 model. So, set `add_special_tokens=False` to avoid it.

```
MODEL_PATH=deepseek-ai/DeepSeek-R1-0528

lm_eval --model local-completions  --tasks gsm8k --batch_size 256 --gen_kwargs temperature=0.0,add_special_tokens=False --num_fewshot 5 --model_args model=${MODEL_PATH},base_url=http://localhost:8000/v1/completions,num_concurrent=32,max_retries=20,tokenized_requests=False --log_samples --output_path trtllm.fp8.gsm8k
```

Sample result in Blackwell:

```
|Tasks|Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|-----|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|gsm8k|      3|flexible-extract|     5|exact_match|↑  |0.9538|±  |0.0058|
|     |       |strict-match    |     5|exact_match|↑  |0.9500|±  |0.0060|
```

FP4 command for GSM8K:

* Note: The tokenizer will add BOS before input prompt by default, which leads to accuracy regression on GSM8K task for DeepSeek R1 model. So set `add_special_tokens=False` to avoid it.

```
MODEL_PATH=nvidia/DeepSeek-R1-0528-FP4

lm_eval --model local-completions  --tasks gsm8k --batch_size 256 --gen_kwargs temperature=0.0,add_special_tokens=False --num_fewshot 5 --model_args model=${MODEL_PATH},base_url=http://localhost:8000/v1/completions,num_concurrent=32,max_retries=20,tokenized_requests=False --log_samples --output_path trtllm.fp4.gsm8k
```

Sample result in Blackwell:

```
|Tasks|Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|-----|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|gsm8k|      3|flexible-extract|     5|exact_match|↑  |0.9462|±  |0.0062|
|     |       |strict-match    |     5|exact_match|↑  |0.9447|±  |0.0063|
```

## Benchmarking Performance[#](#benchmarking-performance "Link to this heading")

To benchmark the performance of your TensorRT LLM server you can leverage the built-in “benchmark\_serving.py” script. To do this first creating a wrapper [bench.sh](http://bench.sh) script.

```
cat <<EOF >  bench.sh
concurrency_list="32 64 128 256 512 1024 2048 4096"
multi_round=5
isl=1024
osl=1024
result_dir=/tmp/deepseek_r1_output

for concurrency in ${concurrency_list}; do
    num_prompts=$((concurrency * multi_round))
    python -m tensorrt_llm.serve.scripts.benchmark_serving \
        --model deepseek-ai/DeepSeek-R1-0528 \
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

To benchmark the FP4 model, replace `--model deepseek-ai/DeepSeek-R1-0528` with `--model nvidia/DeepSeek-R1-0528-FP4`.

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

Sample TensorRT LLM serving benchmark output. Your results may vary due to ongoing software optimizations.

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

Model Recipes](index.md "previous page")
[next

Quick Start Recipe for Llama3.3 70B on TensorRT LLM - Blackwell & Hopper Hardware](quick-start-recipe-for-llama3.3-70b-on-trtllm.md "next page")

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
    - [`kv_cache_config`](#kv-cache-config)
    - [`cuda_graph_config`](#cuda-graph-config)
    - [`moe_config`](#moe-config)
    - [`attention_backend`](#attention-backend)
  + [Wide Expert Parallelism](#wide-expert-parallelism)
* [Testing API Endpoint](#testing-api-endpoint)
  + [Basic Test](#basic-test)
  + [Troubleshooting Tips](#troubleshooting-tips)
  + [Running Evaluations to Verify Accuracy (Optional)](#running-evaluations-to-verify-accuracy-optional)
* [Benchmarking Performance](#benchmarking-performance)
  + [Key Metrics](#key-metrics)