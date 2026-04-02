# Installing on Linux via pip — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/installation/linux.html

Installing on Linux via `pip`#

Install TensorRT LLM (tested on Ubuntu 24.04).

Install prerequisites

Before the pre-built Python wheel can be installed via `pip`, a few
prerequisites must be put into place:

Install CUDA Toolkit 13.1 following the CUDA Installation Guide for Linux
and make sure `CUDA_HOME` environment variable is properly set.

The `cuda-compat-13-1` package may be required depending on your system’s NVIDIA GPU
driver version. For additional information, refer to the CUDA Forward Compatibility.

```text
# By default, PyTorch CUDA 12.8 package is installed. Install PyTorch CUDA 13.0 package to align with the CUDA version used for building TensorRT LLM wheels.
pip3 install torch==2.9.1 torchvision --index-url https://download.pytorch.org/whl/cu130

sudo apt-get -y install libopenmpi-dev

# Optional step: Only required for disagg-serving
sudo apt-get -y install libzmq3-dev
```

Tip

Instead of manually installing the prerequisites as described
above, it is also possible to use the pre-built TensorRT LLM Develop container
image hosted on NGC
(see here for information on container tags).

Install pre-built TensorRT LLM wheel

Once all prerequisites are in place, TensorRT LLM can be installed as follows:

```text
pip3 install --ignore-installed pip setuptools wheel && pip3 install tensorrt_llm
```

Note: The TensorRT LLM wheel on PyPI is built with PyTorch 2.9.1. This version may be incompatible with the NVIDIA NGC PyTorch 25.12 container, which uses a more recent PyTorch build from the main branch. If you are using this container or a similar environment, please install the pre-built wheel located at `/app/tensorrt_llm` inside the TensorRT LLM NGC Release container instead.

This project will download and install additional third-party open source software projects. Review the license terms of these open source projects before use.

Sanity check the installation by running the following in Python (tested on Python 3.12):

```text
 1from tensorrt_llm import LLM, SamplingParams
 2
 3
 4def main():
 5
 6    # Model could accept HF model name, a path to local HF model,
 7    # or Model Optimizer's quantized checkpoints like nvidia/Llama-3.1-8B-Instruct-FP8 on HF.
 8    llm = LLM(model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
 9
10    # Sample prompts.
11    prompts = [
12        "Hello, my name is",
13        "The capital of France is",
14        "The future of AI is",
15    ]
16
17    # Create a sampling params.
18    sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
19
20    for output in llm.generate(prompts, sampling_params):
21        print(
22            f"Prompt: {output.prompt!r}, Generated text: {output.outputs[0].text!r}"
23        )
24
25    # Got output like
26    # Prompt: 'Hello, my name is', Generated text: '\n\nJane Smith. I am a student pursuing my degree in Computer Science at [university]. I enjoy learning new things, especially technology and programming'
27    # Prompt: 'The president of the United States is', Generated text: 'likely to nominate a new Supreme Court justice to fill the seat vacated by the death of Antonin Scalia. The Senate should vote to confirm the'
28    # Prompt: 'The capital of France is', Generated text: 'Paris.'
29    # Prompt: 'The future of AI is', Generated text: 'an exciting time for us. We are constantly researching, developing, and improving our platform to create the most advanced and efficient model available. We are'
30
31
32if __name__ == '__main__':
33    main()
```

Known limitations

There are some known limitations when you pip install pre-built TensorRT LLM wheel package.

MPI in the Slurm environment

If you encounter an error while running TensorRT LLM in a Slurm-managed cluster, you need to reconfigure the MPI installation to work with Slurm.
The setup method depends on your Slurm configuration, please check with your admin. This is not TensorRT LLM specific, but rather a general MPI+Slurm issue.

```text
The application appears to have been direct launched using "srun",
but OMPI was not built with SLURM support. This usually happens
when OMPI was not configured --with-slurm and we weren't able
to discover a SLURM installation in the usual places.
```

Prevent `pip` from replacing existing PyTorch installation

On certain systems, particularly Ubuntu 22.04, users installing TensorRT LLM would find that their existing, CUDA 13.0 compatible PyTorch installation (e.g., `torch==2.9.0+cu130`) was being uninstalled by `pip`. It was then replaced by a CUDA 12.8 version (`torch==2.9.0`), causing the TensorRT LLM installation to be unusable and leading to runtime errors.

The solution is to create a `pip` constraints file, locking `torch` to the currently installed version. Here is an example of how this can be done manually:

```text
CURRENT_TORCH_VERSION=$(python3 -c "import torch; print(torch.__version__)")
echo "torch==$CURRENT_TORCH_VERSION" > /tmp/torch-constraint.txt
pip3 install --ignore-installed pip setuptools wheel && pip3 install tensorrt_llm -c /tmp/torch-constraint.txt
```
