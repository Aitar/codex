* BLS Example

# BLS Example[#](#bls-example "Link to this heading")

In this section we demonstrate an end-to-end example for
[BLS](../../README.md#business-logic-scripting) in Python backend. The
[model repository](../../../user_guide/model_repository.md)
should contain [pytorch](https://github.com/triton-inference-server/python_backend/blob/main/examples/pytorch), [addsub](https://github.com/triton-inference-server/python_backend/blob/main/examples/add_sub). The
[pytorch](https://github.com/triton-inference-server/python_backend/blob/main/examples/pytorch) and [addsub](https://github.com/triton-inference-server/python_backend/blob/main/examples/add_sub) models calculate the sum and
difference of the `INPUT0` and `INPUT1` and put the results in `OUTPUT0` and
`OUTPUT1` respectively. This example is broken into two sections. The first
section demonstrates how to perform synchronous BLS requests and the second
section shows how to execute asynchronous BLS requests.

## Synchronous BLS Requests[#](#synchronous-bls-requests "Link to this heading")

The goal of sync BLS model is the same as [pytorch](https://github.com/triton-inference-server/python_backend/blob/main/examples/pytorch) and
[addsub](https://github.com/triton-inference-server/python_backend/blob/main/examples/add_sub) models but the difference is that the BLS model will not
calculate the sum and difference by itself. The sync BLS model will pass the
input tensors to the [pytorch](https://github.com/triton-inference-server/python_backend/blob/main/examples/pytorch) or [addsub](https://github.com/triton-inference-server/python_backend/blob/main/examples/add_sub) models and
return the responses of that model as the final response. The additional
parameter `MODEL_NAME` determines which model will be used for calculating the
final outputs.

1. Create the model repository:

```
mkdir -p models/add_sub/1
mkdir -p models/bls_sync/1
mkdir -p models/pytorch/1

# Copy the Python models
cp examples/add_sub/model.py models/add_sub/1/
cp examples/add_sub/config.pbtxt models/add_sub/config.pbtxt
cp examples/bls/sync_model.py models/bls_sync/1/model.py
cp examples/bls/sync_config.pbtxt models/bls_sync/config.pbtxt
cp examples/pytorch/model.py models/pytorch/1/
cp examples/pytorch/config.pbtxt models/pytorch/
```

2. Start the tritonserver:

```
tritonserver --model-repository `pwd`/models
```

3. Send inference requests to server:

```
python3 examples/bls/sync_client.py
```

You should see an output similar to the output below:

```
=========='add_sub' model result==========
INPUT0 ([0.34984654 0.6808792  0.6509772  0.6211422 ]) + INPUT1 ([0.37917137 0.9080451  0.60789365 0.33425143]) = OUTPUT0 ([0.7290179 1.5889243 1.2588708 0.9553937])
INPUT0 ([0.34984654 0.6808792  0.6509772  0.6211422 ]) - INPUT1 ([0.37917137 0.9080451  0.60789365 0.33425143]) = OUTPUT1 ([-0.02932483 -0.22716594  0.04308355  0.28689077])


=========='pytorch' model result==========
INPUT0 ([0.34984654 0.6808792  0.6509772  0.6211422 ]) + INPUT1 ([0.37917137 0.9080451  0.60789365 0.33425143]) = OUTPUT0 ([0.7290179 1.5889243 1.2588708 0.9553937])
INPUT0 ([0.34984654 0.6808792  0.6509772  0.6211422 ]) - INPUT1 ([0.37917137 0.9080451  0.60789365 0.33425143]) = OUTPUT1 ([-0.02932483 -0.22716594  0.04308355  0.28689077])


=========='undefined' model result==========
Failed to process the request(s) for model instance 'bls_0', message: TritonModelException: Failed for execute the inference request. Model 'undefined_model' is not ready.

At:
  /tmp/python_backend/models/bls/1/model.py(110): execute
```

The [sync\_model.py](https://github.com/triton-inference-server/python_backend/blob/main/examples/bls/sync_model.py) model file is heavily commented with
explanations about each of the function calls.

### Explanation of the Client Output[#](#explanation-of-the-client-output "Link to this heading")

The [client.py](https://github.com/triton-inference-server/python_backend/blob/main/examples/bls/sync_client.py) sends three inference requests to the âbls\_syncâ
model with different values for the âMODEL\_NAMEâ input. As explained earlier,
âMODEL\_NAMEâ determines the model name that the âblsâ model will use for
calculating the final outputs. In the first request, it will use the âadd\_subâ
model and in the second request it will use the âpytorchâ model. The third
request uses an incorrect model name to demonstrate error handling during
the inference request execution.

## Asynchronous BLS Requests[#](#asynchronous-bls-requests "Link to this heading")

In this section we explain how to send multiple BLS requests without waiting for
their response. Asynchronous execution of BLS requests will not block your
model execution and can lead to speedups under certain conditions.

The `bls_async` model will perform two async BLS requests on the
[pytorch](https://github.com/triton-inference-server/python_backend/blob/main/examples/pytorch) and [addsub](https://github.com/triton-inference-server/python_backend/blob/main/examples/add_sub) models. Then, it will wait until
the inference requests on these models is completed. It will extract `OUTPUT0`
from the [pytorch](https://github.com/triton-inference-server/python_backend/blob/main/examples/pytorch) and `OUTPUT1` from the [addsub](https://github.com/triton-inference-server/python_backend/blob/main/examples/add_sub) model
to construct the final inference response object using these tensors.

1. Create the model repository:

```
mkdir -p models/add_sub/1
mkdir -p models/bls_async/1
mkdir -p models/pytorch/1

# Copy the Python models
cp examples/add_sub/model.py models/add_sub/1/
cp examples/add_sub/config.pbtxt models/add_sub/
cp examples/bls/async_model.py models/bls_async/1/model.py
cp examples/bls/async_config.pbtxt models/bls_async/config.pbtxt
cp examples/pytorch/model.py models/pytorch/1/
cp examples/pytorch/config.pbtxt models/pytorch/
```

2. Start the tritonserver:

```
tritonserver --model-repository `pwd`/models
```

3. Send inference requests to server:

```
python3 examples/bls/async_client.py
```

You should see an output similar to the output below:

```
INPUT0 ([0.72394824 0.45873794 0.4307444  0.07681174]) + INPUT1 ([0.34224355 0.8271524  0.5831284  0.904624  ]) = OUTPUT0 ([1.0661918 1.2858903 1.0138729 0.9814357])
INPUT0 ([0.72394824 0.45873794 0.4307444  0.07681174]) - INPUT1 ([0.34224355 0.8271524  0.5831284  0.904624  ]) = OUTPUT1 ([ 0.3817047  -0.36841443 -0.15238398 -0.82781225])
```

