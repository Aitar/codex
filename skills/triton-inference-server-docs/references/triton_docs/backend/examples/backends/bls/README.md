* *BLS*...

# *BLS* Triton Backend[#](#bls-triton-backend "Link to this heading")

The [*BLS*](https://github.com/triton-inference-server/backend/blob/main/examples/backends/bls) backend demonstrates using in-process C-API to
execute inferences within the backend. This backend serves as an example to
backend developers for implementing their own custom pipeline in C++.
For Python use cases, please refer to
[Business Logic Scripting](../../../../python_backend/README.md#business-logic-scripting)
section in Python backend.

The source code for the *bls* backend is contained in
[src](https://github.com/triton-inference-server/backend/blob/main/examples/backends/bls/src).

* [backend.cc](https://github.com/triton-inference-server/backend/blob/main/examples/backends/bls/src/backend.cc) contains the main backend
  implementation. The content of this file is not BLS specific. It only includes
  the required Triton backend functions that is standard for any backend
  implementation. The BLS logic is set off in the
  `TRITONBACKEND_ModelInstanceExecute` with lines `bls_executor.Execute(requests[r], &responses[r]);`.
* [bls.h](https://github.com/triton-inference-server/backend/blob/main/examples/backends/bls/src/bls.h) is where the BLS (class `BLSExecutor`) of
  this example is located. You can refer to this file to see how to interact with
  Triton in-process C-API to build the custom execution pipeline.
* [bls\_utils.h](https://github.com/triton-inference-server/backend/blob/main/examples/backends/bls/src/bls_utils.h) is where all the utilities that
  are not BLS dependent are located.

The source code contains extensive documentation describing the operation of
the backend and the use of the
[Triton Backend API](../../../README.md#triton-backend-api) and the
[Triton Server API](../../../../customization_guide/inference_protocols.md#in-process-triton-server-api).
Before reading the source code, make sure you understand
the concepts associated with Triton backend abstractions
[TRITONBACKEND\_Backend](../../../README.md#tritonbackend-backend),
[TRITONBACKEND\_Model](../../../README.md#tritonbackend-model), and
[TRITONBACKEND\_ModelInstance](../../../README.md#tritonbackend-modelinstance).

The *bls* backend will send two requests on the âaddsub\_pythonâ and âaddsub\_onnxâ
models. After the inference requests are completed, this backend will extract
OUTPUT0 from the âaddsub\_pythonâ and OUTPUT1 from the âaddsub\_onnxâ model to
construct the final inference response object using these tensors.

There are some self-imposed limitations that were made for the simplicity of
this example:

1. This backend does not support batching.
2. This backend does not support decoupled models.
3. This backend does not support GPU tensors.
4. The model configuration should be strictly set as the comments described in
   [backend.cc](https://github.com/triton-inference-server/backend/blob/main/examples/backends/bls/src/backend.cc).

You can implement your custom backend that is not limited to the limitations
mentioned above.

## Building the *BLS* Backend[#](#building-the-bls-backend "Link to this heading")

[backends/bls/CMakeLists.txt](https://github.com/triton-inference-server/backend/blob/main/examples/backends/bls/CMakeLists.txt)
shows the recommended build and install script for a Triton
backend. Building and installing is the same as described in [Building
the *Minimal* Backend](../../README.md#building-the-minimal-backend).

## Running Triton with the *BLS* Backend[#](#running-triton-with-the-bls-backend "Link to this heading")

After adding the *bls* backend to the Triton server as
described in [Backend Shared
Library](../../../README.md#backend-shared-library), you can run Triton and
have it load the models in
[model\_repos/bls\_models](https://github.com/triton-inference-server/backend/blob/main/examples/model_repos/bls_models). Assuming you have created a
*tritonserver* Docker image by adding the *bls* backend to Triton, the
following command will run Triton:

```
$ docker run --rm -it --net=host -v/path/to/model_repos/bls_models:/models tritonserver --model-repository=/models
```

The console output will show similar to the following indicating that
the *bls\_fp32*, *addsub\_python* and *addsub\_onnx* models from the bls\_models repository have
loaded correctly.

```
I0616 09:34:47.767433 19214 server.cc:629]
+---------------+---------+--------+
| Model         | Version | Status |
+---------------+---------+--------+
| addsub_python | 1       | READY  |
| addsub_onnx     | 1       | READY  |
| bls_fp32      | 1       | READY  |
+---------------+---------+--------+
```

## Testing the *BLS* Backend[#](#testing-the-bls-backend "Link to this heading")

The [clients](https://github.com/triton-inference-server/backend/blob/main/examples/clients) directory holds example clients. The
[bls\_client](https://github.com/triton-inference-server/backend/blob/main/examples/clients/bls_client) Python script demonstrates sending an
inference requests to the *bls* backend. With Triton running as
described in [Running Triton with the *BLS* Backend](#running-triton-with-the-bls-backend),
execute the client:

```
$ clients/bls_client
```

You should see an output similar to the output below:

```
INPUT0 ([0.42935285 0.51512766 0.43625894 ... 0.6670954  0.17747518 0.7976901 ]) + INPUT1 ([6.7752063e-01 2.4223252e-01 6.7743927e-01 ... 4.1531715e-01 2.5451833e-01 7.9097062e-01]) = OUTPUT0 ([1.1068735  0.75736016 1.1136982 ... 1.0824126  0.4319935  1.5886607 ])
INPUT0 ([0.42935285 0.51512766 0.43625894 ... 0.6670954  0.17747518 0.7976901 ]) - INPUT1 ([6.7752063e-01 2.4223252e-01 6.7743927e-01 ... 4.1531715e-01 2.5451833e-01 7.9097062e-01]) = OUTPUT1 ([-0.24816778  0.27289516 -0.24118033 ... 0.25177827 -0.07704315  0.00671947])

PASS
```

