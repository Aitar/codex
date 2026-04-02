* [API Reference](../client_guide/api_reference.md)
* [Extensions](../client_guide/kserve_extension.md)
* Shared-Memor...

# Shared-Memory Extension[#](#shared-memory-extension "Link to this heading")

This document describes Tritonâs shared-memory extensions. The
shared-memory extensions allow a client to communicate input and
output tensors by system or CUDA shared memory. Using shared memory
instead of sending the tensor data over the GRPC or REST interface can
provide significant performance improvement for some use cases.
Because both of these extensions are supported, Triton reports
âsystem\_shared\_memoryâ and âcuda\_shared\_memoryâ in the extensions
field of its Server Metadata.

The shared-memory extensions use a common set of parameters to
indicate that an input or output tensor is communicated via shared
memory. These parameters and their type are:

* âshared\_memory\_regionâ : string value is the name of a previously
  registered shared memory region. Region names share a namespace for
  system-shared-memory regions and CUDA-shared-memory regions.
* âshared\_memory\_offsetâ : int64 value is the offset, in bytes, into
  the region where the data for the tensor starts.
* âshared\_memory\_byte\_sizeâ : int64 value is the size, in bytes, of
  the data.

The âshared\_memory\_offsetâ parameter is optional and defaults to
zero. The other two parameters are required. If only one of the two is
given Triton will return an error.

Note that there is no Windows support for shared memory yet. Jetson only
supports system shared memory.

## HTTP/REST[#](#http-rest "Link to this heading")

In all JSON schemas shown in this document `$number`, `$string`, `$boolean`,
`$object` and `$array` refer to the fundamental JSON types. #optional
indicates an optional JSON field.

The shared-memory parameters may be used in the `$request_input`
parameters to indicate that the corresponding input is being
communicated via shared memory. The parameters may be used in the
`$request_output` parameters to indicate that the requested output
should be communicated via shared memory.

When these parameters are set for an input tensor the âdataâ field of
`$request_input` must not be set. If the âdataâ field is set Triton will
return an error. When these parameters are set for a requested output
tensor the returned `$response_output` must not define the âdataâ field.

Shared memory regions must be created by the client and then
registered with Triton before they can be referenced with a
âshared\_memory\_regionâ parameter. The system and CUDA shared-memory
extensions each require a different set of APIs for registering a
shared memory region.

### System Shared Memory[#](#system-shared-memory "Link to this heading")

The system shared memory extension requires Status, Register and
Unregister APIs.

Triton exposes the following URL to register and unregister system
shared memory regions.

```
GET v2/systemsharedmemory[/region/${REGION_NAME}]/status

POST v2/systemsharedmemory/region/${REGION_NAME}/register

POST v2/systemsharedmemory[/region/${REGION_NAME}]/unregister
```

#### Status[#](#status "Link to this heading")

A system-shared-memory status request is made with an HTTP GET to the
status endpoint. In the corresponding response the HTTP body contains
the response JSON. If REGION\_NAME is provided in the URL the response
includes the status for the corresponding region. If REGION\_NAME is
not provided in the URL the response includes the status for all
registered regions.

A successful status request is indicated by a 200 HTTP status
code. The response object, identified as
`$system_shared_memory_status_response`, is returned in the HTTP body
for every successful request.

```
$system_shared_memory_status_response =
[
  {
    "name" : $string,
    "key" : $string,
    "offset" : $number,
    "byte_size" : $number
  },
  â¦
]
```

* ânameâ : The name of the shared-memory region.
* âkeyâ : The key of the underlying memory object that contains the
  shared memory region.
* âoffsetâ : The offset, in bytes, within the underlying memory object
  to the start of the shared memory region.
* âbyte\_sizeâ : The size of the shared memory region, in bytes.

A failed status request must be indicated by an HTTP error status
(typically 400). The HTTP body must contain the
`$system_shared_memory_status_error_response` object.

```
$system_shared_memory_status_error_response =
{
  "error": $string
}
```

* âerrorâ : The descriptive message for the error.

#### Register[#](#register "Link to this heading")

A system-shared-memory register request is made with a HTTP POST to
the register endpoint. In the corresponding response the HTTP body
contains the response JSON. A successful register request is indicated
by a 200 HTTP status code.

The request object, identified as
`$system_shared_memory_register_request` must be provided in the HTTP
body.

```
$system_shared_memory_register_request =
{
  "key" : $string,
  "offset" : $number,
  "byte_size" : $number
}
```

* âkeyâ : The key of the underlying memory object that contains the
  shared memory region.
* âoffsetâ : The offset, in bytes, within the underlying memory object
  to the start of the shared memory region.
* âbyte\_sizeâ : The size of the shared memory region, in bytes.

A failed register request must be indicated by an HTTP error status
(typically 400). The HTTP body must contain the
`$system_shared_memory_register_error_response` object.

```
$system_shared_memory_register_error_response =
{
  "error": $string
}
```

* âerrorâ : The descriptive message for the error.

#### Unregister[#](#unregister "Link to this heading")

A system-shared-memory unregister request is made with an HTTP POST to
an unregister endpoint. In the request the HTTP body must be empty.

A successful register request is indicated by a 200 HTTP status. If
REGION\_NAME is provided in the URL the single region is
unregistered. If REGION\_NAME is not provided in the URL all regions
are unregisered.

A failed unregister request must be indicated by an HTTP error status
(typically 400). The HTTP body must contain the
`$system_shared_memory_unregister_error_response` object.

```
$system_shared_memory_unregister_error_response =
{
  "error": $string
}
```

* âerrorâ : The descriptive message for the error.

### CUDA Shared Memory[#](#cuda-shared-memory "Link to this heading")

The CUDA shared memory extension requires Status, Register and
Unregister APIs.

Triton exposes the following URL to register and unregister system
shared memory regions.

```
GET v2/cudasharedmemory[/region/${REGION_NAME}]/status

POST v2/cudasharedmemory/region/${REGION_NAME}/register

POST v2/cudasharedmemory[/region/${REGION_NAME}]/unregister
```

#### Status[#](#id1 "Link to this heading")

A CUDA-shared-memory status request is made with an HTTP GET to the
status endpoint. In the corresponding response the HTTP body contains
the response JSON. If REGION\_NAME is provided in the URL the response
includes the status for the corresponding region. If REGION\_NAME is
not provided in the URL the response includes the status for all
registered regions.

A successful status request is indicated by a 200 HTTP status
code. The response object, identified as
`$cuda_shared_memory_status_response`, is returned in the HTTP body
for every successful request.

```
$cuda_shared_memory_status_response =
[
  {
    "name" : $string,
    "device_id" : $number,
    "byte_size" : $number
  },
  â¦
]
```

* ânameâ : The name of the shared memory region.
* âdevice\_idâ : The GPU device ID where the cudaIPC handle was
  created.
* âbyte\_sizeâ : The size of the shared memory region, in bytes.

A failed status request must be indicated by an HTTP error status
(typically 400). The HTTP body must contain the
`$cuda_shared_memory_status_error_response` object.

```
$cuda_shared_memory_status_error_response =
{
  "error": $string
}
```

* âerrorâ : The descriptive message for the error.

#### Register[#](#id2 "Link to this heading")

A CUDA-shared-memory register request is made with a HTTP POST to
the register endpoint. In the corresponding response the HTTP body
contains the response JSON. A successful register request is indicated
by a 200 HTTP status code.

The request object, identified as
`$cuda_shared_memory_register_request` must be provided in the HTTP
body.

```
$cuda_shared_memory_register_request =
{
  "raw_handle" : { "b64" : $string },
  "device_id" : $number,
  "byte_size" : $number
}
```

* âraw\_handleâ : The serialized cudaIPC handle, base64 encoded.
* âdevice\_idâ : The GPU device ID where the cudaIPC handle was
  created.
* âbyte\_sizeâ : The size of the shared memory region, in bytes.

A failed register request must be indicated by an HTTP error status
(typically 400). The HTTP body must contain the
`$cuda_shared_memory_register_error_response` object.

```
$cuda_shared_memory_register_error_response =
{
  "error": $string
}
```

* âerrorâ : The descriptive message for the error.

#### Unregister[#](#id3 "Link to this heading")

A CUDA-shared-memory unregister request is made with an HTTP POST to
an unregister endpoint. In the request the HTTP body must be empty.

A successful register request is indicated by a 200 HTTP status. If
REGION\_NAME is provided in the URL the single region is
unregistered. If REGION\_NAME is not provided in the URL all regions
are unregisered.

A failed unregister request must be indicated by an HTTP error status
(typically 400). The HTTP body must contain the
`$cuda_shared_memory_unregister_error_response` object.

```
$cuda_shared_memory_unregister_error_response =
{
  "error": $string
}
```

* âerrorâ : The descriptive message for the error.

## GRPC[#](#grpc "Link to this heading")

The shared-memory parameters may be used in the
ModelInferRequest::InferInputTensor message to indicate that the
corresponding input is being communicated via shared memory. The
parameters may be used in the
ModelInferRequest::InferRequestedOutputTensor message to indicate that
the requested output should be communicated via shared memory.

When these parameters are set for an input tensor the âcontentsâ field
of ModelInferRequest::InferInputTensor must not be set. If the
âcontentsâ field is set Triton will return an errorâ¦ When these
parameters are set for a requested output tensor the âcontentsâ field
of the ModelInferResponse::InferOutputTensor will not be set in the
inference response.

Shared memory regions must be created by the client and then
registered with Triton before they can be referenced with a
âshared\_memory\_regionâ parameter. The system and CUDA shared-memory
extensions each require a different set of APIs. For all APIs, errors
are indicated by the google.rpc.Status returned for the request. The
OK code indicates success and other codes indicate failure.

### System Shared Memory[#](#id4 "Link to this heading")

The system shared memory extension requires the following API:

```
service GRPCInferenceService
{
  â¦

  // Get the status of all registered system-shared-memory regions.
  rpc SystemSharedMemoryStatus(SystemSharedMemoryStatusRequest)
          returns (SystemSharedMemoryStatusResponse) {}

  // Register system-shared-memory region.
  rpc SystemSharedMemoryRegister(SystemSharedMemoryRegisterRequest)
          returns (SystemSharedMemoryRegisterResponse) {}

  // Unregister system-shared-memory region.
  rpc SystemSharedMemoryUnregister(SystemSharedMemoryUnregisterRequest)
          returns (SystemSharedMemoryUnregisterResponse) {}
}
```

#### Status[#](#id5 "Link to this heading")

The system-shared-memory status API provides information about
registered system shared-memory regions. Errors are indicated by the
google.rpc.Status returned for the request. The OK code indicates
success and other codes indicate failure. The request and response
messages for SystemSharedMemoryStatus are:

```
message SystemSharedMemoryStatusRequest
{
  // The name of the region to get status for. If empty the
  // status is returned for all registered regions.
  string name = 1;
}

message SystemSharedMemoryStatusResponse
{
  // Status for a shared memory region.
  message RegionStatus {
    // The name for the shared memory region.
    string name = 1;

    // The key of the underlying memory object that contains the
    // shared memory region.
    string key = 2;

    // Offset, in bytes, within the underlying memory object to
    // the start of the shared memory region.
    uint64 offset = 3;

    // Size of the shared memory region, in bytes.
    uint64 byte_size = 4;
  }

  // Status for each of the registered regions, indexed by region name.
  map<string, RegionStatus> regions = 1;
}
```

#### Register[#](#id6 "Link to this heading")

The system-shared-memory register API is used to register a new
shared-memory region with Triton. After a region is registered it can
be used in the âshared\_memory\_regionâ parameter for an input or output
tensor. Errors are indicated by the google.rpc.Status returned for the
request. The OK code indicates success and other codes indicate
failure. The request and response messages for
SystemSharedMemoryRegister are:

```
message SystemSharedMemoryRegisterRequest
{
  // The name of the region to register.
  string name = 1;

  // The key of the underlying memory object that contains the
  // shared memory region.
  string key = 2;

  // Offset, in bytes, within the underlying memory object to
  // the start of the shared memory region.
  uint64 offset = 3;

  // Size of the shared memory region, in bytes.
  uint64 byte_size = 4;
}

message SystemSharedMemoryRegisterResponse
{
}
```

#### Unregister[#](#id7 "Link to this heading")

The system-shared-memory unregister API provides unregisters a
shared-memory region from Triton. After a region is
unregistered it can no longer be used to communicate input and output
tensor contents. Errors are indicated by the google.rpc.Status
returned for the request. The OK code indicates success and other
codes indicate failure. The request and response messages for
SystemSharedMemoryStatus are:

```
message SystemSharedMemoryUnregisterRequest
{
  // The name of the region to unregister. If empty all system shared-memory
  // regions are unregistered.
  string name = 1;
}

message SystemSharedMemoryUnregisterResponse
{
}
```

### CUDA Shared Memory[#](#id8 "Link to this heading")

The CUDA shared memory extension requires the following API:

```
service GRPCInferenceService
{
  â¦

  // Get the status of all registered CUDA-shared-memory regions.
  rpc CudaSharedMemoryStatus(CudaSharedMemoryStatusRequest)
          returns (CudaSharedMemoryStatusResponse) {}

  // Register CUDA-shared-memory region.
  rpc CudaSharedMemoryRegister(CudaSharedMemoryRegisterRequest)
          returns (CudaSharedMemoryRegisterResponse) {}

  // Unregister CUDA-shared-memory region.
  rpc CudaSharedMemorUnregister(CudaSharedMemoryUnregisterRequest)
          returns (CudaSharedMemoryUnregisterResponse) {}
}
```

#### Status[#](#id9 "Link to this heading")

The CUDA-shared-memory status API provides information about
registered CUDA shared-memory regions. Errors are indicated by the
google.rpc.Status returned for the request. The OK code indicates
success and other codes indicate failure. The request and response
messages for CudaSharedMemoryStatus are:

```
message CudaSharedMemoryStatusRequest
{
  // The name of the region to get status for. If empty the
  // status is returned for all registered regions.
  string name = 1;
}

message CudaSharedMemoryStatusResponse
{
  // Status for a shared memory region.
  message RegionStatus {
    // The name for the shared memory region.
    string name = 1;

    // The GPU device ID where the cudaIPC handle was created.
    uint64 device_id = 2;

    // Size of the shared memory region, in bytes.
    uint64 byte_size = 3;
  }

  // Status for each of the registered regions, indexed by region name.
  map<string, RegionStatus> regions = 1;
}
```

#### Register[#](#id10 "Link to this heading")

The CUDA-shared-memory register API is used to register a new
shared-memory region with Triton. After a region is
registered it can be used in the âshared\_memory\_regionâ parameter for
an input or output tensor. Errors are indicated by the
google.rpc.Status returned for the request. The OK code indicates
success and other codes indicate failure. The request and response
messages for CudaSharedMemoryRegister are:

```
message CudaSharedMemoryRegisterRequest
{
  // The name of the region to register.
  string name = 1;

  // The raw serialized cudaIPC handle.
  bytes raw_handle = 2;

  // The GPU device ID on which the cudaIPC handle was created.
  int64 device_id = 3;

  // Size of the shared memory region, in bytes.
  uint64 byte_size = 4;
}

message CudaSharedMemoryRegisterResponse
{
}
```

#### Unregister[#](#id11 "Link to this heading")

The CUDA-shared-memory unregister API provides unregisters a
shared-memory region from Triton. After a region is unregistered it
can no longer be used to communicate input and output tensor
contents. Errors are indicated by the google.rpc.Status returned for
the request. The OK code indicates success and other codes indicate
failure. The request and response messages for CudaSharedMemoryStatus
are:

```
message CudaSharedMemoryUnregisterRequest
{
  // The name of the region to unregister. If empty all CUDA shared-memory
  // regions are unregistered.
  string name = 1;
}

message CudaSharedMemoryUnregisterResponse
{
}
```

