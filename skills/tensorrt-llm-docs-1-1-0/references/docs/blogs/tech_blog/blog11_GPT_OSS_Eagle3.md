Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/blogs/tech_blog/blog11_GPT_OSS_Eagle3.md

* Running GPT-OSS-120B with Eagle3 Speculative Decoding on GB200/B200 (TensorRT LLM)

# Running GPT-OSS-120B with Eagle3 Speculative Decoding on GB200/B200 (TensorRT LLM)[#](#running-gpt-oss-120b-with-eagle3-speculative-decoding-on-gb200-b200-tensorrt-llm "Link to this heading")

This guide sets up a production endpoint that uses Eagle3 speculative decoding on NVIDIA GB200 or B200 GPUs only. It replaces the low‑latency flow from the previous guide and intentionally omits max‑throughput, Hopper, and benchmarking content.

## Prerequisites[#](#prerequisites "Link to this heading")

* NVIDIA GB200 or B200 GPUs (example below assumes 8 GPUs; adjust flags for your setup)
* Fast SSD storage for model weights
* Base model weights available under a directory named `gpt-oss-120b` (example path)
* Eagle3 speculative model assets available under a directory named `eagle`

Expected directory layout on the host (example):

```
/path/to/models/
  ├─ gpt-oss-120b/  # base model directory
  └─ eagle/         # Eagle3 speculative decoding assets
```

## Get the TensorRT LLM Container (1.1.0rc0)[#](#get-the-tensorrt-llm-container-1-1-0rc0 "Link to this heading")

If required by your environment, log into NGC and pull the image:

```
# Create an API key at https://ngc.nvidia.com (if you don't have one)
docker login nvcr.io
# Username: $oauthtoken
# Password: <your NGC API key>

docker pull nvcr.io/nvidia/tensorrt-llm/release:1.1.0rc0
```

## Start the TensorRT LLM Container[#](#start-the-tensorrt-llm-container "Link to this heading")

Run the container and bind-mount your models directory to `/config/models` inside the container:

```
docker run --rm --ipc=host -it \
  --ulimit stack=67108864 \
  --ulimit memlock=-1 \
  --gpus all \
  -p 8000:8000 \
  -v /path/to/models:/config/models:rw \
  nvcr.io/nvidia/tensorrt-llm/release:1.1.0rc0 \
  /bin/bash
```

Replace `/path/to/models` with the absolute path on your host.

## Download the models (Base + Eagle3)[#](#download-the-models-base-eagle3 "Link to this heading")

Inside the container, download the base model and the Eagle3 speculative model to the expected directories under `/config/models/`:

```
# Optional: authenticate if the repository requires it
# export HF_TOKEN=hf_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# huggingface-cli login --token "$HF_TOKEN" --add-to-git-credential

pip install -q "huggingface_hub[cli]"

# Base model: openai/gpt-oss-120b
huggingface-cli download openai/gpt-oss-120b \
  --local-dir /config/models/gpt-oss-120b \
  --repo-type model

# Eagle3 model assets
mkdir -p /config/models/eagle
huggingface-cli download nvidia/gpt-oss-120b-Eagle3 \
  --local-dir /config/models/eagle \
  --repo-type model
```

References: `https://huggingface.co/openai/gpt-oss-120b` and `https://huggingface.co/nvidia/gpt-oss-120b-Eagle3`

## Create the Eagle3 Configuration[#](#create-the-eagle3-configuration "Link to this heading")

Inside the container, create the YAML file at `/config/models/eagle/eagle.yaml` with the following content:

```
mkdir -p /config/models/eagle
cat > /config/models/eagle/eagle.yaml << 'EOF'
trust_remote_code: true
kv_cache_config:
  enable_block_reuse: false
  free_gpu_memory_fraction: 0.8
speculative_config:
  decoding_type: Eagle
  max_draft_len: 3
  speculative_model_dir: /config/models/eagle/
cuda_graph_config:
  max_batch_size: 10
use_torch_sampler: true
moe_config:
  backend: TRTLLM
EOF
```

Notes:

* Ensure your base model directory is `/config/models/gpt-oss-120b`.
* Ensure your Eagle3 assets are present under `/config/models/eagle/`.
* If you are running on Top of Tree, replace `use_torch_sampler: true` with `sampler_type: TorchSampler`.

## Launch the Server (Eagle3 Speculative Decoding)[#](#launch-the-server-eagle3-speculative-decoding "Link to this heading")

Run the following command inside the container to start the endpoint:

```
TRTLLM_ENABLE_PDL=1 trtllm-serve /config/models/gpt-oss-120b --host 0.0.0.0 --port 8000 --max_batch_size 10  --tp_size 8 --ep_size 4 --trust_remote_code --extra_llm_api_options /config/models/eagle/eagle.yaml --max_num_tokens 131072 --max_seq_len 131072
```

The server initializes, loads, and optimizes the models. After it is ready, it listens on port 8000.

## Quick Health Check[#](#quick-health-check "Link to this heading")

From another terminal on the host, verify that the server is healthy:

```
curl -s -o /dev/null -w "Status: %{http_code}\n" "http://localhost:8000/health"
```

When `Status: 200` is returned, the endpoint is ready to serve requests.

## Sample Chat Completions Request[#](#sample-chat-completions-request "Link to this heading")

Note: This Eagle3 + TensorRT LLM endpoint currently supports only greedy sampling. The following Chat Completions parameters are ignored (no-ops): `temperature`, `top_p`, `top_k`, and `seed`.

Send a simple OpenAI-compatible Chat Completions request to the running server:

```
curl -X POST "http://localhost:8000/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-oss-120b",
    "messages": [
      {"role": "user", "content": "Give me a two-sentence summary of Eagle3 speculative decoding."}
    ],
    "max_tokens": 128,
    "stream": false
  }'
```

[previous

ADP Balance Strategy](blog10_ADP_Balance_Strategy.md "previous page")
[next

Combining Guided Decoding and Speculative Decoding: Making CPU and GPU Cooperate Seamlessly](blog12_Combining_Guided_Decoding_and_Speculative_Decoding.md "next page")

On this page

* [Prerequisites](#prerequisites)
* [Get the TensorRT LLM Container (1.1.0rc0)](#get-the-tensorrt-llm-container-1-1-0rc0)
* [Start the TensorRT LLM Container](#start-the-tensorrt-llm-container)
* [Download the models (Base + Eagle3)](#download-the-models-base-eagle3)
* [Create the Eagle3 Configuration](#create-the-eagle3-configuration)
* [Launch the Server (Eagle3 Speculative Decoding)](#launch-the-server-eagle3-speculative-decoding)
* [Quick Health Check](#quick-health-check)
* [Sample Chat Completions Request](#sample-chat-completions-request)