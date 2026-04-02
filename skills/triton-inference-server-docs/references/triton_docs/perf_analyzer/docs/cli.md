* Perf Analyzer CLI

# Perf Analyzer CLI[#](#perf-analyzer-cli "Link to this heading")

This document details the Perf Analyzer command line interface:

* [General Options](#general-options)
* [Measurement Options](#measurement-options)
* [Sequence Model Options](#sequence-model-options)
* [Input Data Options](#input-data-options)
* [Request Options](#request-options)
* [Server Options](#server-options)
* [Prometheus Metrics Options](#prometheus-metrics-options)
* [Report Options](#report-options)
* [Trace Options](#trace-options)
* [Deprecated Options](#deprecated-options)

## General Options[#](#general-options "Link to this heading")

### `-?`[#](#id1 "Link to this heading")

### `-h`[#](#h "Link to this heading")

### `--help`[#](#help "Link to this heading")

Prints a description of the Perf Analyzer command line interface.

### `-m <string>`[#](#m-string "Link to this heading")

Specifies the model name for Perf Analyzer to run.

This is a required option.

### `-x <string>`[#](#x-string "Link to this heading")

Specifies the version of the model to be used. If not specified the most
recent version (the highest numbered version) of the model will be used.

### `--service-kind=[triton|triton_c_api|tfserving|torchserve|dynamic_grpc]`[#](#service-kind-triton-triton-c-api-tfserving-torchserve-dynamic-grpc "Link to this heading")

Specifies the kind of service for Perf Analyzer to generate load for. Note: in
order to use `torchserve` backend, the `--input-data` option must point to a
JSON file holding data in the following format:

```
{
  "data": [
    {
      "TORCHSERVE_INPUT": [
        "<complete path to the content file>"
      ]
    },
    {...},
    ...
  ]
}
```

The type of file here will depend on the model. In order to use `triton_c_api`
you must specify the Triton server install path and the model repository path
via the `--triton-server-directory` and `--model-repository` options.

Default is `triton`.

### `--bls-composing-models=<string>`[#](#bls-composing-models-string "Link to this heading")

Specifies the list of all BLS composing models as a comma separated list of
model names (with optional model version number after a colon for each) that may
be called by the input BLS model. For example,
`--bls-composing-models=modelA:3,modelB` would specify that modelA and modelB
are composing models that may be called by the input BLS model, and that modelA
will use version 3, while modelBâs version is unspecified.

### `--model-signature-name=<string>`[#](#model-signature-name-string "Link to this heading")

Specifies the signature name of the saved model to use.

Default is `serving_default`. This option will be ignored if `--service-kind`
is not `tfserving`.

### `-v`[#](#v "Link to this heading")

Enables verbose mode. May be specified an additional time (`-v -v`) to enable
extra verbose mode.

## Measurement Options[#](#measurement-options "Link to this heading")

### `--measurement-mode=[time_windows|count_windows]`[#](#measurement-mode-time-windows-count-windows "Link to this heading")

Specifies the mode used for stabilizing measurements. âtime\_windowsâ will
create windows such that the duration of each window is equal to
`--measurement-interval`. âcount\_windowsâ will create windows such that there
are at least `--measurement-request-count` requests in each window and that
the window is at least one second in duration (adding more requests if
necessary).

Default is `time_windows`.

### `-p <n>`[#](#p-n "Link to this heading")

### `--measurement-interval=<n>`[#](#measurement-interval-n "Link to this heading")

Specifies the time interval used for each measurement in milliseconds when
`--measurement-mode=time_windows` is used. Perf Analyzer will sample a time
interval specified by this option and take measurement over the requests
completed within that time interval.

Default is `5000`.

### `--measurement-request-count=<n>`[#](#measurement-request-count-n "Link to this heading")

Specifies the minimum number of requests to be collected in each measurement
window when `--measurement-mode=count_windows` is used.

Default is `50`.

### `-s <n>`[#](#s-n "Link to this heading")

### `--stability-percentage=<n>`[#](#stability-percentage-n "Link to this heading")

Specifies the allowed variation in latency measurements when determining if a
result is stable. The measurement is considered stable if the ratio of max /
min from the recent 3 measurements is within (stability percentage)% in terms
of both inferences per second and latency.

Default is `10`(%).

### `--percentile=<n>`[#](#percentile-n "Link to this heading")

Specifies the confidence value as a percentile that will be used to determine
if a measurement is stable. For example, a value of `85` indicates that the
85th percentile latency will be used to determine stability. The percentile
will also be reported in the results.

Default is `-1` indicating that the average latency is used to determine
stability.

### `--warmup-request-count=<n>`[#](#warmup-request-count-n "Link to this heading")

Specifies the number of warmup requests to send before benchmarking.

Default is `0`, which means that no warmup requests will be sent.

### `--request-count=<n>`[#](#request-count-n "Link to this heading")

Specifies a total number of requests to use for measurement.

Default is `0`, which means that there is no request count and the measurement
will proceed using windows until stabilization is detected.

### `-r <n>`[#](#r-n "Link to this heading")

### `--max-trials=<n>`[#](#max-trials-n "Link to this heading")

Specifies the maximum number of measurements when attempting to reach stability
of inferences per second and latency for each concurrency or request rate
during the search. Perf Analyzer will terminate if the measurement is still
unstable after the maximum number of trials.

Default is `10`.

### `--concurrency-range=<start:end:step>`[#](#concurrency-range-start-end-step "Link to this heading")

Specifies the range of concurrency levels covered by Perf Analyzer. Perf
Analyzer will start from the concurrency level of âstartâ and go until âendâ
with a stride of âstepâ.

Default of âstartâ, âendâ, and âstepâ are `1`. If âendâ is not specified then
Perf Analyzer will run for a single concurrency level determined by âstartâ. If
âendâ is set as `0`, then the concurrency limit will be incremented by âstepâ
until the latency threshold is met. âendâ and `--latency-threshold` cannot
both be `0`. âendâ cannot be `0` for sequence models while using asynchronous
mode.

### `--periodic-concurrency-range=<start:end:step>`[#](#periodic-concurrency-range-start-end-step "Link to this heading")

Specifies the range of concurrency levels in the similar but slightly different
manner as the `--concurrency-range`. Perf Analyzer will start from the
concurrency level of âstartâ and increase by âstepâ each time. Unlike
`--concurrency-range`, the âendâ indicates the *total* number of concurrency
since the âstartâ (including) and will stop increasing once the cumulative
number of concurrent requests has reached the âendâ. The user can specify
*when* to periodically increase the concurrency level using the
`--request-period` option. The concurrency level will periodically increase for
every `n`-th response specified by `--request-period`. Since this disables
stability check in Perf Analyzer and reports response timestamps only, the user
must provide `--profile-export-file` to specify where to dump all the measured
timestamps.

The default values of âstartâ, âendâ, and âstepâ are `1`.

### `--session-concurrency=<n>`[#](#session-concurrency-n "Link to this heading")

Enables session concurrency inference load mode and specifies the number of
concurrent multi-turn chat sessions to run during the benchmark. A dataset must
be provided using `--input-data` with at least as many unique sessions as the
specified session concurrency. Only supported with `--service-kind=openai`.

### `--request-period=<n>`[#](#request-period-n "Link to this heading")

Specifies the number of responses that each request must receive before new,
concurrent requests are sent when `--periodic-concurrency-range` is specified.

Default value is `10`.

### `--request-parameter=<name:value:type>`[#](#request-parameter-name-value-type "Link to this heading")

Specifies a custom parameter that can be sent to a Triton backend as part of
the request. For example, providing âârequest-parameter max\_tokens:256:intâ
to the command line will set an additional parameter âmax\_tokensâ of type
âintâ to 256 as part of the request. The ârequest-parameter may be specified
multiple times for different custom parameters.

Valid `type` values are: `bool`, `int`, and `string`.

> **NOTE**
>
> The `--request-parameter` is currently only supported by gRPC protocol.

### `--request-rate-range=<start:end:step>`[#](#request-rate-range-start-end-step "Link to this heading")

Specifies the range of request rates for load generated by Perf Analyzer. This
option can take floating-point values. The search along the request rate range
is enabled only when using this option.

If not specified, then Perf Analyzer will search along the concurrency range.
Perf Analyzer will start from the request rate of âstartâ and go until âendâ
with a stride of âstepâ. Default values of âstartâ, âendâ and âstepâ are all
`1.0`. If âendâ is not specified, then Perf Analyzer will run for a single
request rate as determined by âstartâ. If âendâ is set as `0.0`, then the
request rate will be incremented by âstepâ until the latency threshold is met.
âendâ and `--latency-threshold` can not be both `0`.

### `--request-distribution=[constant|poisson]`[#](#request-distribution-constant-poisson "Link to this heading")

Specifies the time interval distribution between dispatching inference requests
to the server. Poisson distribution closely mimics the real-world work load on
a server. This option is ignored if not using `--request-rate-range`.

Default is `constant`.

### `-l <n>`[#](#l-n "Link to this heading")

### `--latency-threshold=<n>`[#](#latency-threshold-n "Link to this heading")

Specifies the limit on the observed latency, in milliseconds. Perf Analyzer
will terminate the concurrency or request rate search once the measured latency
exceeds this threshold.

Default is `0` indicating that Perf Analyzer will run for the entire
concurrency or request rate range.

### `--binary-search`[#](#binary-search "Link to this heading")

Enables binary search on the specified search range (concurrency or request
rate). This option requires âstartâ and âendâ to be expilicitly specified in
the concurrency range or request rate range. When using this option, âstepâ is
more like the precision. When the âstepâ is lower, there are more iterations
along the search path to find suitable convergence.

When `--binary-search` is not specified, linear search is used.

### `--request-intervals=<path>`[#](#request-intervals-path "Link to this heading")

Specifies a path to a file containing time intervals in microseconds. Each time
interval should be in a new line. Perf Analyzer will try to maintain time
intervals between successive generated requests to be as close as possible in
this file. This option can be used to apply custom load to server with a
certain pattern of interest. Perf Analyzer will loop around the file if the
duration of execution exceeds the amount of time specified by the intervals.
This option can not be used with `--request-rate-range` or
`--concurrency-range`.

### `--fixed-schedule`[#](#fixed-schedule "Link to this heading")

Enables fixed schedule inference load mode. In this mode, Perf Analyzer runs
through the `--input-data` JSON once. Each entry represents a request and must
have a `timestamp` âinputâ, which tells Perf Analyzer when to send that request.
A timestamp of `N` means Perf Analyzer will send that request `N` milliseconds
after the start of the benchmark.

See [fixed schedule](inference_load_modes.md#fixed-schedule-mode) documentation
for more info.

### `--max-threads=<n>`[#](#max-threads-n "Link to this heading")

Specifies the maximum number of threads that will be created for providing
desired concurrency or request rate. However, when running in synchronous mode
with `--concurrency-range` having explicit âendâ specification, this value will
be ignored.

Default is `4` if `--request-rate-range` is specified, otherwise default is
`16`.

## Sequence Model Options[#](#sequence-model-options "Link to this heading")

### `--num-of-sequences=<n>`[#](#num-of-sequences-n "Link to this heading")

Specifies the number of concurrent sequences for sequence models. This option
is ignored when `--request-rate-range` is not specified.

Default is `4`.

### `--sequence-length=<n>`[#](#sequence-length-n "Link to this heading")

Specifies the base length of a sequence used for sequence models. A sequence
with length X will be composed of X requests to be sent as the elements in the
sequence. The actual length of the sequencewill be within +/- Y% of the base
length, where Y defaults to 20% and is customizable via
`--sequence-length-variation`. If sequence length is unspecified and input data
is provided, the sequence length will be the number of inputs in the
user-provided input data.

Default is `20`.

### `--sequence-length-variation=<n>`[#](#sequence-length-variation-n "Link to this heading")

Specifies the percentage variation in length of sequences. This option is only
valid when not using user-provided input data or when `--sequence-length` is
specified while using user-provided input data.

Default is `20`(%).

### `--sequence-id-range=<start:end>`[#](#sequence-id-range-start-end "Link to this heading")

Specifies the range of sequence IDs used by Perf Analyzer. Perf Analyzer will
start from the sequence ID of âstartâ and go until âendâ (excluded). If âendâ
is not specified then Perf Analyzer will generate new sequence IDs without
bounds. If âendâ is specified and the concurrency setting may result in
maintaining a number of sequences more than the range of available sequence
IDs, Perf Analyzer will exit with an error due to possible sequence ID
collisions.

The default for âstart is `1`, and âendâ is not specified (no bounds).

### `--serial-sequences`[#](#serial-sequences "Link to this heading")

Enables the serial sequence mode where a maximum of one request is live per sequence.
Note: It is possible that this mode can cause the request rate mode to not achieve the
desired rate, especially if num-of-sequences is too small.

## Input Data Options[#](#input-data-options "Link to this heading")

### `--input-data=[zero|random|<path>]`[#](#input-data-zero-random-path "Link to this heading")

Specifies type of data that will be used for input in inference requests. The
available options are `zero`, `random`, and a path to a directory or a JSON
file.

When pointing to a JSON file, the user must adhere to the format described in
the [input data documentation](input_data.md). By specifying JSON data, users
can control data used with every request. Multiple data streams can be specified
for a sequence model, and Perf Analyzer will select a data stream in a
round-robin fashion for every new sequence. Multiple JSON files can also be
provided (`--input-data json_file1.json --input-data json_file2.json` and so on)
and Perf Analyzer will append data streams from each file. When using
`--service-kind=torchserve`, make sure this option points to a JSON file.

If the option is path to a directory then the directory must contain a binary
text file for each non-string/string input respectively, named the same as the
input. Each file must contain the data required for that input for a batch-1
request. Each binary file should contain the raw binary representation of the
input in row-major order for non-string inputs. The text file should contain
all strings needed by batch-1, each in a new line, listed in row-major order.

Default is `random`.

### `-b <n>`[#](#b-n "Link to this heading")

Specifies the batch size for each request sent.

Default is `1`.

### `--shape=<string>`[#](#shape-string "Link to this heading")

Specifies the shape used for the specified input. The argument must be
specified as âname:shapeâ where the shape is a comma-separated list for
dimension sizes. For example `--shape=input_name:1,2,3` indicates that the
input `input_name` has tensor shape [ 1, 2, 3 ]. `--shape` may be specified
multiple times to specify shapes for different inputs.

### `--string-data=<string>`[#](#string-data-string "Link to this heading")

Specifies the string to initialize string input buffers. Perf Analyzer will
replicate the given string to build tensors of required shape.
`--string-length` will not have any effect. This option is ignored if
`--input-data` points to a JSON file or directory.

### `--string-length=<n>`[#](#string-length-n "Link to this heading")

Specifies the length of the random strings to be generated by Perf Analyzer
for string input. This option is ignored if `--input-data` points to a
JSON file or directory.

Default is `128`.

### `--shared-memory=[none|system|cuda]`[#](#shared-memory-none-system-cuda "Link to this heading")

Specifies the type of the shared memory to use for input and output data.

Default is `none`.

### `--output-shared-memory-size=<n>`[#](#output-shared-memory-size-n "Link to this heading")

Specifies The size, in bytes, of the shared memory region to allocate per
output tensor. Only needed when one or more of the outputs are of string type
and/or variable shape. The value should be larger than the size of the largest
output tensor that the model is expected to return. Perf Analyzer will use the
following formula to calculate the total shared memory to allocate:
output\_shared\_memory\_size \* number\_of\_outputs \* batch\_size.

Default is `102400` (100 KB).

### `--input-tensor-format=[binary|json]`[#](#input-tensor-format-binary-json "Link to this heading")

Specifies the Triton inference request input tensor format. Only valid when HTTP
protocol is used.

Default is `binary`.

### `--output-tensor-format=[binary|json]`[#](#output-tensor-format-binary-json "Link to this heading")

Specifies the Triton inference response output tensor format. Only valid when
HTTP protocol is used.

Default is `binary`.

## Request Options[#](#request-options "Link to this heading")

### `-i [http|grpc]`[#](#i-http-grpc "Link to this heading")

Specifies the communication protocol to use. The available protocols are HTTP
and gRPC. Note that when the service kind is set to `dynamic_grpc`,
Perf Analyzer will automatically set the protocol to `grpc`.

Default is `http`.

### `-a`[#](#a "Link to this heading")

### `--async`[#](#async "Link to this heading")

Enables asynchronous mode in Perf Analyzer.

By default, Perf Analyzer will use a synchronous request API for inference.
However, if the model is sequential, then the default mode is asynchronous.
Specify `--sync` to operate sequential models in synchronous mode. In
synchronous mode, Perf Analyzer will start threads equal to the concurrency
level. Use asynchronous mode to limit the number of threads, yet maintain the
concurrency.

### `--sync`[#](#sync "Link to this heading")

Enables synchronous mode in Perf Analyzer. Can be used to operate Perf
Analyzer with sequential model in synchronous mode.

### `--streaming`[#](#streaming "Link to this heading")

Enables the use of bidirectional streaming RPC. This option is only valid
with gRPC protocol.

### `-H <string>`[#](#h-string "Link to this heading")

Specifies the header that will be added to HTTP requests (ignored for gRPC
requests). The header must be specified as âHeader:Valueâ. `-H` may be
specified multiple times to add multiple headers.

### `--grpc-compression-algorithm=[none|gzip|deflate]`[#](#grpc-compression-algorithm-none-gzip-deflate "Link to this heading")

Specifies the compression algorithm to be used by gRPC when sending requests.
Only supported when gRPC protocol is being used.

Default is `none`.

### `--grpc-method <string>`[#](#grpc-method-string "Link to this heading")

Specifies a fully-qualified gRPC method name in `<package>.<service>/<method>` format.
The option is only supported with `dynamic_grpc` service kind and is used to identify
the RPC to use when sending requests to the server.

### `--proto <string>`[#](#proto-string "Link to this heading")

Specifies the path to the protobuf file that defines all the gRPC service and RPC methods.
The options is only supported with `dynamic_grpc` service kind for dynamically parsing
the protobuf at runtime.

## Server Options[#](#server-options "Link to this heading")

### `-u <url>`[#](#u-url "Link to this heading")

Specifies the URL for the server.

Default is `localhost:8000` when using `--service-kind=triton` with HTTP.
Default is `localhost:8001` when using `--service-kind=triton` with gRPC.
Default is `localhost:8500` when using `--service-kind=tfserving`.

### `--ssl-grpc-use-ssl`[#](#ssl-grpc-use-ssl "Link to this heading")

Enables usage of an encrypted channel to the server.

### `--ssl-grpc-root-certifications-file=<path>`[#](#ssl-grpc-root-certifications-file-path "Link to this heading")

Specifies the path to file containing the PEM encoding of the server root
certificates.

### `--ssl-grpc-private-key-file=<path>`[#](#ssl-grpc-private-key-file-path "Link to this heading")

Specifies the path to file containing the PEM encoding of the clientâs private
key.

### `--ssl-grpc-certificate-chain-file=<path>`[#](#ssl-grpc-certificate-chain-file-path "Link to this heading")

Specifies the path to file containing the PEM encoding of the clientâs
certificate chain.

### `--ssl-https-verify-peer=[0|1]`[#](#ssl-https-verify-peer-0-1 "Link to this heading")

Specifies whether to verify the peerâs SSL certificate. See
https://curl.se/libcurl/c/CURLOPT\_SSL\_VERIFYPEER.md for the meaning of each
value.

Default is `1`.

### `--ssl-https-verify-host=[0|1|2]`[#](#ssl-https-verify-host-0-1-2 "Link to this heading")

Specifies whether to verify the certificateâs name against host. See
https://curl.se/libcurl/c/CURLOPT\_SSL\_VERIFYHOST.md for the meaning of each
value.

Default is `2`.

### `--ssl-https-ca-certificates-file=<path>`[#](#ssl-https-ca-certificates-file-path "Link to this heading")

Specifies the path to Certificate Authority (CA) bundle.

### `--ssl-https-client-certificate-file=<path>`[#](#ssl-https-client-certificate-file-path "Link to this heading")

Specifies the path to the SSL client certificate.

### `--ssl-https-client-certificate-type=[PEM|DER]`[#](#ssl-https-client-certificate-type-pem-der "Link to this heading")

Specifies the type of the client SSL certificate.

Default is `PEM`.

### `--ssl-https-private-key-file=<path>`[#](#ssl-https-private-key-file-path "Link to this heading")

Specifies the path to the private keyfile for TLS and SSL client cert.

### `--ssl-https-private-key-type=[PEM|DER]`[#](#ssl-https-private-key-type-pem-der "Link to this heading")

Specifies the type of the private key file.

Default is `PEM`.

### `--triton-server-directory=<path>`[#](#triton-server-directory-path "Link to this heading")

Specifies the Triton server install path. Required by and only used when C API
is used (`--service-kind=triton_c_api`).

Default is `/opt/tritonserver`.

### `--model-repository=<path>`[#](#model-repository-path "Link to this heading")

Specifies the model repository directory path for loading models. Required by
and only used when C API is used (`--service-kind=triton_c_api`).

## Prometheus Metrics Options[#](#prometheus-metrics-options "Link to this heading")

### `--collect-metrics`[#](#collect-metrics "Link to this heading")

Enables the collection of server-side inference server metrics. Perf Analyzer
will output metrics in the CSV file generated with the `-f` option. Only valid
when `--verbose-csv` option also used.

### `--metrics-url=<url>`[#](#metrics-url-url "Link to this heading")

Specifies the URL to query for server-side inference server metrics.

Default is `localhost:8002/metrics`.

### `--metrics-interval=<n>`[#](#metrics-interval-n "Link to this heading")

Specifies how often within each measurement window, in milliseconds, Perf
Analyzer should query for server-side inference server metrics.

Default is `1000`.

## Report Options[#](#report-options "Link to this heading")

### `-f <path>`[#](#f-path "Link to this heading")

Specifies the path that the latency report file will be generated at.

When `-f` is not specified, a latency report will not be generated.

### `--profile-export-file <path>`[#](#profile-export-file-path "Link to this heading")

Specifies the path that the profile export will be generated at.

When `--profile-export-file` is not specified, a profile export will not be
generated.

### `--verbose-csv`[#](#verbose-csv "Link to this heading")

Enables additional information being output to the CSV file generated by Perf
Analyzer.

## Trace Options[#](#trace-options "Link to this heading")

### `--trace-level=[OFF|TIMESTAMPS|TENSORS]`[#](#trace-level-off-timestamps-tensors "Link to this heading")

Specifies a trace level. `OFF` disables tracing. `TIMESTAMPS` traces
timestamps. `TENSORS` traces tensors. It may be specified multiple times to
trace multiple information. Only used for `--service-kind=triton`.

Default is `OFF`.

### `--trace-rate=<n>`[#](#trace-rate-n "Link to this heading")

Specifies the trace sampling rate (traces per second).

Default is `1000`.

### `--trace-count=<n>`[#](#trace-count-n "Link to this heading")

Specifies the number of traces to be sampled. If the value is `-1`, the number
of traces to be sampled will not be limited.

Default is `-1`.

### `--log-frequency=<n>`[#](#log-frequency-n "Link to this heading")

Specifies the trace log frequency. If the value is `0`, Triton will only log
the trace output to the trace file when shutting down.
Otherwise, Triton will log the trace output to `<trace-file>`. when it
collects the specified number of traces.
For example, if the trace file is `trace_file.log`, and if the log
frequency is `100`, when Triton collects the 100th trace, it logs the traces
to file `trace_file.log.0`, and when it collects the 200th trace, it logs the
101st to the 200th traces to file `trace_file.log.1`.

Default is `0`.

## Deprecated Options[#](#deprecated-options "Link to this heading")

### `--data-directory=<path>`[#](#data-directory-path "Link to this heading")

**DEPRECATED**

Alias for `--input-data=<path>` where `<path>` is the path to a directory. See
`--input-data` option documentation for details.

### `-c <n>`[#](#c-n "Link to this heading")

**DEPRECATED**

Specifies the maximum concurrency that Perf Analyzer will search up to. Cannot
be used with `--concurrency-range`.

### `-d`[#](#d "Link to this heading")

**DEPRECATED**

Enables dynamic concurrency mode. Perf Analyzer will search along
concurrencies up to the maximum concurrency specified via `-c <n>`. Cannot be
used with `--concurrency-range`.

### `-t <n>`[#](#t-n "Link to this heading")

**DEPRECATED**

Specifies the number of concurrent requests. Cannot be used with
`--concurrency-range`.

Default is `1`.

### `-z`[#](#z "Link to this heading")

**DEPRECATED**

Alias for `--input-data=zero`. See `--input-data` option documentation for
details.

