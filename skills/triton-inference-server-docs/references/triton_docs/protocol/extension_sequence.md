* [API Reference](../client_guide/api_reference.md)
* [Extensions](../client_guide/kserve_extension.md)
* Sequence Extension

# Sequence Extension[#](#sequence-extension "Link to this heading")

This document describes Tritonâs sequence extension. The sequence
extension allows Triton to support stateful models that expect a
sequence of related inference requests.

An inference request can specify that it is part of a sequence using
the âsequence\_idâ parameter in the request and by using the
âsequence\_startâ and âsequence\_endâ parameters to indicate the start
and end of sequences.

Because this extension is supported, Triton reports âsequenceâ
in the extensions field of its Server Metadata. Triton may additionally
report âsequence(string\_id)â in the extensions field of the Server Metadata
if the âsequence\_idâ parameter supports string types.

* âsequence\_idâ : a string or uint64 value that identifies the sequence to which
  a request belongs. All inference requests that belong to the same sequence
  must use the same sequence ID. A sequence ID of 0 or ââ indicates the
  inference request is not part of a sequence.
* âsequence\_startâ : boolean value if set to true in a request
  indicates that the request is the first in a sequence. If not set,
  or set to false the request is not the first in a sequence. If set
  the âsequence\_idâ parameter must be set to a non-zero or non-empty string
  value.
* âsequence\_endâ : boolean value if set to true in a request indicates
  that the request is the last in a sequence. If not set, or set to
  false the request is not the last in a sequence. If set the
  âsequence\_idâ parameter must be set to a non-zero or non-empty string
  value.

## HTTP/REST[#](#http-rest "Link to this heading")

The following example shows how a request is marked as part of a
sequence. In this case the sequence\_start and sequence\_end parameters
are not used which means that this request is neither the start nor
end of the sequence.

```
POST /v2/models/mymodel/infer HTTP/1.1
Host: localhost:8000
Content-Type: application/json
Content-Length: <xx>
{
  "parameters" : { "sequence_id" : 42 }
  "inputs" : [
    {
      "name" : "input0",
      "shape" : [ 2, 2 ],
      "datatype" : "UINT32",
      "data" : [ 1, 2, 3, 4 ]
    }
  ],
  "outputs" : [
    {
      "name" : "output0",
    }
  ]
}
```

The example below uses a v4 UUID string as the value for the âsequence\_idâ
parameter.

```
POST /v2/models/mymodel/infer HTTP/1.1
Host: localhost:8000
Content-Type: application/json
Content-Length: <xx>
{
  "parameters" : { "sequence_id" : "e333c95a-07fc-42d2-ab16-033b1a566ed5" }
  "inputs" : [
    {
      "name" : "input0",
      "shape" : [ 2, 2 ],
      "datatype" : "UINT32",
      "data" : [ 1, 2, 3, 4 ]
    }
  ],
  "outputs" : [
    {
      "name" : "output0",
    }
  ]
}
```

## GRPC[#](#grpc "Link to this heading")

In addition to supporting the sequence parameters described above, the
GRPC API adds a streaming version of the inference API to allow a
sequence of inference requests to be sent over the same GRPC
stream. This streaming API is not required to be used for requests
that specify a sequence\_id and may be used by requests that do not
specify a sequence\_id. The ModelInferRequest is the same as for the
ModelInfer API. The ModelStreamInferResponse message is shown below.

```
service GRPCInferenceService
{
  â¦

  // Perform inference using a specific model with GRPC streaming.
  rpc ModelStreamInfer(stream ModelInferRequest) returns (stream ModelStreamInferResponse) {}
}

// Response message for ModelStreamInfer.
message ModelStreamInferResponse
{
  // The message describing the error. The empty message
  // indicates the inference was successful without errors.
  String error_message = 1;

  // Holds the results of the request.
  ModelInferResponse infer_response = 2;
}
```

