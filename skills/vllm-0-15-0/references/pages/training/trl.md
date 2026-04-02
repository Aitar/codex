# Transformers Reinforcement Learning - vLLM

Source: https://docs.vllm.ai/en/v0.15.0/training/trl/

Transformers Reinforcement Learning¶

Transformers Reinforcement Learning (TRL) is a full stack library that provides a set of tools to train transformer language models with methods like Supervised Fine-Tuning (SFT), Group Relative Policy Optimization (GRPO), Direct Preference Optimization (DPO), Reward Modeling, and more. The library is integrated with 🤗 transformers.

Online methods such as GRPO or Online DPO require the model to generate completions. vLLM can be used to generate these completions!

See the vLLM integration guide in the TRL documentation for more information.

TRL currently supports the following online trainers with vLLM:

GRPO

Online DPO

RLOO

Nash-MD

XPO

To enable vLLM in TRL, set the `use_vllm` flag in the trainer configuration to `True`.

Modes of Using vLLM During Training¶

TRL supports two modes for integrating vLLM during training: server mode and colocate mode. You can control how vLLM operates during training with the `vllm_mode` parameter.

Server mode¶

In server mode, vLLM runs as an independent process on dedicated GPUs and communicates with the trainer through HTTP requests. This configuration is ideal when you have separate GPUs for inference, as it isolates generation workloads from training, ensuring stable performance and easier scaling.

```text
from trl import GRPOConfig

training_args = GRPOConfig(
    ...,
    use_vllm=True,
    vllm_mode="server",  # default value, can be omitted
)
```

Colocate mode¶

In colocate mode, vLLM runs inside the trainer process and shares GPU memory with the training model. This avoids launching a separate server and can improve GPU utilization, but may lead to memory contention on the training GPUs.

```text
from trl import GRPOConfig

training_args = GRPOConfig(
    ...,
    use_vllm=True,
    vllm_mode="colocate",
)
```

Some trainers also support vLLM sleep mode, which offloads parameters and caches to GPU RAM during training, helping reduce memory usage. Learn more in the memory optimization docs.

Info

For detailed configuration options and flags, refer to the documentation of the specific trainer you are using.
