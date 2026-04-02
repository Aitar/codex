---
name: trtllm-text-vector
description: Design, build, debug, and optimize TRT-LLM pipelines that return vectors or embeddings instead of generated text. Use when working on text-vector services, pooled hidden states, projection heads, custom vector outputs, engine build profiles, output binding, alignment checks, or performance tuning for TRT-LLM-based embedding systems.
---

# Trtllm Text Vector

## Overview

Use this skill for TRT-LLM systems whose final product is a vector, embedding, or other dense representation rather than decoded text. Keep the semantics explicit first, then build, validate, and optimize against that definition.

## SOP

### 1. Define the vector output semantics

- Identify the exact output source, such as a final hidden state, a pooled sequence representation, a projection head, or a multi-vector layout.
- Fix the special-token rule, pooling rule, normalization rule, output dimension, and any truncation or masking behavior.
- Stop here if the vector definition is still ambiguous.

### 2. Build a trusted reference baseline

- Implement or locate a non-TRT reference path that matches the intended semantics.
- Verify the reference on a small sample first, then on the full validation set.
- Treat the reference as the source of truth for all TRT comparisons.

### 3. Choose the direct output path

- Prefer the simplest path that emits the final vector directly.
- If you must extract intermediate tensors, confirm that the engine, runtime, and service layers preserve them correctly end to end.
- Prefer a custom out-of-tree model or service-side vector head over patching installed packages.
- Avoid treating generation logits or logprob fields as vector outputs unless that is the explicit design.

### 4. Build the engine with real constraints

- Size `max_seq_len`, `max_batch_size`, and any packing or cache settings from the real request distribution.
- Cover production P95 and P99 lengths, plus expected concurrency and memory budget.
- Keep dtype and pooling precision choices tied to measured correctness, not guesswork.

### 5. Validate in layers

- Check shape, dtype, and non-zero values before any deeper comparison.
- Run small-sample alignment next, then full-set alignment.
- Investigate long-input drift, boundary cases, and zero-output failures before changing performance knobs.
- If alignment fails, debug semantics and output binding before tuning batch size or plugins.

### 6. Benchmark and finalize

- Sweep concurrency, QPS, latency, memory, and failure rate on production-like data.
- Pick a recommended operating point only after correctness is stable.
- Lock the serving wrapper, monitoring, and rollback plan last.

## Reference

Read [references/trtllm-text-vector-playbook.md](references/trtllm-text-vector-playbook.md) when you need build knobs, validation gates, failure-mode checks, or benchmark guidance.

## Working Rules

- Do not assume the vector comes from hidden states, mean pooling, or a projection head until the model proves it.
- Do not optimize for throughput before the vector definition is verified.
- Prefer minimal, reproducible changes when touching TRT-LLM configs or custom model code.
