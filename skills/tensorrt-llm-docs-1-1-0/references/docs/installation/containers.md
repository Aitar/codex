Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/installation/containers.md

* [Installation](index.md)
* Pre-built release container images on NGC

# Pre-built release container images on NGC[#](#pre-built-release-container-images-on-ngc "Link to this heading")

Pre-built TensorRT LLM releases are made available as container images
on NGC. This is likely the simplest way to obtain TensorRT LLM. Please refer to the [documentation in NGC](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tensorrt-llm/containers/release) for usage instructions.

Container image tags

In the example shell commands, `x.y.z` corresponds to the TensorRT-LLM container
version to use. If omitted, `IMAGE_TAG` will default to `tensorrt_llm.__version__`
(e.g., this documentation was generated from the `1.1.0` source tree).
If this does not work, e.g., because a container for the version you are
currently working with has not been released yet, you can try using a
container published for a previous
[GitHub pre-release or release](https://github.com/NVIDIA/TensorRT-LLM/releases)
(see also [NGC Catalog](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tensorrt-llm/containers/release/tags)).

Containers can also be built locally, see
[NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM/tree/main/docker)
for all related options.

[previous

Installation](index.md "previous page")
[next

Installing on Linux via `pip`](linux.md "next page")