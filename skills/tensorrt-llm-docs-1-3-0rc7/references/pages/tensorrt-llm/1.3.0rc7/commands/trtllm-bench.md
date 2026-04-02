# trtllm-bench — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/commands/trtllm-bench.html

trtllm-bench#

trtllm-bench is a comprehensive benchmarking tool for TensorRT LLM engines. It provides three main subcommands for different benchmarking scenarios:

Note

Non-breaking: `--config<file.yaml>` is the preferred flag for passing a YAML configuration file.
Existing workflows using `--extra_llm_api_options<file.yaml>` continue to work; it is an equivalent alias.

Syntax#

trtllm-bench#

Usage

```text
trtllm-bench [OPTIONS] COMMAND [ARGS]...
```

Options

-m,--model<model>#

Required The Huggingface name of the model to benchmark.

--model_path<model_path>#

Path to a Huggingface checkpoint directory for loading model components.

-w,--workspace<workspace>#

The directory to store benchmarking intermediate files.

--log_level<log_level>#

The logging level.

Options:

internal_error | error | warning | info | verbose | debug | trace

--revision<revision>#

The revision to use for the HuggingFace model (branch name, tag name, or commit id).

throughput#

Run a throughput test on a TRT-LLM engine.

Usage

```text
trtllm-bench throughput [OPTIONS]
```

Options

--engine_dir<engine_dir>#

Path to a serialized TRT-LLM engine.

--backend<backend>#

The backend to use for benchmark. Default is pytorch backend.

Options:

pytorch | _autodeploy | tensorrt

--custom_module_dirs<custom_module_dirs>#

Paths to custom module directories to import.

--config,--extra_llm_api_options<extra_llm_api_options>#

Path to a YAML file that overwrites the parameters specified by trtllm-bench. Can be specified as either –config or –extra_llm_api_options.

--sampler_options<sampler_options>#

Path to a YAML file that sets sampler options.

--max_batch_size<max_batch_size>#

Maximum runtime batch size to run the engine with.

--max_num_tokens<max_num_tokens>#

Maximum runtime tokens that an engine can accept.

--max_seq_len<max_seq_len>#

Maximum sequence length.

--beam_width<beam_width>#

Number of search beams.

--kv_cache_free_gpu_mem_fraction<kv_cache_free_gpu_mem_fraction>#

The percentage of memory to use for KV Cache after model load.

--dataset<dataset>#

Pass in a dataset file for parsing instead of stdin.

--no_skip_tokenizer_init#

Do not skip tokenizer initialization when loading the model.

--eos_id<eos_id>#

Set the end-of-sequence token for the benchmark. Set to -1 to disable EOS.

--modality<modality>#

Modality of the multimodal requests.

Options:

image | video

--image_data_format<image_data_format>#

Format of the image data for multimodal models.

Options:

pt | pil

--data_device<data_device>#

Device to load the multimodal data on.

Options:

cuda | cpu

--max_input_len<max_input_len>#

Maximum input sequence length to use for multimodal models. This is used only when –modality is specified since the actual number of vision tokens is unknown before the model is run.

--num_requests<num_requests>#

Number of requests to cap benchmark run at. If not specified or set to 0, it will be the length of dataset.

--warmup<warmup>#

Number of requests warm up benchmark.

--target_input_len<target_input_len>#

Target (average) input length for tuning heuristics.

--target_output_len<target_output_len>#

Target (average) sequence length for tuning heuristics.

--tp<tp>#

tensor parallelism size

--pp<pp>#

pipeline parallelism size

--ep<ep>#

expert parallelism size

--cluster_size<cluster_size>#

expert cluster parallelism size

--concurrency<concurrency>#

Desired concurrency rate (number of requests processing at the same time), <=0 for no concurrency limit.

--streaming#

Enable streaming mode for requests.

--report_json<report_json>#

Path where report is written to.

--iteration_log<iteration_log>#

Path where iteration logging is written to.

--output_json<output_json>#

Path where output should be written to.

--request_json<request_json>#

Path where per request information is written to.

--enable_chunked_context,--disable_chunked_context#

Enable/disable chunking in prefill stage for enhanced throughput benchmark.

--scheduler_policy<scheduler_policy>#

KV cache scheduler policy: guaranteed_no_evict prevents request eviction, max_utilization optimizes for throughput.

Options:

guaranteed_no_evict | max_utilization

latency#

Run a latency test on a TRT-LLM engine.

Usage

```text
trtllm-bench latency [OPTIONS]
```

Options

--engine_dir<engine_dir>#

Path to a serialized TRT-LLM engine.

--config,--extra_llm_api_options<extra_llm_api_options>#

Path to a YAML file that overwrites the parameters specified by trtllm-bench. Can be specified as either –config or –extra_llm_api_options.

--backend<backend>#

The backend to use for benchmark. Default is pytorch backend.

Options:

pytorch | _autodeploy | tensorrt

--kv_cache_free_gpu_mem_fraction<kv_cache_free_gpu_mem_fraction>#

The percentage of memory to use for KV Cache after model load.

--max_seq_len<max_seq_len>#

Maximum sequence length.

--dataset<dataset>#

Pass in a dataset file for parsing instead of stdin.

--modality<modality>#

Modality of the multimodal requests.

Options:

image | video

--max_input_len<max_input_len>#

Maximum input sequence length to use for multimodal models. This is used only when –modality is specified since the actual number of vision tokens is unknown before the model is run.

--num_requests<num_requests>#

Number of requests to cap benchmark run at. Minimum between value andlength of dataset.

--warmup<warmup>#

Number of requests warm up benchmark.

--tp<tp>#

tensor parallelism size

--pp<pp>#

pipeline parallelism size

--ep<ep>#

expert parallelism size

--beam_width<beam_width>#

Number of search beams.

--sampler_options<sampler_options>#

Path to a YAML file that sets sampler options.

--concurrency<concurrency>#

Desired concurrency rate (number of requests processing at the same time), <=0 for no concurrency limit.

--medusa_choices<medusa_choices>#

Path to a YAML file that defines the Medusa tree.

--report_json<report_json>#

Path where report should be written to.

--iteration_log<iteration_log>#

Path where iteration logging is written to.

build#

Build engines for benchmarking.

Usage

```text
trtllm-bench build [OPTIONS]
```

Options

-tp,--tp_size<tp_size>#

Number of tensor parallel shards to run the benchmark with.

-pp,--pp_size<pp_size>#

Number of pipeline parallel shards to run the benchmark with.

-q,--quantization<quantization>#

The quantization algorithm to be used when benchmarking. See the documentations for more information.
- https://nvidia.github.io/TensorRT-LLM/precision.html - NVIDIA/TensorRT-LLM

Options:

W8A16 | W4A16 | W4A16_AWQ | W4A8_AWQ | W4A16_GPTQ | FP8 | INT8 | NVFP4

--max_seq_len<max_seq_len>#

Maximum total length of one request, including prompt and outputs.

--no_weights_loading<no_weights_loading>#

Do not load the weights from the checkpoint. Use dummy weights instead.

--trust_remote_code<trust_remote_code>#

Trust remote code for the HF models that are not natively implemented in the transformers library. This is needed when using LLM API when loading the HF config to build the engine.

--dataset<dataset>#

Dataset file to extract the sequence statistics for engine build.

--max_batch_size<max_batch_size>#

Maximum number of requests that the engine can schedule.

--max_num_tokens<max_num_tokens>#

Maximum number of batched tokens the engine can schedule.

--target_input_len<target_input_len>#

Target (average) input length for tuning heuristics.

--target_output_len<target_output_len>#

Target (average) sequence length for tuning heuristics.

Dataset preparation#

prepare_dataset.py#

trtllm-bench is designed to work with the prepare_dataset.py script, which generates benchmark datasets in the required format. The prepare_dataset script supports:

Dataset Types:

Real datasets from various sources

Synthetic datasets with normal or uniform token distributions

LoRA task-specific datasets

Key Features:

Tokenizer integration for proper text preprocessing

Configurable random seeds for reproducible results

Support for LoRA adapters and task IDs

Output in JSON format compatible with trtllm-bench

Important

The `--stdout` flag is required when using prepare_dataset.py with trtllm-bench to ensure proper data streaming format.

Usage:

prepare_dataset#

```text
python prepare_dataset.py [OPTIONS]
```

Options

| Option | Description |
| --- | --- |
| `--tokenizer` | Tokenizer directory or HuggingFace model name (required) |
| `--output` | Output JSON filename (default: preprocessed_dataset.json) |
| `--stdout` | Print output to stdout with JSON dataset entry on each line (required for trtllm-bench) |
| `--random-seed` | Random seed for token generation (default: 420) |
| `--task-id` | LoRA task ID (default: -1) |
| `--rand-task-id` | Random LoRA task range (two integers) |
| `--lora-dir` | Directory containing LoRA adapters |
| `--log-level` | Logging level: info or debug (default: info) |

dataset#

Process real datasets from various sources.

```text
python prepare_dataset.py dataset [OPTIONS]
```

Options

| Option | Description |
| --- | --- |
| `--input` | Input dataset file or directory (required) |
| `--max-input-length` | Maximum input sequence length (default: 2048) |
| `--max-output-length` | Maximum output sequence length (default: 512) |
| `--num-samples` | Number of samples to process (default: all) |
| `--format` | Input format: json, jsonl, csv, or txt (default: auto-detect) |

token_norm_dist#

Generate synthetic datasets with normal token distribution.

```text
python prepare_dataset.py token_norm_dist [OPTIONS]
```

Options

| Option | Description |
| --- | --- |
| `--num-requests` | Number of requests to be generated (required) |
| `--input-mean` | Normal distribution mean for input tokens (required) |
| `--input-stdev` | Normal distribution standard deviation for input tokens (required) |
| `--output-mean` | Normal distribution mean for output tokens (required) |
| `--output-stdev` | Normal distribution standard deviation for output tokens (required) |

token_unif_dist#

Generate synthetic datasets with uniform token distribution

```text
python prepare_dataset.py token_unif_dist [OPTIONS]
```

Options

| Option | Description |
| --- | --- |
| `--num-requests` | Number of requests to be generated (required) |
| `--input-min` | Uniform distribution minimum for input tokens (required) |
| `--input-max` | Uniform distribution maximum for input tokens (required) |
| `--output-min` | Uniform distribution minimum for output tokens (required) |
| `--output-max` | Uniform distribution maximum for output tokens (required) |
