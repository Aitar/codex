* DALI model...

# DALI model configuration file[#](#dali-model-configuration-file "Link to this heading")

## Model parameters[#](#model-parameters "Link to this heading")

### `num_threads`[#](#num-threads "Link to this heading")

This parameter is used to control the number of CPU threads used by the DALI pipeline. Itâs equivalent to setting the `num_threads` parameter in the pipeline definition.

Example use:

```
parameters: [
  {
    key: "num_threads"
    value: { string_value: "4" }
  }
]
```

### `split_along_outer_axis`[#](#split-along-outer-axis "Link to this heading")

This parameters is used to split samples produced by a DALI pipeline removing their outer dimension.
Example use:

```
parameters [
  {
    key: "split_along_outer_axis",
    value: { string_value: "OUTPUT1:OUTPUT2" }
  }
]
```

The value of the this parameter is a colon-separated list of output names that will be transformed.

Effect of the parameter can be described as follows. Letâs assume that DALI pipeline produced a batch of *N* *D+1*-dimensional tensors of following shapes:

\[\lbrace (n\_1, d\_1, ... d\_D), ... (n\_N, d\_1, ... d\_D)\rbrace\]

With the parameter set for this output, the batch produced by the model will uniformly shaped *D*-dimensional samples, with batch-size equal to:

\[\sum\_{i=1}^N n\_i\]

with each sample having a shape of:

\[(d\_1, ... d\_D)\]

The option can be used to split batch of sequences into a batch of images or sub-sequences.

## Backend parameters[#](#backend-parameters "Link to this heading")

### `release_after_unload`[#](#release-after-unload "Link to this heading")

One of the most expensive actions DALI takes while processing is the GPU memory allocation. DALIâs
memory ownership model assumes that the memory which is once allocated will be reused throughout
the lifetime of the process. In other words, when DALI has allocated the memory, it is not released even
after the DALI Pipeline object gets deleted. The release of the memory happens at the process quit [^1].

This property entails that when using Triton, the GPU memory allocated by DALI is not freed, even
after unloading the DALI model. However, should you like to free the GPU memory when DALI model is
unloaded, please pass `release_after_unload` option to `tritonserver` invocation:

```
tritonserver --model-repository /models --log-verbose 1 --backend-config=dali,release_after_unload=true
```

[^1] For more information, refer to [DALIâs documentation](https://docs.nvidia.com/deeplearning/dali/main-user-guide/docs/advanced_topics_performance_tuning.md#freeing-memory-pools)

