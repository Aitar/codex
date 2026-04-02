* [API Reference](../client_guide/api_reference.md)
* [Extensions](../client_guide/kserve_extension.md)
* Trace Extension

# Trace Extension[#](#trace-extension "Link to this heading")

This document describes Tritonâs trace extension. The trace extension enables
the client to configure the trace settings during a Triton run. Because this
extension is supported, Triton reports âtraceâ in the extensions field of
its Server Metadata.

## HTTP/REST[#](#http-rest "Link to this heading")

In all JSON schemas shown in this document `$number`, `$string`, `$boolean`,
`$object` and `$array` refer to the fundamental JSON types. `#optional`
indicates an optional JSON field.

Triton exposes the trace endpoint at the following URL. The client may use
HTTP GET request to retrieve the current trace setting. A HTTP POST request
will modify the trace setting, and the endpoint will return the updated trace
setting on success or an error in the case of failure. Optional model name
can be provided to get or to set the trace settings for specific model.

```
GET v2[/models/${MODEL_NAME}]/trace/setting

POST v2[/models/${MODEL_NAME}]/trace/setting
```

### Trace Setting Response JSON Object[#](#trace-setting-response-json-object "Link to this heading")

A successful trace setting request is indicated by a 200 HTTP status
code. The response object, identified as `$trace_setting_response`, is
returned in the HTTP body for every successful trace setting request.

```
$trace_setting_response =
{
  $trace_setting, ...
}

$trace_setting = $string : $string | [ $string, ...]
```

Each `$trace_setting` JSON describes a ânameâ/âvalueâ pair, where the ânameâ is
the name of the trace setting and the âvalueâ is a `$string representation` of the
setting value, or an array of `$string` for some settings. Currently the following
trace settings are defined:

* âtrace\_fileâ : the file where the trace output will be saved. If
  âlog\_frequencyâ is set, this will be the prefix of the files to save the
  trace output, resulting files in name `"${trace_file}.0", "${trace_file}.1", ...`,
  see trace setting âlog\_frequencyâ below for detail.
* âtrace\_levelâ : the trace level. âOFFâ to disable tracing,
  âTIMESTAMPSâ to trace timestamps, âTENSORSâ to trace tensors.
  This value is an array of string where user may specify multiple levels to
  trace multiple information.
* âtrace\_rateâ : the trace sampling rate. The value represents how many requests
  will one trace be sampled from. For example, if the trace rate is â1000â,
  1 trace will be sampled for every 1000 requests.
* âtrace\_countâ : the number of remaining traces to be sampled. Once the value
  becomes â0â, no more traces will be sampled for the trace setting, and the
  collected traces will be written to indexed trace file in the format described
  in âlog\_frequencyâ, regardless of the âlog\_frequencyâ status.
  If the value is â-1â, the number of traces to be sampled will not be limited.
* âlog\_frequencyâ : the frequency that Triton will log the
  trace output to the files. If the value is â0â, Triton will only log
  the trace output to `${trace_file}` when shutting down. Otherwise, Triton will log
  the trace output to `${trace_file}.${idx}` when it collects
  the specified number of traces. For example, if the log frequency is â100â,
  when Triton collects the 100-th trace, it logs the traces to file
  `"${trace_file}.0"`, and when it collects the 200-th trace, it logs the 101-th to
  the 200-th traces to file `"${trace_file}.1"`. Note that the file index will be
  reset to 0 when âtrace\_fileâ setting is updated.

### Trace Setting Response JSON Error Object[#](#trace-setting-response-json-error-object "Link to this heading")

A failed trace setting request will be indicated by an HTTP error status
(typically 400). The HTTP body must contain the
`$trace_setting_error_response` object.

```
$trace_setting_error_response =
{
  "error": $string
}
```

* âerrorâ : The descriptive message for the error.

#### Trace Setting Request JSON Object[#](#trace-setting-request-json-object "Link to this heading")

A trace setting request is made with a HTTP POST to
the trace endpoint. In the corresponding response the HTTP body contains the
response JSON. A successful request is indicated by a 200 HTTP status code.

The request object, identified as `$trace_setting_request` must be provided in the HTTP
body.

```
$trace_setting_request =
{
  $trace_setting, ...
}
```

The `$trace_setting` JSON is defined in
[Trace Setting Response JSON Object](#trace-setting-response-json-object), only the specified
settings will be updated. In addition to the values mentioned in response JSON
object, JSON null value may be used to remove the specification of
the trace setting. In such case, the current global setting will be used.
Similarly, if this is the first request to initialize a model trace settings,
for the trace settings that are not specified in the request, the current global
setting will be used.

## GRPC[#](#grpc "Link to this heading")

For the trace extension Triton implements the following API:

```
service GRPCInferenceService
{
  â¦

  // Update and get the trace setting of the Triton server.
  rpc TraceSetting(TraceSettingRequest)
          returns (TraceSettingResponse) {}
}
```

The Trace Setting API returns the latest trace settings. Errors are indicated
by the google.rpc.Status returned for the request. The OK code
indicates success and other codes indicate failure. The request and
response messages for Trace Setting are:

```
message TraceSettingRequest
{
  // The values to be associated with a trace setting.
  // If no value is provided, the setting will be clear and
  // the global setting value will be used.
  message SettingValue
  {
    repeated string value = 1;
  }

  // The new setting values to be updated,
  // settings that are not specified will remain unchanged.
  map<string, SettingValue> settings = 1;

  // The name of the model to apply the new trace settings.
  // If not given, the new settings will be applied globally.
  string model_name = 2;
}

message TraceSettingResponse
{
  message SettingValue
  {
    repeated string value = 1;
  }

  // The latest trace settings.
  map<string, SettingValue> settings = 1;
}
```

The trace settings are mentioned in
[Trace Setting Response JSON Object](#trace-setting-response-json-object).
Note that if this is the first request to initialize
a model trace settings, for the trace settings that are not specified
in the request, the value will be copied from the current global settings.

