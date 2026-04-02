* [API Reference](../client_guide/api_reference.md)
* [Extensions](../client_guide/kserve_extension.md)
* Parameters Extension

# Parameters Extension[#](#parameters-extension "Link to this heading")

This document describes Tritonâs parameters extension. The
parameters extension allows an inference request to provide
custom parameters that cannot be provided as inputs. Because this extension is
supported, Triton reports âparametersâ in the extensions field of its
Server Metadata. This extension uses the optional âparametersâ
field in the KServe Protocol in
[HTTP](https://kserve.github.io/website/0.10/modelserving/data_plane/v2_protocol/#inference-request-json-object)
and
[GRPC](https://kserve.github.io/website/0.10/modelserving/data_plane/v2_protocol/#parameters).

The following parameters are reserved for Tritonâs usage and should not be
used as custom parameters:

* sequence\_id
* priority
* timeout
* sequence\_start
* sequence\_end
* headers
* All the keys that start with `"triton_"` prefix. Some examples used today:

  + `"triton_enable_empty_final_response"` request parameter
  + `"triton_final_response"` response parameter

When using both GRPC and HTTP endpoints, you need to make sure to not use
the reserved parameters list to avoid unexpected behavior. The reserved
parameters are not accessible in the Triton C-API.

## HTTP/REST[#](#http-rest "Link to this heading")

The following example shows how a request can include custom parameters.

```
POST /v2/models/mymodel/infer HTTP/1.1
Host: localhost:8000
Content-Type: application/json
Content-Length: <xx>
{
  "parameters" : { "my_custom_parameter" : 42 }
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

The `parameters` field in the
ModelInferRequest message can be used to send custom parameters.

## Forwarding HTTP/GRPC Headers as Parameters[#](#forwarding-http-grpc-headers-as-parameters "Link to this heading")

Triton can forward HTTP/GRPC headers as inference request parameters. By
specifying a regular expression in `--http-header-forward-pattern` and
`--grpc-header-forward-pattern`,
Triton will add the headers that match with the regular expression as request
parameters. All the forwarded headers will be added as a parameter with string
value. For example to forward all the headers that start with âPREFIX\_â from
both HTTP and GRPC, you should add `--http-header-forward-pattern PREFIX_.* --grpc-header-forward-pattern PREFIX_.*` to your `tritonserver` command.

By default, the regular expression pattern matches headers with case-insensitive
mode according to the HTTP protocol. If you want to enforce case-sensitive mode,
simplying adding the `(?-i)` prefix which turns off case-insensitive mode, e.g.
`--http-header-forward-pattern (?-i)PREFIX_.*`. Note, headers sent through the
Python HTTP client may be automatically lower-cased by internal client libraries.

The forwarded headers can be accessed using the
[Python](../python_backend/README.md#inference-request-parameters)
or C Backend APIs as inference request parameters.

