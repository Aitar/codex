* Deploying...

# Deploying Hugging Face Transformer Models in Triton[#](#deploying-hugging-face-transformer-models-in-triton "Link to this heading")

There are multiple ways to run Llama2 with Tritonserver.

1. Infer with [TensorRT-LLM Backend](trtllm_guide.md#infer-with-tensorrt-llm-backend)
2. Infer with [vLLM Backend](vllm_guide.md#infer-with-vllm-backend)
3. Infer with [Python-based Backends as a HuggingFace model](https://github.com/triton-inference-server/tutorials/blob/main/Popular_Models_Guide/Quick_Deploy/HuggingFaceTransformers/README.md#deploying-hugging-face-transformer-models-in-triton)

## Pre-build instructions[#](#pre-build-instructions "Link to this heading")

For the tutorials we are assuming that the Llama2 models, weights, and tokens are cloned from the Huggingface Llama2 repo [here](https://huggingface.co/meta-llama/Llama-2-7b-hf/tree/main).
To run the tutorials, you will need to get permissions for the Llama2 repository as well as access to the huggingface cli.
The cli uses [User access tokens](https://huggingface.co/docs/hub/security-tokens). The tokens can be found here: [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).

