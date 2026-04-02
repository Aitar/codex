# Pre-built release container images on NGC — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/installation/containers.html

Pre-built release container images on NGC#

Pre-built TensorRT LLM releases are made available as container images
on NGC. This is likely the simplest way to obtain TensorRT LLM. Please refer to the documentation in NGC for usage instructions.

Container image tags

In the example shell commands, `x.y.z` corresponds to the TensorRT-LLM container
version to use. If omitted, `IMAGE_TAG` will default to `tensorrt_llm.__version__`
(e.g., this documentation was generated from the `1.3.0rc7` source tree).
If this does not work, e.g., because a container for the version you are
currently working with has not been released yet, you can try using a
container published for a previous
GitHub pre-release or release
(see also NGC Catalog).

Containers can also be built locally, see
NVIDIA/TensorRT-LLM
for all related options.
