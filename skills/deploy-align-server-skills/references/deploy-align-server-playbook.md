# Deploy Align Server Playbook

## Environment

### Reusable经验

- Start by pinning the real execution boundary: local machine, remote host, container, Python environment, backend, and startup entrypoint.
- Validate the GPU stack before launching the service:
  - `torch.cuda.is_available()`
  - a minimal CUDA tensor op
  - backend import and a minimal generate probe
- Check architecture compatibility early. A service can fail only because the installed `torch` or custom wheel does not support the current GPU architecture.
- Prefer "new runnable runtime + compatibility service layer" when the online custom wheel cannot run on the target machine.
- Make runtime compatibility explicit in startup scripts. If the environment depends on compat libraries, export the required `LD_LIBRARY_PATH` directly in the startup path.
- Treat missing build dependencies as first-class environment work. If Triton or related components compile at startup, missing headers such as `Python.h` will block progress.

### 已踩过的坑

- Do not assume an online custom wheel can be reused on a newer GPU. In the project, an old `torch 2.6.0` path failed on `RTX 5090 / sm_120` with `no kernel image is available for execution on the device`.
- Do not skip CUDA compat checks. Missing `cuda-compat-13-1` or missing compat library paths can make CUDA look installed but unusable.
- Do not ignore stray multiprocess workers. A leftover `mpi4py.futures.server` can hold tens of gigabytes of VRAM and cause false OOM diagnoses on the next startup.

## Alignment

### Reusable经验

- Align the client contract first:
  - endpoint path
  - request shape
  - response schema
  - `text` and `finish_reason` fields
  - preprocessing and postprocessing hooks
- Reuse the online `prompt_render` or equivalent request-wrapper logic when possible. This usually produces better parity than rewriting logic from scratch.
- Validate alignment in layers:
  - service is healthy
  - smoke requests pass
  - full-set requests pass
  - schema matches
  - content agreement is measured separately
- Keep exact-match scoring rules explicit. For example:
  - text equality after whitespace normalization
  - bbox equality by parsed structure plus ordering
- If content parity is incomplete but the contract is correct, ship the compatibility layer first and investigate mismatch buckets after.

### 已踩过的坑

- Do not mix up structure alignment with content alignment. Matching schema does not mean matching responses.
- Do not chase full backend parity before confirming what the client actually consumes.
- Do not replace a working service-layer alignment path with deep runtime patching unless the interface contract still misses required behavior.

## Backend Bring-Up

### Reusable经验

- Validate the backend with the smallest possible probe before server integration.
- Use a real script file for multiprocessing or MPI-backed probes.
- Guard probes with `if __name__ == '__main__'` whenever workers can import the file.
- Treat "engine build/load succeeds" and "`LLM init` succeeds" as intermediate milestones only. Always test the first real inference call.
- When a model family is partly supported, separate these states explicitly:
  - architecture recognized
  - engine builds
  - runtime loads
  - first generate succeeds

### 已踩过的坑

- Do not run complex multiprocessing experiments from stdin. The project hit worker failures because MPI-style workers could not resolve `<stdin>`.
- Do not assume a built engine means the runtime request path is complete. The Qwen2.5-VL line still failed on first `generate()` because runtime mRoPE inputs were not truly injected.
- Do not keep long-term patches only in `site-packages`. Promote them to repo-managed patches or move to a matching official environment.
- Do not rely on docs from a newer backend release while staying on an older runtime without calling out the version gap.

## Performance

### Reusable经验

- If concurrency rises but throughput stays flat, inspect the service concurrency model first.
- Prefer a queue plus micro-batch worker over serial one-request-one-generate execution.
- Batch only requests with compatible sampling parameters to avoid semantic drift inside a batch.
- Benchmark with production-like concurrency and duration, not only smoke requests.
- Track throughput with latency together:
  - QPS
  - avg/p95/p99 latency
  - output tokens per second
  - queue wait
  - batch execution time
  - power when relevant
- Expect parameter knees. Increasing `max_batch_size` or `max_num_batched_tokens` beyond a point can reduce both throughput and power efficiency.
- After service-side batching works, inspect higher-order knobs such as micro-batch wait time, concurrency tiers, and GPU utilization counters.

### 已踩过的坑

- Do not blame the model too early when QPS does not scale. In this project, service-side serialization was the main bottleneck.
- Do not optimize with only one metric. A higher power draw without throughput gain is not a real win.
- Do not assume bigger batch settings always help. The project found throughput and power both flattening or falling after a threshold.

## Metrics

### Reusable经验

- Verify the observation path before trusting TTFT or TPOT.
- Confirm whether the service really emits token-by-token streaming, not just a single final chunk under a `stream=true` request.
- Prefer backend-native metrics or service-side parsed metrics when available.
- Expose a resettable metrics endpoint when iterating on repeated benchmarks.
- Separate client-observed end-to-end latency from model-internal TTFT and TPOT.

### 已踩过的坑

- Do not infer TPOT from client timestamps if the service sends only one text chunk. That produces fake near-zero TPOT values.
- Do not forget warmup or probe requests when reconciling counts in a measurement window.

## Handoff

### Reusable经验

- End each phase with a concise handoff:
  - background and goal
  - what changed
  - current healthy state
  - key commands
  - known risks
  - next recommended experiments
- Include cleanup commands for both the service process and hidden worker processes.
- Record the current best-known parameters and the result artifact paths.
- State whether remaining work is "content consistency", "runtime support gap", or "performance headroom" so the next operator does not restart the wrong investigation.

### 已踩过的坑

- Do not write a handoff that only says what changed. The next operator also needs what is healthy now and how to reproduce it.
- Do not leave benchmark scripts and outputs undocumented even if they live under `/tmp`; they are often the fastest route back to a known-good test path.
