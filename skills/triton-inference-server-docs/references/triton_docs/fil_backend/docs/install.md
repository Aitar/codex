* Installation

# Installation[#](#installation "Link to this heading")

The FIL backend is a part of Triton and can be installed via the methods
described in the [main Triton
documentation](https://github.com/triton-inference-server/server#build-and-deploy).
To quickly get up and running with a Triton Docker image, follow these
steps.

**Note**: Looking for instructions to *build* the FIL backend yourself? Check out our [build
guide](build.md).

## Prerequisites[#](#prerequisites "Link to this heading")

* [Docker](https://docs.docker.com/get-docker/)
* [The NVIDIA container toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.md#docker)

## Getting the container[#](#getting-the-container "Link to this heading")

Triton containers are available from NGC and may be pulled down via

```
docker pull nvcr.io/nvidia/tritonserver:25.08-py3
```

Note that the FIL backend cannot be used in the `21.06` version of this
container; the `21.06.1` patch release is the earliest Triton version with a
working FIL backend implementation.

## Starting the container[#](#starting-the-container "Link to this heading")

In order to actually deploy a model, you will need to provide the serialized
model and configuration file in a specially-structured directory called the
âmodel repository.â Check out the
[configuration guide](https://github.com/triton-inference-server/fil_backend/blob/main/docs/docs/model_config.md) for details on how to do this for your model.

Assuming your model repository is on the host system, you can
bind-mount it into the container and start the server via the following
command:

```
docker run --gpus all -p 8000:8000 -p 8001:8001 -p 8002:8002 -v ${MODEL_REPO}:/models --name tritonserver nvcr.io/nvidia/tritonserver:22.11-py3 tritonserver --model-repository=/models
```

Remember that bind-mounts **require an absolute path** to the host
directory, so `${MODEL_REPO}` should be replaced by the absolute path to the
model repository directory on the host.

Assuming you started your container with the name âtritonserverâ as in the
above snippet, you can bring the server down again and remove the
container with:

```
docker rm -f tritonserver
```

