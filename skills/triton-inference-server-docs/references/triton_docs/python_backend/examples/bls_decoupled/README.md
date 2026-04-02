* Example of...

# Example of using BLS with decoupled models[#](#example-of-using-bls-with-decoupled-models "Link to this heading")

In this section we demonstrate an end-to-end example for
[BLS](../../README.md#business-logic-scripting) in Python backend. The
[model repository](../../../user_guide/model_repository.md)
should contain [square](https://github.com/triton-inference-server/python_backend/blob/main/examples/decoupled) model. The [square](https://github.com/triton-inference-server/python_backend/blob/main/examples/decoupled) model
will send ânâ responses where ânâ is the value of input `IN`. For each response,
output `OUT` will equal the value of `IN`. This example is broken into two
sections. The first section demonstrates how to perform synchronous BLS requests
and the second section shows how to execute asynchronous BLS requests.

## Synchronous BLS Requests with Decoupled Models[#](#synchronous-bls-requests-with-decoupled-models "Link to this heading")

The goal of `bls_decoupled_sync` model is to calculate the sum of the responses
returned from the [square](https://github.com/triton-inference-server/python_backend/blob/main/examples/decoupled) model and return the summation as the final response. The value of input âINâ will be passed as an input to the
[square](https://github.com/triton-inference-server/python_backend/blob/main/examples/decoupled) model which determines how many responses the
[square](https://github.com/triton-inference-server/python_backend/blob/main/examples/decoupled) model will generate.

1. Create the model repository:

```
mkdir -p models/bls_decoupled_sync/1
mkdir -p models/square_int32/1

# Copy the Python models
cp examples/bls_decoupled/sync_model.py models/bls_decoupled_sync/1/model.py
cp examples/bls_decoupled/sync_config.pbtxt models/bls_decoupled_sync/config.pbtxt
cp examples/decoupled/square_model.py models/square_int32/1/model.py
cp examples/decoupled/square_config.pbtxt models/square_int32/config.pbtxt
```

2. Start the tritonserver:

```
tritonserver --model-repository `pwd`/models
```

3. Send inference requests to server:

```
python3 examples/bls_decoupled/sync_client.py
```

You should see an output similar to the output below:

```
==========model result==========
The square value of [4] is [16]

==========model result==========
The square value of [2] is [4]

==========model result==========
The square value of [0] is [0]

==========model result==========
The square value of [1] is [1]

PASS: BLS Decoupled Sync
```

The [sync\_model.py](https://github.com/triton-inference-server/python_backend/blob/main/examples/bls_decoupled/sync_model.py) model file is heavily commented with
explanations about each of the function calls.

### Explanation of the Client Output[#](#explanation-of-the-client-output "Link to this heading")

The [client.py](https://github.com/triton-inference-server/python_backend/blob/main/examples/bls_decoupled/sync_client.py) sends 4 inference requests to the
`bls_decoupled_sync` model with the input as: [4], [2], [0] and [1]
respectively. In compliance with the behavior of the sync BLS model,
it will expect the output to be the square value of the input.

## Asynchronous BLS Requests with Decoupled Models[#](#asynchronous-bls-requests-with-decoupled-models "Link to this heading")

In this section we explain how to send multiple BLS requests without waiting for
their response. Asynchronous execution of BLS requests will not block your
model execution and can lead to speedups under certain conditions.

The `bls_decoupled_async` model will perform two async BLS requests on the
[square](https://github.com/triton-inference-server/python_backend/blob/main/examples/decoupled) model. Then, it will wait until the inference requests
are completed. It will calculate the sum of the output `OUT` from the
[square](https://github.com/triton-inference-server/python_backend/blob/main/examples/decoupled) model in both two requests to construct the final
inference response object using these tensors.

1. Create the model repository:

```
mkdir -p models/bls_decoupled_async/1
mkdir -p models/square_int32/1

# Copy the Python models
cp examples/bls_decoupled/async_model.py models/bls_decoupled_async/1/model.py
cp examples/bls_decoupled/async_config.pbtxt models/bls_decoupled_async/config.pbtxt
cp examples/decoupled/square_model.py models/square_int32/1/model.py
cp examples/decoupled/square_config.pbtxt models/square_int32/config.pbtxt
```

2. Start the tritonserver:

```
tritonserver --model-repository `pwd`/models
```

3. Send inference requests to server:

```
python3 examples/bls_decoupled/async_client.py
```

You should see an output similar to the output below:

```
==========model result==========
Two times the square value of [4] is [32]

==========model result==========
Two times the square value of [2] is [8]

==========model result==========
Two times the square value of [0] is [0]

==========model result==========
Two times the square value of [1] is [2]

PASS: BLS Decoupled Async
```

The [async\_model.py](https://github.com/triton-inference-server/python_backend/blob/main/examples/bls_decoupled/async_model.py) model file is heavily commented with
explanations about each of the function calls.

### Explanation of the Client Output[#](#id1 "Link to this heading")

The [client.py](https://github.com/triton-inference-server/python_backend/blob/main/examples/bls_decoupled/async_client.py) sends 4 inference requests to the
âbls\_decoupled\_syncâ model with the input as: [4], [2], [0] and [1]
respectively. In compliance with the behavior of sync BLS model model,
it will expect the output to be two time the square value of the input.

