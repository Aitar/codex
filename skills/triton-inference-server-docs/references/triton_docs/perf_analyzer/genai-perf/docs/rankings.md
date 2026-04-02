* [GenAI Performance Analyzer](../../../perf_benchmark/genai_perf.md)
* Profile...

# Profile Ranking Models with GenAI-Perf[#](#profile-ranking-models-with-genai-perf "Link to this heading")

GenAI-Perf allows you to profile ranking models compatible with Hugging Faceâs
[Text Embeddings Inferenceâs re-ranker API](https://huggingface.co/docs/text-embeddings-inference/en/quick_tour#re-rankers).

## Start a Hugging Face Re-Ranker-Compatible Server[#](#start-a-hugging-face-re-ranker-compatible-server "Link to this heading")

To start a Hugging Face re-ranker-compatible server, run the following commands:

```
model=BAAI/bge-reranker-base

docker run --gpus all -p 8080:80 --pull always ghcr.io/huggingface/text-embeddings-inference:1.3 --model-id $model --port 80
```

To specify the use of the HuggingFace server,
our benchmarking commands below will include
`--endpoint rerank` and `--extra-inputs rankings:tei`.

## Approach 1. Profile Using Synthetic Inputs[#](#approach-1-profile-using-synthetic-inputs "Link to this heading")

To profile ranking models using GenAI-Perf, use the following command:

```
genai-perf profile \
    -m BAAI/bge-reranker-base \
    --endpoint-type rankings \
    --endpoint rerank \
    --input-file synthetic:queries,passages \
    -u localhost:8080 \
    --extra-inputs rankings:tei \
    --synthetic-input-tokens-mean 100 \
    --batch-size-text 2
```

## Approach 2. Profile Using Custom Inputs[#](#approach-2-profile-using-custom-inputs "Link to this heading")

### Create a Sample Rankings Input Directory[#](#create-a-sample-rankings-input-directory "Link to this heading")

To create a sample rankings input directory, follow these steps:

Create a directory called rankings\_jsonl:

```
mkdir rankings_jsonl
```

Inside this directory, create a JSONL file named queries.jsonl with queries data:

```
echo '{"text": "What was the first car ever driven?"}
{"text": "Who served as the 5th President of the United States of America?"}
{"text": "Is the Sydney Opera House located in Australia?"}
{"text": "In what state did they film Shrek 2?"}' > rankings_jsonl/queries.jsonl
```

Create another JSONL file named passages.jsonl with passages data:

```
echo '{"text": "Eric Anderson (born January 18, 1968) is an American sociologist and sexologist."}
{"text": "Kevin Loader is a British film and television producer."}
{"text": "Francisco Antonio Zea Juan Francisco Antonio Hilari was a Colombian journalist, botanist, diplomat, politician, and statesman who served as the 1st Vice President of Colombia."}
{"text": "Daddys Home 2 Principal photography on the film began in Massachusetts in March 2017 and it was released in the United States by Paramount Pictures on November 10, 2017. Although the film received unfavorable reviews, it has grossed over $180 million worldwide on a $69 million budget."}' > rankings_jsonl/passages.jsonl
```

### Run GenAI-Perf[#](#run-genai-perf "Link to this heading")

To profile ranking models using GenAI-Perf, use the following command:

```
genai-perf profile \
    -m BAAI/bge-reranker-base \
    --endpoint-type rankings \
    --endpoint rerank \
    --input-file rankings_jsonl/ \
    -u localhost:8080 \
    --extra-inputs rankings:tei
```

## Review the Output[#](#review-the-output "Link to this heading")

Example output:

```
                          Rankings Metrics
ââââââââââââââââââââââââ³âââââââ³âââââââ³ââââââââ³ââââââââ³âââââââ³âââââââ
â            Statistic â  avg â  min â   max â   p99 â  p90 â  p75 â
â¡âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ©
â Request latency (ms) â 5.48 â 2.50 â 23.91 â 10.27 â 8.34 â 6.07 â
ââââââââââââââââââââââââ´âââââââ´âââââââ´ââââââââ´ââââââââ´âââââââ´âââââââ
Request throughput (per sec): 180.11
```

