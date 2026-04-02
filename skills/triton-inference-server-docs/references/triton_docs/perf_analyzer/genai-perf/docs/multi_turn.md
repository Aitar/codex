* Benchmark...

# Benchmark Multi-Turn Chat with GenAI-Perf[#](#benchmark-multi-turn-chat-with-genai-perf "Link to this heading")

GenAI-Perf allows you to benchmark multi-turn chat. This can be used for
simulating multiple turns in a conversation in a way that matches real-world
user behavior.

You can use either synthetic data or a custom dataset.
This tutorial will guide you through setting up a model server and running a
profiling session with simulated conversations or a predefined dataset.

## Table of Contents[#](#table-of-contents "Link to this heading")

* [Start a Chat Model Server](#start-a-chat-model-server)
* [Approach 1: Benchmark with Synthetic Data](#approach-1-benchmark-with-synthetic-data)
* [Approach 2: Benchmark with a Custom Dataset](#approach-2-benchmark-with-a-custom-dataset)
* [Review the Output](#review-the-output)

## Start a Chat Model Server[#](#start-a-chat-model-server "Link to this heading")

First, launch a vLLM server with an chat endpoint:

```
docker run -it --net=host --rm --gpus=all \
  vllm/vllm-openai:latest \
  --model TinyLlama/TinyLlama-1.1B-Chat-v1.0 \
  --dtype float16 \
  --max-model-len 1024
```

## Approach 1: Benchmark with Synthetic Data[#](#approach-1-benchmark-with-synthetic-data "Link to this heading")

Use synthetic data to simulate multiple chat sessions with controlled token
input and response lengths.

```
genai-perf profile \
  -m TinyLlama/TinyLlama-1.1B-Chat-v1.0 \
  --endpoint-type chat \
  --num-sessions 10 \
  --session-concurrency 5 \
  --session-turns-mean 2 \
  --session-turns-stddev 0 \
  --session-turn-delay-mean 1000 \
  --session-turn-delay-stddev 5 \
  --synthetic-input-tokens-mean 50 \
  --output-tokens-mean 50 \
  --num-prefix-prompts 3 \
  --prefix-prompt-length 15
```

### Understand Key Arguments[#](#understand-key-arguments "Link to this heading")

#### Required Arguments[#](#required-arguments "Link to this heading")

* `--num-sessions 10`: Simulates 10 independent chat sessions.
* `--session-concurrency 5`: Enables session mode and runs up to 5 sessions in
  parallel.

#### Optional Arguments[#](#optional-arguments "Link to this heading")

* `--session-turns-mean 2`: Each session has an average of 2 turns.
* `--session-turn-delay-mean 1000`: Introduces a 1-second delay between user
  turns (simulating real-world interaction).
* `--synthetic-input-tokens-mean 50`: Each user input averages 50 tokens.
* `--output-tokens-mean 50`: Each model response averages 50 tokens.
* `--num-prefix-prompts 3`: Uses a pool of 3 system prompts for the first
  turn in each session.
* `--prefix-prompt-length 15`: Each prefix prompt contains 15 tokens.

---

## Approach 2: Benchmark with a Custom Dataset[#](#approach-2-benchmark-with-a-custom-dataset "Link to this heading")

If you prefer to benchmark using a predefined dataset, create a JSONL input file
with the dataset.

### Example Input File[#](#example-input-file "Link to this heading")

```
echo '{"session_id": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6", "delay": 1000, "input_length": 50, "output_length": 10}
{"session_id": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6", "delay": 2000, "input_length": 50, "output_length": 10}
{"session_id": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6", "input_length": 100, "output_length": 10}
{"session_id": "113059749145936325402354257176981405696", "delay": 1000, "input_length": 25, "output_length": 20}
{"session_id": "113059749145936325402354257176981405696", "input_length": 20, "output_length": 20}' > inputs.jsonl
```

### Understand Key Arguments[#](#id1 "Link to this heading")

Most of the arguments are the same as the synthetic data approach.
The new ones are detailed below.

#### Optional Arguments[#](#id2 "Link to this heading")

* `--session-delay-ratio`: Modifies the delays in the payload file. The delays
  are multiplied by this ratio. This makes it easier to tune delays to represent
  different scenarios.

### Understand Key Fields[#](#understand-key-fields "Link to this heading")

#### Required Fields[#](#required-fields "Link to this heading")

* `delay`: Sets the delay in milliseconds to wait after receiving a response
  before sending the next request. This field is required except for the
  last turn in a session.

#### Optional Fields[#](#optional-fields "Link to this heading")

* `input_length`: Sets the token length of the input for this request.
* `output_length`: Sets the token length of the output for this request.
* `text`: Provides the prompt text, if you prefer to bring your own rather
  than have it be synthetically generated.

### Run GenAI-Perf with Custom Input[#](#run-genai-perf-with-custom-input "Link to this heading")

```
genai-perf profile \
  -m TinyLlama/TinyLlama-1.1B-Chat-v1.0 \
  --endpoint-type chat \
  --input-file payload:inputs.jsonl \
  --session-concurrency 2 \
  --session-delay-ratio 0.5
```

## Review the Output[#](#review-the-output "Link to this heading")

Example output:

```
                             NVIDIA GenAI-Perf | LLM Metrics
âââââââââââââââââââââââââââââââââââââ³âââââââââ³ââââââââ³âââââââââ³âââââââââ³âââââââââ³ââââââââ
â                         Statistic â    avg â   min â    max â    p99 â    p90 â   p75 â
â¡ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ©
â              Request Latency (ms) â  80.88 â 50.25 â 124.29 â 123.21 â 113.50 â 97.31 â
â   Output Sequence Length (tokens) â  14.00 â 10.00 â  20.00 â  20.00 â  20.00 â 20.00 â
â    Input Sequence Length (tokens) â  38.80 â 22.00 â  50.00 â  50.00 â  50.00 â 50.00 â
â Output Token Throughput (per sec) â 315.70 â   N/A â    N/A â    N/A â    N/A â   N/A â
â      Request Throughput (per sec) â  22.55 â   N/A â    N/A â    N/A â    N/A â   N/A â
â             Request Count (count) â   5.00 â   N/A â    N/A â    N/A â    N/A â   N/A â
âââââââââââââââââââââââââââââââââââââ´âââââââââ´ââââââââ´âââââââââ´âââââââââ´âââââââââ´ââââââââ
```

