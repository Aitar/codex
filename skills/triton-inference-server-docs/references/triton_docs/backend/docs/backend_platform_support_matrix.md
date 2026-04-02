* Backend-Plat...

# Backend-Platform Support Matrix[#](#backend-platform-support-matrix "Link to this heading")

Even though Triton supports inference across various platforms such as
cloud, data center, edge and embedded devices on NVIDIA GPUs, x86 and
ARM CPU, or AWS Inferentia, it does so by relying on the backends.
Note that not all Triton backends support every platform. The purpose
of this document is to go over what all compute platforms are supported
by each of these Triton backends.
GPU in this document refers to Nvidia GPU. See
[GPU, Driver, and CUDA Support Matrix](https://docs.nvidia.com/deeplearning/frameworks/support-matrix/index.md)
to learn more about supported GPUs.

## Ubuntu 22.04[#](#ubuntu-22-04 "Link to this heading")

The table below describes target device(s) supported for inference by
each backend on different platforms.

| Backend | x86 | ARM-SBSA |
| --- | --- | --- |
| TensorRT | :heavy\_check\_mark: GPU   :x: CPU | :heavy\_check\_mark: GPU   :x: CPU |
| ONNX Runtime | :heavy\_check\_mark: GPU   :heavy\_check\_mark: CPU | :heavy\_check\_mark: GPU   :heavy\_check\_mark: CPU |
| TensorFlow | :heavy\_check\_mark: GPU   :heavy\_check\_mark: CPU | :heavy\_check\_mark: GPU   :heavy\_check\_mark: CPU |
| PyTorch | :heavy\_check\_mark: GPU   :heavy\_check\_mark: CPU | :heavy\_check\_mark: GPU   :heavy\_check\_mark: CPU |
| OpenVINO | :x: GPU   :heavy\_check\_mark: CPU | :x: GPU   :x: CPU |
| Python[[1]](#id5) | :heavy\_check\_mark: GPU   :heavy\_check\_mark: CPU | :heavy\_check\_mark: GPU   :heavy\_check\_mark: CPU |
| DALI | :heavy\_check\_mark: GPU   :heavy\_check\_mark: CPU | :heavy\_check\_mark: GPU[[2]](#id6)   :heavy\_check\_mark: CPU[[2]](#id6) |
| FIL | :heavy\_check\_mark: GPU   :heavy\_check\_mark: CPU | Unsupported |
| TensorRT-LLM | :heavy\_check\_mark: GPU   :x: CPU | :heavy\_check\_mark: GPU   :x: CPU |
| vLLM | :heavy\_check\_mark: GPU   :heavy\_check\_mark: CPU | Unsupported |

## Windows 10[#](#windows-10 "Link to this heading")

Only TensorRT and ONNX Runtime backends are supported on Windows.

| Backend | x86 | ARM-SBSA |
| --- | --- | --- |
| TensorRT | :heavy\_check\_mark: GPU   :x: CPU | :heavy\_check\_mark: GPU   :x: CPU |
| ONNX Runtime | :heavy\_check\_mark: GPU   :heavy\_check\_mark: CPU | :heavy\_check\_mark: GPU   :heavy\_check\_mark: CPU |

## Jetson JetPack[#](#jetson-jetpack "Link to this heading")

Following backends are currently supported on Jetson Jetpack:

| Backend | Jetson |
| --- | --- |
| TensorRT | :heavy\_check\_mark: GPU   :x: CPU |
| ONNX Runtime | :heavy\_check\_mark: GPU   :heavy\_check\_mark: CPU |
| TensorFlow | :heavy\_check\_mark: GPU   :heavy\_check\_mark: CPU |
| PyTorch | :heavy\_check\_mark: GPU   :heavy\_check\_mark: CPU |
| Python[[1]](#id5) | :x: GPU   :heavy\_check\_mark: CPU |

Look at the [Triton Inference Server Support for Jetson and JetPack](../../user_guide/jetson.md).

## AWS Inferentia[#](#aws-inferentia "Link to this heading")

Currently, inference on AWS Inferentia is only supported via
[python backend](../../python_backend/README.md#running-with-inferentia)
where the deployed python script invokes AWS Neuron SDK.

---



[1]
([1](#id1),[2](#id4))

The supported devices for Python Backend are mentioned with
respect to Triton. The python script running in Python Backend can
be used to execute inference on any hardware if there are available
python APIs to do so. AWS inferentia is one such example. Triton
core is largely unaware of the fact that inference will run on
Inferentia.


[2]
([1](#id2),[2](#id3))

In case of ARM-SBSA, some operations are not fully supported.

