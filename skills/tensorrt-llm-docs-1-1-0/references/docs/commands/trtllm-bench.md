Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/commands/trtllm-bench.md

* trtllm-bench

# trtllm-bench[#](#trtllm-bench "Link to this heading")

trtllm-bench is a comprehensive benchmarking tool for TensorRT LLM engines. It provides three main subcommands for different benchmarking scenarios:

**Common Options for All Commands:**

**Usage:**

## trtllm-bench[#](#trtllm-bench "Link to this heading")

Usage

```
trtllm-bench [OPTIONS] COMMAND [ARGS]...
```

Options

-m, --model <model>[#](#cmdoption-trtllm-bench-m "Link to this definition")
:   **Required** The Huggingface name of the model to benchmark.

--model\_path <model\_path>[#](#cmdoption-trtllm-bench-model_path "Link to this definition")
:   Path to a Huggingface checkpoint directory for loading model components.

-w, --workspace <workspace>[#](#cmdoption-trtllm-bench-w "Link to this definition")
:   The directory to store benchmarking intermediate files.

--log\_level <log\_level>[#](#cmdoption-trtllm-bench-log_level "Link to this definition")
:   The logging level.

    Options:
    :   internal\_error | error | warning | info | verbose | debug | trace

### throughput[#](#trtllm-bench-throughput "Link to this heading")

Run a throughput test on a TRT-LLM engine.

Usage

```
trtllm-bench throughput [OPTIONS]
```

Options

--engine\_dir <engine\_dir>[#](#cmdoption-trtllm-bench-throughput-engine_dir "Link to this definition")
:   Path to a serialized TRT-LLM engine.

--backend <backend>[#](#cmdoption-trtllm-bench-throughput-backend "Link to this definition")
:   The backend to use for benchmark. Default is pytorch backend.

    Options:
    :   pytorch | \_autodeploy | tensorrt

--custom\_module\_dirs <custom\_module\_dirs>[#](#cmdoption-trtllm-bench-throughput-custom_module_dirs "Link to this definition")
:   Paths to custom module directories to import.

--extra\_llm\_api\_options <extra\_llm\_api\_options>[#](#cmdoption-trtllm-bench-throughput-extra_llm_api_options "Link to this definition")
:   Path to a YAML file that overwrites the parameters specified by trtllm-bench.

--sampler\_options <sampler\_options>[#](#cmdoption-trtllm-bench-throughput-sampler_options "Link to this definition")
:   Path to a YAML file that sets sampler options.

--max\_batch\_size <max\_batch\_size>[#](#cmdoption-trtllm-bench-throughput-max_batch_size "Link to this definition")
:   Maximum runtime batch size to run the engine with.

--max\_num\_tokens <max\_num\_tokens>[#](#cmdoption-trtllm-bench-throughput-max_num_tokens "Link to this definition")
:   Maximum runtime tokens that an engine can accept.

--max\_seq\_len <max\_seq\_len>[#](#cmdoption-trtllm-bench-throughput-max_seq_len "Link to this definition")
:   Maximum sequence length.

--beam\_width <beam\_width>[#](#cmdoption-trtllm-bench-throughput-beam_width "Link to this definition")
:   Number of search beams.

--kv\_cache\_free\_gpu\_mem\_fraction <kv\_cache\_free\_gpu\_mem\_fraction>[#](#cmdoption-trtllm-bench-throughput-kv_cache_free_gpu_mem_fraction "Link to this definition")
:   The percentage of memory to use for KV Cache after model load.

--dataset <dataset>[#](#cmdoption-trtllm-bench-throughput-dataset "Link to this definition")
:   Pass in a dataset file for parsing instead of stdin.

--no\_skip\_tokenizer\_init[#](#cmdoption-trtllm-bench-throughput-no_skip_tokenizer_init "Link to this definition")
:   Do not skip tokenizer initialization when loading the model.

--eos\_id <eos\_id>[#](#cmdoption-trtllm-bench-throughput-eos_id "Link to this definition")
:   Set the end-of-sequence token for the benchmark. Set to -1 to disable EOS.

--modality <modality>[#](#cmdoption-trtllm-bench-throughput-modality "Link to this definition")
:   Modality of the multimodal requests.

    Options:
    :   image | video

--image\_data\_format <image\_data\_format>[#](#cmdoption-trtllm-bench-throughput-image_data_format "Link to this definition")
:   Format of the image data for multimodal models.

    Options:
    :   pt | pil

--data\_device <data\_device>[#](#cmdoption-trtllm-bench-throughput-data_device "Link to this definition")
:   Device to load the multimodal data on.

    Options:
    :   cuda | cpu

--max\_input\_len <max\_input\_len>[#](#cmdoption-trtllm-bench-throughput-max_input_len "Link to this definition")
:   Maximum input sequence length to use for multimodal models. This is used only when –modality is specified since the actual number of vision tokens is unknown before the model is run.

--num\_requests <num\_requests>[#](#cmdoption-trtllm-bench-throughput-num_requests "Link to this definition")
:   Number of requests to cap benchmark run at. If not specified or set to 0, it will be the length of dataset.

--warmup <warmup>[#](#cmdoption-trtllm-bench-throughput-warmup "Link to this definition")
:   Number of requests warm up benchmark.

--target\_input\_len <target\_input\_len>[#](#cmdoption-trtllm-bench-throughput-target_input_len "Link to this definition")
:   Target (average) input length for tuning heuristics.

--target\_output\_len <target\_output\_len>[#](#cmdoption-trtllm-bench-throughput-target_output_len "Link to this definition")
:   Target (average) sequence length for tuning heuristics.

--tp <tp>[#](#cmdoption-trtllm-bench-throughput-tp "Link to this definition")
:   tensor parallelism size

--pp <pp>[#](#cmdoption-trtllm-bench-throughput-pp "Link to this definition")
:   pipeline parallelism size

--ep <ep>[#](#cmdoption-trtllm-bench-throughput-ep "Link to this definition")
:   expert parallelism size

--cluster\_size <cluster\_size>[#](#cmdoption-trtllm-bench-throughput-cluster_size "Link to this definition")
:   expert cluster parallelism size

--concurrency <concurrency>[#](#cmdoption-trtllm-bench-throughput-concurrency "Link to this definition")
:   Desired concurrency rate (number of requests processing at the same time), <=0 for no concurrency limit.

--streaming[#](#cmdoption-trtllm-bench-throughput-streaming "Link to this definition")
:   Enable streaming mode for requests.

--report\_json <report\_json>[#](#cmdoption-trtllm-bench-throughput-report_json "Link to this definition")
:   Path where report is written to.

--iteration\_log <iteration\_log>[#](#cmdoption-trtllm-bench-throughput-iteration_log "Link to this definition")
:   Path where iteration logging is written to.

--output\_json <output\_json>[#](#cmdoption-trtllm-bench-throughput-output_json "Link to this definition")
:   Path where output should be written to.

--request\_json <request\_json>[#](#cmdoption-trtllm-bench-throughput-request_json "Link to this definition")
:   Path where per request information is written to.

--enable\_chunked\_context, --disable\_chunked\_context[#](#cmdoption-trtllm-bench-throughput-enable_chunked_context "Link to this definition")
:   Enable/disable chunking in prefill stage for enhanced throughput benchmark.

--scheduler\_policy <scheduler\_policy>[#](#cmdoption-trtllm-bench-throughput-scheduler_policy "Link to this definition")
:   KV cache scheduler policy: guaranteed\_no\_evict prevents request eviction, max\_utilization optimizes for throughput.

    Options:
    :   guaranteed\_no\_evict | max\_utilization

### latency[#](#trtllm-bench-latency "Link to this heading")

Run a latency test on a TRT-LLM engine.

Usage

```
trtllm-bench latency [OPTIONS]
```

Options

--engine\_dir <engine\_dir>[#](#cmdoption-trtllm-bench-latency-engine_dir "Link to this definition")
:   Path to a serialized TRT-LLM engine.

--extra\_llm\_api\_options <extra\_llm\_api\_options>[#](#cmdoption-trtllm-bench-latency-extra_llm_api_options "Link to this definition")
:   Path to a YAML file that overwrites the parameters specified by trtllm-bench.

--backend <backend>[#](#cmdoption-trtllm-bench-latency-backend "Link to this definition")
:   The backend to use for benchmark. Default is pytorch backend.

    Options:
    :   pytorch | \_autodeploy | tensorrt

--kv\_cache\_free\_gpu\_mem\_fraction <kv\_cache\_free\_gpu\_mem\_fraction>[#](#cmdoption-trtllm-bench-latency-kv_cache_free_gpu_mem_fraction "Link to this definition")
:   The percentage of memory to use for KV Cache after model load.

--max\_seq\_len <max\_seq\_len>[#](#cmdoption-trtllm-bench-latency-max_seq_len "Link to this definition")
:   Maximum sequence length.

--dataset <dataset>[#](#cmdoption-trtllm-bench-latency-dataset "Link to this definition")
:   Pass in a dataset file for parsing instead of stdin.

--modality <modality>[#](#cmdoption-trtllm-bench-latency-modality "Link to this definition")
:   Modality of the multimodal requests.

    Options:
    :   image | video

--max\_input\_len <max\_input\_len>[#](#cmdoption-trtllm-bench-latency-max_input_len "Link to this definition")
:   Maximum input sequence length to use for multimodal models. This is used only when –modality is specified since the actual number of vision tokens is unknown before the model is run.

--num\_requests <num\_requests>[#](#cmdoption-trtllm-bench-latency-num_requests "Link to this definition")
:   Number of requests to cap benchmark run at. Minimum between value andlength of dataset.

--warmup <warmup>[#](#cmdoption-trtllm-bench-latency-warmup "Link to this definition")
:   Number of requests warm up benchmark.

--tp <tp>[#](#cmdoption-trtllm-bench-latency-tp "Link to this definition")
:   tensor parallelism size

--pp <pp>[#](#cmdoption-trtllm-bench-latency-pp "Link to this definition")
:   pipeline parallelism size

--ep <ep>[#](#cmdoption-trtllm-bench-latency-ep "Link to this definition")
:   expert parallelism size

--beam\_width <beam\_width>[#](#cmdoption-trtllm-bench-latency-beam_width "Link to this definition")
:   Number of search beams.

--sampler\_options <sampler\_options>[#](#cmdoption-trtllm-bench-latency-sampler_options "Link to this definition")
:   Path to a YAML file that sets sampler options.

--concurrency <concurrency>[#](#cmdoption-trtllm-bench-latency-concurrency "Link to this definition")
:   Desired concurrency rate (number of requests processing at the same time), <=0 for no concurrency limit.

--medusa\_choices <medusa\_choices>[#](#cmdoption-trtllm-bench-latency-medusa_choices "Link to this definition")
:   Path to a YAML file that defines the Medusa tree.

--report\_json <report\_json>[#](#cmdoption-trtllm-bench-latency-report_json "Link to this definition")
:   Path where report should be written to.

--iteration\_log <iteration\_log>[#](#cmdoption-trtllm-bench-latency-iteration_log "Link to this definition")
:   Path where iteration logging is written to.

### build[#](#trtllm-bench-build "Link to this heading")

Build engines for benchmarking.

Usage

```
trtllm-bench build [OPTIONS]
```

Options

-tp, --tp\_size <tp\_size>[#](#cmdoption-trtllm-bench-build-tp "Link to this definition")
:   Number of tensor parallel shards to run the benchmark with.

-pp, --pp\_size <pp\_size>[#](#cmdoption-trtllm-bench-build-pp "Link to this definition")
:   Number of pipeline parallel shards to run the benchmark with.

-q, --quantization <quantization>[#](#cmdoption-trtllm-bench-build-q "Link to this definition")
:   The quantization algorithm to be used when benchmarking. See the documentations for more information.
    - <https://nvidia.github.io/TensorRT-LLM/precision.md> - [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/blogs/quantization-in-TRT-LLM.md)

    Options:
    :   W8A16 | W4A16 | W4A16\_AWQ | W4A8\_AWQ | W4A16\_GPTQ | FP8 | INT8 | NVFP4

--max\_seq\_len <max\_seq\_len>[#](#cmdoption-trtllm-bench-build-max_seq_len "Link to this definition")
:   Maximum total length of one request, including prompt and outputs.

--no\_weights\_loading <no\_weights\_loading>[#](#cmdoption-trtllm-bench-build-no_weights_loading "Link to this definition")
:   Do not load the weights from the checkpoint. Use dummy weights instead.

--trust\_remote\_code <trust\_remote\_code>[#](#cmdoption-trtllm-bench-build-trust_remote_code "Link to this definition")
:   Trust remote code for the HF models that are not natively implemented in the transformers library. This is needed when using LLM API when loading the HF config to build the engine.

--dataset <dataset>[#](#cmdoption-trtllm-bench-build-dataset "Link to this definition")
:   Dataset file to extract the sequence statistics for engine build.

--max\_batch\_size <max\_batch\_size>[#](#cmdoption-trtllm-bench-build-max_batch_size "Link to this definition")
:   Maximum number of requests that the engine can schedule.

--max\_num\_tokens <max\_num\_tokens>[#](#cmdoption-trtllm-bench-build-max_num_tokens "Link to this definition")
:   Maximum number of batched tokens the engine can schedule.

--target\_input\_len <target\_input\_len>[#](#cmdoption-trtllm-bench-build-target_input_len "Link to this definition")
:   Target (average) input length for tuning heuristics.

--target\_output\_len <target\_output\_len>[#](#cmdoption-trtllm-bench-build-target_output_len "Link to this definition")
:   Target (average) sequence length for tuning heuristics.

# prepare\_dataset.py[#](#prepare-dataset-py "Link to this heading")

trtllm-bench is designed to work with the [prepare\_dataset.py](https://github.com/NVIDIA/TensorRT-LLM/blob/main/benchmarks/cpp/prepare_dataset.py) script, which generates benchmark datasets in the required format. The prepare\_dataset script supports:

**Dataset Types:**

* Real datasets from various sources
* Synthetic datasets with normal or uniform token distributions
* LoRA task-specific datasets

**Key Features:**

* Tokenizer integration for proper text preprocessing
* Configurable random seeds for reproducible results
* Support for LoRA adapters and task IDs
* Output in JSON format compatible with trtllm-bench

Important

The `--stdout` flag is **required** when using prepare\_dataset.py with trtllm-bench to ensure proper data streaming format.

**Usage:**

## prepare\_dataset[#](#prepare-dataset "Link to this heading")

```
python prepare_dataset.py [OPTIONS]
```

**Options**

---

| Option | Description |
| --- | --- |
| `--tokenizer` | Tokenizer directory or HuggingFace model name (required) |
| `--output` | Output JSON filename (default: preprocessed\_dataset.json) |
| `--stdout` | Print output to stdout with JSON dataset entry on each line (**required for trtllm-bench**) |
| `--random-seed` | Random seed for token generation (default: 420) |
| `--task-id` | LoRA task ID (default: -1) |
| `--rand-task-id` | Random LoRA task range (two integers) |
| `--lora-dir` | Directory containing LoRA adapters |
| `--log-level` | Logging level: info or debug (default: info) |

## dataset[#](#dataset "Link to this heading")

Process real datasets from various sources.

```
python prepare_dataset.py dataset [OPTIONS]
```

**Options**

---

| Option | Description |
| --- | --- |
| `--input` | Input dataset file or directory (required) |
| `--max-input-length` | Maximum input sequence length (default: 2048) |
| `--max-output-length` | Maximum output sequence length (default: 512) |
| `--num-samples` | Number of samples to process (default: all) |
| `--format` | Input format: json, jsonl, csv, or txt (default: auto-detect) |

## token\_norm\_dist[#](#token-norm-dist "Link to this heading")

Generate synthetic datasets with normal token distribution.

```
python prepare_dataset.py token_norm_dist [OPTIONS]
```

**Options**

---

| Option | Description |
| --- | --- |
| `--num-requests` | Number of requests to be generated (required) |
| `--input-mean` | Normal distribution mean for input tokens (required) |
| `--input-stdev` | Normal distribution standard deviation for input tokens (required) |
| `--output-mean` | Normal distribution mean for output tokens (required) |
| `--output-stdev` | Normal distribution standard deviation for output tokens (required) |

## token\_unif\_dist[#](#token-unif-dist "Link to this heading")

Generate synthetic datasets with uniform token distribution

```
python prepare_dataset.py token_unif_dist [OPTIONS]
```

**Options**

---

| Option | Description |
| --- | --- |
| `--num-requests` | Number of requests to be generated (required) |
| `--input-min` | Uniform distribution minimum for input tokens (required) |
| `--input-max` | Uniform distribution maximum for input tokens (required) |
| `--output-min` | Uniform distribution minimum for output tokens (required) |
| `--output-max` | Uniform distribution maximum for output tokens (required) |

[previous

Adding a New Model](../models/adding-new-model.md "previous page")
[next

trtllm-eval](trtllm-eval.md "next page")

On this page

* [trtllm-bench](#)
  + [trtllm-bench](#trtllm-bench)
    - [throughput](#trtllm-bench-throughput)
    - [latency](#trtllm-bench-latency)
    - [build](#trtllm-bench-build)
* [prepare\_dataset.py](#prepare-dataset-py)
  + [prepare\_dataset](#prepare-dataset)
  + [dataset](#dataset)
  + [token\_norm\_dist](#token-norm-dist)
  + [token\_unif\_dist](#token-unif-dist)