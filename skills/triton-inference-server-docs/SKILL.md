---
name: triton-inference-server-docs
description: Answer questions using the bundled NVIDIA Triton Inference Server documentation in references/triton_docs. Use for Triton setup/deployment, model repository and config.pbtxt, scheduling/batching/ensembles/BLS, client APIs (HTTP/gRPC/C/Java), protocols, backends (TensorRT, Python, ONNX Runtime, PyTorch, TensorRT-LLM, vLLM, DALI, FIL), performance tools (perf_analyzer, model_analyzer, perf_benchmark, model_navigator), metrics, troubleshooting, or tutorials.
---

# Triton Inference Server Docs

## Overview

Use this skill to answer Triton Inference Server questions by loading only the relevant markdown files from the bundled docs in `references/triton_docs/`.

## Quick Start

1) Identify the topic and map it to the closest doc area (see entry points below).
2) Use `rg` to locate keywords across the docs when you are unsure which file to open.
3) Open only the few files needed to answer; summarize and cite paths in the response.

## Entry Points By Topic

- **Getting started**: `references/triton_docs/getting_started/`
- **User guide (model repo, config, batching, ensembles, BLS, metrics)**: `references/triton_docs/user_guide/`
- **Server guide (deployment, security, logging, metrics, scaling)**: `references/triton_docs/server_guide/`
- **Client guide (HTTP/gRPC/C/Java APIs)**: `references/triton_docs/client_guide/`
- **Protocols**: `references/triton_docs/protocol/` and `references/triton_docs/customization_guide/inference_protocols.md`
- **Backends overview and APIs**: `references/triton_docs/backend/` and `references/triton_docs/backend_guide/`
- **Specific backends**:
  - TensorRT: `references/triton_docs/tensorrt_backend/`
  - Python: `references/triton_docs/python_backend/`
  - PyTorch: `references/triton_docs/pytorch_backend/`
  - ONNX Runtime: `references/triton_docs/onnxruntime_backend/`
  - TensorRT-LLM: `references/triton_docs/tensorrtllm_backend/`
  - vLLM: `references/triton_docs/vllm_backend/`
  - DALI: `references/triton_docs/dali_backend/`
  - FIL: `references/triton_docs/fil_backend/`
- **Performance tools**:
  - `references/triton_docs/perf_analyzer/`
  - `references/triton_docs/model_analyzer/`
  - `references/triton_docs/perf_benchmark/`
  - `references/triton_docs/model_navigator/`
- **LLM features**: `references/triton_docs/llm_features/`
- **Examples and tutorials**: `references/triton_docs/examples/` and `references/triton_docs/tutorials/`

## Search Tips

- Find keywords quickly: `rg -n "<keyword>" references/triton_docs`
- Find candidate files: `rg --files -g "*.md" references/triton_docs | rg "<topic>"`
- Start from `references/triton_docs/index.md` for high-level context.

## Answering Guidance

- Prefer primary guidance from the docs; avoid external assumptions.
- If docs are ambiguous, state the ambiguity and suggest the most relevant file to consult next.
- Provide concrete file paths so the user can verify details.
