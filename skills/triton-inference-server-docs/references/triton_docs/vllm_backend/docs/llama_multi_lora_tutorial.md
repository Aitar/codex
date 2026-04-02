* [vLLM](../../backend_guide/vllm.md)
* Tutorial on...

# Tutorial on depolying multi-lora vLLM backend in Triton[#](#tutorial-on-depolying-multi-lora-vllm-backend-in-triton "Link to this heading")

The idea of multi-lora was proposed recently, for more please refer to:

* [S-LoRA: Serving Thousands of Concurrent LoRA Adapters](https://arxiv.org/abs/2311.03285)
* [Punica: Multi-Tenant LoRA Serving](https://arxiv.org/abs/2310.18547)

Now the vLLM has supported multi-lora, which integrated the `Punica` feature and related cuda kernels. See this [PR](https://github.com/vllm-project/vllm/pull/1804) for more. (2024-01-24 this PR has been merged into the main branch of vLLM)

The following tutorial demonstrates how to deploy **a LLaMa model** with **multiple loras** on Triton Inference Server using the Tritonâs [Python-based](../../backend/docs/python_based_backends.md#python-based-backends) [vLLM](https://github.com/triton-inference-server/vllm_backend/tree/main) backend.

> Before you continue reading, itâs important to note that all command-line instructions containing `<xx.yy>` in the document cannot be used directly by copying and pasting.
>
> `<xx.yy>` represents the Triton version, and you must specify the Triton version you want to use for the bash command to work.

## Step 1: Start a docker container for triton-vllm serving[#](#step-1-start-a-docker-container-for-triton-vllm-serving "Link to this heading")

**A docker container is strongly recommended for serving**, and this tutorial will only demonstrate how to launch triton in the docker environment.

First, start a docker container using the tritonserver image with vLLM backend from [NGC](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/tritonserver/tags):

```
# NOTICE: you must first cd to your vllm_workspace path outside the container.
mkdir vllm_workspace && cd vllm_workspace

sudo docker run --gpus all -it --net=host -p 8001:8001 --shm-size=12G \
--ulimit memlock=-1 --ulimit stack=67108864 -v ${PWD}:/vllm_workspace \
-w /vllm_workspace nvcr.io/nvidia/tritonserver:<xx.yy>-vllm-python-py3 \
/bin/bash
```

**NOTICE:** the version of triton docker image should be configurated, here and through this tutorial we use `<xx.yy>` to symbolize the version.

Tritonâs vLLM container has been introduced starting from 23.10 release, and `multi-lora` experimental support was added in vLLM v0.3.0 release.

> Docker image version `nvcr.io/nvidia/tritonserver:24.05-vllm-python-py3` or higher version is strongly recommended.

---

For **pre-24.05 containers**, the docker images didnât support multi-lora feature, so you need to replace that provided in the container `/opt/tritonserver/backends/vllm/model.py` with the most up to date version. Just follow this command:

Download the `model.py` script from github:

```
wget -P /opt/tritonserver/backends/vllm/ https://raw.githubusercontent.com/triton-inference-server/vllm_backend/r<xx.yy>/src/model.py
```

This command will download the `model.py` script to the Triton vllm backend directory which will enable multi-lora feature.

## Step 2: Prepare your weights[#](#step-2-prepare-your-weights "Link to this heading")

To support multi-lora on Triton, you need to manage your file path for **model backbone** and **lora weights** separately.

A typical weights repository can be as follows:

```
weights
âââ backbone
â   âââ llama-7b-hf
âââ loras
    âââ alpaca-lora-7b
    âââ wizardLM-lora-7b
```

* A workspace for `vllm`, and `model backbone weights`, `LoRA adapter weights` is strongly recommended.
* You should expand the storage of these weight files to ensure they are logically organized in the workspace.

## Step 3: Prepare `model repository` for Triton Server[#](#step-3-prepare-model-repository-for-triton-server "Link to this heading")

**3.1 Download the model repository files**

To use Triton, a model repository is needed, for *model path* , *backend configuration* and other information. The vllm backend is implemented based on python backend, and `sampling_params` of vllm are sampled from `model.json`.

To create a triton model repository, you may download the files through these commands:

```
# NOTICE: you must first cd to your vllm_workspace path.
cd /vllm_workspace

mkdir -p model_repository/vllm_model/1
wget -P model_repository/vllm_model/1 https://raw.githubusercontent.com/triton-inference-server/vllm_backend/r<xx.yy>/samples/model_repository/vllm_model/1/model.json
wget -P model_repository/vllm_model/ https://raw.githubusercontent.com/triton-inference-server/vllm_backend/r<xx.yy>/samples/model_repository/vllm_model/config.pbtxt
```

The model repository should look like this:

```
model_repository/
âââ vllm_model
    âââ 1
    â   âââ model.json
    âââ config.pbtxt
```

---

Now, you have finished the basic deployment, and the file structure should look like this:

```
vllm_workspace
âââ weights
â   âââ backbone
â   â   âââ llama-7b-hf
â   âââ loras
â       âââ alpaca-lora-7b
â       âââ bactrian-x-llama-lora-7b
â
âââ model_repository
    âââ vllm_model
        âââ 1
        â   âââ model.json
        âââ config.pbtxt
```

**3.2 Populate `model.json`**

For this tutorial we will use the following set of parameters, specified in the `model.json`.

```
{
    "model":"/vllm_workspace/weights/backbone/llama-7b-hf",
    "gpu_memory_utilization": 0.8,
    "tensor_parallel_size": 2,
    "block_size": 16,
    "enforce_eager": "true",
    "enable_lora": "true",
    "max_lora_rank": 16
}
```

* `model`: The path to your model repository
* `gpu_memory_utilization`: The gpu memory allocated for the model weights and vllm *PagedAttention* kv cache manager.
* `tensor_parallel_size`: The vllm now support the tensor paralism, so you can decide how many gpus you want to use for serving.
* `block_size`: vLLM kv cache block size.
* `enable_lora`: If you want to support vllm multi-lora, this should be configured and set `true`.
* `max_lora_rank`: The maximum of LoRA rank of your lora adapter.

The full set of parameters can be found [here](https://github.com/Yard1/vllm/blob/multi_lora/vllm/engine/arg_utils.py#L11).

**3.3 Specify local lora path**

vLLM v0.4.0.post1 supported the inference of **local lora weights applying**, which means that the vllm cannot pull any lora adapter from huggingface. So triton should know where the local lora weights are.

Create a `multi_lora.json` file under `model_repository/vllm_model/1/` path:

```
cd model_repository/vllm_model/1
touch multi_lora.json
```

The content of `multi_lora.json` should look like this:

```
{
    "alpaca": "/vllm_workspace/weights/loras/alpaca-lora-7b",
    "bactrian": "/vllm_workspace/weights/loras/bactrian-x-llama-7b-lora"
}
```

The **key** should be the supported lora name, and the **value** should be the specific path in your machine.

> **Warning**: if you set `enable_lora` to `true` in `model.json` without creating a `multi_lora.json` file, the server will throw `FileNotFoundError` when initializing.

## Step 4: Launch Triton[#](#step-4-launch-triton "Link to this heading")

```
# NOTICE: you must first cd to your vllm_workspace path.
cd /vllm_workspace
tritonserver --model-store ./model_repository
```

After you start Triton you will see output on the console showing the server starting up and loading the model. When you see output like the following, Triton is ready to accept inference requests.

```
I1030 22:33:28.291908 1 grpc_server.cc:2513] Started GRPCInferenceService at 0.0.0.0:8001
I1030 22:33:28.292879 1 http_server.cc:4497] Started HTTPService at 0.0.0.0:8000
I1030 22:33:28.335154 1 http_server.cc:270] Started Metrics Service at 0.0.0.0:8002
```

## Step 5: Send a request[#](#step-5-send-a-request "Link to this heading")

A client request script for multi-lora was prepared, downloading the client script from source:

```
wget https://raw.githubusercontent.com/triton-inference-server/vllm_backend/main/samples/client.py
wget https://raw.githubusercontent.com/triton-inference-server/vllm_backend/main/samples/prompts.txt
```

Try running this script by the following command:

```
python3 client.py -l <your-prepared-lora-name>
```

Here we assume you have prepared alpaca lora weight, thus we use:

```
python3 client.py -l alpaca
```

