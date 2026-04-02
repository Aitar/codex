* Generate Extension

# Generate Extension[#](#generate-extension "Link to this heading")

> [!NOTE]
> The Generate Extension is *provisional* and likely to change in future versions.

This document describes Tritonâs generate extension. The generate
extension provides a simple text-oriented endpoint schema for interacting with
large language models (LLMs). The generate endpoint is specific to HTTP/REST
frontend.

## HTTP/REST[#](#http-rest "Link to this heading")

In all JSON schemas shown in this document, `$number`, `$string`, `$boolean`,
`$object` and `$array` refer to the fundamental JSON types. #optional
indicates an optional JSON field.

Triton exposes the generate endpoint at the following URLs. The client may use
HTTP POST request to different URLs for different response behavior, the
endpoint will return the generate results on success or an error in the case of
failure.

```
POST v2/models/${MODEL_NAME}[/versions/${MODEL_VERSION}]/generate

POST v2/models/${MODEL_NAME}[/versions/${MODEL_VERSION}]/generate_stream
```

### generate vs. generate\_stream[#](#generate-vs-generate-stream "Link to this heading")

Both URLs expect the same request JSON object, and generate the same JSON
response object. However, there are some differences in the format used to
return each:

* `/generate` returns exactly 1 response JSON object with a
  `Content-Type` of `application/json`
* `/generate_stream` may return multiple responses based on the inference
  results, with a `Content-Type` of `text/event-stream; charset=utf-8`.
  These responses will be sent as
  [Server-Sent Events](https://html.spec.whatwg.org/multipage/server-sent-events.md#server-sent-events)
  (SSE), where each response will be a âdataâ chunk in the HTTP
  response body. In the case of inference errors, responses will have
  an [error JSON object](#generate-response-json-error-object).

  + Note that the HTTP response code is set in the first response of the SSE,
    so if the first response succeeds but an error occurs in a subsequent
    response for the request, it can result in receiving an error object
    while the status code shows success (200). Therefore, the user must
    always check whether an error object is received when generating
    responses through `/generate_stream`.
  + If the request fails before inference begins, then a JSON error will
    be returned with `Content-Type` of `application/json`, similar to errors
    from other endpoints with the status code set to an error.

### Generate Request JSON Object[#](#generate-request-json-object "Link to this heading")

The generate request object, identified as *$generate\_request*, is
required in the HTTP body of the POST request. The model name and
(optionally) version must be available in the URL. If a version is not
provided, the server may choose a version based on its own policies or
return an error.

```
$generate_request =
{
  "id" : $string, #optional
  "text_input" : $string,
  "parameters" : $parameters #optional
}
```

* âidâ: An identifier for this request. Optional, but if specified this identifier must be returned in the response.
* âtext\_inputâ : The text input that the model should generate output from.
* âparametersâ : An optional object containing zero or more parameters for this
  generate request expressed as key/value pairs. See
  [Parameters](#parameters) for more information.

> [!NOTE]
> Any additional properties in the request object are passed either as
> parameters or tensors based on model specification.

#### Parameters[#](#parameters "Link to this heading")

The `$parameters` JSON describes zero or more ânameâ/âvalueâ pairs,
where the ânameâ is the name of the parameter and the âvalueâ is a
`$string`, `$number`, or `$boolean`.

```
$parameters =
{
  $parameter, ...
}

$parameter = $string : $string | $number | $boolean
```

Parameters are model-specific. The user should check with the model
specification to set the parameters.

#### Example Request[#](#example-request "Link to this heading")

Below is an example to send generate request with additional model parameters `stream` and `temperature`.

```
$ curl -X POST localhost:8000/v2/models/mymodel/generate -d '{"id": "42", "text_input": "client input", "parameters": {"stream": false, "temperature": 0}}'

POST /v2/models/mymodel/generate HTTP/1.1
Host: localhost:8000
Content-Type: application/json
Content-Length: <xx>
{
  "id" : "42",
  "text_input" :  "client input",
  "parameters" :
    {
      "stream": false,
      "temperature": 0
    }
}
```

### Generate Response JSON Object[#](#generate-response-json-object "Link to this heading")

A successful generate request is indicated by a 200 HTTP status code.
The generate response object, identified as `$generate_response`, is returned in
the HTTP body.

```
$generate_response =
{
  "id" : $string
  "model_name" : $string,
  "model_version" : $string,
  "text_output" : $string
}
```

* âidâ : The âidâ identifier given in the request, if any.
* âmodel\_nameâ : The name of the model used for inference.
* âmodel\_versionâ : The specific model version used for inference.
* âtext\_outputâ : The output of the inference.

#### Example Response[#](#example-response "Link to this heading")

```
200
{
  "id" : "42"
  "model_name" : "mymodel",
  "model_version" : "1",
  "text_output" : "model output"
}
```

### Generate Response JSON Error Object[#](#generate-response-json-error-object "Link to this heading")

A failed generate request must be indicated by an HTTP error status
(typically 400). The HTTP body must contain the
`$generate_error_response` object.

```
$generate_error_response =
{
  "error": <error message string>
}
```

* âerrorâ : The descriptive message for the error.

#### Example Error[#](#example-error "Link to this heading")

```
400
{
  "error" : "error message"
}
```

