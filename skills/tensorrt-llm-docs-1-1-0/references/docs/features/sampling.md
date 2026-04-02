Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/features/sampling.md

* Sampling

# Sampling[#](#sampling "Link to this heading")

The PyTorch backend supports most of the sampling features that are supported on the C++ backend, such as temperature, top-k and top-p sampling, beam search, stop words, bad words, penalty, context and generation logits, log probability and logits processors

## General usage[#](#general-usage "Link to this heading")

To use the feature:

1. Enable the `enable_trtllm_sampler` option in the `LLM` class
2. Pass a [`SamplingParams`](https://github.com/NVIDIA/TensorRT-LLM/tree/48b7b5d/tensorrt_llm/sampling_params.py) object with the desired options to the `generate()` function

The following example prepares two identical prompts which will give different results due to the sampling parameters chosen:

```
from tensorrt_llm import LLM, SamplingParams
llm = LLM(model='nvidia/Llama-3.1-8B-Instruct-FP8',
          enable_trtllm_sampler=True)
sampling_params = SamplingParams(
        temperature=1.0,
        top_k=8,
        top_p=0.5,
    )
llm.generate(["Hello, my name is",
            "Hello, my name is"], sampling_params)
```

Note: The `enable_trtllm_sampler` option is not currently supported when using speculative decoders, such as MTP or Eagle-3, so there is a smaller subset of sampling options available.

## Beam search[#](#beam-search "Link to this heading")

Beam search is a decoding strategy that maintains multiple candidate sequences (beams) during text generation, exploring different possible continuations to find higher quality outputs. Unlike greedy decoding or sampling, beam search considers multiple hypotheses simultaneously.

To enable beam search, you must:

1. Enable the `use_beam_search` option in the `SamplingParams` object
2. Set the `max_beam_width` parameter in the `LLM` class to match the `best_of` parameter in `SamplingParams`
3. Disable overlap scheduling using the `disable_overlap_scheduler` parameter of the `LLM` class
4. Disable the usage of CUDA Graphs by passing `None` to the `cuda_graph_config` parameter of the `LLM` class

Parameter Configuration:

* `best_of`: Controls the number of beams processed during generation (beam width)
* `n`: Controls the number of output sequences returned (can be less than `best_of`)
* If `best_of` is omitted, the number of beams processed defaults to `n`
* `max_beam_width` in the `LLM` class must equal `best_of` in `SamplingParams`

The following example demonstrates beam search with a beam width of 4, returning the top 3 sequences:

```
from tensorrt_llm import LLM, SamplingParams
llm = LLM(model='nvidia/Llama-3.1-8B-Instruct-FP8',
          enable_trtllm_sampler=True,
          max_beam_width=4,   # must equal SamplingParams.best_of
          disable_overlap_scheduler=True,
          cuda_graph_config=None)
sampling_params = SamplingParams(
        best_of=4,   # must equal LLM.max_beam_width
        use_beam_search=True,
        n=3,         # return top 3 sequences
    )
llm.generate(["Hello, my name is",
            "Hello, my name is"], sampling_params)
```

## Logits processor[#](#logits-processor "Link to this heading")

Logits processors allow you to modify the logits produced by the network before sampling, enabling custom generation behavior and constraints.

To use a custom logits processor:

1. Create a custom class that inherits from [`LogitsProcessor`](https://github.com/NVIDIA/TensorRT-LLM/tree/48b7b5d/tensorrt_llm/sampling_params.py) and implements the `__call__` method
2. Pass an instance of this class to the `logits_processor` parameter of `SamplingParams`

The following example demonstrates logits processing:

```
import torch
from typing import List, Optional

from tensorrt_llm import LLM, SamplingParams
from tensorrt_llm.sampling_params import LogitsProcessor

class MyCustomLogitsProcessor(LogitsProcessor):
    def __call__(self,
        req_id: int,
        logits: torch.Tensor,
        token_ids: List[List[int]],
        stream_ptr: Optional[int],
        client_id: Optional[int]
    ) -> None:
        # Implement your custom inplace logits processing logic
        logits *= logits

llm = LLM(model='nvidia/Llama-3.1-8B-Instruct-FP8')
sampling_params = SamplingParams(
        logits_processor=MyCustomLogitsProcessor()
    )
llm.generate(["Hello, my name is"], sampling_params)
```

You can find a more detailed example on logits processors [here](https://github.com/NVIDIA/TensorRT-LLM/tree/48b7b5d/examples/llm-api/llm_logits_processor.py).