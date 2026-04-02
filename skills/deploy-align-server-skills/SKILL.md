---
name: deploy-align-server-skills
description: Deploy, align, debug, and tune local or remote inference services that must match an existing online service. Use when Codex needs to bring up a local compatibility server, align request and response behavior with an online endpoint, switch or validate backends such as vLLM or TRT-LLM, fix CUDA or GPU runtime compatibility issues, benchmark throughput or latency or power, or produce a clean handoff for later operators.
---

# Deploy Align Server Skills

## Overview

Use this skill to make a local or remote inference service usable first, then aligned, then fast. Prefer reproducible environment checks, service-layer compatibility, and trustworthy metrics over deep backend patching too early.

## Workflow

### 1. Establish the execution boundary first

- Confirm whether work should happen on the local machine, over SSH, or inside a container.
- Reuse the existing service entrypoints, health checks, and benchmark scripts before inventing new ones.
- Record the exact host, container, virtualenv, backend, and startup command before making changes.

### 2. Prove the environment can run the stack

- Validate CUDA visibility and a minimal GPU tensor before starting the service.
- Check GPU architecture against the installed `torch`, CUDA, and backend packages.
- Prefer a new runnable environment plus a compatibility layer when an online custom wheel cannot run on the current machine.
- Fix compatibility prerequisites explicitly, including packages such as `cuda-compat-13-1` and `LD_LIBRARY_PATH` when the runtime requires them.

### 3. Align the service before chasing model parity

- Identify the exact online endpoint, required fields, and any pre-process or post-process hooks that clients actually depend on.
- Preserve interface shape first: request path, response schema, field names, finish reasons, and wrapper behavior.
- Reuse the online preprocessing and postprocessing logic when possible instead of reimplementing from scratch.
- Measure structure alignment separately from content alignment.

### 4. Validate the backend with the smallest possible probe

- Prove a minimal `generate` path works before wiring the backend into the server.
- Use real script files for probes in multiprocessing environments; avoid stdin-based experiments.
- Guard probe scripts with `if __name__ == '__main__'` when workers or MPI-style executors are involved.
- Treat "engine can build and load" as only a partial milestone; confirm the first real request path too.

### 5. Tune service scheduling before blaming the model

- If concurrency rises but QPS does not, inspect the service dispatch model before touching model internals.
- Prefer queue plus micro-batch worker designs over one-request-one-generate serialization.
- Group requests by compatible sampling parameters when batching.
- Tune with multiple metrics together: QPS, latency, token throughput, queue wait, and power.

### 6. Trust only metrics whose observation path is valid

- Confirm whether the service is truly streaming tokens before computing TPOT from client events.
- Prefer backend-native or service-side metrics for TTFT and TPOT when available.
- Reset measurement windows before a run and account for warmup or probe requests in the totals.

### 7. Leave the system easy to hand off

- Record the current healthy startup command, active parameters, result files, known warnings, and cleanup commands.
- Document residual risks separately from finished work.
- Include the next three most useful experiments instead of a vague backlog.

## Reference

Read [references/deploy-align-server-playbook.md](references/deploy-align-server-playbook.md) when you need the detailed playbook for environment setup, alignment strategy, performance tuning, metric pitfalls, and repeatable handoff patterns.

## Working Rules

- Prefer service-layer compatibility over reverse-engineering an old custom runtime unless exact runtime parity is required.
- Prefer minimal, reproducible probes and scripts over ad hoc shell snippets for backend validation.
- Do not trust client-side latency decomposition until the response delivery pattern is verified.
- Do not stop after a successful health check; verify smoke requests, full-set structure checks, and at least one realistic benchmark.
