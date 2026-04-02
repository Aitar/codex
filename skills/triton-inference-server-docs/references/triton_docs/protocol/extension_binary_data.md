* [API Reference](../client_guide/api_reference.md)
* [Extensions](../client_guide/kserve_extension.md)
* Binary...

# Binary Tensor Data Extension[#](#binary-tensor-data-extension "Link to this heading")

This document describes Tritonâs binary tensor data extension. The
binary tensor data extension allows Triton to support tensor data
represented in a binary format in the body of an HTTP/REST
request. Because this extension is supported, Triton reports
âbinary\_tensor\_dataâ in the extensions field of its Server Metadata.

## Binary Tensor Request[#](#binary-tensor-request "Link to this heading")

Tensor data represented as binary data is organized in little-endian
byte order, row major, without stride or padding between elements. All
tensor data types are representable as binary data in the native size
of the data type. For BOOL type element true is a single byte with
value 1 and false is a single byte with value 0. For BYTES type an
element is represented by a 4-byte unsigned integer giving the length
followed by the actual bytes. The binary data for a tensor is
delivered in the HTTP body after the JSON object (see Examples).

The binary tensor data extension uses parameters to indicate that an
input or output tensor is communicated as binary data. The first
parameter is used in `$request_input` and `$response_output` to indicate
that the input or output tensor is communicated as binary data:

* âbinary\_data\_sizeâ : int64 parameter indicating the size of the
  tensor binary data, in bytes.

The second parameter is used in `$request_output` to indicate that the
output should be returned from Triton as binary data.

* âbinary\_dataâ : bool parameter that is true if the output should be
  returned as binary data and false (or not given) if the tensor
  should be returned as JSON.

The third parameter is used in $inference\_request to indicate that all
outputs should be returned from Triton as binary data, unless
overridden by âbinary\_dataâ on a specific output.

* âbinary\_data\_outputâ : bool parameter that is true if all outputs
  should be returned as binary data and false (or not given) if the
  outputs should be returned as JSON. If âbinary\_dataâ is specified on
  an output it overrides this setting.

When one or more tensors are communicated as binary data, the HTTP
body of the request or response will contain the JSON inference
request or response object followed by the binary tensor data in the
same order as the order of the input or output tensors are specified
in the JSON. If any binary data is present in the request or response
the Inference-Header-Content-Length header must be provided to give
the length of the JSON object, and Content-Length continues to give
the full body length (as HTTP requires).

### Examples[#](#examples "Link to this heading")

For the following request the input tensors are sent as binary data
and the output tensor must be returned as binary data as that is what
is requested. Also note that the total size of the binary data is 19
bytes and that size must be reflected in the content length headers.

```
POST /v2/models/mymodel/infer HTTP/1.1
Host: localhost:8000
Content-Type: application/octet-stream
Inference-Header-Content-Length: <xx>
Content-Length: <xx+19>
{
  "model_name" : "mymodel",
  "inputs" : [
    {
      "name" : "input0",
      "shape" : [ 2, 2 ],
      "datatype" : "UINT32",
      "parameters" : {
        "binary_data_size" : 16
      }
    },
    {
      "name" : "input1",
      "shape" : [ 3 ],
      "datatype" : "BOOL",
      "parameters" : {
        "binary_data_size" : 3
      }
    }
  ],
  "outputs" : [
    {
      "name" : "output0",
      "parameters" : {
        "binary_data" : true
      }
    }
  ]
}
<16 bytes of data for input0 tensor>
<3 bytes of data for input1 tensor>
```

Assuming the model returns a [ 3, 2 ] tensor of data type FP32 the
following response would be returned.

```
HTTP/1.1 200 OK
Content-Type: application/octet-stream
Inference-Header-Content-Length: <yy>
Content-Length: <yy+24>
{
  "outputs" : [
    {
      "name" : "output0",
      "shape" : [ 3, 2 ],
      "datatype"  : "FP32",
      "parameters" : {
        "binary_data_size" : 24
      }
    }
  ]
}
<24 bytes of data for output0 tensor>
```

## Raw Binary Request[#](#raw-binary-request "Link to this heading")

For models whose tensor metadata can be deduced from the byte size of the binary
data. User may send the binary tensor request without specifying inference
header. In other words, the request body only contains the binary data of the
tensor. Below is the constraints for the qualified models:

1. Only has 1 input
2. If the input data type is non-BYTE, the number of variable size dimensions is
   at most 1. If the data type is BYTE, the shape must be [1]. The supported data
   types can be found [here](https://github.com/kserve/kserve/blob/master/docs/predict-api/v2/required_api.md#tensor-data-types)

To send a raw binary request, the Inference-Header-Content-Length header must be
provided with value 0 to indicate that the request body doesnât include the
inference header.

Note: if the model supports batching, the request will be treated as batch-1
request because the inference header is omitted. Additionally, all the model
output will be requested to be returned in binary tensor form as described in
the previous section.

### Examples[#](#id1 "Link to this heading")

The following is the example of sending raw binary request. Note that the total
size of the binary data is 16 bytes and that size must be reflected in
the content length headers.

```
POST /v2/models/mymodel/infer HTTP/1.1
Host: localhost:8000
Content-Type: application/octet-stream
Inference-Header-Content-Length: 0
Content-Length: 16
<16 bytes of data for input tensor>
```

Assuming the model returns two outputs which both has shape [ 3, 1 ] and data
type FP32, then the following response would be returned.

```
HTTP/1.1 200 OK
Content-Type: application/octet-stream
Inference-Header-Content-Length: <yy>
Content-Length: <yy+24>
{
  "outputs" : [
    {
      "name" : "output0",
      "shape" : [ 3, 1 ],
      "datatype"  : "FP32",
      "parameters" : {
        "binary_data_size" : 12
      }
    },
    {
      "name" : "output1",
      "shape" : [ 3, 1 ],
      "datatype"  : "FP32",
      "parameters" : {
        "binary_data_size" : 12
      }
    }
  ]
}
<12 bytes of data for output0 tensor>
<12 bytes of data for output1 tensor>
```

