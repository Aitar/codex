* Triton Server Trace

# Triton Server Trace[#](#triton-server-trace "Link to this heading")

Triton includes that capability to generate a detailed trace for
individual inference requests. Tracing is enable by command-line
arguments when running the tritonserver executable.

`--trace-config` command line option in Triton can be used to specify
global and trace mode specific config setting. The format of this flag
is `--trace-config <mode>,<setting>=<value>`, where `<mode>`
is either `triton` or `opentelemetry`. By default, the trace mode is set to `triton`,
and the server will use Tritonâs trace APIs. For `opentelemetry` mode,
the server will use the [OpenTelemetryâs APIs](#opentelemetry-trace-support) to generate,
collect and export traces for individual inference requests.

To specify global trace settings (level, rate, count, or mode),
the format is `--trace-config <setting>=<value>`.

An example usage, which invokes Tritonâs trace APIs:

```
$ tritonserver \
    --trace-config triton,file=/tmp/trace.json \
    --trace-config triton,log-frequency=50 \
    --trace-config rate=100 \
    --trace-config level=TIMESTAMPS \
    --trace-config count=100 ...
```

## Trace Settings[#](#trace-settings "Link to this heading")

### Global Settings[#](#global-settings "Link to this heading")

The following table shows available global trace settings to pass to `--trace-config`

| Setting | Default Value | Description |
| --- | --- | --- |
| `rate` | 1000 | Specifies the sampling rate. The same as deprecated `--trace-rate`.   For example, a value of 1000 specifies that every 1000-th inference   request will be traced. |
| `level` | OFF | Indicates the level of trace detail that should be collected and   may be specified multiple times to trace multiple information.   The same as deprecated `--trace-level`.   Choices are `TIMESTAMPS` and `TENSORS`.  **Note** that `opentelemetry` mode does not currently   support `TENSORS` level. |
| `count` | -1 | Specifies the remaining number of traces to be collected.   The default value of -1 specifies to never stop collecting traces.   With a value of 100, Triton will stop tracing requests  after 100 traces are collected.  The same as deprecated `--trace-count`. |
| `mode` | triton | Specifies which trace APIs to use for collecting traces.   The choices are `triton` or `opentelemetry`. |

### Triton Trace APIs Settings[#](#triton-trace-apis-settings "Link to this heading")

The following table shows available Triton trace APIs settings for
`--trace-config triton,<setting>=<value>`.

| Setting | Default Value | Description |
| --- | --- | --- |
| `file` | empty string | Indicates where the trace output should be written.   The same as deprecated `--trace-file`. |
| `log-frequency` | 0 | Specifies the rate that the traces are written to file.   For example, a value of 50 specifies that Triton will log   to file for every 50 traces collected.   The same as deprecated `--trace-log-frequency`. |

In addition to the trace configuration settings in the command line, you can
modify the trace configuration using the [trace
protocol](../protocol/extension_trace.md). This option is currently not supported,
when trace mode is set to `opentelemetry`.

**Note**: the following flags are **deprecated**:

The `--trace-file` option indicates where the trace output should be
written. The `--trace-rate` option specifies the sampling rate. In
this example every 100-th inference request will be traced. The
`--trace-level` option indicates the level of trace detail that should
be collected. `--trace-level` option may be specified multiple times to
trace multiple information. The `--trace-log-frequency` option specifies the
rate that the traces are written to file. In this example Triton will log to
file for every 50 traces collected. The `--trace-count` option specifies the
remaining number of traces to be collected. In this example Triton will stop
tracing more requests after 100 traces are collected. Use the `--help` option
to get more information.

## Supported Trace Level Option[#](#supported-trace-level-option "Link to this heading")

* `TIMESTAMPS`: Tracing execution timestamps of each request.
* `TENSORS`: Tracing input and output tensors during the execution.

## JSON Trace Output[#](#json-trace-output "Link to this heading")

The trace output is a JSON file with the following schema.

```
[
  {
    "model_name": $string,
    "model_version": $number,
    "id": $number,
    "request_id": $string,
    "parent_id": $number
  },
  {
    "id": $number,
    "timestamps": [
      { "name" : $string, "ns" : $number }
    ]
  },
  {
    "id": $number
    "activity": $string,
    "tensor":{
      "name": $string,
      "data": $string,
      "shape": $string,
      "dtype": $string
    }
  },
  ...
]
```

Each trace is assigned a âidâ, which indicates the model name and
version of the inference request. If the trace is from a
model run as part of an ensemble, the âparent\_idâ will indicate the
âidâ of the containing ensemble.
For example:

```
[
  {
    "id": 1,
    "model_name": "simple",
    "model_version": 1
  },
  ...
]
```

Each `TIMESTAMPS` trace will have one or more âtimestampsâ with
each timestamp having a name and the timestamp in nanoseconds (ânsâ).
For example:

```
[
  {"id": 1, "timestamps": [{ "name": "HTTP_RECV_START", "ns": 2356425054587444 }] },
  {"id": 1, "timestamps": [{ "name": "HTTP_RECV_END", "ns": 2356425054632308 }] },
  {"id": 1, "timestamps": [{ "name": "REQUEST_START", "ns": 2356425054785863 }] },
  {"id": 1, "timestamps": [{ "name": "QUEUE_START", "ns": 2356425054791517 }] },
  {"id": 1, "timestamps": [{ "name": "INFER_RESPONSE_COMPLETE", "ns": 2356425057587919 }] },
  {"id": 1, "timestamps": [{ "name": "COMPUTE_START", "ns": 2356425054887198 }] },
  {"id": 1, "timestamps": [{ "name": "COMPUTE_INPUT_END", "ns": 2356425057152908 }] },
  {"id": 1, "timestamps": [{ "name": "COMPUTE_OUTPUT_START", "ns": 2356425057497763 }] },
  {"id": 1, "timestamps": [{ "name": "COMPUTE_END", "ns": 2356425057540989 }] },
  {"id": 1, "timestamps": [{ "name": "REQUEST_END", "ns": 2356425057643164 }] },
  {"id": 1, "timestamps": [{ "name": "HTTP_SEND_START", "ns": 2356425057681578 }] },
  {"id": 1, "timestamps": [{ "name": "HTTP_SEND_END", "ns": 2356425057712991 }] }
]
```

Each `TENSORS` trace will contain an âactivityâ and a âtensorâ.
âactivityâ indicates the type of tensor, including âTENSOR\_QUEUE\_INPUTâ
and âTENSOR\_BACKEND\_OUTPUTâ by now. âtensorâ has the detail of tensor,
including its ânameâ, âdataâ and âdtypeâ. For example:

```
[
  {
    "id": 1,
    "activity": "TENSOR_QUEUE_INPUT",
    "tensor":{
      "name": "input",
      "data": "0.1,0.1,0.1,...",
      "shape": "1,16",
      "dtype": "FP32"
    }
  }
]
```

## Trace Summary Tool[#](#trace-summary-tool "Link to this heading")

An example [trace summary tool](https://github.com/triton-inference-server/server/blob/main/qa/common/trace_summary.py) can be
used to summarize a set of traces collected from Triton. Basic usage
is:

```
$ trace_summary.py <trace file>
```

This produces a summary report for all traces in the file. HTTP and
GRPC inference requests are reported separately.

```
File: trace.json
Summary for simple (-1): trace count = 1
HTTP infer request (avg): 403.578us
	Receive (avg): 20.555us
	Send (avg): 4.52us
	Overhead (avg): 24.592us
	Handler (avg): 353.911us
  		Overhead (avg): 23.675us
  		Queue (avg): 18.019us
  		Compute (avg): 312.217us
  			Input (avg): 24.151us
  			Infer (avg): 244.186us
  			Output (avg): 43.88us
Summary for simple (-1): trace count = 1
GRPC infer request (avg): 383.601us
	Send (avg): 62.816us
	Handler (avg): 392.924us
  		Overhead (avg): 51.968us
  		Queue (avg): 21.45us
  		Compute (avg): 319.506us
  			Input (avg): 27.76us
  			Infer (avg): 227.844us
  			Output (avg): 63.902us
```

Note: The âReceive (avg)â metric is not included in the gRPC summary as gRPC library does not provide any non-intrusive hooks to detect time spent in reading a message from the wire. Tracing an HTTP request will provide an accurate measurement of time spent reading a request from the network.

Use the -t option to get a summary for each trace in the file. This
summary shows the time, in microseconds, between different points in
the processing of an inference request. For example, the below output
shows that it took 15us from the start of handling the request until
the request was enqueued in the scheduling queue.

```
$ trace_summary.py -t <trace file>
...
simple (-1):
  	request handler start
  		15us
  	queue start
  		20us
  	compute start
  		266us
  	compute end
  		4us
  	request handler end
  		19us
  	grpc send start
  		77us
  	grpc send end
...
```

The script can also show the data flow of the first request if there are
`TENSORS` traces in the file. If the `TENSORS` traces are from an ensemble,
the data flow will be shown with the dependency of each model.

```
...
Data Flow:
	==========================================================
	Name:   ensemble
	Version:1
	QUEUE_INPUT:
		input: [[0.705676  0.830855  0.833153]]
	BACKEND_OUTPUT:
		output: [[1. 2. 7. 0. 4. 7. 9. 3. 4. 9.]]
	==========================================================
		==================================================
		Name:   test_trt1
		Version:1
		QUEUE_INPUT:
			input: [[0.705676  0.830855  0.833153]]
		BACKEND_OUTPUT:
			output1: [[1. 1. ...]]
		==================================================
		==================================================
		Name:   test_trt2
		Version:1
		QUEUE_INPUT:
			input: [[0.705676  0.830855  0.833153]]
		BACKEND_OUTPUT:
			output2: [[2. 2. ...]]
		==================================================
		==================================================
		Name:   test_py
		Version:1
		QUEUE_INPUT:
			output1: [[1. 1. ...]]
		QUEUE_INPUT:
			output2: [[2. 2. ...]]
		BACKEND_OUTPUT:
			output: [[1. 2. 7. 0. 4. 7. 9. 3. 4. 9.]]
		==================================================
...
```

The meaning of the trace timestamps is:

* HTTP Request Receive: Collected only for inference requests that use the
  HTTP protocol. The time required to read the inference request from
  the network.
* Send: The time required to send the inference response.
* Overhead: Additional time required in the HTTP endpoint to
  process the inference request and response.
* Handler: The total time spent handling the inference request, not
  including the HTTP and GRPC request/response handling.

  + Queue: The time the inference request spent in the scheduling queue.
  + Compute: The time the inference request spent executing the actual
    inference. This time includes the time spent copying input and
    output tensors. If âtrace-level=TIMESTAMPS then a breakdown of the
    compute time will be provided as follows:

    - Input: The time to copy input tensor data as required by the
      inference framework / backend. This includes the time to copy
      input tensor data to the GPU.
    - Infer: The time spent executing the model to perform the
      inference.
    - Output: The time to copy output tensor data as required by the
      inference framework / backend. This includes the time to copy
      output tensor data from the GPU.
  + Overhead: Additional time required for request handling not
    covered by Queue or Compute times.
* Data Flow: The data flow of the first request. It contains the input and
  output tensors of each part of execution.

  + Name: The name of model.
  + Version: The version of model.
  + QUEUE\_INPUT: The tensor entering the queue of a backend to wait for
    scheduling.
  + BACKEND\_OUTPUT: The tensor in the response of a backend.

## Tracing for BLS models[#](#tracing-for-bls-models "Link to this heading")

Triton does not collect traces for child models invoked from
[BLS](../python_backend/README.md#business-logic-scripting)
models by default.

To include child models into collected traces, user needs to provide the `trace`
argument (as shown in the example below), when constructing an InferenceRequest object.
This helps Triton associate the child model with the parent modelâs trace (`request.trace()`).

```
import triton_python_backend_utils as pb_utils


class TritonPythonModel:
  ...
    def execute(self, requests):
      ...
      for request in requests:
        ...
        inference_request = pb_utils.InferenceRequest(
            model_name='model_name',
            requested_output_names=['REQUESTED_OUTPUT_1', 'REQUESTED_OUTPUT_2'],
            inputs=[<pb_utils.Tensor object>], trace = request.trace())
```

## OpenTelemetry trace support[#](#opentelemetry-trace-support "Link to this heading")

Triton provides an option to generate and export traces using
[OpenTelemetry APIs and SDKs](https://opentelemetry.io/).

To specify OpenTelemetry mode for tracing, specify the `--trace-config`
flag as follows:

```
$ tritonserver --trace-config mode=opentelemetry \
    --trace-config opentelemetry,url=<endpoint> ...
```

Tritonâs OpenTelemetry trace mode uses
[Batch Span Processor](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/#batch-span-processor),
which batches ended spans and sends them in bulk. Batching helps
with data compression and reduces the number of outgoing connections
required to transmit the data. This processor supports both size and
time based batching. Size-based batching is controlled by 2 parameters:
`bsp_max_export_batch_size` and `bsp_max_queue_size`, while time-based batching
is controlled by `bsp_schedule_delay`. Collected spans will be exported when
the batch size reaches `bsp_max_export_batch_size`, or delay since last export
reaches `bsp_schedule_delay`, whatever comes first. Additionally, user should
make sure that `bsp_max_export_batch_size` is always less than
`bsp_max_queue_size`, otherwise the excessive spans will be dropped
and trace data will be lost.

Default parameters for the Batch Span Processor are provided in
[`OpenTelemetry trace APIs settings`](#opentelemetry-trace-apis-settings).
As a general recommendation, make sure that `bsp_max_queue_size` is large enough
to hold all collected spans, and `bsp_schedule_delay` does not cause frequent
exports, which will affect Triton Serverâs latency. A minimal Triton trace
consists of 3 spans: top level span, model span, and compute span.

* **Top level span**: The top-level span collects timestamps for when
  request was received by Triton, and when the response was sent. Any Triton
  trace contains only 1 top level span.
* **Model span**: Model spans collect information, when request for
  this model was started, when it was placed in a queue, and when it was ended.
  A minimal Triton trace contains 1 model span.
* **Compute span**: Compute spans record compute timestamps. A minimal
  Triton trace contains 1 compute span.

The total amount of spans depends on the complexity of your model.
A general rule is any base model - a single model that performs computations -
produces 1 model span and one compute span. For ensembles, every composing
model produces model and compute spans in addition to one model span for the
ensemble. [BLS](#tracing-for-bls-models) models produce the same number of
model and compute spans as the total amount of models involved in the BLS request,
including the main BLS model.

### Differences in trace contents from Tritonâs trace [output](#json-trace-output)[#](#differences-in-trace-contents-from-triton-s-trace-output "Link to this heading")

OpenTelemetry APIs produce [spans](https://opentelemetry.io/docs/concepts/observability-primer/#spans)
that collect the same timestamps as Tritonâs Trace
APIs. Each span also includes `model_name`, `model_version`, `request_id`,
and `parent_id` as an [attribute](https://opentelemetry.io/docs/concepts/observability-primer/#span-attributes).

The span collects `TIMESTAMPS` that consist of a name and a timestamp
in nanoseconds, which is similar to Triton Trace APIs. However,
OpenTelemetry relies on the systemâs clock for event timestamps, which is based
on the systemâs real-time clock. On the other hand, Triton Trace APIs
report timestamps using steady clock, which is a monotonic clock that ensures
time always movess forward. This clock is not related to wall clock time
and, for example, can measure time since last reboot.

### OpenTelemetry trace APIs settings[#](#opentelemetry-trace-apis-settings "Link to this heading")

The following table shows available OpenTelemetry trace APIs settings for
`--trace-config opentelemetry,<setting>=<value>`.

| Setting | Default Value | Description |
| --- | --- | --- |
| `url` | `http://localhost:4318/v1/traces` | `host:port` to which the receiver is going to receive trace data. |
| `resource` | `service.name=triton-inference-server` | Key-value pairs to be used as resource attributes.   Should be specified following the provided template:  `--trace-config opentelemetry,resource=<key>=<value>`  For example:  `--trace-config opentelemetry,resource=service.name=triton`  `--trace-config opentelemetry,resource=service.version=1`  Alternatively, key-value attributes can be specified through   [OTEL\_RESOURCE\_ATTRIBUTES](https://opentelemetry.io/docs/concepts/sdk-configuration/general-sdk-configuration/#otel_resource_attributes) environment variable. |
| [Batch Span Processor](https://opentelemetry.io/docs/specs/otel/trace/sdk/#batching-processor) |  |  |
| `bsp_max_queue_size` | 2048 | Maximum queue size.   This setting can also be specified through   [OTEL\_BSP\_MAX\_QUEUE\_SIZE](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/#batch-span-processor) environment variable. |
| `bsp_schedule_delay` | 5000 | Delay interval (in milliseconds) between two consecutive exports.   This setting can also be specified through   [OTEL\_BSP\_SCHEDULE\_DELAY](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/#batch-span-processor) environment variable. |
| `bsp_max_export_batch_size` | 512 | Maximum batch size. Must be less than or equal to `bsp_max_queue_size`.  This setting can also be specified through   [OTEL\_BSP\_MAX\_EXPORT\_BATCH\_SIZE](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/#batch-span-processor) environment variable. |

### OpenTelemetry Context Propagation[#](#opentelemetry-context-propagation "Link to this heading")

Triton supports [context propagation](https://opentelemetry.io/docs/concepts/context-propagation/)
in OpenTelemetry mode starting in version 24.01. Note, that every request
with propagated OpenTelemetry context will be traced, regardless of `rate` and
`count` trace settings. If a user wishes to trace only those requests, for which
OpenTelemetry context was injected on the client side, please start Triton with
`--trace-config rate=0`:

```
$ tritonserver \
    --trace-config rate=0 \
    --trace-config level=TIMESTAMPS \
    --trace-config count=-1 \
    --trace-config mode=opentelemetry
```

Please, be aware that this option is subject to change in future releases.

#### How to inject OpenTelemetry context on the client side[#](#how-to-inject-opentelemetry-context-on-the-client-side "Link to this heading")

For C++ clients, please refer to [gRPC](https://github.com/open-telemetry/opentelemetry-cpp/blob/main/examples/grpc/README.md)
and [HTTP](https://github.com/open-telemetry/opentelemetry-cpp/blob/main/examples/http/README.md)
examples.

For python clients, please make sure to install
[OpenTelemetry Python](https://github.com/open-telemetry/opentelemetry-python/tree/main?tab=readme-ov-file#install).
You can then use the `opentelemetry.propagate.inject` method to prepare headers to
pass with the request, as shown [here](https://github.com/open-telemetry/opentelemetry-python/blob/main/docs/examples/auto-instrumentation/client.py#L37-L41).
Then, you can specify headers in the `infer` method. For references, please
look at our [tests](https://github.com/triton-inference-server/server/blob/main/qa/L0_trace/opentelemetry_unittest.py),
e.g. [http context propagation test](https://github.com/triton-inference-server/server/blob/main/qa/L0_trace/opentelemetry_unittest.py#L494-L508).

### Custom Backend Tracing[#](#custom-backend-tracing "Link to this heading")

In the case when a custom activity needs to be traced in the backend, please
use `TRITONSERVER_InferenceTraceReportActivity` API. For examples, please
refer to the [identity backend](https://github.com/triton-inference-server/identity_backend/blob/main/src/identity.cc).

In `openTelemetry` trace mode, if one wishes to start a new span, make sure
that the name of your custom activity ends with `_START`. To end the new span,
make sure that corresponding activity ends with `_END`. For example, in the
identity backend, we start a `CUSTOM_ACTIVITY` span, by [reporting](https://github.com/triton-inference-server/identity_backend/blob/oandreeva-custom-trace-activity/src/identity.cc#L872-L876)
`CUSTOM_ACTIVITY_START` event; and we close this span by [reporting](https://github.com/triton-inference-server/identity_backend/blob/oandreeva-custom-trace-activity/src/identity.cc#L880-L883)
`CUSTOM_ACTIVITY_END` event.

Please note, that it is userâs responsibility to make sure that all custom started
spans are properly ended.

### Limitations[#](#limitations "Link to this heading")

* OpenTelemetry trace mode is not supported on Windows systems.
* Triton supports only
  [OTLP/HTTP Exporter](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/protocol/otlp.md#otlphttp)
  and allows specification of only url for this exporter through
  `--trace-config`. Other options and corresponding default values can be
  found [here](https://github.com/open-telemetry/opentelemetry-cpp/tree/v1.8.3/exporters/otlp#configuration-options--otlp-http-exporter-).
* Triton does not support configuration of the opentelemetry trace settings
  during a Triton run and opentelemetry specific settings are not available
  for the retrieval through [Tritonâs trace extension](../protocol/extension_trace.md).

