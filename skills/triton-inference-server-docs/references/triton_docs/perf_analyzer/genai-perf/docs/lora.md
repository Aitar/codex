* [GenAI Performance Analyzer](../../../perf_benchmark/genai_perf.md)
* Profile...

# Profile Multiple LoRA Adapters[#](#profile-multiple-lora-adapters "Link to this heading")

GenAI-Perf allows you to profile multiple LoRA adapters on top of a base model.

## Select LoRA Adapters[#](#select-lora-adapters "Link to this heading")

To do this, list multiple adapters after the model name option `-m`:

```
genai-perf profile \
    -m lora_adapter1 lora_adapter2 lora_adapter3 \
    --tokenizer model_name
```

## Choose a Strategy for Selecting Models[#](#choose-a-strategy-for-selecting-models "Link to this heading")

When profiling with multiple models, you can specify how the models should be
assigned to prompts using the `--model-selection-strategy` option:

```
genai-perf profile \
    -m lora_adapter1 lora_adapter2 lora_adapter3 \
    --tokenizer model_name \
    --model-selection-strategy round_robin
```

This setup will cycle through the lora\_adapter1, lora\_adapter2, and
lora\_adapter3 models in a round-robin manner for each prompt.

For more details on additional options and configurations, refer to the
[Command Line Options section](../README.md#command-line-options) in the README.

## Profile Llama running on OpenAI Completions API-Compatible Server [#](#profile-llama-running-on-openai-completions-api-compatible-server "Link to this heading")

### Run Llama on [OpenAI Chat Completions API](https://platform.openai.com/docs/api-reference/chat)-compatible server[#](#run-llama-on-openai-chat-completions-api-compatible-server "Link to this heading")

See instructions

Download the adapters:

```
python3
from huggingface_hub import snapshot_download
lora_path = snapshot_download(repo_id="yard1/llama-2-7b-sql-lora-test")
lora_path_2 = snapshot_download(repo_id="monsterapi/llama2-code-generation")
```

Run the vLLM inference server:

```
docker run -it --net=host --rm --gpus=all \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    vllm/vllm-openai:latest \
    --model meta-llama/Llama-2-7b-hf \
    --dtype float16 \
    --max-model-len 1024 \
    --lora-modules \
    adapter1=/root/.cache/huggingface/hub/models--monsterapi--llama2-code-generation/snapshots/${SNAPSHOT_ID}/  \
    adapter2=/root/.cache/huggingface/hub/models--yard1-llama-2-7b-sql-lora-test/snapshots/${SNAPSHOT_ID}/ \
    --enable-lora
```

### Run GenAI-Perf[#](#run-genai-perf "Link to this heading")

Run GenAI-Perf from the Triton Inference Server SDK container:

```
export RELEASE="25.01"

docker run -it --net=host --gpus=all nvcr.io/nvidia/tritonserver:${RELEASE}-py3-sdk

# Run GenAI-Perf in the container:
genai-perf profile \
  -m adapter1 adapter2 \
  --tokenizer meta-llama/Llama-2-7b-hf \
  --endpoint-type completions \
  --model-selection-strategy round_robin
```

Example output:

```
                              NVIDIA GenAI-Perf | LLM Metrics
âââââââââââââââââââââââââââââââââââââ³âââââââââ³âââââââââ³âââââââââ³âââââââââ³âââââââââ³âââââââââ
â                         Statistic â    avg â    min â    max â    p99 â    p90 â    p75 â
â¡ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ©
â              Request latency (ms) â 442.59 â 175.95 â 652.26 â 608.05 â 463.43 â 449.82 â
â            Output sequence length â  16.84 â   2.00 â  19.00 â  19.00 â  17.00 â  17.00 â
â             Input sequence length â 550.05 â 550.00 â 553.00 â 551.40 â 550.00 â 550.00 â
â Output token throughput (per sec) â  38.04 â    N/A â    N/A â    N/A â    N/A â    N/A â
â      Request throughput (per sec) â   2.26 â    N/A â    N/A â    N/A â    N/A â    N/A â
âââââââââââââââââââââââââââââââââââââ´âââââââââ´âââââââââ´âââââââââ´âââââââââ´âââââââââ´âââââââââ
```

## Profile Mistral running on Hugging Face TGI Server [#](#profile-mistral-running-on-hugging-face-tgi-server "Link to this heading")

### Run Mistral on [Hugging Face TGI](https://huggingface.co/docs/text-generation-inference/en/conceptual/lora) server[#](#run-mistral-on-hugging-face-tgi-server "Link to this heading")

See instructions

Run the TGI server:

```
mkdir data
model=mistralai/Mistral-7B-v0.1
volume=$PWD/data

docker run \
    --gpus all \
    --shm-size 1g \
    -p 8000:80 \
    -v $volume:/data \
    --env "HUGGING_FACE_HUB_TOKEN=$HF_TOKEN" \
    ghcr.io/huggingface/text-generation-inference:2.1.1 \
    --model-id $model \
    --lora-adapters=predibase/customer_support,predibase/magicoder
```

### Run GenAI-Perf[#](#id1 "Link to this heading")

Run GenAI-Perf from the Triton Inference Server SDK container:

```
export RELEASE="25.01"

docker run -it --net=host --gpus=all nvcr.io/nvidia/tritonserver:${RELEASE}-py3-sdk

# Run GenAI-Perf in the container:
genai-perf profile \
  -m predibase/customer_support predibase/magicoder \
  --tokenizer mistralai/Mistral-7B-v0.1 \
  --endpoint-type completions \
  --model-selection-strategy round_robin
```

Example output:

```
                                   NVIDIA GenAI-Perf | LLM Metrics
âââââââââââââââââââââââââââââââââââââ³âââââââââââ³âââââââââ³âââââââââââ³âââââââââââ³âââââââââââ³âââââââââââ
â                         Statistic â      avg â    min â      max â      p99 â      p90 â      p75 â
â¡ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ©
â              Request latency (ms) â 1,655.06 â 155.95 â 1,942.88 â 1,941.54 â 1,935.78 â 1,927.85 â
â            Output sequence length â    88.43 â   6.00 â   108.00 â   107.80 â   106.00 â   103.00 â
â             Input sequence length â   550.00 â 550.00 â   550.00 â   550.00 â   550.00 â   550.00 â
â Output token throughput (per sec) â    53.43 â    N/A â      N/A â      N/A â      N/A â      N/A â
â      Request throughput (per sec) â     0.60 â    N/A â      N/A â      N/A â      N/A â      N/A â
âââââââââââââââââââââââââââââââââââââ´âââââââââââ´âââââââââ´âââââââââââ´âââââââââââ´âââââââââââ´âââââââââââ
```

## Profile Mistral running on Lorax Server [#](#profile-mistral-running-on-lorax-server "Link to this heading")

### Run Mistral on [Lorax](https://github.com/predibase/lorax) server[#](#run-mistral-on-lorax-server "Link to this heading")

See instructions

Run the TGI server:

```
mkdir data
model=mistralai/Mistral-7B-Instruct-v0.1
volume=$PWD/data

docker run \
    --gpus all \
    --shm-size 1g \
    -p 8000:80 \
    -v $volume:/data \
    --env "HUGGING_FACE_HUB_TOKEN=$HF_TOKEN" \
     ghcr.io/predibase/lorax:main \
    --model-id $model
```

### Run GenAI-Perf[#](#id2 "Link to this heading")

Run GenAI-Perf from the Triton Inference Server SDK container:

```
export RELEASE="25.01"

docker run -it --net=host --gpus=all nvcr.io/nvidia/tritonserver:${RELEASE}-py3-sdk

# Run GenAI-Perf in the container:
genai-perf profile \
  -m alignment-handbook/zephyr-7b-dpo-lora Undi95/Mistral-7B-roleplay_alpaca-lora \
  --tokenizer mistralai/Mistral-7B-Instruct-v0.1 \
  --endpoint-type completions \
  --model-selection-strategy round_robin \
  --concurrency=128
```

Example output:

```
                                      NVIDIA GenAI-Perf | LLM Metrics
âââââââââââââââââââââââââââââââââââââ³ââââââââââââ³âââââââââââ³ââââââââââââ³ââââââââââââ³ââââââââââââ³ââââââââââââ
â                         Statistic â       avg â      min â       max â       p99 â       p90 â       p75 â
â¡âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ©
â              Request latency (ms) â 20,277.80 â 1,229.48 â 33,166.99 â 33,082.30 â 32,320.14 â 31,206.61 â
â            Output sequence length â     24.86 â     4.00 â     96.00 â     91.50 â     51.00 â     19.50 â
â             Input sequence length â    550.00 â   550.00 â    550.00 â    550.00 â    550.00 â    550.00 â
â Output token throughput (per sec) â      5.25 â      N/A â       N/A â       N/A â       N/A â       N/A â
â      Request throughput (per sec) â      0.21 â      N/A â       N/A â       N/A â       N/A â       N/A â
âââââââââââââââââââââââââââââââââââââ´ââââââââââââ´âââââââââââ´ââââââââââââ´ââââââââââââ´ââââââââââââ´ââââââââââââ
```

