* [In-Process Triton Server API](in_process.md)
* Python

# Python[#](#python "Link to this heading")

## Triton Inference Server In-Process Python API [BETA][#](#triton-inference-server-in-process-python-api-beta "Link to this heading")

Starting with release 24.01 Triton Inference Server will include a
Python package enabling developers to embed Triton Inference Server
instances in their Python applications. The in-process Python API is
designed to match the functionality of the in-process C API while
providing a higher level abstraction. At its core the API relies on a
1:1 python binding of the C API and provides all the flexibility and
power of the C API with a simpler to use interface.

> [!Note] As the API is in BETA please expect some changes as we test
> out different features and get feedback. All feedback is weclome and
> we look forward to hearing from you!

[Requirements](#requirements) | [Installation](#installation)
| [Hello World](#hello-world) | [Stable
Diffusion](#stable-diffusion) | [Ray Serve
Deployment](../tutorials/Triton_Inference_Server_Python_API/examples/rayserve) |

### Requirements[#](#requirements "Link to this heading")

The following instructions require a linux system with Docker installed.
For CUDA support, make sure your CUDA driver meets the requirements in
âNVIDIA Driverâ section of Deep Learning Framework support matrix:
<https://docs.nvidia.com/deeplearning/frameworks/support-matrix/index.md>

### Installation[#](#installation "Link to this heading")

The tutorial and Python API package are designed to be installed and run
within the `nvcr.io/nvidia/tritonserver:24.01-py3` docker image.

A set of convenience scripts are provided to create a docker image based
on the `nvcr.io/nvidia/tritonserver:24.01-py3` image with the Python
API installed plus additional dependencies required for the examples.

#### Triton Inference Server 24.01 + Python API[#](#triton-inference-server-24-01-python-api "Link to this heading")

##### Clone Repository[#](#clone-repository "Link to this heading")

##### Build `triton-python-api:r24.01` Image[#](#build-triton-python-api-r24-01-image "Link to this heading")

##### Supported Backends[#](#supported-backends "Link to this heading")

The built image includes all the backends shipped by default in the
tritonserver `nvcr.io/nvidia/tritonserver:24.01-py3` container.

```
dali  fil  identity  onnxruntime  openvino  python  pytorch  repeat  square  tensorrt
```

##### Included Models[#](#included-models "Link to this heading")

The `default` build includes an `identity` model that can be used
for exercising basic operations including sending input tensors of
different data types. The `identity` model copies provided inputs of
`shape [-1, -1]` to outputs of shape `[-1, -1]`. Inputs are named
`data_type_input` and outputs are named `data_type_output`
(e.g. `string_input`, `string_output`, `fp16_input`,
`fp16_output`).

### Hello World[#](#hello-world "Link to this heading")

#### Start `triton-python-api:r24.01` Container[#](#start-triton-python-api-r24-01-container "Link to this heading")

The following command starts a container and volume mounts the current
directory as `workspace`.

#### Enter Python Shell[#](#enter-python-shell "Link to this heading")

#### Create and Start a Server Instance[#](#create-and-start-a-server-instance "Link to this heading")

#### List Models[#](#list-models "Link to this heading")

```
server.models()
```

##### Example Output[#](#example-output "Link to this heading")

`server.models()` returns a dictionary of the available models with
their current state.

#### Send an Inference Request[#](#send-an-inference-request "Link to this heading")

#### Iterate through Responses[#](#iterate-through-responses "Link to this heading")

`model.infer()` returns an iterator that can be used to process the
results of an inference request.

##### Example Output[#](#example-output-1 "Link to this heading")

### Stable Diffusion[#](#stable-diffusion "Link to this heading")

This example is based on the
[Popular\_Models\_Guide/StableDiffusion](../tutorials/Popular_Models_Guide/StableDiffusion/README.md)
tutorial.

Please note the following command will take many minutes depending on
your hardware configuration and network connection.

The built image includes all the backends shipped by default in the
tritonserver `nvcr.io/nvidia/tritonserver:24.01-py3` container.

```
dali  fil  identity  onnxruntime  openvino  python  pytorch  repeat  square  tensorrt
```

The `diffusion` build includes a `stable_diffustion` pipeline that
takes a text prompt and returns a generated image. For more details on
the models and pipeline please see the
[Popular\_Models\_Guide/StableDiffusion](../tutorials/Popular_Models_Guide/StableDiffusion/README.md)
tutorial.

#### Start Container[#](#start-container "Link to this heading")

The following command starts a container and volume mounts the current
directory as `workspace`.

#### Enter Python Shell[#](#enter-python-shell-1 "Link to this heading")

#### Create and Start a Server Instance[#](#create-and-start-a-server-instance-1 "Link to this heading")

#### List Models[#](#list-models-1 "Link to this heading")

```
server.models()
```

##### Example Output[#](#example-output-2 "Link to this heading")

#### Send an Inference Request[#](#send-an-inference-request-1 "Link to this heading")

#### Iterate through Responses and save image[#](#iterate-through-responses-and-save-image "Link to this heading")

##### Example Output[#](#example-output-3 "Link to this heading")

![sample_generated_image](../_images/sample_generated_image.jpg)


Fig. 1 sample\_generated\_image[#](#id8 "Link to this image")

