* ONNX Runtime Backend

[![License](https://img.shields.io/badge/License-BSD3-lightgrey.svg)](https://opensource.org/licenses/BSD-3-Clause)

# ONNX Runtime Backend[#](#onnx-runtime-backend "Link to this heading")

The Triton backend for the [ONNX
Runtime](https://github.com/microsoft/onnxruntime). You can learn more
about Triton backends in the [backend
repo](https://github.com/triton-inference-server/backend). Ask
questions or report problems on the [issues
page](https://github.com/triton-inference-server/onnxruntime_backend/issues).

Use a recent cmake to build and install in a local directory.
Typically you will want to build an appropriate ONNX Runtime
implementation as part of the build. You do this by specifying a ONNX
Runtime version and a Triton container version that you want to use
with the backend. You can find the combination of versions used in a
particular Triton release in the TRITON\_VERSION\_MAP at the top of
build.py in the branch matching the Triton release you are interested
in. For example, to build the ONNX Runtime backend for Triton 23.04,
use the versions from TRITON\_VERSION\_MAP in the [r23.04 branch of
build.py](https://github.com/triton-inference-server/server/blob/r23.04/build.py#L73).

```
$ mkdir build
$ cd build
$ cmake -DCMAKE_INSTALL_PREFIX:PATH=`pwd`/install -DTRITON_BUILD_ONNXRUNTIME_VERSION=1.14.1 -DTRITON_BUILD_CONTAINER_VERSION=23.04 ..
$ make install
```

The resulting install/backends/onnxruntime directory can be added to a
Triton installation as /opt/tritonserver/backends/onnxruntime.

The following required Triton repositories will be pulled and used in
the build. By default the âmainâ branch/tag will be used for each repo
but the listed CMake argument can be used to override.

* triton-inference-server/backend: -DTRITON\_BACKEND\_REPO\_TAG=[tag]
* triton-inference-server/core: -DTRITON\_CORE\_REPO\_TAG=[tag]
* triton-inference-server/common: -DTRITON\_COMMON\_REPO\_TAG=[tag]

You can add TensorRT support to the ONNX Runtime backend by using
-DTRITON\_ENABLE\_ONNXRUNTIME\_TENSORRT=ON. You can add OpenVino support
by using -DTRITON\_ENABLE\_ONNXRUNTIME\_OPENVINO=ON
-DTRITON\_BUILD\_ONNXRUNTIME\_OPENVINO\_VERSION=<version>, where
<version> is the OpenVino version to use and should match the
TRITON\_VERSION\_MAP entry as described above. So, to build with both
TensorRT and OpenVino support:

```
$ mkdir build
$ cd build
$ cmake -DCMAKE_INSTALL_PREFIX:PATH=`pwd`/install -DTRITON_BUILD_ONNXRUNTIME_VERSION=1.14.1 -DTRITON_BUILD_CONTAINER_VERSION=23.04 -DTRITON_ENABLE_ONNXRUNTIME_TENSORRT=ON -DTRITON_ENABLE_ONNXRUNTIME_OPENVINO=ON -DTRITON_BUILD_ONNXRUNTIME_OPENVINO_VERSION=2021.2.200 ..
$ make install
```

## ONNX Runtime with TensorRT optimization[#](#onnx-runtime-with-tensorrt-optimization "Link to this heading")

TensorRT can be used in conjunction with an ONNX model to further optimize the
performance. To enable TensorRT optimization you must set the model configuration
appropriately. There are several optimizations available for TensorRT, like
selection of the compute precision and workspace size. The optimization
parameters and their description are as follows.

* `precision_mode`: The precision used for optimization. Allowed values are âFP32â, âFP16â and âINT8â. Default value is âFP32â.
* `max_workspace_size_bytes`: The maximum GPU memory the model can use temporarily during execution. Default value is 1GB.
* `int8_calibration_table_name`: Specify INT8 calibration table name. Applicable when precision\_mode==âINT8â and the models do not contain Q/DQ nodes. If calibration table is provided for model with Q/DQ nodes then ORT session creation will fail.
* `int8_use_native_calibration_table`: Calibration table to use. Allowed values are 1 (use native TensorRT generated calibration table) and 0 (use ORT generated calibration table). Default is 0. \*\*Note: Latest calibration table file needs to be copied to trt\_engine\_cache\_path before inference. Calibration table is specific to models and calibration data sets. Whenever new calibration table is generated, old file in the path should be cleaned up or be replaced.
* `trt_engine_cache_enable`: Enable engine caching.
* `trt_engine_cache_path`: Specify engine cache path.

To explore the usage of more parameters, follow the mapping table below and
check [ONNX Runtime doc](https://onnxruntime.ai/docs/execution-providers/TensorRT-ExecutionProvider.md#execution-provider-options) for detail.

> Please link to the latest ONNX Runtime binaries in CMake or build from
> [main branch of ONNX Runtime](https://github.com/microsoft/onnxruntime/tree/main) to enable latest options.

### Parameter mapping between ONNX Runtime and Triton ONNXRuntime Backend[#](#parameter-mapping-between-onnx-runtime-and-triton-onnxruntime-backend "Link to this heading")

| Key in Triton model configuration | Value in Triton model config | Corresponding TensorRT EP option in ONNX Runtime | Type |
| --- | --- | --- | --- |
| max\_workspace\_size\_bytes | e.g: â4294967296â | trt\_max\_workspace\_size | int |
| trt\_max\_partition\_iterations | e.g: â1000â | trt\_max\_partition\_iterations | int |
| trt\_min\_subgraph\_size | e.g: â1â | trt\_min\_subgraph\_size | int |
| precision\_mode | âFP16â | trt\_fp16\_enable | bool |
| precision\_mode | âINT8â | trt\_int8\_enable | bool |
| int8\_calibration\_table\_name |  | trt\_int8\_calibration\_table\_name | string |
| int8\_use\_native\_calibration\_table | e.g: â1â or âtrueâ, â0â or âfalseâ | trt\_int8\_use\_native\_calibration\_table | bool |
| trt\_dla\_enable |  | trt\_dla\_enable | bool |
| trt\_dla\_core | e.g: â0â | trt\_dla\_core | int |
| trt\_engine\_cache\_enable | e.g: â1â or âtrueâ, â0â or âfalseâ | trt\_engine\_cache\_enable | bool |
| trt\_engine\_cache\_path |  | trt\_engine\_cache\_path | string |
| trt\_engine\_cache\_prefix |  | trt\_engine\_cache\_prefix | string |
| trt\_dump\_subgraphs | e.g: â1â or âtrueâ, â0â or âfalseâ | trt\_dump\_subgraphs | bool |
| trt\_force\_sequential\_engine\_build | e.g: â1â or âtrueâ, â0â or âfalseâ | trt\_force\_sequential\_engine\_build | bool |
| trt\_context\_memory\_sharing\_enable | e.g: â1â or âtrueâ, â0â or âfalseâ | trt\_context\_memory\_sharing\_enable | bool |
| trt\_layer\_norm\_fp32\_fallback | e.g: â1â or âtrueâ, â0â or âfalseâ | trt\_layer\_norm\_fp32\_fallback | bool |
| trt\_timing\_cache\_enable | e.g: â1â or âtrueâ, â0â or âfalseâ | trt\_timing\_cache\_enable | bool |
| trt\_timing\_cache\_path |  | trt\_timing\_cache\_path | string |
| trt\_force\_timing\_cache | e.g: â1â or âtrueâ, â0â or âfalseâ | trt\_force\_timing\_cache | bool |
| trt\_detailed\_build\_log | e.g: â1â or âtrueâ, â0â or âfalseâ | trt\_detailed\_build\_log | bool |
| trt\_build\_heuristics\_enable | e.g: â1â or âtrueâ, â0â or âfalseâ | trt\_build\_heuristics\_enable | bool |
| trt\_sparsity\_enable | e.g: â1â or âtrueâ, â0â or âfalseâ | trt\_sparsity\_enable | bool |
| trt\_builder\_optimization\_level | e.g: â3â | trt\_builder\_optimization\_level | int |
| trt\_auxiliary\_streams | e.g: â-1â | trt\_auxiliary\_streams | int |
| trt\_tactic\_sources | e.g: â-CUDNN,+CUBLASâ; | trt\_tactic\_sources | string |
| trt\_extra\_plugin\_lib\_paths |  | trt\_extra\_plugin\_lib\_paths | string |
| trt\_profile\_min\_shapes | e.g: âinput1:dim1xdimd2â¦,input2:dim1xdim2â¦,â¦â | trt\_profile\_min\_shapes | string |
| trt\_profile\_max\_shapes | e.g: âinput1:dim1xdimd2â¦,input2:dim1xdim2â¦,â¦â | trt\_profile\_max\_shapes | string |
| trt\_profile\_opt\_shapes | e.g: âinput1:dim1xdimd2â¦,input2:dim1xdim2â¦,â¦â | trt\_profile\_opt\_shapes | string |
| trt\_cuda\_graph\_enable | e.g: â1â or âtrueâ, â0â or âfalseâ | trt\_cuda\_graph\_enable | bool |
| trt\_dump\_ep\_context\_model | e.g: â1â or âtrueâ, â0â or âfalseâ | trt\_dump\_ep\_context\_model | bool |
| trt\_ep\_context\_file\_path |  | trt\_ep\_context\_file\_path | string |
| trt\_ep\_context\_embed\_mode | e.g: â1â | trt\_ep\_context\_embed\_mode | int |

The section of model config file specifying these parameters will look like:

```
.
.
.
optimization { execution_accelerators {
  gpu_execution_accelerator : [ {
    name : "tensorrt"
    parameters { key: "precision_mode" value: "FP16" }
    parameters { key: "max_workspace_size_bytes" value: "1073741824" }}
    parameters { key: "trt_engine_cache_enable" value: "1" }}
  ]
}}
.
.
.
```

## ONNX Runtime with CUDA Execution Provider optimization[#](#onnx-runtime-with-cuda-execution-provider-optimization "Link to this heading")

When GPU is enabled for ORT, CUDA execution provider is enabled. If TensorRT is
also enabled then CUDA EP is treated as a fallback option (only comes into
picture for nodes which TensorRT cannot execute). If TensorRT is not enabled
then CUDA EP is the primary EP which executes the models. ORT enabled
configuring options for CUDA EP to further optimize based on the specific model
and user scenarios. There are several optimizations available, please refer to
the [ONNX Runtime doc](https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.md#cuda-execution-provider)
for more details. To enable CUDA EP optimization you must set the model
configuration appropriately:

```
optimization { execution_accelerators {
  gpu_execution_accelerator : [ {
    name : "cuda"
    parameters { key: "cudnn_conv_use_max_workspace" value: "0" }
    parameters { key: "use_ep_level_unified_stream" value: "1" }}
  ]
}}
```

### Deprecated Parameters[#](#deprecated-parameters "Link to this heading")

The way to specify these specific parameters as shown below is deprecated. For
backward compatibility, these parameters are still supported. Please use the
above method to specify the parameters.

* `cudnn_conv_algo_search`: CUDA Convolution algorithm search configuration.
  Available options are 0 - EXHAUSTIVE (expensive exhaustive benchmarking using
  cudnnFindConvolutionForwardAlgorithmEx). This is also the default option,
  1 - HEURISTIC (lightweight heuristic based search using
  cudnnGetConvolutionForwardAlgorithm\_v7), 2 - DEFAULT (default algorithm using
  CUDNN\_CONVOLUTION\_FWD\_ALGO\_IMPLICIT\_PRECOMP\_GEMM)
* `gpu_mem_limit`: CUDA memory limit. To use all possible memory pass in maximum
  size\_t. Defaults to SIZE\_MAX.
* `arena_extend_strategy`: Strategy used to grow the memory arena. Available
  options are: 0 = kNextPowerOfTwo, 1 = kSameAsRequested. Defaults to 0.
* `do_copy_in_default_stream`: Flag indicating if copying needs to take place on
  the same stream as the compute stream in the CUDA EP. Available options are:
  0 = Use separate streams for copying and compute, 1 = Use the same stream for
  copying and compute. Defaults to 1.

In the model config file, specifying these parameters will look like:

```
.
.
.
parameters { key: "cudnn_conv_algo_search" value: { string_value: "0" } }
parameters { key: "gpu_mem_limit" value: { string_value: "4294967200" } }
.
.
.
```

## ONNX Runtime with OpenVINO optimization[#](#onnx-runtime-with-openvino-optimization "Link to this heading")

[OpenVINO](https://docs.openvinotoolkit.org/latest/index.md) can be
used in conjunction with an ONNX model to further optimize
performance. To enable OpenVINO optimization you must set the model
configuration as shown below.

```
.
.
.
optimization { execution_accelerators {
  cpu_execution_accelerator : [ {
    name : "openvino"
  } ]
}}
.
.
.
```

## Other Optimization Options with ONNX Runtime[#](#other-optimization-options-with-onnx-runtime "Link to this heading")

Details regarding when to use these options and what to expect from them can be
found [here](https://onnxruntime.ai/docs/performance/tune-performance.md)

### Model Config Options[#](#model-config-options "Link to this heading")

* `intra_op_thread_count`: Sets the number of threads used to parallelize the
  execution within nodes. A value of 0 means ORT will pick a default which is
  number of cores.
* `inter_op_thread_count`: Sets the number of threads used to parallelize the
  execution of the graph (across nodes). If sequential execution is enabled this
  value is ignored.
  A value of 0 means ORT will pick a default which is number of cores.
* `execution_mode`: Controls whether operators in the graph are executed
  sequentially or in parallel. Usually when the model has many branches, setting
  this option to 1 .i.e. âparallelâ will give you better performance. Default is
  0 which is âsequential execution.â
* `level`: Refers to the graph optimization level. By default all optimizations
  are enabled. Allowed values are -1, 1 and 2. -1 refers to BASIC optimizations,
  1 refers to basic plus extended optimizations like fusions and 2 refers to all
  optimizations being disabled. Please find the details
  [here](https://onnxruntime.ai/docs/performance/graph-optimizations.md).

```
optimization {
  graph : {
    level : 1
}}

parameters { key: "intra_op_thread_count" value: { string_value: "0" } }
parameters { key: "execution_mode" value: { string_value: "0" } }
parameters { key: "inter_op_thread_count" value: { string_value: "0" } }
```

* `enable_mem_arena`: Use 1 to enable the arena and 0 to disable. See
  [this](https://onnxruntime.ai/docs/api/c/struct_ort_api.md#a0bbd62df2b3c119636fba89192240593)
  for more information.
* `enable_mem_pattern`: Use 1 to enable memory pattern and 0 to disable.
  See [this](https://onnxruntime.ai/docs/api/c/struct_ort_api.md#ad13b711736956bf0565fea0f8d7a5d75)
  for more information.
* `memory.enable_memory_arena_shrinkage`:
  See [this](https://github.com/microsoft/onnxruntime/blob/master/include/onnxruntime/core/session/onnxruntime_run_options_config_keys.h)
  for more information.
* `session.use_device_allocator_for_initializers`: Use â1â to enable using device allocator for allocating initialized tensor memory and â0â to disable. The default is â0â. See [this](https://onnxruntime.ai/docs/get-started/with-c.md) for more information.

### Command line options[#](#command-line-options "Link to this heading")

#### Thread Pools[#](#thread-pools "Link to this heading")

When intra and inter op threads is set to 0 or a value higher than 1, by default
ORT creates threadpool per session. This may not be ideal in every scenario,
therefore ORT also supports global threadpools. When global threadpools are
enabled ORT creates 1 global threadpool which is shared by every session.
Use the backend config to enable global threadpool. When global threadpool is
enabled, intra and inter op num threads config should also be provided via
backend config. Config values provided in model config will be ignored.

```
--backend-config=onnxruntime,enable-global-threadpool=<0,1>, --backend-config=onnxruntime,intra_op_thread_count=<int> , --backend-config=onnxruntime,inter_op_thread_count=<int>
```

#### Default Max Batch Size[#](#default-max-batch-size "Link to this heading")

The default-max-batch-size value is used for max\_batch\_size during
[Autocomplete](../user_guide/model_configuration.md#auto-generated-model-configuration)
when no other value is found. Assuming server was not launched with
`--disable-auto-complete-config` command-line option, the onnxruntime backend
will set the max\_batch\_size of the model to this default value under the
following conditions:

1. Autocomplete has determined the model is capable of batching requests.
2. max\_batch\_size is 0 in the model configuration or max\_batch\_size
   is omitted from the model configuration.

If max\_batch\_size > 1 and no
[scheduler](../user_guide/model_configuration.md#scheduling-and-batching)
is provided, the dynamic batch scheduler will be used.

```
--backend-config=onnxruntime,default-max-batch-size=<int>
```

The default value of `default-max-batch-size` is 4.

