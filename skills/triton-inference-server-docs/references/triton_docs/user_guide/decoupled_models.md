* Decoupled...

# Decoupled Backends and Models[#](#decoupled-backends-and-models "Link to this heading")

Triton can support [backends](https://github.com/triton-inference-server/backend)
and models that send multiple responses for a request or zero responses
for a request. A decoupled model/backend may also send responses out-of-order
relative to the order that the request batches are executed. This allows
backend to deliver response whenever it deems fit. This is specifically
useful in Automated Speech Recognition (ASR). The requests with large number
of responses, will not block the responses from other requests from being
delivered.

## Developing Decoupled Backend/Model[#](#developing-decoupled-backend-model "Link to this heading")

### C++ Backend[#](#c-backend "Link to this heading")

Read carefully about the [Triton Backend API](../backend/README.md#triton-backend-api),
[Inference Requests and Responses](../backend/README.md#inference-requests-and-responses)
and [Decoupled Responses](../backend/README.md#decoupled-responses).
The [repeat backend](https://github.com/triton-inference-server/repeat_backend)
and [square backend](https://github.com/triton-inference-server/square_backend)
demonstrate how the Triton Backend API can be used to implement a decoupled
backend. The example is designed to show the flexibility of the Triton API
and in no way should be used in production. This example may process multiple
batches of requests at the same time without having to increase the
[instance count](model_configuration.md#instance-groups). In real deployment,
the backend should not allow the caller thread to return from
TRITONBACKEND\_ModelInstanceExecute until that instance is ready to
handle another set of requests. If not designed properly the backend
can be easily over-subscribed. This can also cause under-utilization
of features like [Dynamic Batching](model_configuration.md#dynamic-batcher)
as it leads to eager batching.

### Python model using Python Backend[#](#python-model-using-python-backend "Link to this heading")

Read carefully about the [Python Backend](https://github.com/triton-inference-server/python_backend),
and specifically [`execute`](../python_backend/README.md#execute).

The [decoupled examples](https://github.com/triton-inference-server/python_backend/tree/main/examples/decoupled)
demonstrates how decoupled API can be used to implement a decoupled
python model. As noted in the examples, these are designed to show
the flexibility of the decoupled API and in no way should be used
in production.

## Deploying Decoupled Models[#](#deploying-decoupled-models "Link to this heading")

The [decoupled model transaction policy](model_configuration.md#decoupled)
must be set in the provided [model configuration](model_configuration.md)
file for the model. Triton requires this information to enable special
handling required for decoupled models. Deploying decoupled models without
this configuration setting will throw errors at the runtime.

## Running Inference on Decoupled Models[#](#running-inference-on-decoupled-models "Link to this heading")

[Inference Protocols and APIs](../customization_guide/inference_protocols.md) describes various ways
a client can communicate and run inference on the server. For decoupled models,
Tritonâs HTTP endpoint cannot be used for running inference as it supports
exactly one response per request. Even standard ModelInfer RPC in the GRPC endpoint
does not support decoupled responses. In order to run inference on a decoupled
model, the client must use the bi-directional streaming RPC. See
[here](https://github.com/triton-inference-server/common/blob/main/protobuf/grpc_service.proto)
for more details. The [decoupled\_test.py](https://github.com/triton-inference-server/server/blob/main/qa/L0_decoupled/decoupled_test.py) demonstrates
how the gRPC streaming can be used to infer decoupled models.

If using [Tritonâs in-process C API](../customization_guide/inference_protocols.md#in-process-triton-server-api),
your application should be cognizant that the callback function you registered with
`TRITONSERVER_InferenceRequestSetResponseCallback` can be invoked any number of times,
each time with a new response. You can take a look at [grpc\_server.cc](https://github.com/triton-inference-server/server/blob/main/src/grpc/grpc_server.cc)

### Using Decoupled Models in Ensembles[#](#using-decoupled-models-in-ensembles "Link to this heading")

When using decoupled models within an [ensemble pipeline](ensemble_models.md), you may encounter unbounded memory growth if the decoupled model produces responses faster than downstream models can consume them.

To prevent unbounded memory growth in this scenario, consider using the `max_inflight_requests` configuration field. This field limits the maximum number of concurrent inflight requests permitted at each ensemble step for each inference request.

For more details and examples, see [Managing Memory Usage in Ensemble Models](ensemble_models.md#managing-memory-usage-in-ensemble-models).

## Knowing When a Decoupled Inference Request is Complete[#](#knowing-when-a-decoupled-inference-request-is-complete "Link to this heading")

An inference request is considered complete when a response containing the
`TRITONSERVER_RESPONSE_COMPLETE_FINAL` flag is received from a model/backend.

1. Client applications using streaming GRPC can access this information by
   checking the response parameters for the `"triton_final_response"` parameter.
   Decoupled models may not send a response for each request depending on how
   the model/backend is designed. In these cases where no response is sent by
   the backend, the streaming GRPC client can opt-in to receive an empty final
   response for each request. By default, empty final responses are not sent to
   save on network traffic.

   ```
   # Example of streaming GRPC client opting-in
   client.async_stream_infer(
     ...,
     enable_empty_final_response=True
   )
   ```
2. Client applications using the C API can check the
   `TRITONSERVER_RESPONSE_COMPLETE_FINAL` flag directly in their response
   handling / callback logic.

The [decoupled\_test.py](https://github.com/triton-inference-server/server/blob/main/qa/L0_decoupled/decoupled_test.py)
demonstrates an example of opting-in through the streaming GRPC
Python client API and programmatically identifying when a final response
is received through the `"triton_final_response"` response parameter.

