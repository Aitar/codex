* [API Reference](api_reference.md)
* OpenAI-Compa...

# OpenAI-Compatible Frontend for Triton Inference Server[#](#openai-compatible-frontend-for-triton-inference-server "Link to this heading")

## Pre-requisites[#](#pre-requisites "Link to this heading")

1. Docker + NVIDIA Container Runtime
2. A correctly configured `HF_TOKEN` for access to HuggingFace models.

   * The current examples and testing primarily use the
     [`meta-llama/Meta-Llama-3.1-8B-Instruct`](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct)
     model, but you can manually bring your own models and adjust accordingly.

## VLLM[#](#vllm "Link to this heading")

1. Launch the container and install dependencies:

* Mounts the `~/.huggingface/cache` for re-use of downloaded models across runs, containers, etc.
* Sets the [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/en/package_reference/environment_variables#hftoken) environment variable to
  access gated models, make sure this is set in your local environment if needed.

```
docker run -it --net=host --gpus all --rm \
  -v ${HOME}/.cache/huggingface:/root/.cache/huggingface \
  -e HF_TOKEN \
  nvcr.io/nvidia/tritonserver:25.12-vllm-python-py3
```

2. Launch the OpenAI-compatible Triton Inference Server:

```
cd /opt/tritonserver/python/openai

# NOTE: Adjust the --tokenizer based on the model being used
python3 openai_frontend/main.py --model-repository tests/vllm_models --tokenizer meta-llama/Meta-Llama-3.1-8B-Instruct
```

Example output

```
...
+-----------------------+---------+--------+
| Model                 | Version | Status |
+-----------------------+---------+--------+
| llama-3.1-8b-instruct | 1       | READY  | <- Correct Model Loaded in Triton
+-----------------------+---------+--------+
...
Found model: name='llama-3.1-8b-instruct', backend='vllm'
[WARNING] Adding CORS for the following origins: ['http://localhost']
INFO:     Started server process [126]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:9000 (Press CTRL+C to quit) <- OpenAI Frontend Started Successfully
```

3. Send a `/v1/chat/completions` request:

* Note the use of `jq` is optional, but provides a nicely formatted output for JSON responses.

```
MODEL="llama-3.1-8b-instruct"
curl -s http://localhost:9000/v1/chat/completions -H 'Content-Type: application/json' -d '{
  "model": "'${MODEL}'",
  "messages": [{"role": "user", "content": "Say this is a test!"}]
}' | jq
```

Example output

```
{
  "id": "cmpl-0242093d-51ae-11f0-b339-e7480668bfbe",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message":
      {
        "content": "This is only a test.",
        "tool_calls": null,
        "role": "assistant",
        "function_call": null
      },
      "logprobs": null
    }
  ],
  "created": 1750846825,
  "model": "llama-3.1-8b-instruct",
  "system_fingerprint": null,
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 7,
    "prompt_tokens": 42,
    "total_tokens": 49
  }
}
```

4. Send a `/v1/completions` request:

* Note the use of `jq` is optional, but provides a nicely formatted output for JSON responses.

```
MODEL="llama-3.1-8b-instruct"
curl -s http://localhost:9000/v1/completions -H 'Content-Type: application/json' -d '{
  "model": "'${MODEL}'",
  "prompt": "Machine learning is"
}' | jq
```

Example output

```
{
  "id": "cmpl-58fba3a0-51ae-11f0-859d-e7480668bfbe",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "text": " an amazing field that can truly understand the hidden patterns that exist in the data,"
    }
  ],
  "created": 1750846970,
  "model": "llama-3.1-8b-instruct",
  "system_fingerprint": null,
  "object": "text_completion",
  "usage": {
    "completion_tokens": 16,
    "prompt_tokens": 4,
    "total_tokens": 20
  }
}
```

5. Benchmark with `genai-perf`:

* To install genai-perf in this container, see the instructions [here](../perf_analyzer/genai-perf/README.md#install-perf-analyzer-ubuntu-python-38)
* Or try using genai-perf from the [SDK container](../perf_analyzer/genai-perf/README.md#install-perf-analyzer-ubuntu-python-38)

```
MODEL="llama-3.1-8b-instruct"
TOKENIZER="meta-llama/Meta-Llama-3.1-8B-Instruct"
genai-perf profile \
  --model ${MODEL} \
  --tokenizer ${TOKENIZER} \
  --service-kind openai \
  --endpoint-type chat \
  --url localhost:9000 \
  --streaming
```

Example output

```
2024-10-14 22:43 [INFO] genai_perf.parser:82 - Profiling these models: llama-3.1-8b-instruct
2024-10-14 22:43 [INFO] genai_perf.wrapper:163 - Running Perf Analyzer : 'perf_analyzer -m llama-3.1-8b-instruct --async --input-data artifacts/llama-3.1-8b-instruct-openai-chat-concurrency1/inputs.json -i http --concurrency-range 1 --endpoint v1/chat/completions --service-kind openai -u localhost:9000 --measurement-interval 10000 --stability-percentage 999 --profile-export-file artifacts/llama-3.1-8b-instruct-openai-chat-concurrency1/profile_export.json'
                              NVIDIA GenAI-Perf | LLM Metrics
âââââââââââââââââââââââââââââââââââââ³âââââââââ³âââââââââ³âââââââââ³âââââââââ³âââââââââ³âââââââââ
â                         Statistic â    avg â    min â    max â    p99 â    p90 â    p75 â
â¡ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ©
â          Time to first token (ms) â  71.66 â  64.32 â  86.52 â  76.13 â  74.92 â  73.26 â
â          Inter token latency (ms) â  18.47 â  18.25 â  18.72 â  18.67 â  18.61 â  18.53 â
â              Request latency (ms) â 348.00 â 274.60 â 362.27 â 355.41 â 352.29 â 350.66 â
â            Output sequence length â  15.96 â  12.00 â  16.00 â  16.00 â  16.00 â  16.00 â
â             Input sequence length â 549.66 â 548.00 â 551.00 â 550.00 â 550.00 â 550.00 â
â Output token throughput (per sec) â  45.84 â    N/A â    N/A â    N/A â    N/A â    N/A â
â      Request throughput (per sec) â   2.87 â    N/A â    N/A â    N/A â    N/A â    N/A â
âââââââââââââââââââââââââââââââââââââ´âââââââââ´âââââââââ´âââââââââ´âââââââââ´âââââââââ´âââââââââ
2024-10-14 22:44 [INFO] genai_perf.export_data.json_exporter:62 - Generating artifacts/llama-3.1-8b-instruct-openai-chat-concurrency1/profile_export_genai_perf.json
2024-10-14 22:44 [INFO] genai_perf.export_data.csv_exporter:71 - Generating artifacts/llama-3.1-8b-instruct-openai-chat-concurrency1/profile_export_genai_perf.csv
```

6. Use the OpenAI python client directly:

```
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:9000/v1",
    api_key="EMPTY",
)

model = "llama-3.1-8b-instruct"
completion = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {"role": "user", "content": "What are LLMs?"},
    ],
    max_completion_tokens=256,
)

print(completion.choices[0].message.content)
```

7. Run tests (NOTE: The server should not be running, the tests will handle starting/stopping the server as necessary):

```
cd /opt/tritonserver/python/openai/
pip install -r requirements-test.txt

pytest -v tests/
```

### LoRA Adapters[#](#lora-adapters "Link to this heading")

If the command line argument `--lora-separator=<separator_string>` is provided
when starting the OpenAI Frontend, a LoRA adaptor listed in `multi_lora.json`
may be selected by appending the LoRA name to the model name,
separated by the LoRA separator, on the inference request in
`<model_name><separator_string><lora_name>` format.

For example

```
# start server with model named gemma-2b
python3 openai_frontend/main.py --lora-separator=_lora_ ...

# inference without LoRA
curl -s http://localhost:9000/v1/completions -H 'Content-Type: application/json' -d '{
  "model": "gemma-2b",
  "temperature": 0,
  "prompt": "When was the wheel invented?"
}'
{
  ...
  "choices":[{..."text":"\n\nThe wheel was invented by the Sumerians in Mesopotamia around 350"}],
  ...
}

# inference with LoRA named doll
curl -s http://localhost:9000/v1/completions -H 'Content-Type: application/json' -d '{
  "model": "gemma-2b_lora_doll",
  "temperature": 0,
  "prompt": "When was the wheel invented?"
}'
{
  ...
  "choices":[{..."text":"\n\nThe wheel was invented in Mesopotamia around 3500 BC.\n\n"}],
  ...
}

# inference with LoRA named sheep
curl -s http://localhost:9000/v1/completions -H 'Content-Type: application/json' -d '{
  "model": "gemma-2b_lora_sheep",
  "temperature": 0,
  "prompt": "When was the wheel invented?"
}'
{
  ...
  "choices":[{..."text":"\n\nThe wheel was invented around 3000 BC in Mesopotamia.\n\n"}],
  ...
}
```

When listing or retrieving model(s), the model id will include the LoRA name in
the same `<model_name><separator_string><lora_name>` format for each LoRA
adapter listed on the `multi_lora.json`. Note: The LoRA name inclusion is
limited to locally stored models, inference requests are not limited though.

#### vLLM[#](#id1 "Link to this heading")

See the
[vLLM documentation](../vllm_backend/docs/llama_multi_lora_tutorial.md)
on how to serve a vLLM model with LoRA adapters.

#### TensorRT-LLM[#](#tensorrt-llm "Link to this heading")

Similarly, see [TensorRT-LLM document](../tensorrtllm_backend/docs/lora.md)
on how to prepare LoRA-enabled TensorRT-LLM engines and generate LoRA tensors.
The path of LoRA adapter in `multi_lora.json` is the directory of
`model.lora_config.npy` and `model.lora_weights.npy` tensors.

For example

model repository

```
inflight_batcher_llm
âââ postprocessing
|   âââ 1
|   |   âââ model.py
|   âââ config.pbtxt
âââ preprocessing
|   âââ 1
|   |   âââ model.py
|   âââ config.pbtxt
âââ tensorrt_llm
|   âââ 1
|   |   âââ model.py
|   âââ config.pbtxt
âââ tensorrt_llm_bls
    âââ 1
    |   âââ Japanese-Alpaca-LoRA-7b-v0-weights
    |   |   âââ model.lora_config.npy
    |   |   âââ model.lora_weights.npy
    |   âââ luotuo-lora-7b-0.1-weights
    |   |   âââ model.lora_config.npy
    |   |   âââ model.lora_weights.npy
    |   âââ model.py
    |   âââ multi_lora.json
    âââ config.pbtxt
```

multi\_lora.json

```
{
  "doll": "inflight_batcher_llm/tensorrt_llm_bls/1/luotuo-lora-7b-0.1-weights",
  "sheep": "inflight_batcher_llm/tensorrt_llm_bls/1/Japanese-Alpaca-LoRA-7b-v0-weights"
}
```

### Embedding Models[#](#embedding-models "Link to this heading")

Currently, OpenAI-Compatible Frontend supports loading embedding models and embeddings endpoints via vLLM backend. Check [vLLM supported models](https://docs.vllm.ai/en/latest/models/supported_models.md#embedding) for all supported embedding models from vLLM.

1. Launch the container and install dependencies:

* Mounts the `~/.huggingface/cache` for re-use of downloaded models across runs, containers, etc.
* Sets the [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/en/package_reference/environment_variables#hftoken) environment variable to
  access gated models, make sure this is set in your local environment if needed.

```
docker run -it --net=host --gpus all --rm \
  -v ${HOME}/.cache/huggingface:/root/.cache/huggingface \
  -e HF_TOKEN \
  nvcr.io/nvidia/tritonserver:25.12-vllm-python-py3
```

2. Launch the OpenAI-compatible Triton Inference Server:

```
cd /opt/tritonserver/python/openai

# NOTE: Embeddings endpoint does not require "--tokenizer"
python3 openai_frontend/main.py --model-repository tests/vllm_embedding_models
```

Example output

```
...
+------------------+---------+--------+
| Model            | Version | Status |
+------------------+---------+--------+
| all-MiniLM-L6-v2 | 1       | READY  | <- Correct Model Loaded in Triton
+------------------+---------+--------+
...
Found model: name='all-MiniLM-L6-v2', backend='vllm'
[WARNING] Adding CORS for the following origins: ['http://localhost']
INFO:     Started server process [133]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:9000 (Press CTRL+C to quit) <- OpenAI Frontend Started Successfully
```

3. Send a `/v1/embeddings` request:

* Note the use of `jq` is optional, but provides a nicely formatted output for JSON responses.

```
MODEL="all-MiniLM-L6-v2"
curl -s http://localhost:9000/v1/embeddings \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "'${MODEL}'",
    "input": "The food was delicious and the waiter...",
    "dimensions": 10,
    "encoding_format": "float"
  }' | jq
```

Example output

```
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "embedding": [
        -0.1914404183626175,
        0.4000193178653717,
        0.058502197265625,
        0.18909454345703125,
        -0.4690297544002533,
        0.004936536308377981,
        0.45893096923828125,
        -0.31141534447669983,
        0.18299102783203125,
        -0.4907582700252533
      ],
      "index": 0
    }
  ],
  "model": "all-MiniLM-L6-v2",
  "usage": {
    "prompt_tokens": 12,
    "total_tokens": 12
  }
}
```

## TensorRT-LLM[#](#id2 "Link to this heading")

0. Prepare your model repository for a TensorRT-LLM model, build the engine, etc. You can try any of the following options:

* [Triton CLI](https://github.com/triton-inference-server/triton_cli/)
* [TRT-LLM Backend Quickstart](https://github.com/triton-inference-server/tensorrtllm_backend?tab=readme-ov-file#quick-start)

1. Launch the container:

* Mounts the `~/.huggingface/cache` for re-use of downloaded models across runs, containers, etc.
* Sets the [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/en/package_reference/environment_variables#hftoken) environment variable to
  access gated models, make sure this is set in your local environment if needed.

```
docker run -it --net=host --gpus all --rm \
  -v ${HOME}/.cache/huggingface:/root/.cache/huggingface \
  -e HF_TOKEN \
  -e TRTLLM_ORCHESTRATOR=1 \
  nvcr.io/nvidia/tritonserver:25.12-trtllm-python-py3
```

2. Install dependencies inside the container:

```
# Install python bindings for tritonserver and tritonfrontend
pip install /opt/tritonserver/python/triton*.whl

# Install application requirements
git clone https://github.com/triton-inference-server/server.git
cd server/python/openai/
pip install -r requirements.txt
```

2. Launch the OpenAI server:

```
# NOTE: Adjust the --tokenizer based on the model being used
python3 openai_frontend/main.py --model-repository path/to/models --tokenizer meta-llama/Meta-Llama-3.1-8B-Instruct
```

3. Send a `/v1/chat/completions` request:

* Note the use of `jq` is optional, but provides a nicely formatted output for JSON responses.

```
# MODEL should be the client-facing model name in your model repository for a pipeline like TRT-LLM.
# For example, this could also be "ensemble", or something like "gpt2" if generated from Triton CLI
MODEL="tensorrt_llm_bls"
curl -s http://localhost:9000/v1/chat/completions -H 'Content-Type: application/json' -d '{
  "model": "'${MODEL}'",
  "messages": [{"role": "user", "content": "Say this is a test!"}]
}' | jq
```

Example output

```
{
  "id": "cmpl-5ad4f860-bf13-11f0-b137-b75b7f0a8586",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "It looks like you're ready to see if I'm functioning properly. What would",
        "tool_calls": null,
        "role": "assistant",
        "function_call": null
      },
      "logprobs": null
    }
  ],
  "created": 1762875029,
  "model": "tensorrt_llm_bls",
  "system_fingerprint": null,
  "object": "chat.completion",
  "usage": {
    "prompt_tokens": 42,
    "total_tokens": 58,
    "completion_tokens": 16
  }
}
```

The other examples should be the same as vLLM, except that you should set `MODEL="tensorrt_llm_bls"` or `MODEL="ensemble"`,
everywhere applicable as seen in the example request above.

## KServe Frontends[#](#kserve-frontends "Link to this heading")

To support serving requests through both the OpenAI-Compatible and
KServe Predict v2 frontends to the same running Triton Inference Server,
the `tritonfrontend` python bindings are included for optional use in this
application as well.

You can opt-in to including these additional frontends, assuming `tritonfrontend`
is installed, with `--enable-kserve-frontends` like below:

```
python3 openai_frontend/main.py \
  --model-repository tests/vllm_models \
  --tokenizer meta-llama/Meta-Llama-3.1-8B-Instruct \
  --enable-kserve-frontends
```

See `python3 openai_frontend/main.py --help` for more information on the
available arguments and default values.

For more information on the `tritonfrontend` python bindings, see the docs
[here](../customization_guide/tritonfrontend.md).

## Model Parallelism Support[#](#model-parallelism-support "Link to this heading")

* [x] vLLM ([EngineArgs](../vllm_backend/README.md#using-the-vllm-backend))

  + ex: Configure `tensor_parallel_size: 2` in the
    [model.json](https://github.com/triton-inference-server/vllm_backend/blob/main/samples/model_repository/vllm_model/1/model.json)
* [x] TensorRT-LLM ([Orchestrator Mode](../tensorrtllm_backend/README.md#orchestrator-mode))

  + Set the following environment variable: `export TRTLLM_ORCHESTRATOR=1`
* [ ] TensorRT-LLM ([Leader Mode](../tensorrtllm_backend/README.md#leader-mode))

  + Not currently supported

## Tool Calling[#](#tool-calling "Link to this heading")

The OpenAI frontend supports `tools` and `tool_choice` in the `v1/chat/completions` API. Please refer to the OpenAI API reference for more details about these parameters:
[tools](https://platform.openai.com/docs/api-reference/chat/create#chat-create-tools),
[tool\_choice](https://platform.openai.com/docs/api-reference/chat/create#chat-create-tool_choice)

To enable the tool-calling feature, add the `--tool-call-parser {parser_name}` flag when starting the server. The two available parsers are `llama3` and `mistral`.
The `llama3` parser supports tool-calling features for LLaMA 3.1, 3.2, and 3.3 models, while the `mistral` parser supports tool-calling features for the Mistral Instruct model.

Example for launching the OpenAI frontend with a tool call parser:

```
python3 openai_frontend/main.py \
  --model-repository tests/vllm_models \
  --tokenizer meta-llama/Meta-Llama-3.1-8B-Instruct \
  --tool-call-parser llama3
```

Example for making a tool calling request:

```
import json
from openai import OpenAI


def get_current_weather(city: str, state: str, unit: "str"):
    return (
        "The weather in Dallas, Texas is 85 degrees fahrenheit. It is "
        "partly cloudly, with highs in the 90's."
    )

available_tools = {"get_current_weather": get_current_weather}

openai_api_key = "EMPTY"
openai_api_base = "http://localhost:9000/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

model = "llama-3.1-8b-instruct" # change this to the model in the repository

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city to find the weather for, e.g. 'San Francisco'",
                    },
                    "state": {
                        "type": "string",
                        "description": "the two-letter abbreviation for the state that the city is"
                        " in, e.g. 'CA' which would mean 'California'",
                    },
                    "unit": {
                        "type": "string",
                        "description": "The unit to fetch the temperature in",
                        "enum": ["celsius", "fahrenheit"],
                    },
                },
                "required": ["city", "state", "unit"],
            },
        },
    }
]

messages = [
    {
        "role": "system",
        "content": "You're a helpful assistant! Answer the users question best you can.",
    },
    {"role": "user", "content": "What is the weather in Dallas, Texas in Fahrenheit?"},
]

tool_calls = client.chat.completions.create(
    messages=messages, model=model, tools=tools, max_completion_tokens=128
)
function_name = tool_calls.choices[0].message.tool_calls[0].function.name
function_arguments = tool_calls.choices[0].message.tool_calls[0].function.arguments

print(f"function name: " f"{function_name}")
print(f"function arguments: {function_arguments}")
print(f"tool calling result: {available_tools[function_name](https://github.com/triton-inference-server/server/blob/main/docs/client_guide/**json.loads(function_arguments))}")
```

Example output:

```
function name: get_current_weather
function arguments: {"city": "Dallas", "state": "TX", "unit": "fahrenheit"}
tool calling result: The weather in Dallas, Texas is 85 degrees fahrenheit. It is partly cloudly, with highs in the 90's.
```

### Named Tool Calling[#](#named-tool-calling "Link to this heading")

The OpenAI frontend supports named function calling, utilizing structured outputs in the vLLM backend and guided decoding in TensorRT-LLM backend. Users can specify one of the tools in `tool_choice` to force the model to select a specific tool for function calling.

> [!NOTE]
> For instructions on enabling guided decoding in the TensorRT-LLM backend, please refer to [this guide](../tensorrtllm_backend/docs/guided_decoding.md)

Example for making a named tool calling request:

```
import json
from openai import OpenAI


def get_current_weather(city: str, state: str, unit: "str"):
    return (
        "The weather in Dallas, Texas is 85 degrees fahrenheit. It is "
        "partly cloudly, with highs in the 90's."
    )

def get_n_day_weather_forecast(city: str, state: str, unit: str, num_days: int):
    return (
        f"The weather in Dallas, Texas is 85 degrees fahrenheit in next {num_days} days."
    )

available_tools = {"get_current_weather": get_current_weather,
                  "get_n_day_weather_forecast": get_n_day_weather_forecast}

openai_api_key = "EMPTY"
openai_api_base = "http://localhost:9000/v1"
client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)
model = "llama-3.1-8b-instruct" # change this to the model in the repository
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city to find the weather for, e.g. 'San Francisco'",
                    },
                    "state": {
                        "type": "string",
                        "description": "the two-letter abbreviation for the state that the city is"
                        " in, e.g. 'CA' which would mean 'California'",
                    },
                    "unit": {
                        "type": "string",
                        "description": "The unit to fetch the temperature in",
                        "enum": ["celsius", "fahrenheit"],
                    },
                },
                "required": ["city", "state", "unit"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_n_day_weather_forecast",
            "description": "Get an N-day weather forecast",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city to find the weather for, "
                        "e.g. 'San Francisco'",
                    },
                    "state": {
                        "type": "string",
                        "description": "must the two-letter abbreviation for the state "
                        "that the city is in, e.g. 'CA' which would "
                        "mean 'California'",
                    },
                    "unit": {
                        "type": "string",
                        "description": "The unit to fetch the temperature in",
                        "enum": ["celsius", "fahrenheit"],
                    },
                    "num_days": {
                        "type": "integer",
                        "description": "The number of days to forecast",
                    },
                },
                "required": ["city", "state", "unit", "num_days"],
            },
        },
     }
]

tool_choice = {"function": {"name": "get_n_day_weather_forecast"}, "type": "function"}

messages = [
    {
        "role": "system",
        "content": "You're a helpful assistant! Answer the users question best you can.",
    },
    {"role": "user", "content": "What is the weather in Dallas, Texas in Fahrenheit?"},
]

tool_calls = client.chat.completions.create(
    messages=messages, model=model, tools=tools, tool_choice=tool_choice, max_completion_tokens=128
)
function_name = tool_calls.choices[0].message.tool_calls[0].function.name
function_arguments = tool_calls.choices[0].message.tool_calls[0].function.arguments

print(f"function name: {function_name}")
print(f"function arguments: {function_arguments}")
print(f"tool calling result: {available_tools[function_name](https://github.com/triton-inference-server/server/blob/main/docs/client_guide/**json.loads(function_arguments))}")
```

Example output:

```
function name: get_n_day_weather_forecast
function arguments: {"city": "Dallas", "state": "TX", "unit": "fahrenheit", num_days: 1}
tool calling result: The weather in Dallas, Texas is 85 degrees fahrenheit in next 1 days.
```

## Limit Endpoint Access[#](#limit-endpoint-access "Link to this heading")

The OpenAI-compatible server supports restricting access to specific API endpoints through authentication headers. This feature allows you to protect sensitive endpoints while keeping others publicly accessible.

### Configuration[#](#configuration "Link to this heading")

Use the `--openai-restricted-api` command-line argument to configure endpoint restrictions:

```
--openai-restricted-api <API_1>,<API_2>,... <restricted-key> <restricted-value>
```

* **`API`**: A comma-separated list of APIs to be included in this group. Note that currently a given API is not allowed to be included in multiple groups. The following protocols / APIs are recognized:

  + **inference**: Chat completions and text completions endpoints

    - `POST /v1/chat/completions`
    - `POST /v1/completions`
  + **embedding**: Embedding endpoint

    - `POST /v1/embeddings`
  + **model-repository**: Model listing and information endpoints

    - `GET /v1/models`
    - `GET /v1/models/{model_name}`
  + **metrics**: Server metrics endpoint

    - `GET /metrics`
  + **health**: Health check endpoint

    - `GET /health/ready`
* **`restricted-key`**: The HTTP request header to be checked when a request is received.
* **`restricted-value`**: The header value required to access the specified protocols.

### Examples[#](#examples "Link to this heading")

#### Restrict Inference API Endpoints Only[#](#restrict-inference-api-endpoints-only "Link to this heading")

```
--openai-restricted-api "inference api-key my-secret-key"
```

Clients must include the header:

```
curl -H "api-key: my-secret-key" \
     -X POST http://localhost:9000/v1/chat/completions \
     -d '{"model": "my-model", "messages": [{"role": "user", "content": "Hello"}]}'
```

#### Restrict Multiple API Endpoints[#](#restrict-multiple-api-endpoints "Link to this heading")

```
# Different authentication for different APIs
--openai-restricted-api "inference user-key user-secret" \
--openai-restricted-api "model-repository admin-key admin-secret"

# Multiple APIs in single argument with shared authentication
--openai-restricted-api "inference,model-repository shared-key shared-secret"
```

