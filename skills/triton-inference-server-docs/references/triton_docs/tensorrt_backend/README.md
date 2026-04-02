* TensorRT Backend

[![License](https://img.shields.io/badge/License-BSD3-lightgrey.svg)](https://opensource.org/licenses/BSD-3-Clause)

# TensorRT Backend[#](#tensorrt-backend "Link to this heading")

The Triton backend for [TensorRT](https://github.com/NVIDIA/TensorRT).
You can learn more about Triton backends in the [backend
repo](https://github.com/triton-inference-server/backend). Ask
questions or report problems on the [issues
page](https://github.com/triton-inference-server/server/issues).
This backend is designed to run a serialized [TensorRT engine](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.md#build_engine_c)
models using the TensorRT C++ API.

Where can I ask general questions about Triton and Triton backends?
Be sure to read all the information below as well as the [general
Triton documentation](https://github.com/triton-inference-server/server#triton-inference-server)
available in the main [server](https://github.com/triton-inference-server/server)
repo. If you donât find your answer there you can ask questions on the
main Triton [issues page](https://github.com/triton-inference-server/server/issues).

## Command-line Options[#](#command-line-options "Link to this heading")

The command-line options configure properties of the TensorRT
backend that are then applied to all models that use the backend.

Below is an example of how to specify the backend config and the full list of
options.

### âbackend-config=tensorrt,coalesce-request-input=<boolean>,plugins=â/path/plugin1.so;/path2/plugin2.so,version-compatible=trueâ[#](#backend-config-tensorrt-coalesce-request-input-boolean-plugins-path-plugin1-so-path2-plugin2-so-version-compatible-true "Link to this heading")

* The `coalesce-request-input` flag instructs TensorRT to consider the requestsâ inputs with the same name as
  one contiguous buffer if their memory addresses align with each other.
  This option should only be enabled if all requestsâ input tensors are allocated
  from the same memory region. The default value is false.
* The `execution-policy` flag instructs TensorRT backend to execute the model with
  different Triton execution policies (see `TRITONBACKEND_ExecutionPolicy`
  for detail). Currently the following values are accepted:

  + `DEVICE_BLOCKING`: corresponds to `TRITONBACKEND_EXECUTION_DEVICE_BLOCKING`,
    this option can be set to avoid possible CUDA contention from launching
    many kernels from multiple threads.
  + `BLOCKING`: corresponds to `TRITONBACKEND_EXECUTION_BLOCKING`, this option
    can be set to overlap the host thread workload between model instances.
* The `plugins` flag provides a way to load any custom TensorRT plugins that your models rely on. If you have
  multiple plugins to load, use a semicolon as the delimiter.
* The `version-compatible` flag enables the loading of version-compatible TensorRT models where the version of
  TensorRT used for building does not matching the engine version used by Triton. You must trust the models
  loaded in this mode, as version-compatible models include a lean runtime which gets deserialized and executed
  by Triton. You can find more information in the TensorRT documentation
  [here](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.md#version-compat).
  The default value is false.

## Build the TensorRT Backend[#](#build-the-tensorrt-backend "Link to this heading")

Appropriate version of TensorRT must be installed on the system. Check the support matrix to find the correct version of TensorRT to be installed.

```
$ mkdir build
$ cd build
$ cmake -DCMAKE_INSTALL_PREFIX:PATH=`pwd`/install ..
$ make install
```

The following required Triton repositories will be pulled and used in
the build. By default the âmainâ branch/tag will be used for each repo
but the listed CMake argument can be used to override.

* triton-inference-server/backend: -DTRITON\_BACKEND\_REPO\_TAG=[tag]
* triton-inference-server/core: -DTRITON\_CORE\_REPO\_TAG=[tag]
* triton-inference-server/common: -DTRITON\_COMMON\_REPO\_TAG=[tag]

## Parameters[#](#parameters "Link to this heading")

Triton exposes some flags to control the execution mode of the TensorRT models through
the Parameters section of the modelâs `config.pbtxt` file.

### execution\_context\_allocation\_strategy[#](#execution-context-allocation-strategy "Link to this heading")

Different memory allocation behaviors for IExecutionContext. IExecutionContext requires a block of device memory for internal activation tensors during inference. The user can let the execution context manage the memory in various ways. Current options are âSTATICâ (default) and âON\_PROFILE\_CHANGEâ.

* âSTATICâ: Default static allocation with the maximum size across all profiles.
* âON\_PROFILE\_CHANGEâ: Reallocate for a profile when itâs selected.

```
parameters: {
  key: "execution_context_allocation_strategy"
  value: {
    string_value: "STATIC"
  }
}
```

