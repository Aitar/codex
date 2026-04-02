---
name: tensorrt-llm-docs-1-1-0
description: Answer questions using the bundled TensorRT-LLM 1.1.0 documentation in this skill. Use for queries about TensorRT-LLM usage, installation, model building, APIs, features, examples, or performance tuning/optimization (e.g., "trtllm", “如何用trtllm?”, “trtllm如何构建模型?”, “性能还能优化吗?”).
---

# TensorRT-LLM Docs 1.1.0

## Overview

Use the local TensorRT-LLM 1.1.0 docs under `references/docs` to answer questions. Keep answers grounded in this version and cite file paths and section headings.

## Workflow

1. Extract keywords from the user question (English + Chinese terms).
2. Search the docs with `rg` inside `references/docs`.
3. Open only the relevant files and sections.
4. If the question is about custom architecture or engine buildability, first determine backend scope:
   - PyTorch backend model extension path (`_torch`) vs TensorRT engine build/deploy path.
   - Check `models/supported-models.md` and `models/adding-new-model.md` together before concluding.
5. Synthesize a concise answer and mention the version (1.1.0) if “current/latest” wording appears.
6. If the docs do not cover the question, state the gap and suggest what additional info is needed.

### Search tips

- Start with high-level entry points:
  - `references/docs/overview.md`
  - `references/docs/quick-start-guide.md`
  - `references/docs/installation/`
  - `references/docs/developer-guide/`
  - `references/docs/features/`
  - `references/docs/_modules/tensorrt_llm/llmapi/llm.md`
  - `references/docs/_modules/tensorrt_llm/runtime/model_runner.md`
  - `references/docs/models/`
  - `references/docs/examples/`
- Prefer `rg -n "<keyword>" references/docs` and then open specific files.
- Search both English and Chinese keywords when relevant (e.g., “performance”, “优化”, “build”, “构建”, “模型”, “engine”).

### Answering guidelines

- Cite the exact file path(s) and section titles you used.
- Do not assume content from newer versions; note “TensorRT-LLM 1.1.0 docs” explicitly when helpful.
- When asked about “current/latest,” clarify that the answer is based on 1.1.0 documentation.

### Backend and Buildability Rules (1.1.0)

- `models/adding-new-model.md` is explicitly a "PyTorch Backend" guide; do not treat it as proof that an architecture is directly buildable into a TensorRT engine.
- Use this quick decision path:
  - If user asks "can this architecture run/build in TRT-LLM", check `models/supported-models.md` first.
  - If architecture is absent from supported list, call out uncertainty for direct engine build and recommend classic TensorRT backend integration/registration validation before promising build success.
- Mark this explicitly as an inference from docs when needed:
  - `adding-new-model.md` explains `_torch` model registration (including out-of-tree).
  - `supported-models.md` enumerates supported architectures.

### Local runtime notes (practical shortcuts)

- If you hit backend-mismatch errors or need explicit TensorRT backend behavior, use `from tensorrt_llm._tensorrt_engine import LLM`.
- Building and saving a TensorRT engine uses an `LLM` implementation with `save()` (documented in `_modules/tensorrt_llm/llmapi/llm.md`).
- Offline engine inference expects an engine directory containing at least `config.json` and `rank0.engine`.
- Prefer `tensorrt_llm.runtime.ModelRunner.from_dir(engine_dir)` for offline engine execution.
- Tokenizer is typically loaded from a Hugging Face model dir; the engine dir may not include a full tokenizer, so pass `--tokenizer`/`tokenizer_dir` explicitly when needed.
- Engine build limits are fixed by `BuildConfig` (e.g., `max_input_len`, `max_seq_len`, `max_batch_size`, `max_num_tokens`); runtime inputs must not exceed these.
- `remove_input_padding` and `max_num_tokens` are coupled for packed-token scheduling; tune them together for throughput/latency balance (`features/paged-attention-ifb-scheduler.md`).

### Minimal build template (smallest working settings)

- `BuildConfig(max_input_len=256, max_seq_len=512, max_batch_size=1, max_num_tokens=512, opt_batch_size=1, opt_num_tokens=256)`
- Use this as a starting point, then scale up limits if longer context or larger batch is required.

### Troubleshooting fast checks

- `LLM` missing `save()` or backend mismatch hints -> use `from tensorrt_llm._tensorrt_engine import LLM`.
- `TypeError: MoeConfig...` during engine load -> engine/config version mismatch with local TRT-LLM.
- Engine dir missing `config.json` -> `ModelRunner.from_dir` will fail; rebuild or copy the engine dir fully.
- Architecture unsupported during build -> re-check `models/supported-models.md`; do not assume `_torch` out-of-tree registration implies TensorRT engine buildability.

### Practical gotchas for custom-output / embedding workloads

- For decoder-only embedding/vector workloads, prefer a custom classic TensorRT-LLM model that computes the final target tensor inside the graph and exposes it as a normal `mark_output(...)`.
- Do not treat `additional_model_outputs` as the default solution for decoder-only hidden-state export. It can be useful, but it is a higher-risk path for productionization than a custom primary output.
- If the workload is context-only embedding (no decoding), consider a context-only engine shape:
  - Disable KV cache in `BuildConfig` when generation cache is not needed.
  - Otherwise runtime may require generation-oriented tensors such as KV/cache-related inputs that are irrelevant to the actual workload.
- When validating a custom embedding engine, check build limits before debugging math:
  - `max_input_len`
  - `max_seq_len`
  - `max_batch_size`
  - `max_num_tokens`
  Long prompts that exceed engine limits can look like model-quality regressions when the real issue is shape coverage.
- For pooled hidden-state outputs, use a higher-precision reduction path when alignment matters:
  - A practical pattern is lower-precision backbone (`bf16`/`fp16`) plus `fp32` pooling/reduction and `fp32` final embedding output.
  - Do not assume `fp16` and `bf16` will match equally well; verify each configuration separately.
- For throughput benchmarking, remember reported GPU memory may be whole-device usage, not single-process usage. Check for other resident services before attributing all memory to the engine under test.

### Project Notes (Non-official, from local implementation)

- These points are not from upstream docs; they are validated in this workspace and should be labeled as project-specific when used in answers.
- `trtllm_custom_model_plan.md` indicates:
  - Unsupported HF architecture can fail engine build even after `_torch` custom modeling.
  - Stable parity path used `gpt_attention_plugin=auto` with `remove_input_padding=True`.
  - Triton Python backend startup required `TORCHDYNAMO_DISABLE=1` and `TORCHINDUCTOR_DISABLE=1`.
- `triton_ensemble_plan.md` and `triton_postprocess_plan.md` provide a practical Triton rollout path:
  - `tokenizer -> trtllm -> postprocess` ensemble.
  - Output mapping aligned to legacy service fields.

## Resources

- `references/docs/`: Full TensorRT-LLM 1.1.0 documentation tree copied from the repo root.
