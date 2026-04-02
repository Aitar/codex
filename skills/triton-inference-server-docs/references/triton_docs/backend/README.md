* Triton...

[![License](https://img.shields.io/badge/License-BSD3-lightgrey.svg)](https://opensource.org/licenses/BSD-3-Clause)

# Triton Inference Server Backend[#](#triton-inference-server-backend "Link to this heading")

A Triton *backend* is the implementation that executes a model. A
backend can be a wrapper around a deep-learning framework, like
PyTorch, TensorFlow, TensorRT or ONNX Runtime. Or a backend can be
custom C/C++ logic performing any operation (for example, image
pre-processing).

This repo contains documentation on Triton backends and also source,
scripts and utilities for creating Triton backends. You do not need to
use anything provided in this repo to create a Triton backend but you
will likely find its contents useful.

## Frequently Asked Questions[#](#frequently-asked-questions "Link to this heading")

Full documentation is included below but these shortcuts can help you
get started in the right direction.

### Where can I ask general questions about Triton and Triton backends?[#](#where-can-i-ask-general-questions-about-triton-and-triton-backends "Link to this heading")

Be sure to read all the information below as well as the [general
Triton
documentation](https://github.com/triton-inference-server/server#triton-inference-server)
available in the main
[server](https://github.com/triton-inference-server/server) repo. If
you donât find your answer there you can ask questions on the main
Triton [issues
page](https://github.com/triton-inference-server/server/issues).

### Where can I find all the backends that are available for Triton?[#](#where-can-i-find-all-the-backends-that-are-available-for-triton "Link to this heading")

Anyone can develop a Triton backend, so it isnât possible for us to
know about all available backends. But the Triton project does provide
a set of supported backends that are tested and updated with each
Triton release.

**TensorRT**: The TensorRT backend is used to execute TensorRT
models. The
[tensorrt\_backend](https://github.com/triton-inference-server/tensorrt_backend)
repo contains the source for the backend.

**ONNX Runtime**: The ONNX Runtime backend is used to execute ONNX
models. The
[onnxruntime\_backend](https://github.com/triton-inference-server/onnxruntime_backend)
repo contains the documentation and source for the backend.

**TensorFlow**: The TensorFlow backend is used to execute TensorFlow
models in both GraphDef and SavedModel formats. The same backend is
used to execute both TensorFlow 1 and TensorFlow 2 models. The
[tensorflow\_backend](https://github.com/triton-inference-server/tensorflow_backend)
repo contains the documentation and source for the backend.

**PyTorch**: The PyTorch backend is used to execute PyTorch models in both
TorchScript and PyTorch 2.0 formats. The
[pytorch\_backend](https://github.com/triton-inference-server/pytorch_backend)
repo contains the documentation and source for the backend.

**OpenVINO**: The OpenVINO backend is used to execute
[OpenVINO](https://docs.openvinotoolkit.org/latest/index.md)
models. The
[openvino\_backend](https://github.com/triton-inference-server/openvino_backend)
repo contains the documentation and source for the backend.

**Python**: The Python backend allows you to write your model logic in
Python. For example, you can use this backend to execute pre/post
processing code written in Python, or to execute a PyTorch Python
script directly (instead of first converting it to TorchScript and
then using the PyTorch backend). The
[python\_backend](https://github.com/triton-inference-server/python_backend)
repo contains the documentation and source for the backend.

**DALI**: [DALI](https://github.com/NVIDIA/DALI) is a collection of
highly optimized building blocks and an execution engine that
accelerates the pre-processing of the input data for deep learning
applications. The DALI backend allows you to execute your DALI
pipeline within Triton. The
[dali\_backend](https://github.com/triton-inference-server/dali_backend)
repo contains the documentation and source for the backend.

**FIL**: The FIL ([Forest Inference
Library](https://github.com/rapidsai/cuml/tree/branch-21.10/python/cuml/fil))
backend is used to execute a variety of tree-based ML models, including
XGBoost models, LightGBM models, Scikit-Learn random forest models, and cuML
random forest models. The
[fil\_backend](https://github.com/triton-inference-server/fil_backend) repo
contains the documentation and source for the backend.

**TensorRT-LLM**: The TensorRT-LLM backend allows you to serve
[TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) models with Triton Server.
Check out the
[Triton TRT-LLM user guide](../getting_started/trtllm_user_guide.md)
for more information. The
[tensorrtllm\_backend](https://github.com/triton-inference-server/tensorrtllm_backend)
repo contains the documentation and source for the backend.

**vLLM**: The vLLM backend is designed to run
[supported models](https://vllm.readthedocs.io/en/latest/models/supported_models.md)
on a [vLLM engine](https://github.com/vllm-project/vllm/blob/main/vllm/engine/async_llm_engine.py).
This backend depends on [python\_backend](https://github.com/triton-inference-server/python_backend)
to load and serve models. The
[vllm\_backend](https://github.com/triton-inference-server/vllm_backend) repo
contains the documentation and source for the backend.

**Important Note!** Not all the above backends are supported on every platform
supported by Triton. Look at the
[Backend-Platform Support Matrix](docs/backend_platform_support_matrix.md)
to learn about the same.

### How can I develop my own Triton backend?[#](#how-can-i-develop-my-own-triton-backend "Link to this heading")

First you probably want to ask on the main Triton [issues
page](https://github.com/triton-inference-server/server/issues) to
make sure you are not duplicating a backend that already exists. Then
follow the [tutorial](examples/README.md) to learn how to create your
first simple Triton backend and incrementally improve it to add more
features. You should also read the complete documentation on [Triton
backends](#backends).

### Can I add (or remove) a backend to an existing Triton installation?[#](#can-i-add-or-remove-a-backend-to-an-existing-triton-installation "Link to this heading")

Yes. See [Backend Shared Library](#backend-shared-library) for general
information about how the shared library implementing a backend is
managed by Triton, and [Triton with Unsupported and Custom
Backends](../customization_guide/compose.md#triton-with-unsupported-and-custom-backends)
for documentation on how to add your backend to the released Triton
Docker image. For a standard install the globally available backends
are in /opt/tritonserver/backends.

### What about backends developed using the âlegacy custom backendâ API.[#](#what-about-backends-developed-using-the-legacy-custom-backend-api "Link to this heading")

The legacy custom API is removed from Triton. If you have custom
backends that you developed using this older API you must port them to
the new [Triton Backend API](#triton-backend-api).

## Backends[#](#backends "Link to this heading")

A Triton *backend* is the implementation that executes a model. A
backend can be a wrapper around a deep-learning framework, like
PyTorch, TensorFlow, TensorRT, ONNX Runtime or OpenVINO. A backend can
also implement any functionality you want as long as it adheres to the
[backend API](#triton-backend-api). Triton uses this API to send
requests to the backend for execution and the backend uses the API to
communicate with Triton.

Every model must be associated with a backend. A modelâs backend is
specified in the modelâs configuration using the `backend` setting.
For using TensorRT backend, the value of this setting should be `tensorrt`.
Similarly, for using PyTorch, ONNX and TensorFlow backends, the `backend`
field should be set to `pytorch`, `onnxruntime` or `tensorflow` respectively.
For all other backends, `backend` must be set to the name of the backend.
Some backends may also check the `platform` setting for categorizing the model,
for example, in TensorFlow backend, `platform` should be set to
`tensorflow_savedmodel` or `tensorflow_graphdef` according to the model format.
Please refer to the specific backend repository on whether `platform` is used.

### Backend Shared Library[#](#backend-shared-library "Link to this heading")

Each backend must be implemented as a shared library and the name of
the shared library must be *libtriton\_<backend-name>.so*. For
example, if the name of the backend is âmybackendâ, a model indicates
that it uses the backend by setting the model configuration âbackendâ
setting to âmybackendâ, and Triton looks for *libtriton\_mybackend.so*
as the shared library that implements the backend. The
[tutorial](examples/README.md) shows examples of how to build your
backend logic into the appropriate shared library.

For a model, *M* that specifies backend *B*, Triton searches for the
backend shared library in the following places, in this order:

* <model\_repository>/M/<version\_directory>/libtriton\_B.so
* <model\_repository>/M/libtriton\_B.so
* <global\_backend\_directory>/B/libtriton\_B.so

Where <global\_backend\_directory> is by default
/opt/tritonserver/backends. The âbackend-directory flag can be used
to override the default.

Typically you will install your backend into the global backend
directory. For example, if using Triton Docker images you can follow
the instructions in [Triton with Unsupported and Custom
Backends](../customization_guide/compose.md#triton-with-unsupported-and-custom-backends). Continuing
the example of a backend names âmybackendâ, you would install into the
Triton image as:

```
/opt/
  tritonserver/
    backends/
      mybackend/
        libtriton_mybackend.so
        ... # other files needed by mybackend
```

Starting from 24.01, the default backend shared library name can be changed by
providing the `runtime` setting in the model configuration. For example,

```
runtime: "my_backend_shared_library_name.so"
```

A model may choose a specific runtime implementation provided by the backend.

### Triton Backend API[#](#triton-backend-api "Link to this heading")

A Triton backend must implement the C interface defined in
[tritonbackend.h](https://github.com/triton-inference-server/core/tree/main/include/triton/core/tritonbackend.h). The
following abstractions are used by the API.

#### TRITONBACKEND\_Backend[#](#tritonbackend-backend "Link to this heading")

A TRITONBACKEND\_Backend object represents the backend itself. The
same backend object is shared across all models that use the
backend. The associated API, like TRITONBACKEND\_BackendName, is used
to get information about the backend and to associate a user-defined
state with the backend.

A backend can optionally implement TRITONBACKEND\_Initialize and
TRITONBACKEND\_Finalize to get notification of when the backend object
is created and destroyed (for more information see [backend
lifecycles](#backend-lifecycles)).

#### TRITONBACKEND\_Model[#](#tritonbackend-model "Link to this heading")

A TRITONBACKEND\_Model object represents a model. Each model loaded by
Triton is associated with a TRITONBACKEND\_Model. Each model can use
the TRITONBACKEND\_ModelBackend API to get the backend object
representing the backend that is used by the model.

The same model object is shared across all instances of that
model. The associated API, like TRITONBACKEND\_ModelName, is used to
get information about the model and to associate a user-defined state
with the model.

Most backends will implement TRITONBACKEND\_ModelInitialize and
TRITONBACKEND\_ModelFinalize to initialize the backend for a given
model and to manage the user-defined state associated with the model
(for more information see [backend lifecycles](#backend-lifecycles)).

The backend must take into account threading concerns when
implementing TRITONBACKEND\_ModelInitialize and
TRITONBACKEND\_ModelFinalize. Triton will not perform multiple
simultaneous calls to these functions for a given model; however, if a
backend is used by multiple models Triton may simultaneously call the
functions with a different thread for each model. As a result, the
backend must be able to handle multiple simultaneous calls to the
functions. Best practice for backend implementations is to use only
function-local and model-specific user-defined state in these
functions, as is shown in the [tutorial](examples/README.md).

#### TRITONBACKEND\_ModelInstance[#](#tritonbackend-modelinstance "Link to this heading")

A TRITONBACKEND\_ModelInstance object represents a model
*instance*. Triton creates one or more instances of the model based on
the *instance\_group* settings specified in the model
configuration. Each of these instances is associated with a
TRITONBACKEND\_ModelInstance object.

The only function that the backend must implement is
TRITONBACKEND\_ModelInstanceExecute. The
TRITONBACKEND\_ModelInstanceExecute function is called by Triton to
perform inference/computation on a batch of inference requests. Most
backends will also implement TRITONBACKEND\_ModelInstanceInitialize
and TRITONBACKEND\_ModelInstanceFinalize to initialize the backend for
a given model instance and to manage the user-defined state associated
with the model (for more information see [backend
lifecycles](#backend-lifecycles)).

The backend must take into account threading concerns when
implementing TRITONBACKEND\_ModelInstanceInitialize,
TRITONBACKEND\_ModelInstanceFinalize and
TRITONBACKEND\_ModelInstanceExecute. Triton will not perform multiple
simultaneous calls to these functions for a given model instance;
however, if a backend is used by a model with multiple instances or by
multiple models Triton may simultaneously call the functions with a
different thread for each model instance. As a result, the backend
must be able to handle multiple simultaneous calls to the
functions. Best practice for backend implementations is to use only
function-local and model-specific user-defined state in these
functions, as is shown in the [tutorial](examples/README.md).

#### TRITONBACKEND\_Request[#](#tritonbackend-request "Link to this heading")

A TRITONBACKEND\_Request object represents an inference request made
to the model. The backend takes ownership of the request object(s) in
TRITONBACKEND\_ModelInstanceExecute and must release each request by
calling TRITONBACKEND\_RequestRelease. However, the ownership of request
object is returned back to Triton in case TRITONBACKEND\_ModelInstanceExecute
returns an error. See [Inference Requests and Responses](#inference-requests-and-responses)
for more information about request lifecycle.

The Triton Backend API allows the backend to get information about the
request as well as the input and request output tensors of the
request. Each request input is represented by a TRITONBACKEND\_Input
object.

#### TRITONBACKEND\_Response[#](#tritonbackend-response "Link to this heading")

A TRITONBACKEND\_Response object represents a response sent by the
backend for a specific request. The backend uses the response API to
set the name, shape, datatype and tensor values for each output tensor
included in the response. The response can indicate either a failed or
a successful request. See [Inference Requests and
Responses](#inference-requests-and-responses) for more information
about request-response lifecycle.

#### TRITONBACKEND\_BackendAttribute[#](#tritonbackend-backendattribute "Link to this heading")

A `TRITONBACKEND_BackendAttribute` allows a backend to set certain attributes which
are queried by Triton to inform certain feature support, preferred configurations, and
other types of backend-specific behavior.

When initializing a backend, Triton will query the `TRITONBACKEND_GetBackendAttribute` function
if implemented by the backend. This function is optional to implement, but is generally used to call
the related `TRITONBACKEND_BackendAttribute` APIs for setting backend-specific attributes.

Some of the relevant BackendAttribute setter APIs are listed below:

* `TRITONBACKEND_BackendSetExecutionPolicy`
* `TRITONBACKEND_BackendAttributeAddPreferredInstanceGroup`

  + Defines a priority list of instance groups to prefer for this backend if a model config doesnât explicitly define any instance groups.
* `TRITONBACKEND_BackendAttributeSetParallelModelInstanceLoading`

  + Defines whether the backend can safely handle concurrent calls to `TRITONBACKEND_ModelInstanceInitialize` or not.
  + Loading model instances in parallel can improve server startup times for large instance counts.
  + By default, this attribute is set to false, meaning that parallel instance loading is disabled for all backends unless explicitly enabled.
  + The following official backends currently support loading model instances in parallel:

    - Python
    - ONNXRuntime

The full list of `TRITONBACKEND_BackendAttribute` related APIs are defined in
[tritonbackend.h](https://github.com/triton-inference-server/core/blob/main/include/triton/core/tritonbackend.h).

### Backend Lifecycles[#](#backend-lifecycles "Link to this heading")

A backend must carefully manage the lifecycle of the backend itself,
the models and model instances that use the backend and the inference
requests that execute on the model instances using the backend.

#### Backend and Model[#](#backend-and-model "Link to this heading")

Backend, model and model instance initialization is triggered when
Triton loads a model.

* If the model requires a backend that is not already in use by an
  already loaded model, then:

  + Triton [loads the shared library](#backend-shared-library) that
    implements the backend required by the model.
  + Triton creates the TRITONBACKEND\_Backend object that represents
    the backend.
  + Triton calls TRITONBACKEND\_Initialize if it is implemented in the
    backend shared library. TRITONBACKEND\_Initialize should not return
    until the backend is completely initialized. If
    TRITONBACKEND\_Initialize returns an error, Triton will report that
    the model failed to load.
* Triton creates the TRITONBACKEND\_Model object that represents the
  model. Triton calls TRITONBACKEND\_ModelInitialize if it is
  implemented in the backend shared library.
  TRITONBACKEND\_ModelInitialize should not return until the backend
  is completely initialized for the model. If
  TRITONBACKEND\_ModelInitialize returns an error, Triton will show
  that the model failed to load.
* For each model instance specified for the model in the model
  configuration:

  + Triton creates the TRITONBACKEND\_ModelInstance object that
    represents the model instance.
  + Triton calls TRITONBACKEND\_ModelInstanceInitialize if it is
    implemented in the backend shared library.
    TRITONBACKEND\_ModelInstanceInitialize should not return until the
    backend is completely initialized for the instance. If
    TRITONBACKEND\_ModelInstanceInitialize returns an error, Triton
    will show that the model failed to load.

Backend, model and model instance finalization is triggered when
Triton unloads a model.

* For each model instance:

  + Triton calls TRITONBACKEND\_ModelInstanceFinalize if it is
    implemented in the backend shared library.
    TRITONBACKEND\_ModelInstanceFinalize should not return until the
    backend is completely finalized, including stopping any threads
    create for the model instance and freeing any user-defined state
    created for the model instance.
  + Triton destroys the TRITONBACKEND\_ModelInstance object that
    represents the model instance.
* Triton calls TRITONBACKEND\_ModelFinalize if it is implemented in the
  backend shared library. TRITONBACKEND\_ModelFinalize should not
  return until the backend is completely finalized, including stopping
  any threads create for the model and freeing any user-defined state
  created for the model.
* Triton destroys the TRITONBACKEND\_Model object that represents the
  model.
* Even if no other loaded model requires the backend, Triton does not
  finalize and unload the backend until the tritonserver process is
  exiting. When the tritonserver process exits:

  + Triton calls TRITONBACKEND\_Finalize if it is implemented in the
    backend shared library. TRITONBACKEND\_ModelFinalize should not
    return until the backend is completely finalized, including
    stopping any threads create for the backend and freeing any
    user-defined state created for the backend.
  + Triton destroys the TRITONBACKEND\_Backend object that represents
    the backend.

#### Inference Requests and Responses[#](#inference-requests-and-responses "Link to this heading")

Triton calls TRITONBACKEND\_ModelInstanceExecute to execute inference
requests on a model instance. Each call to
TRITONBACKEND\_ModelInstanceExecute communicates a batch of requests
to execute and the instance of the model that should be used to
execute those requests. The backend should not allow the caller
thread to return from TRITONBACKEND\_ModelInstanceExecute until that
instance is ready to handle another set of requests. Typically this
means that the TRITONBACKEND\_ModelInstanceExecute function will
create responses and release the requests before returning. However,
in case TRITONBACKEND\_ModelInstanceExecute returns an error, the ownership
of requests is transferred back to Triton which will then be responsible
for releasing them. Therefore, in the case where TRITONBACKEND\_ModelInstanceExecute
returns an error, the backend must not retain references to the requests
or access them in any way. For more detailed description of request/response
lifetimes, study the documentation of TRITONBACKEND\_ModelInstanceExecute in
[tritonbackend.h](https://github.com/triton-inference-server/core/blob/main/include/triton/core/tritonbackend.h).

##### Single Response[#](#single-response "Link to this heading")

Most backends will create a single response for each request. For that
kind of backend, executing a single inference request requires the
following steps:

* Create a response for the request using TRITONBACKEND\_ResponseNew.
* For each request input tensor use TRITONBACKEND\_InputProperties to
  get shape and datatype of the input as well as the buffer(s)
  containing the tensor contents.
* For each output tensor which the request expects to be returned, use
  TRITONBACKEND\_ResponseOutput to create the output tensor of the
  required datatype and shape. Use TRITONBACKEND\_OutputBuffer to get a
  pointer to the buffer where the tensorâs contents should be written.
* Use the inputs to perform the inference computation that produces
  the requested output tensor contents into the appropriate output
  buffers.
* Optionally set parameters in the response.
* Send the response using TRITONBACKEND\_ResponseSend.
* Release the request using TRITONBACKEND\_RequestRelease.

For a batch of requests the backend should attempt to combine the
execution of the individual requests as much as possible to increase
performance.

##### Decoupled Responses[#](#decoupled-responses "Link to this heading")

It is also possible for a backend to send multiple responses
for a request. A backend may also
send responses out-of-order relative to the order that the request
batches are executed. Such backends are called *decoupled* backends.

The decoupled backends use one `ResponseFactory` object per request to
create and send any number of responses for the request. They must send at
least one final response per request (even if it is a flags-only response).
You can send a flags-only response with TRITONBACKEND\_ResponseFactorySendFlags.
For this kind of backend, executing a single inference request typically requires
the following steps:

1. For each request input tensor, use TRITONBACKEND\_InputProperties to
   get shape and datatype of the input as well as the buffer(s)
   containing the tensor contents.
2. Create a `ResponseFactory` object for the request using
   TRITONBACKEND\_ResponseFactoryNew.
3. Create a response from the `ResponseFactory` object using
   TRITONBACKEND\_ResponseNewFromFactory. As long as you have the
   `ResponseFactory` object, you can continue creating responses.
4. For each output tensor which the request expects to be returned, use
   TRITONBACKEND\_ResponseOutput to create the output tensor of the
   required datatype and shape. Use TRITONBACKEND\_OutputBuffer to get a
   pointer to the buffer where the tensorâs contents should be written.
5. Use the inputs to perform the inference computation that produces
   the requested output tensor contents into the appropriate output
   buffers.
6. Optionally set parameters in the response.
7. Send the response using TRITONBACKEND\_ResponseSend.
8. Repeat steps 3-7 until there are no more responses.
9. Send the last response for a request using either TRIONBACKEND\_ResponseSend
   with a TRITONSERVER\_ResponseCompleteFlag or after all responses have been
   sent for a request using TRITONBACKEND\_ResponseFactorySendFlags.
   This is required for every request.
10. Release the request using TRITONBACKEND\_RequestRelease.

###### Special Cases[#](#special-cases "Link to this heading")

The decoupled API is powerful and supports various special cases:

* The model can also send responses out-of-order in which it received
  requests.
* The backend can copy out the contents of the input buffer(s) if
  request is to be released before the contents are completely
  consumed to generate responses. After copy, the request can be
  released anytime before exiting TRITONBACKEND\_ModelInstanceExecute.
  The copies and `ResponseFactory` object can be passed to a separate
  thread in backend. This means main caller thread can exit from
  TRITONBACKEND\_ModelInstanceExecute and the backend can still continue
  generating responses as long as it holds `ResponseFactory` object.

The [repeat example](examples/README.md) demonstrates full power of
what can be achieved from decoupled API.

Study documentation of these TRITONBACKEND\_\* functions in
[tritonbackend.h](https://github.com/triton-inference-server/core/blob/main/include/triton/core/tritonbackend.h)
for more details on these APIs. Read
[Decoupled Backends and Models](../user_guide/decoupled_models.md)
for more details on how to host a decoupled model.

## Build the Backend Utilities[#](#build-the-backend-utilities "Link to this heading")

The source in this repo builds into a single âbackend utilitiesâ
library that is useful when building backends. You donât need to use
these utilities but they will be helpful for most backends.

Typically you donât need to build this repo directly but instead you
can include it in the build of your backend as is shown in the
CMakeLists.txt files of the [tutorial examples](examples/README.md).

To build and install in a local directory use the following commands.

```
$ mkdir build
$ cd build
$ cmake -DCMAKE_INSTALL_PREFIX:PATH=`pwd`/install ..
$ make install
```

The following required Triton repositories will be pulled and used in
the build. By default the âmainâ branch/tag will be used for each repo
but the listed CMake argument can be used to override.

* triton-inference-server/common: -DTRITON\_COMMON\_REPO\_TAG=[tag]
* triton-inference-server/core: -DTRITON\_CORE\_REPO\_TAG=[tag]

See the [CMakeLists.txt](https://github.com/triton-inference-server/backend/blob/main/CMakeLists.txt) file for other build options.

## Python-based Backends[#](#python-based-backends "Link to this heading")

Triton also provides an option to create [Python-based backends](docs/python_based_backends.md).
These backends should implement the
[`TritonPythonModel` interface](../python_backend/README.md#usage),
which could be re-used as a backend by multiple models.
While the only required function is `execute`,
you may find it helpful to enhance your implementation by adding `initialize`,
`finalize`, and any other helper functions. For examples, please refer to
the [vLLM backend](https://github.com/triton-inference-server/vllm_backend),
which provides a common python script to serve models supported by vLLM.

