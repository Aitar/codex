* [API Reference](../client_guide/api_reference.md)
* [Extensions](../client_guide/kserve_extension.md)
* Model...

# Model Configuration Extension[#](#model-configuration-extension "Link to this heading")

This document describes Tritonâs model configuration extension. The
model configuration extension allows Triton to return server-specific
information. Because this extension is supported, Triton reports
âmodel\_configurationâ in the extensions field of its Server Metadata.

## HTTP/REST[#](#http-rest "Link to this heading")

In all JSON schemas shown in this document `$number`, `$string`, `$boolean`,
`$object` and `$array` refer to the fundamental JSON types. #optional
indicates an optional JSON field.

Triton exposes the model configuration endpoint at the following
URL. The versions portion of the URL is optional; if not provided
Triton will return model configuration for the highest-numbered
version of the model.

```
GET v2/models/${MODEL_NAME}[/versions/${MODEL_VERSION}]/config
```

A model configuration request is made with an HTTP GET to the model
configuration endpoint.A successful model configuration request is
indicated by a 200 HTTP status code. The model configuration response
object, identified as `$model_configuration_response`, is returned in
the HTTP body for every successful request.

```
$model_configuration_response =
{
  # configuration JSON
}
```

The contents of the response will be the JSON representation of the
modelâs configuration described by the [ModelConfig message from
model\_config.proto](https://github.com/triton-inference-server/common/blob/main/protobuf/model_config.proto).

A failed model configuration request must be indicated by an HTTP
error status (typically 400). The HTTP body must contain the
`$model_configuration_error_response` object.

```
$model_configuration_error_response =
{
  "error": <error message string>
}
```

* âerrorâ : The descriptive message for the error.

## GRPC[#](#grpc "Link to this heading")

The GRPC definition of the service is:

```
service GRPCInferenceService
{
  â¦

  // Get model configuration.
  rpc ModelConfig(ModelConfigRequest) returns (ModelConfigResponse) {}
}
```

Errors are indicated by the google.rpc.Status returned for the
request. The OK code indicates success and other codes indicate
failure. The request and response messages for ModelConfig are:

```
message ModelConfigRequest
{
  // The name of the model.
  string name = 1;

  // The version of the model. If not given the version of the model
  // is selected automatically based on the version policy.
  string version = 2;
}

message ModelConfigResponse
{
  // The model configuration.
  ModelConfig config = 1;
}
```

Where the ModelConfig message is defined in
[model\_config.proto](https://github.com/triton-inference-server/common/blob/main/protobuf/model_config.proto).

