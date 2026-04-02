* Speculative Decoding

# Speculative Decoding[#](#speculative-decoding "Link to this heading")

## About Speculative Decoding[#](#about-speculative-decoding "Link to this heading")

Speculative Decoding (also referred to as Speculative Sampling) is a set of techniques designed
to allow generation of more than one token per forward pass iteration. This can lead to a reduction
in the average per-token latency in situations where the GPU is underutilized due to small batch sizes.

Speculative decoding involves predicting a sequence of future tokens, referred to as draft tokens,
using a method that is substantially more efficient than repeatedly executing the target Large Language
Model (LLM). These draft tokens are then collectively validated by processing them through the target LLM
in a single forward pass. The underlying assumptions are twofold:

1. processing multiple draft tokens concurrently will be as rapid as processing a single token
2. multiple draft tokens will be validated successfully over the course of the full generation

If the first assumption holds true, the latency of speculative decoding will no worse than the standard
approach. If the second holds, output token generation advances by statistically more than one token per
forward pass. The combination of both these allows speculative decoding to result in reduced latency.

## Performance Improvements[#](#performance-improvements "Link to this heading")

Itâs important to note that the effectiveness of speculative decoding techniques is highly dependent
on the specific task at hand. For instance, forecasting subsequent tokens in a code-completion scenario
may prove simpler than generating a summary for an article. [Spec-Bench](https://sites.google.com/view/spec-bench)
shows the performance of different speculative decoding approaches on different tasks.

