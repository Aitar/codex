# LLM API Introduction — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/llm-api/index.html

LLM API Introduction#

The LLM API is a high-level Python API designed to streamline LLM inference workflows.

It supports a broad range of use cases, from single-GPU setups to multi-GPU and multi-node deployments, with built-in support for various parallelism strategies and advanced features. The LLM API integrates seamlessly with the broader inference ecosystem, including NVIDIA Dynamo.

While the LLM API simplifies inference workflows with a high-level interface, it is also designed with flexibility in mind. Under the hood, it uses a PyTorch-native and modular backend, making it easy to customize, extend, or experiment with the runtime.

Quick Start Example#

A simple inference example with TinyLlama using the LLM API:

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

For more advanced usage including distributed inference, multimodal, and speculative decoding, please refer to this README.

Model Input#

The `LLM()` constructor accepts either a Hugging Face model ID or a local model path as input.

1. Using a Model from the Hugging Face Hub#

To load a model directly from the Hugging Face Model Hub, simply pass its model ID (i.e., repository name) to the LLM constructor. The model will be automatically downloaded:

```text
llm = LLM(model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
```

You can also use quantized checkpoints (FP4, FP8, etc) of popular models provided by NVIDIA in the same way.

2. Using a Local Hugging Face Model#

To use a model from local storage, first download it manually:

```text
git lfs install
git clone https://huggingface.co/meta-llama/Meta-Llama-3.1-8B
```

Then, load the model by specifying a local directory path:

```text
llm = LLM(model=<local_path_to_model>)
```

Note: Some models require accepting specific license agreements. Make sure you have agreed to the terms and authenticated with Hugging Face before downloading.

Tips and Troubleshooting#

The following tips typically assist new LLM API users who are familiar with other APIs that are part of TensorRT-LLM:

RuntimeError: only rank 0 can start multi-node session, got 1#

There is no need to add an `mpirun` prefix for launching single node multi-GPU inference with the LLM API.

For example, you can run `pythonllm_inference_distributed.py` to perform multi-GPU on a single node.

Hang issue on Slurm Node#

If you experience a hang or other issue on a node managed with Slurm, add prefix `mpirun-n1--oversubscribe--allow-run-as-root` to your launch script.

For example, try `mpirun-n1--oversubscribe--allow-run-as-rootpythonllm_inference_distributed.py`.

MPI_ABORT was invoked on rank 1 in communicator MPI_COMM_WORLD with errorcode 1.#

Because the LLM API relies on the `mpi4py` library, put the LLM class in a function and protect the main entrypoint to the program under the `__main__` namespace to avoid a recursive spawn process in `mpi4py`.

This limitation is applicable for multi-GPU inference only.

Cannot quit after generation#

The LLM instance manages threads and processes, which may prevent its reference count from reaching zero. To address this issue, there are two common solutions:

Wrap the LLM instance in a function, as demonstrated in the quickstart guide. This will reduce the reference count and trigger the shutdown process.

Use LLM as a context manager, with the following code: `withLLM(...)asllm:...`, the shutdown method will be invoked automatically once it goes out of the `with`-statement block.

Single node hanging when using `dockerrun--net=host`#

The root cause may be related to `mpi4py`. There is a workaround suggesting a change from `--net=host` to `--ipc=host`, or setting the following environment variables:

```text
export OMPI_MCA_btl_tcp_if_include=lo
export OMPI_MCA_oob_tcp_if_include=lo
```

Another option to improve compatibility with `mpi4py` is to launch the task using:

```text
mpirun -n 1 --oversubscribe --allow-run-as-root python my_llm_task.py
```

This command can help avoid related runtime issues.
