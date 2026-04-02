# TRT-LLM Text Vector Playbook

## Purpose

Use this reference when the final product is a vector, embedding, or other dense representation built on TRT-LLM.
It focuses on the checks that keep vector semantics, engine shape, and runtime behavior aligned.

## Table of Contents

- Semantics Checklist
- Build Knobs
- Validation Ladder
- Common Failure Modes
- Benchmarking Checklist
- Decision Rules

## Semantics Checklist

- Identify the output source: final hidden state, pooled sequence embedding, projection head, or multi-vector layout.
- Fix the token rule: special tokens, BOS handling, prompt truncation, and masking.
- Fix the reduction rule: mean, max, CLS, last token, learned pooling, or segmentation.
- Fix post-processing: normalization, quantization, slicing, or packing.
- Record the expected output dimension, dtype, and shape invariants.

## Build Knobs

- `max_seq_len`: cover production P99 plus safety margin.
- `max_input_len`: match the longest prompt expected by the service.
- `max_batch_size`: fit target concurrency and memory budget.
- `max_num_tokens`: cap the total active token load if the runtime uses it.
- `dtype`: prefer the smallest dtype that preserves alignment.
- `remove_input_padding`: use only when the packed-token path is correct end to end.
- `paged_kv_cache`: enable only when the service actually needs decode-state caching.
- `use_paged_context_fmha`: keep it consistent with the model and input packing mode.
- `profiling_verbosity`: raise it only while debugging build or runtime behavior.

## Validation Ladder

1. Smoke test the output shape, dtype, and non-zero values on a tiny prompt set.
2. Compare against the reference baseline on a small sample.
3. Run a full-set alignment pass and inspect avg/min metrics.
4. Slice the validation set by long inputs, short inputs, and boundary cases.
5. Repeat the same request twice to check stability and determinism.
6. Rebuild and recheck whenever semantics, shape, or input limits change.

## Common Failure Modes

- Semantic mismatch: the output source or pooling rule is not the one the business expects.
- Zero output: the tensor is present in the engine but not copied back correctly at runtime.
- Length truncation: the engine profile is too small for the real prompt distribution.
- Wrong output name: the model, engine, and executor are using different names for the same tensor.
- Logprob confusion: a vector is serialized through a logprob-shaped field, but the semantics are still vector semantics.
- Over-optimized build: performance tuning hides a correctness bug instead of fixing it.

## Benchmarking Checklist

- Use a prompt distribution that resembles production.
- Keep the workload fixed when comparing builds.
- Record QPS, p50, p95, p99, memory, and failure rate.
- Sweep concurrency until throughput plateaus or latency becomes unacceptable.
- Compare dtype and profile variants only after correctness is stable.

## Decision Rules

- If the vector definition is unclear, stop and clarify before building the engine.
- If there is no trusted reference baseline, build one first.
- If runtime output is zero or stale, debug the binding and copy path before tuning performance.
- If correctness passes, optimize profile and concurrency next.
- If the service needs long-term maintainability, prefer a custom model or service-side vector head over patching installed packages.
