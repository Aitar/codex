# Building from Source Code on Linux — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/installation/build-from-source-linux.html

Building from Source Code on Linux#

This document provides instructions for building TensorRT LLM from source code on Linux. Building from source is recommended for achieving optimal performance, enabling debugging capabilities, or when you need a different GNU CXX11 ABI configuration than what is available in the pre-built TensorRT LLM wheel on PyPI. Note that the current pre-built TensorRT LLM wheel on PyPI is linked against PyTorch 2.9.1, which uses the new CXX11 ABI.

Prerequisites#

Use Docker to build and run TensorRT LLM. Instructions to install an environment to run Docker containers for the NVIDIA platform can be found here.

If you intend to build any TensorRT-LLM artifacts, such as any of the container images (note that there exist pre-built develop and release container images in NGC), or the TensorRT LLM Python wheel, you first need to clone the TensorRT LLM repository:

```text
# TensorRT LLM uses git-lfs, which needs to be installed in advance.
apt-get update && apt-get -y install git git-lfs
git lfs install

git clone https://github.com/NVIDIA/TensorRT-LLM.git
cd TensorRT-LLM
git submodule update --init --recursive
git lfs pull
```

Building a TensorRT LLM Docker Image#

There are two options to create a TensorRT LLM Docker image. The approximate disk space required to build the image is 63 GB.

Option 1: Build TensorRT LLM in One Step#

Tip

If you just want to run TensorRT LLM, you can instead use the pre-built TensorRT LLM Release container images.

TensorRT LLM contains a simple command to create a Docker image. Note that if you plan to develop on TensorRT LLM, we recommend using Option 2: Build TensorRT LLM Step-By-Step.

```text
make -C docker release_build
```

You can add the `CUDA_ARCHS="<listofarchitecturesinCMakeformat>"` optional argument to specify which architectures should be supported by TensorRT LLM. It restricts the supported GPU architectures but helps reduce compilation time:

```text
# Restrict the compilation to Ada and Hopper architectures.
make -C docker release_build CUDA_ARCHS="89-real;90-real"
```

After the image is built, the Docker container can be run.

```text
make -C docker release_run
```

The `make` command supports the `LOCAL_USER=1` argument to switch to the local user account instead of `root` inside the container. The examples of TensorRT LLM are installed in the `/app/tensorrt_llm/examples` directory.

Since TensorRT LLM has been built and installed, you can skip the remaining steps.

Option 2: Container for building TensorRT LLM Step-by-Step#

If you are looking for more flexibility, TensorRT LLM has commands to create and run a development container in which TensorRT LLM can be built.

Tip

As an alternative to building the container image following the instructions below,
you can pull a pre-built TensorRT LLM Develop container image from NGC (see here for information on container tags).
Follow the linked catalog entry to enter a new container based on the pre-built container image, with the TensorRT source repository mounted into it. You can then skip this section and continue straight to building TensorRT LLM.

On systems with GNU `make`

Create a Docker image for development. The image will be tagged locally with `tensorrt_llm/devel:latest`.

```text
make -C docker build
```

Run the container.

```text
make -C docker run
```

If you prefer to work with your own user account in that container, instead of `root`, add the `LOCAL_USER=1` option.

```text
make -C docker run LOCAL_USER=1
```

If you wish to use enroot instead of docker, then you can build a sqsh file that has the identical environment as the development image `tensorrt_llm/devel:latest` as follows.

Allocate a compute node:

```text
salloc --nodes=1
```

Create a sqsh file with essential TensorRT LLM dependencies installed

```text
# Using default sqsh filename (enroot/tensorrt_llm.devel.sqsh)
make -C enroot build_sqsh

# Or specify a custom path (optional)
make -C enroot build_sqsh SQSH_PATH=/path/to/dev_trtllm_image.sqsh
```

Once this squash file is ready, you can follow the steps under Build TensorRT LLM by launching an enroot sandbox from `dev_trtllm_image.sqsh`. To do this, proceed as follows:

```text
export SQSH_PATH=/path/to/dev_trtllm_image.sqsh

# Start a pseudo terminal for interactive session
make -C enroot run_sqsh

# Or, you could run commands directly
make -C enroot run_sqsh RUN_CMD="python3 scripts/build_wheel.py"
```

On systems without GNU `make`

Create a Docker image for development.

```text
docker build --pull  \
            --target devel \
            --file docker/Dockerfile.multi \
            --tag tensorrt_llm/devel:latest \
            .
```

Run the container.

```text
docker run --rm -it \
        --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 --gpus=all \
        --volume ${PWD}:/code/tensorrt_llm \
        --workdir /code/tensorrt_llm \
        tensorrt_llm/devel:latest
```

Note: please make sure to set `--ipc=host` as a docker run argument to avoid `Buserror(coredumped)`.

Once inside the container, follow the next steps to build TensorRT LLM from source.

Advanced topics#

For more information on building and running various TensorRT LLM container images,
check NVIDIA/TensorRT-LLM.

Build TensorRT LLM#

Option 1: Full Build with C++ Compilation#

The following command compiles the C++ code and packages the compiled libraries along with the Python files into a wheel. When developing C++ code, you need this full build command to apply your code changes.

```text
# To build the TensorRT LLM code.
python3 ./scripts/build_wheel.py
```

Once the wheel is built, install it by:

```text
pip install ./build/tensorrt_llm*.whl
```

Alternatively, you can use editable installation, which is convenient if you also develop Python code.

```text
pip install -e .
```

By default, `build_wheel.py` enables incremental builds. To clean the build
directory, add the `--clean` option:

```text
python3 ./scripts/build_wheel.py --clean
```

It is possible to restrict the compilation of TensorRT LLM to specific CUDA
architectures. For that purpose, the `build_wheel.py` script accepts a
semicolon separated list of CUDA architecture as shown in the following
example:

```text
# Build TensorRT LLM for Ampere.
python3 ./scripts/build_wheel.py --cuda_architectures "80-real;86-real"
```

To use the C++ benchmark scripts under benchmark/cpp, for example `gptManagerBenchmark.cpp`, add the `--benchmarks` option:

```text
python3 ./scripts/build_wheel.py --benchmarks
```

Refer to the Hardware section for a list of architectures.

Building the Python Bindings for the C++ Runtime#

The C++ Runtime can be exposed to Python via bindings. This feature can be turned on through the default build options.

```text
python3 ./scripts/build_wheel.py
```

After installing, the resulting wheel as described above, the C++ Runtime bindings will be available in
the `tensorrt_llm.bindings` package. Running `help` on this package in a Python interpreter will provide on overview of the
relevant classes. The associated unit tests should also be consulted for understanding the API.

This feature will not be enabled when `buildingonlytheC++runtime`.

Linking with the TensorRT LLM C++ Runtime#

The `build_wheel.py` script will also compile the library containing the C++ runtime of TensorRT LLM. If Python support and `torch` modules are not required, the script provides the option `--cpp_only` which restricts the build to the C++ runtime only.

```text
python3 ./scripts/build_wheel.py --cuda_architectures "80-real;86-real" --cpp_only --clean
```

This is particularly useful for avoiding linking issues that may arise with older versions of `torch` (prior to 2.7.0) due to the Dual ABI support in GCC. The `--clean` option removes the build directory before starting a new build. By default, TensorRT LLM uses `cpp/build` as the build directory, but you can specify a different location with the `--build_dir` option. For a complete list of available build options, run `python3./scripts/build_wheel.py--help`.

The shared library can be found in the following location:

```text
cpp/build/tensorrt_llm/libtensorrt_llm.so
```

In addition, link against the library containing the LLM plugins for TensorRT.

```text
cpp/build/tensorrt_llm/plugins/libnvinfer_plugin_tensorrt_llm.so
```

Supported C++ Header Files#

When using TensorRT LLM, you need to add the `cpp` and `cpp/include` directories to the project’s include paths. Only header files contained in `cpp/include` are part of the supported API and may be directly included. Other headers contained under `cpp` should not be included directly since they might change in future versions.

Option 2: Python-Only Build without C++ Compilation#

If you only need to modify Python code, it is possible to package and install TensorRT LLM without compilation.

```text
# Package TensorRT LLM wheel.
TRTLLM_USE_PRECOMPILED=1 pip wheel . --no-deps --wheel-dir ./build

# Install TensorRT LLM wheel.
pip install ./build/tensorrt_llm*.whl
```

Alternatively, you can use editable installation for convenience during Python development.

```text
TRTLLM_USE_PRECOMPILED=1 pip install -e .
```

Setting `TRTLLM_USE_PRECOMPILED=1` enables downloading a prebuilt wheel of the version specified in `tensorrt_llm/version.py`, extracting compiled libraries into your current directory, thus skipping C++ compilation. This version can be overridden by specifying `TRTLLM_USE_PRECOMPILED=x.y.z`.

You can specify a custom URL or local path for downloading using `TRTLLM_PRECOMPILED_LOCATION`. For example, to use version 0.16.0 from PyPI:

```text
TRTLLM_PRECOMPILED_LOCATION=https://pypi.nvidia.com/tensorrt-llm/tensorrt_llm-0.16.0-cp312-cp312-linux_x86_64.whl pip install -e .
```

Known Limitations#

When using `TRTLLM_PRECOMPILED_LOCATION`, ensure that your wheel is compiled based on the same version of C++ code as your current directory; any discrepancies may lead to compatibility issues.
