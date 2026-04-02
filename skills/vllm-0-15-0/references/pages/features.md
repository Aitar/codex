# Features - vLLM

Source: https://docs.vllm.ai/en/v0.15.0/features/

Features¶

Compatibility Matrix¶

The tables below show mutually exclusive features and the support on some hardware.

The symbols used have the following meanings:

✅ = Full compatibility

🟠 = Partial compatibility

❌ = No compatibility

❔ = Unknown or TBD

Note

Check the ❌ or 🟠 with links to see tracking issue for unsupported feature/hardware combination.

Feature x Feature¶

| Feature | CP | APC | LoRA | SD | CUDA graph | pooling | enc-dec | logP | prmpt logP | async output | multi-step | mm | best-of | beam-search | prompt-embeds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CP | ✅ | | | | | | | | | | | | | | |
| APC | ✅ | ✅ | | | | | | | | | | | | | |
| LoRA | ✅ | ✅ | ✅ | | | | | | | | | | | | |
| SD | ✅ | ✅ | ❌ | ✅ | | | | | | | | | | | |
| CUDA graph | ✅ | ✅ | ✅ | ✅ | ✅ | | | | | | | | | | |
| pooling | 🟠* | 🟠* | ✅ | ❌ | ✅ | ✅ | | | | | | | | | |
| enc-dec | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | | | | | | | | |
| logP | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | | | | | | | |
| prmpt logP | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | | | | | | |
| async output | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | | | | | |
| multi-step | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | | | | |
| mm | ✅ | ✅ | 🟠^ | ❔ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❔ | ✅ | | | |
| best-of | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | ❔ | ❌ | ✅ | ✅ | | |
| beam-search | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | ❔ | ❌ | ❔ | ✅ | ✅ | |
| prompt-embeds | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | ❔ | ❔ | ❌ | ❔ | ❔ | ✅ |

* Chunked prefill and prefix caching are only applicable to last-token or all pooling with causal attention.
^ LoRA is only applicable to the language backbone of multimodal models.

Feature x Hardware¶

| Feature | Volta | Turing | Ampere | Ada | Hopper | CPU | AMD | Intel GPU |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CP | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| APC | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| LoRA | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| SD | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ |
| CUDA graph | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ |
| pooling | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| enc-dec | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ |
| mm | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| prompt-embeds | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❔ | ✅ |
| logP | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| prmpt logP | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| async output | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ |
| multi-step | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ |
| best-of | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| beam-search | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Note

For information on feature support on Google TPU, please refer to the TPU-Inference Recommended Models and Features documentation.
