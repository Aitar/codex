* [API Reference](../client_guide/api_reference.md)
* [Extensions](../client_guide/kserve_extension.md)
* Classificati...

# Classification Extension[#](#classification-extension "Link to this heading")

This document describes Tritonâs classification extension. The
classification extension allows Triton to return an output as a
classification index and (optional) label instead of returning the
output as raw tensor data. Because this extension is supported,
Triton reports âclassificationâ in the extensions field of its Server
Metadata.

An inference request can use the âclassificationâ parameter to request
that one or more classifications be returned for an output. For such
an output the returned tensor will not be the shape and type produced
by the model, but will instead be type BYTES with shape [ batch-size,
<count> ] where each element returns the classification index and
label as a single string. The <count> dimension of the returned tensor
will equal the âcountâ value specified in the classification
parameter.

When the classification parameter is used, Triton will determine the
top-n classifications as the n highest-valued elements in the output
tensor compared using the output tensorâs data type. For example, if
an output tensor is [ 1, 5, 10, 4 ], the highest-valued element is 10
(index 2), followed by 5 (index 1), followed by 4 (index 3), followed
by 1 (index 0). So, for example, the top-2 classifications by index
are [ 2, 1 ].

The format of the returned string will be â<value>:<index>[:<label>]â,
where <index> is the index of the class in the model output tensor,
<value> is the value associated with that index in the model output,
and the <label> associated with that index is optional. For example,
continuing the example from above, the returned tensor will be [
â10:2â, â5:1â ]. If the model has labels associated with those
indices, the returned tensor will be [ â10:2:appleâ, â5:1:pickleâ ].

## HTTP/REST[#](#http-rest "Link to this heading")

In all JSON schemas shown in this document `$number`, `$string`, `$boolean`,
`$object` and `$array` refer to the fundamental JSON types. #optional
indicates an optional JSON field.

The classification extension requires that the âclassificationâ
parameter, when applied to a requested inference output, be recognized
by Triton as follows:

* âclassificationâ : `$number` indicating the number of classes that
  should be returned for the output.

The following example shows how the classification parameter is used
in an inference request.

```
POST /v2/models/mymodel/infer HTTP/1.1
Host: localhost:8000
Content-Type: application/json
Content-Length: <xx>
{
  "id" : "42",
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
      "parameters" : { "classification" : 2 }
    }
  ]
}
```

For the above request Triton will return the âoutput0â output tensor
as a STRING tensor with shape [ 2 ]. Assuming the model produces
output0 tensor [ 1.1, 3.3, 0.5, 2.4 ] from the above inputs, the
response will be the following.

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: <yy>
{
  "id" : "42"
  "outputs" : [
    {
      "name" : "output0",
      "shape" : [ 2 ],
      "datatype"  : "STRING",
      "data" : [ "3.3:1", "2.4:3" ]
    }
  ]
}
```

If the model has labels associated with each classification index
Triton will return those as well, as shown below.

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: <yy>
{
  "id" : "42"
  "outputs" : [
    {
      "name" : "output0",
      "shape" : [ 2 ],
      "datatype"  : "STRING",
      "data" : [ "3.3:1:index_1_label", "2.4:3:index_3_label" ]
    }
  ]
}
```

## GRPC[#](#grpc "Link to this heading")

The classification extension requires that the âclassificationâ
parameter, when applied to a requested inference output, be recognized
by Triton as follows:

* âclassificationâ : int64\_param indicating the number of classes that
  should be returned for the output.

The following example shows how the classification parameter is used
in an inference request.

```
ModelInferRequest {
  model_name : "mymodel"
  model_version : -1
  inputs [
    {
      name : "input0"
      shape : [ 2, 2 ]
      datatype : "UINT32"
      contents { int_contents : [ 1, 2, 3, 4 ] }
    }
  ]
  outputs [
    {
      name : "output0"
      parameters [
        {
          key : "classification"
          value : { int64_param : 2 }
        }
      ]
    }
  ]
}
```

For the above request Triton will return the âoutput0â output tensor
as a STRING tensor with shape [ 2 ]. Assuming the model produces
output0 tensor [ 1.1, 3.3, 0.5, 2.4 ] from the above inputs, the
response will be the following.

```
ModelInferResponse {
  model_name : "mymodel"
  outputs [
    {
      name : "output0"
      shape : [ 2 ]
      datatype  : "STRING"
      contents { bytes_contents : [ "3.3:1", "2.4:3" ] }
    }
  ]
}
```

