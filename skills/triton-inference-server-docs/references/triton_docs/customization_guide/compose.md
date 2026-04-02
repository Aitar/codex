* Customize...

# Customize Triton Container[#](#customize-triton-container "Link to this heading")

Two Docker images are available from [NVIDIA GPU Cloud
(NGC)](https://ngc.nvidia.com) that make it possible to easily
construct customized versions of Triton. By customizing Triton you can
significantly reduce the size of the Triton image by removing
functionality that you donât require.

Currently the customization is limited as described below but future
releases will increase the amount of customization that is available.
It is also possible to [build Triton](build.md#building-triton)
from source to get more exact customization.

## Use the compose.py script[#](#use-the-compose-py-script "Link to this heading")

The `compose.py` script can be found in the
[server repository](https://github.com/triton-inference-server/server).
Simply clone the repository and run `compose.py` to create a custom container.
Note: Created container version will depend on the branch that was cloned.
For example branch
[r24.12](https://github.com/triton-inference-server/server/tree/r24.12)
should be used to create a image based on the NGC 24.12 Triton release.

`compose.py` provides `--backend`, `--repoagent` options that allow you to
specify which backends and repository agents to include in the custom image.
For example, the following creates a new docker image that
contains only the Pytorch backends and the checksum repository agent.

Example:

```
python3 compose.py --backend pytorch --repoagent checksum
```

will provide a container `tritonserver` locally. You can access the container
with

```
$ docker run -it tritonserver:latest
```

Note: If `compose.py` is run on release versions `r21.08` and earlier,
the resulting container will have DCGM version 2.2.3 installed.
This may result in different GPU statistic reporting behavior.

### Compose a specific version of Triton[#](#compose-a-specific-version-of-triton "Link to this heading")

`compose.py` requires two containers: a `min` container which is the
base the compose container is built from and a `full` container from which the
script will extract components. The version of the `min` and `full` container
is determined by the branch of Triton `compose.py` is on.
For example, running

```
python3 compose.py --backend pytorch --repoagent checksum
```

on branch [r24.12](https://github.com/triton-inference-server/server/tree/r24.12) pulls:

* `min` container `nvcr.io/nvidia/tritonserver:24.12-py3-min`
* `full` container `nvcr.io/nvidia/tritonserver:24.12-py3`

Alternatively, users can specify the version of Triton container to pull from
any branch by either:

1. Adding flag `--container-version <container version>` to branch

```
python3 compose.py --backend pytorch --repoagent checksum --container-version 24.12
```

2. Specifying `--image min,<min container image name> --image full,<full container image name>`.
   The user is responsible for specifying compatible `min` and `full` containers.

```
python3 compose.py --backend pytorch --repoagent checksum --image min,nvcr.io/nvidia/tritonserver:24.12-py3-min --image full,nvcr.io/nvidia/tritonserver:24.12-py3
```

Method 1 and 2 will result in the same composed container. Furthermore,
`--image` flag overrides the `--container-version` flag when both are specified.

Note:

1. All contents in `/opt/tritonserver` repository of the `min` image will be
   removed to ensure dependencies of the composed image are added properly.
2. vLLM and TensorRT-LLM backends are currently not supported backends for
   `compose.py`. If you want to build additional backends on top of these backends,
   it would be better to [build it yourself](#build-it-yourself) by using
   `nvcr.io/nvidia/tritonserver:24.12-vllm-python-py3` or
   `nvcr.io/nvidia/tritonserver:24.12-trtllm-python-py3` as a `min` container.

### CPU-only container composition[#](#cpu-only-container-composition "Link to this heading")

CPU-only containers are not yet available for customization. Please see
[build documentation](build.md) for instructions to build a full CPU-only
container. When including PyTorch backend in the composed
container, an additional `gpu-min` container is needed
since this container provided the CUDA stubs and runtime dependencies which are
not provided in the CPU only min container.

## Build it yourself[#](#build-it-yourself "Link to this heading")

If you would like to do what `compose.py` is doing under the hood yourself, you
can run `compose.py` with the `--dry-run` option and then modify the
`Dockerfile.compose` file to satisfy your needs.

### Triton with Unsupported and Custom Backends[#](#triton-with-unsupported-and-custom-backends "Link to this heading")

You can [create and build your own Triton
backend](https://github.com/triton-inference-server/backend). The
result of that build should be a directory containing your backend
shared library and any additional files required by the
backend. Assuming your backend is called âmybackendâ and that the
directory is â./mybackendâ, adding the following to the Dockerfile `compose.py`
created will create a Triton image that contains all the supported Triton
backends plus your custom backend.

```
COPY ./mybackend /opt/tritonserver/backends/mybackend
```

You also need to install any additional dependencies required by your
backend as part of the Dockerfile. Then use Docker to create the
image.

```
$ docker build -t tritonserver_custom -f Dockerfile.compose .
```

