# Ray Orchestrator (Prototype) — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/features/ray-orchestrator.html

Ray Orchestrator (Prototype)#

Note

This project is under active development and currently in a prototype stage. The current focus is on core functionality, with performance optimization coming soon. While we strive for correctness, there are currently no guarantees regarding functionality, stability, or reliability.

Motivation#

The Ray orchestrator uses Ray instead of MPI to manage workers for single- and multi-node inference. It’s a first step toward making TensorRT-LLM a better fit for Reinforcement Learning from Human Feedback (RLHF) workflows. For RLHF, Ray can dynamically spawn and reconnect distributed inference actors, each with its own parallelism strategy. This feature is a prototype and under active development. MPI remains the default in TensorRT-LLM.

Basic Usage#

To use Ray orchestrator, you need to first install Ray.

```text
cd examples/ray_orchestrator
pip install -r requirements.txt
```

To run a simple `TP=2` example with a Hugging Face model:

```text
python llm_inference_distributed_ray.py
```

This example is the same as in `/examples/llm-api`, with the only change being `orchestrator_type="ray"` on `LLM()`. Other examples can be adapted similarly by toggling this flag.

Features#

Currently available:

Generate text asynchronously (refer to llm_inference_async_ray.py)

Multi-node inference (refer to multi-node README)

Disaggregated serving (refer to disagg README)

Initial testing has been focused on LLaMA and DeepSeek variants. Please open an Issue if you encounter problems with other models so we can prioritize support.

Roadmap#

Performance optimization

Integration with RLHF frameworks, such as Verl and NVIDIA NeMo-RL.

Architecture#

This feature introduces new classes such as RayExecutor and RayGPUWorker for Ray actor lifecycle management and distributed inference. In Ray mode, collective ops run on torch.distributed without MPI. We welcome contributions to improve and extend this support.
