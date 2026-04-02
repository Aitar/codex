* Deploying...

# Deploying Hugging Face Llava1.5-7b Model in Triton[#](#deploying-hugging-face-llava1-5-7b-model-in-triton "Link to this heading")

TensorRT-LLM is Nvidiaâs recommended solution of running Large Language
Models(LLMs) on Nvidia GPUs. Read more about TensoRT-LLM [here](https://github.com/NVIDIA/TensorRT-LLM)
and Tritonâs TensorRT-LLM Backend [here](https://github.com/triton-inference-server/tensorrtllm_backend).

*NOTE:* If some parts of this tutorial doesnât work, it is possible that there
are some version mismatches between the `tutorials` and `tensorrtllm_backend`
repository. Refer to [llama.md](../../../tensorrtllm_backend/docs/llama.md)
for more detailed modifications if necessary. And if you are familiar with
python, you can also try using
[High-level API](https://github.com/NVIDIA/TensorRT-LLM/blob/main/examples/high-level-api/README.md)
for LLM workflow.

## Acquiring Llava1.5-7B model[#](#acquiring-llava1-5-7b-model "Link to this heading")

For this tutorial, we are using the Llava1.5-7B HuggingFace model with pre-trained
weights. Clone the repo of the model with weights and tokens
[here](https://huggingface.co/llava-hf/llava-1.5-7b-hf/tree/main).

## Deploying with Triton Inference Server[#](#deploying-with-triton-inference-server "Link to this heading")

Next steps will guide you over the process of TensorRT and TensorRT-LLM engine
building and Triton model repository set up.

### Prerequisite: TensorRT-LLM backend[#](#prerequisite-tensorrt-llm-backend "Link to this heading")

This tutorial requires TensorRT-LLM Backend repository. Please note,
that for best user experience we recommend using the latest
[release tag](https://github.com/triton-inference-server/tensorrtllm_backend/tags)
of `tensorrtllm_backend` and
the latest [Triton Server container.](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/tritonserver/tags)

To clone TensorRT-LLM Backend repository, make sure to run the following
set of commands.

```
git clone https://github.com/triton-inference-server/tensorrtllm_backend.git  --branch <release branch>
# Update the submodules
cd tensorrtllm_backend
# Install git-lfs if needed
apt-get update && apt-get install git-lfs -y --no-install-recommends
git lfs install
git submodule update --init --recursive
```

### Launch Triton TensorRT-LLM container[#](#launch-triton-tensorrt-llm-container "Link to this heading")

Launch Triton docker container with TensorRT-LLM backend.
Note that weâre mounting `tensorrtllm_backend` to `/tensorrtllm_backend`
and the Llava1.5 model to `/Llava-1.5-7b-hf` in the docker container for simplicity.
Make an `engines` folder outside docker to reuse engines for future runs.
Please, make sure to replace <xx.yy> with the version of Triton that you want
to use.

```
docker run --rm -it --net host --shm-size=2g \
    --ulimit memlock=-1 --ulimit stack=67108864 --gpus all \
    -v </path/to/tensorrtllm_backend>:/tensorrtllm_backend \
    -v </path/to/Llava1.5/repo>:/llava-1.5-7b-hf \
    -v </path/to/engines>:/engines \
    -v </path/to/tutorials>:/tutorials \
    nvcr.io/nvidia/tritonserver:<xx.yy>-trtllm-python-py3
```

Alternatively, you can follow instructions
[here](https://github.com/triton-inference-server/tensorrtllm_backend?tab=readme-ov-file#build-the-docker-container)
to build Triton Server with Tensorrt-LLM Backend if you want
to build a specialized container.

Donât forget to allow gpu usage when you launch the container.

### Create Engines for each model [skip this step if you already have engines][#](#create-engines-for-each-model-skip-this-step-if-you-already-have-engines "Link to this heading")

TensorRT-LLM requires each model to be compiled for the configuration
you need before running. To do so, before you run your model for the first time
on Triton Server you will need to create a TensorRT-LLM engine.

Starting with [24.04 release](https://github.com/triton-inference-server/server/releases/tag/v2.45.0),
Triton Server TensrRT-LLM container comes with
pre-installed TensorRT-LLM package, which allows users to build engines inside
the Triton container.

Llava1.5 requires 2 engines: a TensorRT engine for visual components,
and a TRT-LLM engine for the language components. This tutorial bases on 24.05
release, which corresponds to `v0.9.0` version of TensorRT-LLM and
TensorRT-LLM backend and follows [this](https://github.com/NVIDIA/TensorRT-LLM/tree/v0.9.0/examples/multimodal#llava-and-vila)
TensorRT-LLM multi-modal guide.

To generate engines, simply follow the next steps:

```
HF_LLAVA_MODEL=/llava-1.5-7b-hf
UNIFIED_CKPT_PATH=/tmp/ckpt/llava/7b/
ENGINE_DIR=/engines/llava1.5
CONVERT_CHKPT_SCRIPT=/tensorrtllm_backend/tensorrt_llm/examples/llama/convert_checkpoint.py
python3 ${CONVERT_CHKPT_SCRIPT} --model_dir ${HF_LLAVA_MODEL} --output_dir ${UNIFIED_CKPT_PATH} --dtype float16
trtllm-build --checkpoint_dir ${UNIFIED_CKPT_PATH} \
            --output_dir ${ENGINE_DIR} \
            --gemm_plugin float16 \
            --use_fused_mlp \
            --max_batch_size 1 \
            --max_input_len 2048 \
            --max_output_len 512 \
            --max_multimodal_len 576 # 1 (max_batch_size) * 576 (num_visual_features)

python /tensorrtllm_backend/tensorrt_llm/examples/multimodal/build_visual_engine.py --model_path ${HF_LLAVA_MODEL} --model_type llava --output_dir ${ENGINE_DIR}
```

> Optional: You can check test the output of the model with `run.py`
> located in the same llama examples folder.
>
> ```
>  python3 /tensorrtllm_backend/tensorrt_llm/examples/multimodal/run.py --max_new_tokens 30 --hf_model_dir ${HF_LLAVA_MODEL} --visual_engine_dir ${ENGINE_DIR} --llm_engine_dir ${ENGINE_DIR} --decoder_llm --input_text "Question: which city is this? Answer:"
> ```
>
> You should expect the following response:
>
> ```
> [TensorRT-LLM] TensorRT-LLM version: 0.9.0
> ...
> [06/18/2024-01:02:24] [TRT-LLM] [I] ---------------------------------------------------------
> [06/18/2024-01:02:24] [TRT-LLM] [I]
> [Q] Question: which city is this? Answer:
> [06/18/2024-01:02:24] [TRT-LLM] [I]
> [A] ['Singapore']
> [06/18/2024-01:02:24] [TRT-LLM] [I] Generated 1 tokens
> [06/18/2024-01:02:24] [TRT-LLM] [I] ---------------------------------------------------------
> ```

### Serving with Triton[#](#serving-with-triton "Link to this heading")

The last step is to set up a Triton model repository. For this tutorial,
we provide all necessary Triton related files under `model_repository/`.
You simply need to provide TensorRT-LLM engine location in its `config.pbtxt`:

```
FILL_TEMPLATE_SCRIPT=/tensorrtllm_backend/tools/fill_template.py
python3 ${FILL_TEMPLATE_SCRIPT} -i /tutorials/Popular_Models_Guide/Llava1.5/model_repository/tensorrt_llm/config.pbtxt engine_dir:${ENGINE_DIR}
```

3. Launch Tritonserver

Use the [launch\_triton\_server.py](https://github.com/triton-inference-server/tensorrtllm_backend/blob/release/0.5.0/scripts/launch_triton_server.py) script. This launches multiple instances of `tritonserver` with MPI.

```
export TRT_ENGINE_LOCATION="/engines/llava1.5/visual_encoder.engine"
export HF_LOCATION="/llava-1.5-7b-hf"
python3 /tensorrtllm_backend/scripts/launch_triton_server.py --world_size=<world size of the engine> --model_repo=/tutorials/Popular_Models_Guide/Llava1.5/model_repository
```

> You should expect the following response:
>
> ```
> ...
> I0503 22:01:25.210518 1175 grpc_server.cc:2463] Started GRPCInferenceService at 0.0.0.0:8001
> I0503 22:01:25.211612 1175 http_server.cc:4692] Started HTTPService at 0.0.0.0:8000
> I0503 22:01:25.254914 1175 http_server.cc:362] Started Metrics Service at 0.0.0.0:8002
> ```

To stop Triton Server inside the container, run:

```
pkill tritonserver
```

### Send an inference request[#](#send-an-inference-request "Link to this heading")

You can test the results of the run with:

1. The [multi\_modal\_client.py](https://github.com/triton-inference-server/tutorials/blob/main/Popular_Models_Guide/Llava1.5/tutorials/Popular_Models_Guide/Llava1.5/multi_modal_client.py) script.

```
# Using the SDK container as an example
docker run --rm -it --net host --shm-size=2g \
    --ulimit memlock=-1 --ulimit stack=67108864 --gpus all \
    -v /path/to/tutorials:/tutorials
    nvcr.io/nvidia/tritonserver:<xx.yy>-py3-sdk

CLIENT_SCRIPT=/tutorials/Popular_Models_Guide/Llava1.5/multi_modal_client.py
python3 ${CLIENT_SCRIPT} --prompt "Describe the picture." --image_url "http://images.cocodataset.org/test2017/000000155781.jpg" --max-tokens=15
```

> You should expect the following response:
>
> ```
> Got completed request
> The image features a city bus parked on the side of a street.
> ```

2. The [generate endpoint](https://github.com/triton-inference-server/tensorrtllm_backend/tree/release/0.5.0#query-the-server-with-the-triton-generate-endpoint).

```
curl -X POST localhost:8000/v2/models/llava-1.5/generate -d '{"prompt":"USER: <image>\nQuestion:Describe the picture. Answer:", "image":"http://images.cocodataset.org/test2017/000000155781.jpg", "max_tokens":100}'
```

> You should expect the following response:
>
> ```
> data: {"completion_tokens":77,"finish_reason":"stop","model_name":"llava-1.5","model_version":"1","prompt_tokens":592,"text":"The image features a city bus parked on the side of a street. The bus is positioned near a railroad crossing, and there is a stop sign visible in the scene. The bus is also displaying an \"Out of Service\" sign, indicating that it is not currently in operation. The street appears to be foggy, adding a sense of atmosphere to the scene.</s>","total_tokens":669}
> ```

## References[#](#references "Link to this heading")

For more examples feel free to refer to [End to end workflow to run multi-modal models.](https://github.com/NVIDIA/TensorRT-LLM/blob/main/examples/multimodal/README.md)

