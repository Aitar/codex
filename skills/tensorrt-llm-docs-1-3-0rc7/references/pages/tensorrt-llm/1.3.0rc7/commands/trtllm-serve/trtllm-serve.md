# trtllm-serve — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/commands/trtllm-serve/trtllm-serve.html

trtllm-serve#

About#

The `trtllm-serve` command starts an OpenAI compatible server that supports the following endpoints:

`/v1/models`

`/v1/completions`

`/v1/chat/completions`

For information about the inference endpoints, refer to the OpenAI API Reference.

The server also supports the following endpoints:

`/health`

`/metrics`

`/version`

The `metrics` endpoint provides runtime-iteration statistics such as GPU memory use and inflight-batching details.

Starting a Server#

The following abbreviated command syntax shows the commonly used arguments to start a server:

```text
trtllm-serve <model> [--tp_size <tp> --pp_size <pp> --ep_size <ep> --host <host> --port <port>]
```

For the full syntax and argument descriptions, refer to Syntax.

Inference Endpoints#

After you start the server, you can send inference requests through completions API, Chat API and Responses API, which are compatible with corresponding OpenAI APIs. We use TinyLlama-1.1B-Chat-v1.0 for examples in the following sections.

Chat API#

You can query Chat API with any http clients, a typical example is OpenAI Python client:

```text
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

```text
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

Completions API#

You can query Completions API with any http clients, a typical example is OpenAI Python client:

```text
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

```text
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

Responses API#

You can query Responses API with any http clients, a typical example is OpenAI Python client:

```text
 1### :title OpenAI Responses Client
 2
 3from openai import OpenAI
 4
 5client = OpenAI(
 6    base_url="http://localhost:8000/v1",
 7    api_key="tensorrt_llm",
 8)
 9
10response = client.responses.create(
11    model="TinyLlama-1.1B-Chat-v1.0",
12    input="Where is New York?",
13    max_output_tokens=20,
14)
15print(response)
```

Another example uses `curl`:

```text
1#! /usr/bin/env bash
2
3curl http://localhost:8000/v1/responses \
4    -H "Content-Type: application/json" \
5    -d '{
6        "model": "TinyLlama-1.1B-Chat-v1.0",
7        "input": "Where is New York?",
8        "max_output_tokens": 16
9    }'
```

More openai compatible examples can be found in the compatibility examples directory.

Multimodal Serving#

For multimodal models, you need to create a configuration file and start the server with additional options due to the following limitations:

TRT-LLM multimodal is currently not compatible with `kv_cache_reuse`

Multimodal models require `chat_template`, so only the Chat API is supported

To set up multimodal models:

First, create a configuration file:

```text
cat >./config.yml<<EOF
kv_cache_config:
    enable_block_reuse: false
EOF
```

Then, start the server with the configuration file:

```text
trtllm-serve Qwen/Qwen2-VL-7B-Instruct \
    --config ./config.yml
```

Multimodal Chat API#

You can query Completions API with any http clients, a typical example is OpenAI Python client:

Another example uses `curl`:

```text
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

Multimodal Modality Coverage#

TRT-LLM multimodal supports the following modalities and data types (depending on the model):

Text

No type specified:

```text
{"role": "user", "content": "What's the capital of South Korea?"}
```

Explicit “text” type:

```text
{"role": "user", "content": [{"type": "text", "text": "What's the capital of South Korea?"}]}
```

Image

Using “image_url” with URL:

```text
{"role": "user", "content": [
    {"type": "text", "text": "What's in this image?"},
    {"type": "image_url", "image_url": {"url": "https://example.com/image.png"}}
]}
```

Using “image_url” with base64-encoded data:

```text
{"role": "user", "content": [
    {"type": "text", "text": "What's in this image?"},
    {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,{image_base64}"}}
]}
```

Note

To convert images to base64-encoded format, use the utility function
`tensorrt_llm.utils.load_base64_image()`. Refer to the
load_base64_image utility
for implementation details.

Image embeddings

It is also possible to directly provide the image embeddings to use by the multimodal
model.

Using “image_embeds” with base64-encoded data:

```text
{"role": "user", "content": [
    {"type": "text", "text": "What's in this image?"},
    {"type": "image_embeds", "image_embeds": {"data": "{image_embeddings_base64}"}}}
]}
```

Note

The contents of image_embeddings_base64 can be generated by base64-encoding
the result of serializing a tensor via torch.save.

Video

Using “video_url”:

```text
{"role": "user", "content": [
    {"type": "text", "text": "What's in this video?"},
    {"type": "video_url", "video_url": {"url": "https://example.com/video.mp4"}}
]}
```

Audio

Using “audio_url”:

```text
{"role": "user", "content": [
    {"type": "text", "text": "What's in this audio?"},
    {"type": "audio_url", "audio_url": {"url": "https://example.com/audio.mp3"}}
]}
```

Visual Generation Serving#

`trtllm-serve` supports diffusion-based visual generation models (FLUX.1, FLUX.2, Wan2.1, Wan2.2) for image and video generation. When a diffusion model directory is provided (detected by the presence of `model_index.json`), the server automatically launches in visual generation mode with dedicated endpoints.

Note

VisualGen is in prototype stage. APIs, supported models, and optimization options are actively evolving and may change in future releases.

```text
# Video generation (Wan)
trtllm-serve Wan-AI/Wan2.2-T2V-A14B-Diffusers \
    --extra_visual_gen_options config.yml

# Image generation (FLUX)
trtllm-serve black-forest-labs/FLUX.2-dev \
    --extra_visual_gen_options config.yml
```

The `--extra_visual_gen_options` flag accepts a YAML file that configures quantization, parallelism, and TeaCache. Available visual generation endpoints include `/v1/images/generations`, `/v1/videos`, `/v1/videos/generations`, and video management APIs.

For full details, see the ../../models/visual-generation.md feature documentation. Example client scripts are available in the examples/visual_gen/serve/ directory.

Multi-node Serving with Slurm#

You can deploy DeepSeek-V3 model across two nodes with Slurm and `trtllm-serve`

```text
echo -e "enable_attention_dp: true\npytorch_backend_config:\n  enable_overlap_scheduler: true" > config.yml

srun -N 2 -w [NODES] \
    --output=benchmark_2node.log \
    --ntasks 16 --ntasks-per-node=8 \
    --mpi=pmix --gres=gpu:8 \
    --container-image=<CONTAINER_IMG> \
    --container-mounts=/workspace:/workspace \
    --container-workdir /workspace \
    bash -c "trtllm-llmapi-launch trtllm-serve deepseek-ai/DeepSeek-V3 --max_batch_size 161 --max_num_tokens 1160 --tp_size 16 --ep_size 4 --kv_cache_free_gpu_memory_fraction 0.95 --config ./config.yml"
```

See the source code of `trtllm-llmapi-launch` for more details.

Metrics Endpoint#

Note

The metrics endpoint for the default PyTorch backend are in beta and are not as comprehensive as those for the TensorRT backend.

Some fields, such as CPU memory usage, are not yet available for the PyTorch backend.

Enabling `enable_iter_perf_stats` in the PyTorch backend can slightly impact performance, depending on the serving configuration.

The `/metrics` endpoint provides runtime iteration statistics such as GPU memory usage and KV cache details.

For the default PyTorch backend, iteration statistics logging is enabled by setting the `enable_iter_perf_stats` field in a YAML file:

```text
# extra_llm_config.yaml
enable_iter_perf_stats: true
```

Start the server and specify the `--config` argument with the path to the YAML file:

```text
trtllm-serve "TinyLlama/TinyLlama-1.1B-Chat-v1.0" --config config.yaml
```

After sending at least one inference request to the server, you can fetch runtime iteration statistics by polling the `/metrics` endpoint.
Since the statistics are stored in an internal queue and removed once retrieved, it’s recommended to poll the endpoint shortly after each request and store the results if needed.

```text
curl -X GET http://localhost:8000/metrics
```

Example output:

```text
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

Configuring with YAML Files#

You can configure various options of `trtllm-serve` using YAML files by setting the `--config` option to the path of a YAML file. The arguments in the file override the corresponding command line arguments.

Note

Non-breaking: `--config<file.yaml>` is the preferred flag for passing a YAML configuration file.
Existing workflows using `--extra_llm_api_options<file.yaml>` continue to work; it is an equivalent alias.

The yaml file is configuration of tensorrt_llm.llmapi.LlmArgs, the class has multiple levels of hierarchy, to configure the top level arguments like `max_batch_size`, the yaml file should be like:

```text
max_batch_size: 8
```

To configure the nested level arguments like `moe_config.backend`, the yaml file should be like:

```text
moe_config:
    backend: CUTLASS
```

Syntax#

This syntax section lists all command line arguments for `trtllm-serve`’s subcommands. Some of the arguments are accompanied with a stability tag indicating their development status. Refer to our API Reference for details

trtllm-serve#

Usage

```text
trtllm-serve [OPTIONS] COMMAND [ARGS]...
```

disaggregated#

Running server in disaggregated mode

Usage

```text
trtllm-serve disaggregated [OPTIONS]
```

Options

-c,--config_file<config_file>#

Specific option for disaggregated mode.

-m,--metadata_server_config_file<metadata_server_config_file>#

Path to metadata server config file

-t,--server_start_timeout<server_start_timeout>#

Server start timeout

-r,--request_timeout<request_timeout>#

Request timeout

-l,--log_level<log_level>#

The logging level.

Options:

internal_error | error | warning | info | verbose | debug | trace

--metrics-log-interval<metrics_log_interval>#

The interval of logging metrics in seconds. Set to 0 to disable metrics logging.

disaggregated_mpi_worker#

Launching disaggregated MPI worker

Usage

```text
trtllm-serve disaggregated_mpi_worker [OPTIONS]
```

Options

-c,--config_file<config_file>#

Specific option for disaggregated mode.

--log_level<log_level>#

The logging level.

Options:

internal_error | error | warning | info | verbose | debug | trace

mm_embedding_serve#

Running an OpenAI API compatible server

MODEL: model name | HF checkpoint path | TensorRT engine path

Usage

```text
trtllm-serve mm_embedding_serve [OPTIONS] MODEL
```

Options

--host<host>#

Hostname of the server.

--port<port>#

Port of the server.

--log_level<log_level>#

The logging level.

Options:

internal_error | error | warning | info | verbose | debug | trace

--max_batch_size<max_batch_size>#

Maximum number of requests that the engine can schedule.

--max_num_tokens<max_num_tokens>#

Maximum number of batched input tokens after padding is removed in each batch.

--gpus_per_node<gpus_per_node>#

Number of GPUs per node. Default to None, and it will be detected automatically.

--trust_remote_code#

Flag for HF transformers.

--extra_encoder_options<extra_encoder_options>#

Path to a YAML file that overwrites the parameters specified by trtllm-serve.

--metadata_server_config_file<metadata_server_config_file>#

Path to metadata server config file

Arguments

MODEL#

Required argument

serve#

Running an OpenAI API compatible server

MODEL: model name | HF checkpoint path | TensorRT engine path

Usage

```text
trtllm-serve serve [OPTIONS] MODEL
```

Options

--tokenizer<tokenizer>#

`beta` Path | Name of the tokenizer.

--custom_tokenizer<custom_tokenizer>#

`prototype` Custom tokenizer type: alias (e.g., ‘deepseek_v32’) or Python import path (e.g., ‘tensorrt_llm.tokenizer.deepseek_v32.DeepseekV32Tokenizer’).

--host<host>#

`beta` Hostname of the server.

--port<port>#

`beta` Port of the server.

--backend<backend>#

`beta` The backend to use to serve the model. Default is pytorch backend.

Options:

pytorch | tensorrt | _autodeploy

--custom_module_dirs<custom_module_dirs>#

`prototype` Paths to custom module directories to import.

--log_level<log_level>#

`beta` The logging level.

Options:

internal_error | error | warning | info | verbose | debug | trace

--max_beam_width<max_beam_width>#

`beta` Maximum number of beams for beam search decoding.

--max_batch_size<max_batch_size>#

`beta` Maximum number of requests that the engine can schedule.

--max_num_tokens<max_num_tokens>#

`beta` Maximum number of batched input tokens after padding is removed in each batch.

--max_seq_len<max_seq_len>#

`beta` Maximum total length of one request, including prompt and outputs. If unspecified, the value is deduced from the model config.

--tensor_parallel_size,--tp_size<tensor_parallel_size>#

`beta` Tensor parallelism size.

--pipeline_parallel_size,--pp_size<pipeline_parallel_size>#

`beta` Pipeline parallelism size.

--context_parallel_size,--cp_size<context_parallel_size>#

`beta` Context parallelism size.

--moe_expert_parallel_size,--ep_size<moe_expert_parallel_size>#

`beta` expert parallelism size

--moe_cluster_parallel_size,--cluster_size<moe_cluster_parallel_size>#

`beta` expert cluster parallelism size

--gpus_per_node<gpus_per_node>#

`beta` Number of GPUs per node. Default to None, and it will be detected automatically.

--free_gpu_memory_fraction,--kv_cache_free_gpu_memory_fraction<free_gpu_memory_fraction>#

`beta` Free GPU memory fraction reserved for KV Cache, after allocating model weights and buffers.

--kv_cache_dtype<kv_cache_dtype>#

`prototype` KV cache quantization dtype for PyTorch backend. ‘auto’ uses checkpoint/model metadata; explicit values force override.

Options:

auto | fp8 | nvfp4

--num_postprocess_workers<num_postprocess_workers>#

`prototype` Number of workers to postprocess raw responses to comply with OpenAI protocol.

--trust_remote_code#

`beta` Flag for HF transformers.

--revision<revision>#

`beta` The revision to use for the HuggingFace model (branch name, tag name, or commit id).

--config,--extra_llm_api_options<extra_llm_api_options>#

`prototype` Path to a YAML file that overwrites the parameters specified by trtllm-serve. Can be specified as either –config or –extra_llm_api_options.

--reasoning_parser<reasoning_parser>#

`prototype` Specify the parser for reasoning models.

Options:

deepseek-r1 | qwen3 | nano-v3

--tool_parser<tool_parser>#

`prototype` Specify the parser for tool models.

Options:

qwen3 | qwen3_coder | kimi_k2 | deepseek_v3 | deepseek_v31 | deepseek_v32

--metadata_server_config_file<metadata_server_config_file>#

`prototype` Path to metadata server config file

--server_role<server_role>#

`prototype` Server role. Specify this value only if running in disaggregated mode.

--fail_fast_on_attention_window_too_large#

`prototype` Exit with runtime error when attention window is too large to fit even a single sequence in the KV cache.

--otlp_traces_endpoint<otlp_traces_endpoint>#

`prototype` Target URL to which OpenTelemetry traces will be sent.

--disagg_cluster_uri<disagg_cluster_uri>#

`prototype` URI of the disaggregated cluster.

--enable_chunked_prefill#

`prototype` Enable chunked prefill

--media_io_kwargs<media_io_kwargs>#

`prototype` Keyword arguments for media I/O.

--chat_template<chat_template>#

`prototype` Specify a custom chat template. Can be a file path or one-liner template string

--grpc#

Run gRPC server instead of OpenAI HTTP server. gRPC server accepts pre-tokenized requests and returns raw token IDs.

--served_model_name<served_model_name>#

`prototype` The model name used in the API. If not specified, the model path is used as the model name. This is useful when the model path is long or when you want to expose a custom name to clients.

--extra_visual_gen_options<extra_visual_gen_options>#

`prototype` Path to a YAML file with extra VISUAL_GEN model options.

Arguments

MODEL#

Required argument

Besides the above examples, trtllm-serve is also used as an entrypoint for performance benchmarking.
Please refer to Performance Benchmarking with `trtllm-serve <NVIDIA/TensorRT-LLM>` for more details.
