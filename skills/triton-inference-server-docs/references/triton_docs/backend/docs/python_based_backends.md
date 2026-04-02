* Python-based...

# Python-based Backends[#](#python-based-backends "Link to this heading")

Python-based backend is a special type of Tritonâs backends, which does
not require any C++ code. However, this type of backends depends on
[Python backend](https://github.com/triton-inference-server/python_backend)
and requires the following artifacts being present:
`libtriton_python.so`, `triton_python_backend_stub`,
and `triton_python_backend_utils.py`.

## Usage[#](#usage "Link to this heading")

To implement and use a Python-based backend, make sure to follow these steps.

* Implement the
  [`TritonPythonModel` interface](../../python_backend/README.md#usage),
  which could be re-used as a backend by multiple models.
  This script should be named `model.py`.
* Create a folder for your custom backend under the backends directory
  (ex: /opt/tritonserver/backends) with the corresponding backend name,
  containing the `model.py`. For example, for a backend named
  `my_python_based_backend`, Triton would expect to find the full path
  `/opt/tritonserver/backends/my_python_based_backend/model.py`.
* Make sure that `libtriton_python.so`, `triton_python_backend_stub`,
  and `triton_python_backend_utils.py` are present either under
  `/opt/tritonserver/backends/my_python_based_backend/` or
  `/opt/tritonserver/backends/python/`. When both locations contain
  mentioned artifacts, custom backendâs artifacts will take priority over Python
  backendâs artifacts. This way, if custom backends needs to use a different
  Python version than what is shipped by default, it can easily be done. Please,
  refer to [customization](#customization) section for more details.
* Specify `my_python_based_backend` as a backend in `config.pbtxt`
  for any model, that should use this backend.

```
...
backend: "my_python_based_backend"
...
```

Since Triton uses Python backend under the hood, it is expected,
to see `python` backend entry in server logs, even when Python backend
is not explicitly used.

```
I1013 21:52:45.756456 18668 server.cc:619]
+-------------------------+-------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Backend                 | Path                                                        | Config                                                                                                              |
+-------------------------+-------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| python                  | /opt/tritonserver/backends/python/libtriton_python.so       | {"cmdline":{"auto-complete-config":"true","backend-directory":"/opt/tritonserver/backends","min-compute-capability" |
|                         |                                                             | :"6.000000","default-max-batch-size":"4"}}                                                                          |
| my_python_based_backend | /opt/tritonserver/backends/my_python_based_backend/model.py | {"cmdline":{"auto-complete-config":"true","backend-directory":"/opt/tritonserver/backends","min-compute-capability" |
|                         |                                                             | :"6.000000","default-max-batch-size":"4"}}                                                                          |
+-------------------------+-------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
```

## Customization[#](#customization "Link to this heading")

Python backend shipped in the NVIDIA GPU Cloud containers uses Python 3.10.
Python backend is able to use the libraries that exist in the
current Python environment. These libraries can be installed in a virtualenv,
conda environment, or the global system Python, and
will only be used if the Python version matches the Python version
of the Python backendâs stub executable (`triton_python_backend_stub`).
For example, if you install a set of libraries in a Python 3.9 environment
and your Python backend stub is compiled with Python 3.10 these libraries
will *NOT* be available. You would need to
[compile](../../python_backend/README.md#building-custom-python-backend-stub)
the stub executable with Python 3.9.

If you want to create a tar file that contains all your Python dependencies
or you want to use different Python environments for each Python model
you need to create a
[Custom Execution Environment](../../python_backend/README.md#creating-custom-execution-environments)
in Python backend.

## Background[#](#background "Link to this heading")

In some use cases, it is sufficient to implement
[`TritonPythonModel` interface](../../python_backend/README.md#usage)
only once and re-use it across multiple models. As an example, please refer
to the [vLLM backend](https://github.com/triton-inference-server/vllm_backend),
which provides a common python script to serve models supported by vLLM.

Triton Inference Server can handle this special case and treats common
`model.py` script as a Python-based backend. In the scenario, when model
relies on a custom Python-based backend, Triton loads `libtriton_python.so`
first, this ensures that Triton knows how to send requests to the backend
for execution and the backend knows how to communicate with Triton. Then,
Triton makes sure to use common `model.py` from the backendâs repository,
and not look for it in the model repository.

While the only required function is `execute`, it is typically helpful
to enhance your implementation by adding `initialize`, `finalize`,
and any other helper functions. Users are also encouraged to make use of the
[`auto_complete_config`](../../python_backend/README.md#auto-complete-config)
function to define standardized input and output properties upfront.

