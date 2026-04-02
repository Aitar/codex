* [GenAI Performance Analyzer](../../../perf_benchmark/genai_perf.md)
* Profile...

# Profile Embeddings Models with GenAI-Perf[#](#profile-embeddings-models-with-genai-perf "Link to this heading")

GenAI-Perf allows you to profile embedding models running on an
[OpenAI Embeddings API](https://platform.openai.com/docs/api-reference/embeddings)-compatible server.

## Start an OpenAI Embeddings-Compatible Server[#](#start-an-openai-embeddings-compatible-server "Link to this heading")

To start an OpenAI embeddings-compatible server, run the following command:

```
docker run -it --net=host --rm --gpus=all vllm/vllm-openai:latest --model intfloat/e5-mistral-7b-instruct --dtype float16 --max-model-len 1024
```

## Approach 1. Profile Using Synthetic Inputs[#](#approach-1-profile-using-synthetic-inputs "Link to this heading")

To profile embeddings models using GenAI-Perf, use the following command:

```
genai-perf profile \
    -m intfloat/e5-mistral-7b-instruct \
    --endpoint-type embeddings \
    --batch-size-text 2
```

## Approach 2. Profile Using Custom Inputs[#](#approach-2-profile-using-custom-inputs "Link to this heading")

### Create a Sample Embeddings Input File[#](#create-a-sample-embeddings-input-file "Link to this heading")

To create a sample embeddings input file, use the following command:

```
echo '{"text": "What was the first car ever driven?"}
{"text": "Who served as the 5th President of the United States of America?"}
{"text": "Is the Sydney Opera House located in Australia?"}
{"text": "In what state did they film Shrek 2?"}' > embeddings.jsonl
```

This will generate a file named embeddings.jsonl with the following content:

```
{"text": "What was the first car ever driven?"}
{"text": "Who served as the 5th President of the United States of America?"}
{"text": "Is the Sydney Opera House located in Australia?"}
{"text": "In what state did they film Shrek 2?"}
```

### Run GenAI-Perf[#](#run-genai-perf "Link to this heading")

To profile embeddings models using GenAI-Perf, use the following command:

```
genai-perf profile \
    -m intfloat/e5-mistral-7b-instruct \
    --endpoint-type embeddings \
    --batch-size-text 2 \
    --input-file embeddings.jsonl
```

* `-m intfloat/e5-mistral-7b-instruct` is to specify what model you want to run
  (`intfloat/e5-mistral-7b-instruct`)
* `--endpoint-type embeddings` is to specify that the sent requests should be
  formatted to follow the OpenAI [embeddings
  API](https://platform.openai.com/docs/api-reference/embeddings/create)
* `--batch-size-text 2` is to specify that each request will contain the inputs for 2
  individual inferences, making a batch size of 2
* `--input-file embeddings.jsonl` is to specify the input data to be used for
  inferencing

This will use default values for optional arguments. You can also pass in
additional arguments with the `--extra-inputs` [flag](../README.md#input-options).
For example, you could use this command:

```
genai-perf profile \
    -m intfloat/e5-mistral-7b-instruct \
    --endpoint-type embeddings \
    --extra-inputs user:sample_user
```

## Review the Output[#](#review-the-output "Link to this heading")

Example output:

```
                          Embeddings Metrics
ââââââââââââââââââââââââ³ââââââââ³ââââââââ³âââââââââ³ââââââââ³ââââââââ³ââââââââ
â Statistic            â avg   â min   â max    â p99   â p90   â p75   â
â¡ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ©
â Request latency (ms) â 42.21 â 28.18 â 318.61 â 56.50 â 49.21 â 43.07 â
ââââââââââââââââââââââââ´ââââââââ´ââââââââ´âââââââââ´ââââââââ´ââââââââ´ââââââââ
Request throughput (per sec): 23.63
```

