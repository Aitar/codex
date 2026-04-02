* Auto-Complet...

# Auto-Complete Example[#](#auto-complete-example "Link to this heading")

This example shows how to implement
[`auto_complete_config`](../../README.md#auto-complete-config)
function in Python backend to provide
[`max_batch_size`](../../../user_guide/model_configuration.md#maximum-batch-size),
[`input`](../../../user_guide/model_configuration.md#inputs-and-outputs)
and [`output`](../../../user_guide/model_configuration.md#inputs-and-outputs)
properties. These properties will allow Triton to load the Python model with
[Minimal Model Configuration](../../../user_guide/model_configuration.md#minimal-model-configuration)
in absence of a configuration file.

The
[model repository](../../../user_guide/model_repository.md)
should contain [nobatch\_auto\_complete](https://github.com/triton-inference-server/python_backend/blob/main/examples/auto_complete/nobatch_model.py), and
[batch\_auto\_complete](https://github.com/triton-inference-server/python_backend/blob/main/examples/auto_complete/batch_model.py) models.
The max\_batch\_size of [nobatch\_auto\_complete](https://github.com/triton-inference-server/python_backend/blob/main/examples/auto_complete/nobatch_model.py) model is set
to zero, whereas the max\_batch\_size of [batch\_auto\_complete](https://github.com/triton-inference-server/python_backend/blob/main/examples/auto_complete/batch_model.py)
model is set to 4. For models with a non-zero value of max\_batch\_size, the
configuration can specify a different value of max\_batch\_size as long as it
does not exceed the value set in the model file.

The
[nobatch\_auto\_complete](https://github.com/triton-inference-server/python_backend/blob/main/examples/auto_complete/nobatch_model.py) and
[batch\_auto\_complete](https://github.com/triton-inference-server/python_backend/blob/main/examples/auto_complete/batch_model.py) models calculate the sum and difference
of the `INPUT0` and `INPUT1` and put the results in `OUTPUT0` and `OUTPUT1`
respectively.

## Deploying the Auto-Complete Models[#](#deploying-the-auto-complete-models "Link to this heading")

1. Create the model repository:

```
mkdir -p models/nobatch_auto_complete/1/
mkdir -p models/batch_auto_complete/1/

# Copy the Python models
cp examples/auto_complete/nobatch_model.py models/nobatch_auto_complete/1/model.py
cp examples/auto_complete/batch_model.py models/batch_auto_complete/1/model.py
```

**Note that we donât need a model configuration file since Triton will use the
auto-complete model configuration provided in the Python model.**

2. Start the tritonserver:

```
tritonserver --model-repository `pwd`/models
```

## Running inferences on Nobatch and Batch models:[#](#running-inferences-on-nobatch-and-batch-models "Link to this heading")

Send inference requests using [client.py](https://github.com/triton-inference-server/python_backend/blob/main/examples/auto_complete/client.py).

```
python3 examples/auto_complete/client.py
```

You should see an output similar to the output below:

```
'nobatch_auto_complete' configuration matches the expected auto complete configuration

'batch_auto_complete' configuration matches the expected auto complete configuration

PASS: auto_complete
```

The [nobatch\_model.py](https://github.com/triton-inference-server/python_backend/blob/main/examples/auto_complete/nobatch_model.py) and [batch\_model.py](https://github.com/triton-inference-server/python_backend/blob/main/examples/auto_complete/batch_model.py)
model files are heavily commented with explanations about how to utilize
`set_max_batch_size`, `add_input`, and `add_output`functions to set
`max_batch_size`, `input` and `output` properties of the model.

### Explanation of the Client Output[#](#explanation-of-the-client-output "Link to this heading")

For each model, the [client.py](https://github.com/triton-inference-server/python_backend/blob/main/examples/auto_complete/client.py) first requests the model
configuration from Triton to validate if the model configuration has been
registered as expected. The client then sends an inference request to verify
whether the inference has run properly and the result is correct.

