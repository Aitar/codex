* Support Matrix

# Support Matrix[#](#support-matrix "Link to this heading")

Please find below information about tested models, used environment and libraries.

## Verified Models[#](#verified-models "Link to this heading")

We have verified that the NVIDIA Triton Model Navigator Optimize works correctly for the following models.

| Source | Model |
| --- | --- |
| [NVIDIA DeepLearningExamples](https://github.com/NVIDIA/DeepLearningExamples) | [ResNet50 PyT](https://github.com/NVIDIA/DeepLearningExamples/tree/master/PyTorch/Classification/ConvNets) |
| [NVIDIA DeepLearningExamples](https://github.com/NVIDIA/DeepLearningExamples) | [EfficientNet PyT](https://github.com/NVIDIA/DeepLearningExamples/tree/master/PyTorch/Classification/ConvNets) |
| [NVIDIA DeepLearningExamples](https://github.com/NVIDIA/DeepLearningExamples) | [EfficientNet TF2](https://github.com/NVIDIA/DeepLearningExamples/tree/master/TensorFlow2/Classification/ConvNets) |
| [NVIDIA DeepLearningExamples](https://github.com/NVIDIA/DeepLearningExamples) | [BERT TF2](https://github.com/NVIDIA/DeepLearningExamples/tree/master/TensorFlow2/LanguageModeling/BERT) |
| [HuggingFace](https://huggingface.co/) | [GPT2 Jax](https://huggingface.co/docs/transformers/model_doc/gpt2) |
| [HuggingFace](https://huggingface.co/) | [GPT2 PyT](https://huggingface.co/docs/transformers/model_doc/gpt2) |
| [HuggingFace](https://huggingface.co/) | [GPT2 TF2](https://huggingface.co/docs/transformers/model_doc/gpt2) |
| [HuggingFace](https://huggingface.co/) | [DistilBERT PyT](https://huggingface.co/docs/transformers/model_doc/distilbert) |
| [HuggingFace](https://huggingface.co/) | [DistilGPT2 TF2](https://huggingface.co/docs/transformers/model_doc/gpt2) |
| [HuggingFace](https://huggingface.co/) | [Stable Diffusion](https://huggingface.co/spaces/stabilityai/stable-diffusion) |
| [HuggingFace](https://huggingface.co/) | [Automatic Speech Recognition](https://huggingface.co/learn/audio-course/chapter2/asr_pipeline) |

## Libraries and Packages[#](#libraries-and-packages "Link to this heading")

A set of component versions are imposed by the used NGC container. During testing, we have used `24.02` a container version
that contains:

* [PyTorch 2.3.0a0+ebedce2](https://github.com/pytorch/pytorch/commit/ebedce2)
* [TensorFlow 2.15.0](https://github.com/tensorflow/tensorflow/releases/tag/v2.15.0)
* [TensorRT 8.6.3](https://docs.nvidia.com/deeplearning/tensorrt/release-notes/index.md)
* [Torch-TensorRT 2.0.0.dev0](https://github.com/NVIDIA/Torch-TensorRT)
* [ONNX Runtime 1.17.1](https://github.com/microsoft/onnxruntime/tree/v1.17.1)
* [Polygraphy](https://github.com/NVIDIA/TensorRT/tree/master/tools/Polygraphy/): 0.49.4
* [GraphSurgeon](https://github.com/NVIDIA/TensorRT/tree/master/tools/onnx-graphsurgeon/): 0.4.6
* [tf2onnx v1.16.1](https://github.com/onnx/tensorflow-onnx/releases/tag/v1.16.1)
* Other components versions depend on the used framework containers versions.
  See its [support matrix](https://docs.nvidia.com/deeplearning/frameworks/support-matrix/index.md)
  for a detailed summary.

