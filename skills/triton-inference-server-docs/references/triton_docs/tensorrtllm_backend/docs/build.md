* Building from Source

# Building from Source[#](#building-from-source "Link to this heading")

This document describes how to build the TensorRT-LLM backend and the Triton
TRT-LLM container from source. The Triton container includes TensorRT-LLM,
along with the TensorRT-LLM backend and the Python backend.

## Build the TensorRT-LLM Backend from source[#](#build-the-tensorrt-llm-backend-from-source "Link to this heading")

Make sure TensorRT-LLM is installed before building the backend. Since the
version of TensorRT-LLM and the TensorRT-LLM backend has to be aligned, it is
recommended to directly use the Triton TRT-LLM container from NGC or build the
whole container from source as described below in the Build the Docker Container
section.

```
cd tensorrt_llm/triton_backend/inflight_batcher_llm
bash scripts/build.sh
```

## Build the Docker Container[#](#build-the-docker-container "Link to this heading")

> [!CAUTION]
> [build.sh](https://github.com/triton-inference-server/tensorrtllm_backend/blob/main/build.sh) is currently not working and will be fixed in the next weekly update.

### Build via Docker[#](#build-via-docker "Link to this heading")

You can build the container using the instructions in the [TensorRT-LLM Docker Build](https://github.com/triton-inference-server/tensorrtllm_backend/blob/main/tensorrt_llm/docker/README.md)
with `tritonrelease` stage. Please make sure to add CUDA\_ARCHS flag for your GPU, for example if compute capability of your GPU is 89:

```
cd tensorrt_llm/
make -C docker tritonrelease_build CUDA_ARCHS='89-real'
```

