* Custom Operations

# Custom Operations[#](#custom-operations "Link to this heading")

Modeling frameworks that allow custom operations are partially
supported by the Triton Inference Server. Custom operations can be
added to Triton at build time or at startup and are made available to
all loaded models.

## TensorRT[#](#tensorrt "Link to this heading")

TensorRT allows a user to create [custom
layers](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.md#extending)
which can then be used in TensorRT models. For those models to run in
Triton the custom layers must be made available.

To make the custom layers available to Triton, the TensorRT custom
layer implementations must be compiled into one or more shared
libraries which must then be loaded into Triton using LD\_PRELOAD. For
example, assuming your TensorRT custom layers are compiled into
libtrtcustom.so, starting Triton with the following command makes
those custom layers available to all TensorRT models.

```
$ LD_PRELOAD=libtrtcustom.so:${LD_PRELOAD} tritonserver --model-repository=/tmp/models ...
```

A limitation of this approach is that the custom layers must be
managed separately from the model repository itself. And more
seriously, if there are custom layer name conflicts across multiple
shared libraries there is currently no way to handle it.

When building the custom layer shared library it is important to use
the same version of TensorRT as is being used in Triton. You can find
the TensorRT version in the [Triton Release
Notes](https://docs.nvidia.com/deeplearning/triton-inference-server/release-notes/index.md). A
simple way to ensure you are using the correct version of TensorRT is
to use the [NGC TensorRT
container](https://ngc.nvidia.com/catalog/containers/nvidia:tensorrt)
corresponding to the Triton container. For example, if you are using
the 24.12 version of Triton, use the 24.12 version of the TensorRT
container.

## PyTorch[#](#pytorch "Link to this heading")

Torchscript allows users to [add custom
operations](https://pytorch.org/tutorials/advanced/torch_script_custom_ops.md)
which can then be used in Torchscript models. By using LD\_PRELOAD you
can load your custom C++ operations into Triton. For example, if you
follow the instructions in the
[pytorch/extension-script](https://github.com/pytorch/extension-script)
repository and your Torchscript custom operations are compiled into
libpytcustom.so, starting Triton with the following command makes
those operations available to all PyTorch models. Since all Pytorch
custom operations depend on one or more PyTorch shared libraries
that must be available to the custom shared library when it is
loading. In practice this means that you must make sure that
/opt/tritonserver/backends/pytorch is on the library path while
launching the server. There are several ways to control the library path
and a common one is to use the LD\_LIBRARY\_PATH.

```
$ LD_LIBRARY_PATH=/opt/tritonserver/backends/pytorch:$LD_LIBRARY_PATH LD_PRELOAD=libpytcustom.so:${LD_PRELOAD} tritonserver --model-repository=/tmp/models ...
```

A limitation of this approach is that the custom operations must be
managed separately from the model repository itself. And more
seriously, if there are custom layer name conflicts across multiple
shared libraries or the handles used to register them in PyTorch there
is currently no way to handle it.

Starting with the 20.07 release of Triton the [TorchVision
operations](https://github.com/pytorch/vision) will be included with
the PyTorch backend and hence they do not have to be explicitly added
as custom operations.

When building the custom operations shared library it is important to
use the same version of PyTorch as is being used in Triton. You can
find the PyTorch version in the [Triton Release
Notes](https://docs.nvidia.com/deeplearning/triton-inference-server/release-notes/index.md). A
simple way to ensure you are using the correct version of PyTorch is
to use the [NGC PyTorch
container](https://ngc.nvidia.com/catalog/containers/nvidia:pytorch)
corresponding to the Triton container. For example, if you are using
the 24.12 version of Triton, use the 24.12 version of the PyTorch
container.

## ONNX[#](#onnx "Link to this heading")

ONNX Runtime allows users to [add custom
operations](https://onnxruntime.ai/docs/reference/operators/add-custom-op.md)
which can then be used in ONNX models. To register your custom
operations library you need to include it in the model configuration
as an additional field. For example, if you follow [this
example](https://github.com/microsoft/onnxruntime/blob/master/onnxruntime/test/shared_lib/test_inference.cc)
from the
[microsoft/onnxruntime](https://github.com/microsoft/onnxruntime)
repository and your ONNXRuntime custom operations are compiled into
libonnxcustom.so, adding the following to the model configuration of
your model makes those operations available to that specific ONNX
model.

```
$ model_operations { op_library_filename: "/path/to/libonnxcustom.so" }
```

When building the custom operations shared library it is important to
use the same version of ONNXRuntime as is being used in Triton. You
can find the ONNXRuntime version in the [Triton Release
Notes](https://docs.nvidia.com/deeplearning/triton-inference-server/release-notes/index.md).

