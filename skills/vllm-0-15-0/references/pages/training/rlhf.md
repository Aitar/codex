# Reinforcement Learning from Human Feedback - vLLM

Source: https://docs.vllm.ai/en/v0.15.0/training/rlhf/

Reinforcement Learning from Human Feedback¶

Reinforcement Learning from Human Feedback (RLHF) is a technique that fine-tunes language models using human-generated preference data to align model outputs with desired behaviors. vLLM can be used to generate the completions for RLHF.

The following open-source RL libraries use vLLM for fast rollouts (sorted alphabetically and non-exhaustive):

Cosmos-RL

ms-swift

NeMo-RL

Open Instruct

OpenRLHF

PipelineRL

Prime-RL

SkyRL

TRL

Unsloth

verl

See the following basic examples to get started if you don't want to use an existing library:

Training and inference processes are located on separate GPUs (inspired by OpenRLHF)

Training and inference processes are colocated on the same GPUs using Ray

Utilities for performing RLHF with vLLM

See the following notebooks showing how to use vLLM for GRPO:

Efficient Online Training with GRPO and vLLM in TRL

Qwen-3 4B GRPO using Unsloth + vLLM
