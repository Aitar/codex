* Model...

# Model Explainability with Shapley Values[#](#model-explainability-with-shapley-values "Link to this heading")

**NOTE: The CPU version of this feature is in an experimental state as of version 23.04**

In addition to providing model output from forest models, the FIL backend
can help you understand *why* the model came to a particular conclusion by
providing Shapley values. Shapley values offer a measure of the extent to
which individual features in an input contributed to the final model output.
Features with high Shapley value scores can generally be understood to be more
important to the modelâs conclusion than those with lower scores.

Generally speaking, Shapley values are computed by computing the model output
with and without a particular feature input and looking at how much the output
changed. This is referred to as the marginal contribution of that
feature. For a more complete understanding, check out the [Wikipedia
article](https://en.wikipedia.org/wiki/Shapley_value) on Shapley values or
Lloyd Shapleyâs [original
paper](https://www.rand.org/content/dam/rand/pubs/research_memoranda/2008/RM670.pdf).

**NOTE: Tree depth is limited to 32 for shapley value computation. Tree models with higher depth will throw an error.**

## Using Shapley Values in the FIL Backend[#](#using-shapley-values-in-the-fil-backend "Link to this heading")

Because it takes additional time to compute and return the relatively large
output arrays for Shapley values, Shapley value computation is turned off by
default in the FIL backend.

To turn on Shapley Value support, you must add an additional output to the
`config.pbtxt` file for your model as shown below:

```
output [
 {
    name: "output__0"
    data_type: TYPE_FP32
    dims: [ 2 ]
  },
 {
    name: "treeshap_output"
    data_type: TYPE_FP32
    dims: [ 501 ]
  }
]
backend: "fil"
max_batch_size: 32768
input [
 {
    name: "input__0"
    data_type: TYPE_FP32
    dims: [ $NUM_FEATURES ]
  }
]
output [
 {
    name: "output__0"
    data_type: TYPE_FP32
    dims: [ 1 ]
 },
 {
    name: "treeshap_output"
    data_type: TYPE_FP32
    dims: [ $NUM_FEATURES_PLUS_ONE ]
  }
]
instance_group [{ kind: KIND_AUTO }]
parameters [
  {
    key: "model_type"
    value: { string_value: "$MODEL_TYPE" }
  },
  {
    key: "is_classifier"
    value: { string_value: "$IS_A_CLASSIFIER" }
  }
]

dynamic_batching {}
```

Note that the length of the `treeshap_output` is equal to the number of input
features plus one to account for the bias term in the Shapley output. For a
working example of model deployment with Shapley values, including how to
retrieve those values using Tritonâs Python client, check out the [FAQ
Notebook](https://nbviewer.org/github/triton-inference-server/fil_backend/blob/main/notebooks/faq/FAQs.ipynb#$%5Ccolor%7B#76b900%7D%7B%5Ctext%7BFAQ-12:-How-do-I-retrieve-Shapley-values-for-model-explainability?%7D%7D$)

