* GenAI...

# GenAI Performance Analyzer[#](#genai-performance-analyzer "Link to this heading")

## GenAI-Perf[#](#genai-perf "Link to this heading")

GenAI-Perf is a command line tool for measuring the throughput and
latency of generative AI models as served through an inference server.
For large language models (LLMs), GenAI-Perf provides metrics such as
[output token throughput](#output_token_throughput_metric), [time to
first token](#time_to_first_token_metric), [inter token
latency](#inter_token_latency_metric), and [request
throughput](#request_throughput_metric). For a full list of metrics
please see the [Metrics section](#metrics).

Users specify a model name, an inference server URL, the type of inputs
to use (synthetic or from dataset), and the type of load to generate
(number of concurrent requests, request rate).

GenAI-Perf generates the specified load, measures the performance of the
inference server and reports the metrics in a simple table as console
output. The tool also logs all results in a csv and json file that can
be used to derive additional metrics and visualizations. The inference
server must already be running when GenAI-Perf is run.

You can use GenAI-Perf to run performance benchmarks on - [Large
Language Models](docs/tutorial.md) - [Vision Language
Models](docs/multi_modal.md) - [Embedding
Models](docs/embeddings.md) - [Ranking Models](docs/rankings.md) -
[Multiple LoRA Adapters](docs/lora.md)

> [!Note] GenAI-Perf is currently in early release and under rapid
> development. While we will try to remain consistent, command line
> options and functionality are subject to change as the tool matures.

### Installation[#](#installation "Link to this heading")

The easiest way to install GenAI-Perf is through [Triton Server SDK
container](https://ngc.nvidia.com/catalog/containers/nvidia:tritonserver).
Install the latest release using the following command:

```
export RELEASE="yy.mm" # e.g. export RELEASE="24.06"

docker run -it --net=host --gpus=all  nvcr.io/nvidia/tritonserver:${RELEASE}-py3-sdk

# Check out genai_perf command inside the container:
genai-perf --help
```

Alternatively, to install from source:

Since GenAI-Perf depends on Perf Analyzer, youâll need to install the
Perf Analyzer binary:

#### Install Perf Analyzer (Ubuntu, Python 3.8+)[#](#install-perf-analyzer-ubuntu-python-3-8 "Link to this heading")

**NOTE**: you must already have CUDA 12 installed (checkout the [CUDA
installation
guide](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.md)).

```
pip install tritonclient

apt update && apt install -y --no-install-recommends libb64-0d libcurl4
```

You can also build Perf Analyzer [from
source](../docs/install.md#build-from-source) as well.

#### Install GenAI-Perf from source[#](#install-genai-perf-from-source "Link to this heading")

```
git clone https://github.com/triton-inference-server/perf_analyzer.git && cd perf_analyzer

pip install -e genai-perf
```

### Quick Start[#](#quick-start "Link to this heading")

In this quick start, we will use GenAI-Perf to run performance
benchmarking on the GPT-2 model running on Triton Inference Server with
a TensorRT-LLM engine.

#### Serve GPT-2 TensorRT-LLM model using Triton CLI[#](#serve-gpt-2-tensorrt-llm-model-using-triton-cli "Link to this heading")

You can follow the [quickstart
guide](https://github.com/triton-inference-server/triton_cli?tab=readme-ov-file#serving-a-trt-llm-model)
on Triton CLI github repo to run GPT-2 model locally. The full
instructions are copied below for convenience:

```
# This container comes with all of the dependencies for building TRT-LLM engines
# and serving the engine with Triton Inference Server.
docker run -ti \
    --gpus all \
    --network=host \
    --shm-size=1g --ulimit memlock=-1 \
    -v /tmp:/tmp \
    -v ${HOME}/models:/root/models \
    -v ${HOME}/.cache/huggingface:/root/.cache/huggingface \
    nvcr.io/nvidia/tritonserver:24.05-trtllm-python-py3

# Install the Triton CLI
pip install git+https://github.com/triton-inference-server/triton_cli.git@0.0.8

# Build TRT LLM engine and generate a Triton model repository pointing at it
triton remove -m all
triton import -m gpt2 --backend tensorrtllm

# Start Triton pointing at the default model repository
triton start
```

#### Running GenAI-Perf[#](#running-genai-perf "Link to this heading")

Now we can run GenAI-Perf from Triton Inference Server SDK container:

```
export RELEASE="yy.mm" # e.g. export RELEASE="24.06"

docker run -it --net=host --rm --gpus=all nvcr.io/nvidia/tritonserver:${RELEASE}-py3-sdk

# Run GenAI-Perf in the container:
genai-perf profile \
  -m gpt2 \
  --service-kind triton \
  --backend tensorrtllm \
  --num-prompts 100 \
  --random-seed 123 \
  --synthetic-input-tokens-mean 200 \
  --synthetic-input-tokens-stddev 0 \
  --streaming \
  --output-tokens-mean 100 \
  --output-tokens-stddev 0 \
  --output-tokens-mean-deterministic \
  --tokenizer hf-internal-testing/llama-tokenizer \
  --concurrency 1 \
  --measurement-interval 4000 \
  --profile-export-file my_profile_export.json \
  --url localhost:8001
```

Example output:

```
                                   LLM Metrics
ââââââââââââââââââââââââââââ³âââââââââ³âââââââââ³âââââââââ³âââââââââ³âââââââââ³âââââââââ
â                Statistic â    avg â    min â    max â    p99 â    p90 â    p75 â
â¡âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ©
â Time to first token (ms) â  11.70 â   9.88 â  17.21 â  14.35 â  12.01 â  11.87 â
â Inter token latency (ms) â   1.46 â   1.08 â   1.89 â   1.87 â   1.62 â   1.52 â
â     Request latency (ms) â 161.24 â 153.45 â 200.74 â 200.66 â 179.43 â 162.23 â
â   Output sequence length â 103.39 â  95.00 â 134.00 â 120.08 â 107.30 â 105.00 â
â    Input sequence length â 200.01 â 200.00 â 201.00 â 200.13 â 200.00 â 200.00 â
ââââââââââââââââââââââââââââ´âââââââââ´âââââââââ´âââââââââ´âââââââââ´âââââââââ´âââââââââ
Output token throughput (per sec): 635.61
Request throughput (per sec): 6.15
```

See [Tutorial](docs/tutorial.md) for additional examples.

### Visualization[#](#visualization "Link to this heading")

GenAI-Perf can also generate various plots that visualize the
performance of the current profile run. This is disabled by default but
users can easily enable it by passing the `--generate-plots` option
when running the benchmark:

```
genai-perf profile \
  -m gpt2 \
  --service-kind triton \
  --backend tensorrtllm \
  --streaming \
  --concurrency 1 \
  --generate-plots
```

This will generate a [set of default
plots](docs/compare.md#example-plots) such as: - Time to first token
(TTFT) analysis - Request latency analysis - TTFT vs Input sequence
lengths - Inter token latencies vs Token positions - Input sequence
lengths vs Output sequence lengths

#### Using `compare` Subcommand to Visualize Multiple Runs[#](#using-compare-subcommand-to-visualize-multiple-runs "Link to this heading")

The `compare` subcommand in GenAI-Perf facilitates users in comparing
multiple profile runs and visualizing the differences through plots.

##### Usage[#](#usage "Link to this heading")

Assuming the user possesses two profile export JSON files, namely
`profile1.json` and `profile2.json`, they can execute the
`compare` subcommand using the `--files` option:

```
genai-perf compare --files profile1.json profile2.json
```

Executing the above command will perform the following actions under the
`compare` directory: 1. Generate a YAML configuration file
(e.g.Â `config.yaml`) containing the metadata for each plot generated
during the comparison process. 2. Automatically generate the [default
set of plots](docs/compare.md#example-plots) (e.g.Â TTFT vs.Â Input
Sequence Lengths) that compare the two profile runs.

```
compare
âââ config.yaml
âââ distribution_of_input_sequence_lengths_to_output_sequence_lengths.jpeg
âââ request_latency.jpeg
âââ time_to_first_token.jpeg
âââ time_to_first_token_vs_input_sequence_lengths.jpeg
âââ token-to-token_latency_vs_output_token_position.jpeg
âââ ...
```

##### Customization[#](#customization "Link to this heading")

Users have the flexibility to iteratively modify the generated YAML
configuration file to suit their specific requirements. They can make
alterations to the plots according to their preferences and execute the
command with the `--config` option followed by the path to the
modified configuration file:

```
genai-perf compare --config compare/config.yaml
```

This command will regenerate the plots based on the updated
configuration settings, enabling users to refine the visual
representation of the comparison results as per their needs.

See [Compare documentation](docs/compare.md) for more details.

### Model Inputs[#](#model-inputs "Link to this heading")

GenAI-Perf supports model input prompts from either synthetically
generated inputs, or from the HuggingFace
[OpenOrca](https://huggingface.co/datasets/Open-Orca/OpenOrca) or
[CNN\_DailyMail](https://huggingface.co/datasets/cnn_dailymail)
datasets. This is specified using the `--input-dataset` CLI option.

When the dataset is synthetic, you can specify the following options: \*
`--num-prompts <int>`: The number of unique prompts to generate as
stimulus, >= 1. \* `--synthetic-input-tokens-mean <int>`: The mean of
number of tokens in the generated prompts when using synthetic data, >=
1. \* `--synthetic-input-tokens-stddev <int>`: The standard deviation
of number of tokens in the generated prompts when using synthetic data,
>= 0. \* `--random-seed <int>`: The seed used to generate random
values, >= 0.

When the dataset is coming from HuggingFace, you can specify the
following options: \* `--input-dataset {openorca,cnn_dailymail}`:
HuggingFace dataset to use for benchmarking. \* `--num-prompts <int>`:
The number of unique prompts to generate as stimulus, >= 1.

When the dataset is coming from a file, you can specify the following
options: \* `--input-file <path>`: The input file containing the
prompts to use for benchmarking as JSON objects.

For any dataset, you can specify the following options: \*
`--output-tokens-mean <int>`: The mean number of tokens in each
output. Ensure the `--tokenizer` value is set correctly, >= 1. \*
`--output-tokens-stddev <int>`: The standard deviation of the number
of tokens in each output. This is only used when output-tokens-mean is
provided, >= 1. \* `--output-tokens-mean-deterministic`: When using
`--output-tokens-mean`, this flag can be set to improve precision by
setting the minimum number of tokens equal to the requested number of
tokens. This is currently supported with the Triton service-kind. Note
that there is still some variability in the requested number of output
tokens, but GenAi-Perf attempts its best effort with your model to get
the right number of output tokens.

You can optionally set additional model inputs with the following
option: \* `--extra-inputs <input_name>:<value>`: An additional input
for use with the model with a singular value, such as `stream:true` or
`max_tokens:5`. This flag can be repeated to supply multiple extra
inputs.

For [Large Language Models](docs/tutorial.md), there is no batch size
(i.e. batch size is always `1`). Each request includes the inputs for
one individual inference. Other modes such as the
[embeddings](docs/embeddings.md) and [rankings](docs/rankings.md)
endpoints support client-side batching, where `--batch-size N` means
that each request sent will include the inputs for `N` separate
inferences, allowing them to be processed together.

### Metrics[#](#metrics "Link to this heading")

GenAI-Perf collects a diverse set of metrics that captures the
performance of the inference server.

| Metric | Description | Aggregations |
| --- | --- | --- |
| Time to First Token | Time between when a request is sent and when its first response is received, one value per request in benchmark | Avg, min, max, p99, p90, p75 |
| Inter Token Latency | Time between intermediate responses for a single request divided by the number of generated tokens of the latter response, one value per response per request in benchmark | Avg, min, max, p99, p90, p75 |
| Request Latency | Time between when a request is sent and when its final response is received, one value per request in benchmark | Avg, min, max, p99, p90, p75 |
| Output Sequence Length | Total number of output tokens of a request, one value per request in benchmark | Avg, min, max, p99, p90, p75 |
| Input Sequence Length | Total number of input tokens of a request, one value per request in benchmark | Avg, min, max, p99, p90, p75 |
| Output Token Throughput | Total number of output tokens from benchmark divided by benchmark duration | Noneâone value per benchmark |
| Request Throughput | Number of final responses from benchmark divided by benchmark duration | Noneâone value per benchmark |

### Command Line Options[#](#command-line-options "Link to this heading")

Show the help message and exit.

#### Endpoint Options:[#](#endpoint-options "Link to this heading")

The names of the models to benchmark. A single model is recommended,
unless you are [profiling multiple LoRA adapters](docs/lora.md).
(default: `None`)

When multiple models are specified, this is how a specific model is
assigned to a prompt. Round robin means that each model receives a
request in order. Random means that assignment is uniformly random
(default: `round_robin`)

When using the âtritonâ service-kind, this is the backend of the model.
For the TRT-LLM backend, you currently must set
`exclude_input_in_output` to true in the model config to not echo the
input tokens in the output. (default: tensorrtllm)

Set a custom endpoint that differs from the OpenAI defaults. (default:
`None`)

The endpoint-type to send requests to on the server. This is only used
with the `openai` service-kind. (default: `None`)

The kind of service perf\_analyzer will generate load for. In order to
use `openai`, you must specify an api via `--endpoint-type`.
(default: `triton`)

An option to enable the use of the streaming API. (default: `False`)

URL of the endpoint to target for benchmarking. (default: `None`)

#### Input Options[#](#input-options "Link to this heading")

The batch size of the requests GenAI-Perf should send. This is currently
only supported with the [embeddings](docs/embeddings.md),
image\_retrieval, and [rankings](docs/rankings.md) endpoint types.
(default: `1`)

Provide additional inputs to include with every request. You can repeat
this flag for multiple inputs. Inputs should be in an input\_name:value
format. Alternatively, a string representing a json formatted dict can
be provided. (default: `None`)

The HuggingFace dataset to use for prompts. (default: `openorca`)

The input file containing the prompts to use for profiling. Each line
should be a JSON object with a âtext\_inputâ field in JSONL format.
Example: {âtext\_inputâ: âYour prompt hereâ}â

The number of unique prompts to generate as stimulus. (default: `100`)

The mean number of tokens in each output. Ensure the `--tokenizer`
value is set correctly. (default: `-1`)

When using `--output-tokens-mean`, this flag can be set to improve
precision by setting the minimum number of tokens equal to the requested
number of tokens. This is currently supported with the Triton
service-kind. Note that there is still some variability in the requested
number of output tokens, but GenAi-Perf attempts its best effort with
your model to get the right number of output tokens. (default:
`False`)

The standard deviation of the number of tokens in each output. This is
only used when `--output-tokens-mean` is provided. (default: `0`)

The seed used to generate random values. (default: `0`)

The mean of number of tokens in the generated prompts when using
synthetic data. (default: `550`)

The standard deviation of number of tokens in the generated prompts when
using synthetic data. (default: `0`)

#### Profiling Options[#](#profiling-options "Link to this heading")

The concurrency value to benchmark. (default: `None`)

The time interval used for each measurement in milliseconds. Perf
Analyzer will sample a time interval specified and take measurement over
the requests completed within that time interval. (default: `10000`)

Sets the request rate for the load generated by PA. (default: `None`)

The allowed variation in latency measurements when determining if a
result is stable. The measurement is considered as stable if the ratio
of max / min from the recent 3 measurements is within (stability
percentage) in terms of both infer per second and latency. (default:
`999`)

#### Output Options[#](#output-options "Link to this heading")

The directory to store all the (output) artifacts generated by
GenAI-Perf and Perf Analyzer. (default: `artifacts`)

An option to enable the generation of plots. (default: False)

The path where the perf\_analyzer profile export will be generated. By
default, the profile export will be to `profile_export.json`. The
genai-perf files will be exported to
`<profile_export_file>_genai_perf.json` and
`<profile_export_file>_genai_perf.csv`. For example, if the profile
export file is `profile_export.json`, the genai-perf file will be
exported to `profile_export_genai_perf.csv`. (default:
`profile_export.json`)

#### Other Options[#](#other-options "Link to this heading")

The HuggingFace tokenizer to use to interpret token metrics from prompts
and responses. (default: `hf-internal-testing/llama-tokenizer`)

An option to enable verbose mode. (default: `False`)

An option to print the version and exit.

### Known Issues[#](#known-issues "Link to this heading")

* GenAI-Perf can be slow to finish if a high request-rate is provided
* Token counts may not be exact

