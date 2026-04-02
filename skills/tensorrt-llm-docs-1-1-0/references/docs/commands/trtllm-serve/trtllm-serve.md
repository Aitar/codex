Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/commands/trtllm-serve/trtllm-serve.md

* [trtllm-serve](index.md)
* trtllm-serve

# trtllm-serve[#](#trtllm-serve "Link to this heading")

## About[#](#about "Link to this heading")

The `trtllm-serve` command starts an OpenAI compatible server that supports the following endpoints:

* `/v1/models`
* `/v1/completions`
* `/v1/chat/completions`

For information about the inference endpoints, refer to the [OpenAI API Reference](https://platform.openai.com/docs/api-reference).

The server also supports the following endpoints:

* `/health`
* `/metrics`
* `/version`

The `metrics` endpoint provides runtime-iteration statistics such as GPU memory use and inflight-batching details.

## Starting a Server[#](#starting-a-server "Link to this heading")

The following abbreviated command syntax shows the commonly used arguments to start a server:

```
trtllm-serve <model> [--tp_size <tp> --pp_size <pp> --ep_size <ep> --host <host> --port <port>]
```

For the full syntax and argument descriptions, refer to [Syntax](#syntax).

## Inference Endpoints[#](#inference-endpoints "Link to this heading")

After you start the server, you can send inference requests through completions API and Chat API, which are compatible with corresponding OpenAI APIs. We use [TinyLlama-1.1B-Chat-v1.0](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0) for examples in the following sections.

### Chat API[#](#chat-api "Link to this heading")

You can query Chat API with any http clients, a typical example is OpenAI Python client:

```
 1### :title OpenAI Chat Client
 2
 3from openai import OpenAI
 4
 5client = OpenAI(
 6    base_url="http://localhost:8000/v1",
 7    api_key="tensorrt_llm",
 8)
 9
10response = client.chat.completions.create(
11    model="TinyLlama-1.1B-Chat-v1.0",
12    messages=[{
13        "role": "system",
14        "content": "you are a helpful assistant"
15    }, {
16        "role": "user",
17        "content": "Where is New York?"
18    }],
19    max_tokens=20,
20)
21print(response)
```

Another example uses `curl`:

```
 1#! /usr/bin/env bash
 2
 3curl http://localhost:8000/v1/chat/completions \
 4    -H "Content-Type: application/json" \
 5    -d '{
 6        "model": "TinyLlama-1.1B-Chat-v1.0",
 7        "messages":[{"role": "system", "content": "You are a helpful assistant."},
 8                    {"role": "user", "content": "Where is New York?"}],
 9        "max_tokens": 16,
10        "temperature": 0
11    }'
```

### Completions API[#](#completions-api "Link to this heading")

You can query Completions API with any http clients, a typical example is OpenAI Python client:

```
 1### :title OpenAI Completion Client
 2
 3from openai import OpenAI
 4
 5client = OpenAI(
 6    base_url="http://localhost:8000/v1",
 7    api_key="tensorrt_llm",
 8)
 9
10response = client.completions.create(
11    model="TinyLlama-1.1B-Chat-v1.0",
12    prompt="Where is New York?",
13    max_tokens=20,
14)
15print(response)
```

Another example uses `curl`:

```
 1#! /usr/bin/env bash
 2
 3curl http://localhost:8000/v1/completions \
 4    -H "Content-Type: application/json" \
 5    -d '{
 6        "model": "TinyLlama-1.1B-Chat-v1.0",
 7        "prompt": "Where is New York?",
 8        "max_tokens": 16,
 9        "temperature": 0
10    }'
```

### Multimodal Serving[#](#multimodal-serving "Link to this heading")

For multimodal models, you need to create a configuration file and start the server with additional options due to the following limitations:

* TRT-LLM multimodal is currently not compatible with `kv_cache_reuse`
* Multimodal models require `chat_template`, so only the Chat API is supported

To set up multimodal models:

First, create a configuration file:

```
cat >./extra-llm-api-config.yml<<EOF
kv_cache_config:
    enable_block_reuse: false
EOF
```

Then, start the server with the configuration file:

```
trtllm-serve Qwen/Qwen2-VL-7B-Instruct \
    --extra_llm_api_options ./extra-llm-api-config.yml
```

### Multimodal Chat API[#](#multimodal-chat-api "Link to this heading")

You can query Completions API with any http clients, a typical example is OpenAI Python client:

Another example uses `curl`:

```
 1#! /usr/bin/env bash
 2
 3# SINGLE IMAGE INFERENCE
 4curl http://localhost:8000/v1/chat/completions \
 5    -H "Content-Type: application/json"  \
 6    -d '{
 7        "model": "Qwen2.5-VL-3B-Instruct",
 8        "messages":[{
 9            "role": "system",
10            "content": "You are a helpful assistant."
11        }, {
12            "role": "user",
13            "content": [
14                {
15                    "type": "text",
16                    "text": "Describe the natural environment in the image."
17                },
18                {
19                    "type":"image_url",
20                    "image_url": {
21                        "url": "https://huggingface.co/datasets/YiYiXu/testing-images/resolve/main/seashore.png"
22                    }
23                }
24            ]
25        }],
26        "max_tokens": 64,
27        "temperature": 0
28    }'
29
30# MULTI IMAGE INFERENCE
31curl http://localhost:8000/v1/chat/completions \
32    -H "Content-Type: application/json" \
33    -d '{
34        "model": "Qwen2.5-VL-3B-Instruct",
35        "messages":[{
36            "role": "system",
37            "content": "You are a helpful assistant."
38        }, {
39            "role": "user",
40            "content": [
41                {
42                    "type": "text",
43                    "text":"Tell me the difference between two images"
44                },
45                {
46                    "type":"image_url",
47                    "image_url": {
48                        "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/inpaint.png"
49                    }
50                },
51                {
52                    "type":"image_url",
53                    "image_url": {
54                        "url": "https://huggingface.co/datasets/YiYiXu/testing-images/resolve/main/seashore.png"
55                    }
56                }
57            ]
58        }],
59        "max_tokens": 64,
60        "temperature": 0
61    }'
62
63# SINGLE VIDEO INFERENCE
64curl http://localhost:8000/v1/chat/completions \
65    -H "Content-Type: application/json" \
66    -d '{
67        "model": "Qwen2.5-VL-3B-Instruct",
68        "messages":[{
69            "role": "system",
70            "content": "You are a helpful assistant."
71        }, {
72            "role": "user",
73            "content": [
74                {
75                    "type": "text",
76                    "text":"Tell me what you see in the video briefly."
77                },
78                {
79                    "type":"video_url",
80                    "video_url": {
81                        "url": "https://huggingface.co/datasets/Efficient-Large-Model/VILA-inference-demos/resolve/main/OAI-sora-tokyo-walk.mp4"
82                    }
83                }
84            ]
85        }],
86        "max_tokens": 64,
87        "temperature": 0
88    }'
```

### Multimodal Modality Coverage[#](#multimodal-modality-coverage "Link to this heading")

TRT-LLM multimodal supports the following modalities and data types (depending on the model):

**Text**

* No type specified:

  ```
  {"role": "user", "content": "What's the capital of South Korea?"}
  ```
* Explicit “text” type:

  ```
  {"role": "user", "content": [{"type": "text", "text": "What's the capital of South Korea?"}]}
  ```

**Image**

* Using “image\_url” with URL:

  ```
  {"role": "user", "content": [
      {"type": "text", "text": "What's in this image?"},
      {"type": "image_url", "image_url": {"url": "https://example.com/image.png"}}
  ]}
  ```
* Using “image\_url” with base64-encoded data:

  ```
  {"role": "user", "content": [
      {"type": "text", "text": "What's in this image?"},
      {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,{image_base64}"}}
  ]}
  ```

Note

To convert images to base64-encoded format, use the utility function
`tensorrt_llm.utils.load_base64_image()`. Refer to the
[load\_base64\_image utility](https://github.com/NVIDIA/TensorRT-LLM/blob/main/tensorrt_llm/utils/load_base64_image.py)
for implementation details.

**Video**

* Using “video\_url”:

  ```
  {"role": "user", "content": [
      {"type": "text", "text": "What's in this video?"},
      {"type": "video_url", "video_url": {"url": "https://example.com/video.mp4"}}
  ]}
  ```

**Audio**

* Using “audio\_url”:

  ```
  {"role": "user", "content": [
      {"type": "text", "text": "What's in this audio?"},
      {"type": "audio_url", "audio_url": {"url": "https://example.com/audio.mp3"}}
  ]}
  ```

## Multi-node Serving with Slurm[#](#multi-node-serving-with-slurm "Link to this heading")

You can deploy [DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3) model across two nodes with Slurm and `trtllm-serve`

```
echo -e "enable_attention_dp: true\npytorch_backend_config:\n  enable_overlap_scheduler: true" > extra-llm-api-config.yml

srun -N 2 -w [NODES] \
    --output=benchmark_2node.log \
    --ntasks 16 --ntasks-per-node=8 \
    --mpi=pmix --gres=gpu:8 \
    --container-image=<CONTAINER_IMG> \
    --container-mounts=/workspace:/workspace \
    --container-workdir /workspace \
    bash -c "trtllm-llmapi-launch trtllm-serve deepseek-ai/DeepSeek-V3 --max_batch_size 161 --max_num_tokens 1160 --tp_size 16 --ep_size 4 --kv_cache_free_gpu_memory_fraction 0.95 --extra_llm_api_options ./extra-llm-api-config.yml"
```

See [the source code](https://github.com/NVIDIA/TensorRT-LLM/blob/main/tensorrt_llm/llmapi/trtllm-llmapi-launch) of `trtllm-llmapi-launch` for more details.

## Metrics Endpoint[#](#metrics-endpoint "Link to this heading")

Note

The metrics endpoint for the default PyTorch backend are in beta and are not as comprehensive as those for the TensorRT backend.

Some fields, such as CPU memory usage, are not yet available for the PyTorch backend.

Enabling `enable_iter_perf_stats` in the PyTorch backend can slightly impact performance, depending on the serving configuration.

The `/metrics` endpoint provides runtime iteration statistics such as GPU memory usage and KV cache details.

For the default PyTorch backend, iteration statistics logging is enabled by setting the `enable_iter_perf_stats` field in a YAML file:

```
# extra_llm_config.yaml
enable_iter_perf_stats: true
```

Start the server and specify the `--extra_llm_api_options` argument with the path to the YAML file:

```
trtllm-serve "TinyLlama/TinyLlama-1.1B-Chat-v1.0" --extra_llm_api_options extra_llm_config.yaml
```

After sending at least one inference request to the server, you can fetch runtime iteration statistics by polling the `/metrics` endpoint.
Since the statistics are stored in an internal queue and removed once retrieved, it’s recommended to poll the endpoint shortly after each request and store the results if needed.

```
curl -X GET http://localhost:8000/metrics
```

Example output:

```
[
    {
        "gpuMemUsage": 76665782272,
        "iter": 154,
        "iterLatencyMS": 7.00688362121582,
        "kvCacheStats": {
            "allocNewBlocks": 3126,
            "allocTotalBlocks": 3126,
            "cacheHitRate": 0.00128,
            "freeNumBlocks": 101253,
            "maxNumBlocks": 101256,
            "missedBlocks": 3121,
            "reusedBlocks": 4,
            "tokensPerBlock": 32,
            "usedNumBlocks": 3
        },
        "numActiveRequests": 1
        ...
    }
]
```

## Configuring with YAML Files[#](#configuring-with-yaml-files "Link to this heading")

You can configure various options of `trtllm-serve` using YAML files by setting the `--extra_llm_api_options` option to the path of a YAML file, the arguments in the file will override the corresponding command line arguments.

The yaml file is configuration of [tensorrt\_llm.llmapi.LlmArgs](https://nvidia.github.io/TensorRT-LLM/llm-api/reference.md#tensorrt_llm.llmapi.TorchLlmArgs), the class has multiple levels of hierarchy, to configure the top level arguments like `max_batch_size`, the yaml file should be like:

```
max_batch_size: 8
```

To configure the nested level arguments like `moe_config.backend`, the yaml file should be like:

```
moe_config:
    backend: CUTLASS
```

## Syntax[#](#syntax "Link to this heading")

### trtllm-serve[#](#trtllm-serve "Link to this heading")

Usage

```
trtllm-serve [OPTIONS] COMMAND [ARGS]...
```

#### disaggregated[#](#trtllm-serve-disaggregated "Link to this heading")

Running server in disaggregated mode

Usage

```
trtllm-serve disaggregated [OPTIONS]
```

Options

-c, --config\_file <config\_file>[#](#cmdoption-trtllm-serve-disaggregated-c "Link to this definition")
:   Specific option for disaggregated mode.

-m, --metadata\_server\_config\_file <metadata\_server\_config\_file>[#](#cmdoption-trtllm-serve-disaggregated-m "Link to this definition")
:   Path to metadata server config file

-t, --server\_start\_timeout <server\_start\_timeout>[#](#cmdoption-trtllm-serve-disaggregated-t "Link to this definition")
:   Server start timeout

-r, --request\_timeout <request\_timeout>[#](#cmdoption-trtllm-serve-disaggregated-r "Link to this definition")
:   Request timeout

-l, --log\_level <log\_level>[#](#cmdoption-trtllm-serve-disaggregated-l "Link to this definition")
:   The logging level.

    Options:
    :   internal\_error | error | warning | info | verbose | debug | trace

--metrics-log-interval <metrics\_log\_interval>[#](#cmdoption-trtllm-serve-disaggregated-metrics-log-interval "Link to this definition")
:   The interval of logging metrics in seconds. Set to 0 to disable metrics logging.

#### disaggregated\_mpi\_worker[#](#trtllm-serve-disaggregated-mpi-worker "Link to this heading")

Launching disaggregated MPI worker

Usage

```
trtllm-serve disaggregated_mpi_worker [OPTIONS]
```

Options

-c, --config\_file <config\_file>[#](#cmdoption-trtllm-serve-disaggregated_mpi_worker-c "Link to this definition")
:   Specific option for disaggregated mode.

--log\_level <log\_level>[#](#cmdoption-trtllm-serve-disaggregated_mpi_worker-log_level "Link to this definition")
:   The logging level.

    Options:
    :   internal\_error | error | warning | info | verbose | debug | trace

#### mm\_embedding\_serve[#](#trtllm-serve-mm-embedding-serve "Link to this heading")

Running an OpenAI API compatible server

MODEL: model name | HF checkpoint path | TensorRT engine path

Usage

```
trtllm-serve mm_embedding_serve [OPTIONS] MODEL
```

Options

--host <host>[#](#cmdoption-trtllm-serve-mm_embedding_serve-host "Link to this definition")
:   Hostname of the server.

--port <port>[#](#cmdoption-trtllm-serve-mm_embedding_serve-port "Link to this definition")
:   Port of the server.

--log\_level <log\_level>[#](#cmdoption-trtllm-serve-mm_embedding_serve-log_level "Link to this definition")
:   The logging level.

    Options:
    :   internal\_error | error | warning | info | verbose | debug | trace

--max\_batch\_size <max\_batch\_size>[#](#cmdoption-trtllm-serve-mm_embedding_serve-max_batch_size "Link to this definition")
:   Maximum number of requests that the engine can schedule.

--max\_num\_tokens <max\_num\_tokens>[#](#cmdoption-trtllm-serve-mm_embedding_serve-max_num_tokens "Link to this definition")
:   Maximum number of batched input tokens after padding is removed in each batch.

--gpus\_per\_node <gpus\_per\_node>[#](#cmdoption-trtllm-serve-mm_embedding_serve-gpus_per_node "Link to this definition")
:   Number of GPUs per node. Default to None, and it will be detected automatically.

--trust\_remote\_code[#](#cmdoption-trtllm-serve-mm_embedding_serve-trust_remote_code "Link to this definition")
:   Flag for HF transformers.

--extra\_encoder\_options <extra\_encoder\_options>[#](#cmdoption-trtllm-serve-mm_embedding_serve-extra_encoder_options "Link to this definition")
:   Path to a YAML file that overwrites the parameters specified by trtllm-serve.

--metadata\_server\_config\_file <metadata\_server\_config\_file>[#](#cmdoption-trtllm-serve-mm_embedding_serve-metadata_server_config_file "Link to this definition")
:   Path to metadata server config file

Arguments

MODEL[#](#cmdoption-trtllm-serve-mm_embedding_serve-arg-MODEL "Link to this definition")
:   Required argument

#### serve[#](#trtllm-serve-serve "Link to this heading")

Running an OpenAI API compatible server

MODEL: model name | HF checkpoint path | TensorRT engine path

Usage

```
trtllm-serve serve [OPTIONS] MODEL
```

Options

--tokenizer <tokenizer>[#](#cmdoption-trtllm-serve-serve-tokenizer "Link to this definition")
:   Path | Name of the tokenizer.Specify this value only if using TensorRT engine as model.

--host <host>[#](#cmdoption-trtllm-serve-serve-host "Link to this definition")
:   Hostname of the server.

--port <port>[#](#cmdoption-trtllm-serve-serve-port "Link to this definition")
:   Port of the server.

--backend <backend>[#](#cmdoption-trtllm-serve-serve-backend "Link to this definition")
:   The backend to use to serve the model. Default is pytorch backend.

    Options:
    :   pytorch | tensorrt | \_autodeploy

--log\_level <log\_level>[#](#cmdoption-trtllm-serve-serve-log_level "Link to this definition")
:   The logging level.

    Options:
    :   internal\_error | error | warning | info | verbose | debug | trace

--max\_beam\_width <max\_beam\_width>[#](#cmdoption-trtllm-serve-serve-max_beam_width "Link to this definition")
:   Maximum number of beams for beam search decoding.

--max\_batch\_size <max\_batch\_size>[#](#cmdoption-trtllm-serve-serve-max_batch_size "Link to this definition")
:   Maximum number of requests that the engine can schedule.

--max\_num\_tokens <max\_num\_tokens>[#](#cmdoption-trtllm-serve-serve-max_num_tokens "Link to this definition")
:   Maximum number of batched input tokens after padding is removed in each batch.

--max\_seq\_len <max\_seq\_len>[#](#cmdoption-trtllm-serve-serve-max_seq_len "Link to this definition")
:   Maximum total length of one request, including prompt and outputs. If unspecified, the value is deduced from the model config.

--tp\_size <tp\_size>[#](#cmdoption-trtllm-serve-serve-tp_size "Link to this definition")
:   Tensor parallelism size.

--pp\_size <pp\_size>[#](#cmdoption-trtllm-serve-serve-pp_size "Link to this definition")
:   Pipeline parallelism size.

--ep\_size <ep\_size>[#](#cmdoption-trtllm-serve-serve-ep_size "Link to this definition")
:   expert parallelism size

--cluster\_size <cluster\_size>[#](#cmdoption-trtllm-serve-serve-cluster_size "Link to this definition")
:   expert cluster parallelism size

--gpus\_per\_node <gpus\_per\_node>[#](#cmdoption-trtllm-serve-serve-gpus_per_node "Link to this definition")
:   Number of GPUs per node. Default to None, and it will be detected automatically.

--kv\_cache\_free\_gpu\_memory\_fraction <kv\_cache\_free\_gpu\_memory\_fraction>[#](#cmdoption-trtllm-serve-serve-kv_cache_free_gpu_memory_fraction "Link to this definition")
:   Free GPU memory fraction reserved for KV Cache, after allocating model weights and buffers.

--num\_postprocess\_workers <num\_postprocess\_workers>[#](#cmdoption-trtllm-serve-serve-num_postprocess_workers "Link to this definition")
:   [Experimental] Number of workers to postprocess raw responses to comply with OpenAI protocol.

--trust\_remote\_code[#](#cmdoption-trtllm-serve-serve-trust_remote_code "Link to this definition")
:   Flag for HF transformers.

--extra\_llm\_api\_options <extra\_llm\_api\_options>[#](#cmdoption-trtllm-serve-serve-extra_llm_api_options "Link to this definition")
:   Path to a YAML file that overwrites the parameters specified by trtllm-serve.

--reasoning\_parser <reasoning\_parser>[#](#cmdoption-trtllm-serve-serve-reasoning_parser "Link to this definition")
:   [Experimental] Specify the parser for reasoning models.

    Options:
    :   deepseek-r1

--metadata\_server\_config\_file <metadata\_server\_config\_file>[#](#cmdoption-trtllm-serve-serve-metadata_server_config_file "Link to this definition")
:   Path to metadata server config file

--server\_role <server\_role>[#](#cmdoption-trtllm-serve-serve-server_role "Link to this definition")
:   Server role. Specify this value only if running in disaggregated mode.

--fail\_fast\_on\_attention\_window\_too\_large[#](#cmdoption-trtllm-serve-serve-fail_fast_on_attention_window_too_large "Link to this definition")
:   Exit with runtime error when attention window is too large to fit even a single sequence in the KV cache.

Arguments

MODEL[#](#cmdoption-trtllm-serve-serve-arg-MODEL "Link to this definition")
:   Required argument

Besides the above examples, trtllm-serve is also used as an entrypoint for performance benchmarking.
Please refer to Performance Benchmarking with `trtllm-serve <[NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/commands/trtllm-serve/trtllm-serve-bench.md)>` for more details.

[previous

trtllm-serve](index.md "previous page")
[next

Run benchmarking with `trtllm-serve`](run-benchmark-with-trtllm-serve.md "next page")

On this page

* [About](#about)
* [Starting a Server](#starting-a-server)
* [Inference Endpoints](#inference-endpoints)
  + [Chat API](#chat-api)
  + [Completions API](#completions-api)
  + [Multimodal Serving](#multimodal-serving)
  + [Multimodal Chat API](#multimodal-chat-api)
  + [Multimodal Modality Coverage](#multimodal-modality-coverage)
* [Multi-node Serving with Slurm](#multi-node-serving-with-slurm)
* [Metrics Endpoint](#metrics-endpoint)
* [Configuring with YAML Files](#configuring-with-yaml-files)
* [Syntax](#syntax)
  + [trtllm-serve](#trtllm-serve)
    - [disaggregated](#trtllm-serve-disaggregated)
    - [disaggregated\_mpi\_worker](#trtllm-serve-disaggregated-mpi-worker)
    - [mm\_embedding\_serve](#trtllm-serve-mm-embedding-serve)
    - [serve](#trtllm-serve-serve)