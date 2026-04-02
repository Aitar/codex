* Model Analyzer

# Model Analyzer[#](#model-analyzer "Link to this heading")

The Triton [Model Analyzer](https://github.com/triton-inference-server/model_analyzer)
is a tool that uses
[Performance Analyzer](../perf_analyzer/README.md)
to send requests to your model while measuring GPU memory and compute
utilization. The Model Analyzer is specifically useful for characterizing the
GPU memory requirements for your model under different batching and model
instance configurations. Once you have this GPU memory usage information you can
more intelligently decide on how to combine multiple models on the same GPU
while remaining within the memory capacity of the GPU.

For more detailed examples and explanations of using Model Analyzer, see:

* [Model Analyzer Conceptual Guide](https://github.com/triton-inference-server/tutorials/tree/main/Conceptual_Guide/Part_3-optimizing_triton_configuration)
* [Maximizing Deep Learning
  Inference Performance with NVIDIA Model
  Analyzer](https://developer.nvidia.com/blog/maximizing-deep-learning-inference-performance-with-nvidia-model-analyzer)