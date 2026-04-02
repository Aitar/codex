Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/features/overlap-scheduler.md

* Overlap Scheduler

# Overlap Scheduler[#](#overlap-scheduler "Link to this heading")

To maximize GPU utilization, the scheduler overlaps CPU tasks (e.g., checking sampling stop criteria, updating responses, scheduling the next batch) with GPU computation.

## How It Works[#](#how-it-works "Link to this heading")

At step *n*, the system launches GPU computation for step *n+1* without waiting for CPU tasks (e.g., stop criteria checks) from step *n* to complete. This allows:

* CPU work (step *n*) and GPU computation (step *n+1*) to run concurrently.
* Better GPU occupancy by reducing idle time.

This concurrent execution pipeline is illustrated in the `PyExecutor`’s logic:

```
# Schedule and launch GPU work for the current step (n)
scheduled_batch, _, _ = self._schedule()
batch_outputs = self._forward_step(scheduled_batch, previous_tensors_device)
sample_state = self._sample_async(scheduled_batch, batch_outputs)

# While the GPU is busy, process the CPU-bound results from the previous step (n-1)
if self.previous_batch is not None:
    self._process_previous_batch()
```

## Tradeoff[#](#tradeoff "Link to this heading")

The optimization introduces one extra decoding step but significantly improves throughput.

## Usage[#](#usage "Link to this heading")

Enabled by default. To disable, set `disable_overlap_scheduler=True` in the configuration.

## References[#](#references "Link to this heading")

* [NanoFlow: Towards Optimal Large Language Model Serving Throughput](https://arxiv.org/abs/2408.12757)
* https://lmsys.org/blog/2024-12-04-sglang-v0-4/#zero-overhead-batch-scheduler

[previous

Multimodal Support in TensorRT LLM](multi-modality.md "previous page")
[next

Paged Attention, IFB, and Request Scheduling](paged-attention-ifb-scheduler.md "next page")

On this page

* [How It Works](#how-it-works)
* [Tradeoff](#tradeoff)
* [Usage](#usage)
* [References](#references)