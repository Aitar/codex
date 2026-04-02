* [Performance Analyzer](../../perf_benchmark/perf_analyzer.md)
* Measurement Modes

# Measurement Modes[#](#measurement-modes "Link to this heading")

Currently, Perf Analyzer has 2 measurement modes.

## Time Windows[#](#time-windows "Link to this heading")

When using time windows measurement mode
([`--measurement-mode=time_windows`](cli.md#measurement-mode-time-windows-count-windows)),
Perf Analyzer will count how many requests have completed during a window of
duration `X` (in milliseconds, via
[`--measurement-interval=X`](cli.md#measurement-interval-n), default is
`5000`). This is the default measurement mode.

## Count Windows[#](#count-windows "Link to this heading")

When using count windows measurement mode
([`--measurement-mode=count_windows`](cli.md#measurement-mode-time-windows-count-windows)),
Perf Analyzer will start the window duration at 1 second and potentially
dynamically increase it until `X` requests have completed (via
[`--measurement-request-count=X`](cli.md#measurement-request-count-n), default
is `50`).

# Metrics[#](#metrics "Link to this heading")

## How Throughput is Calculated[#](#how-throughput-is-calculated "Link to this heading")

Perf Analyzer calculates throughput to be the total number of requests completed
during a measurement, divided by the duration of the measurement, in seconds.

## How Latency is Calculated[#](#how-latency-is-calculated "Link to this heading")

For each request concurrency level Perf Analyzer reports latency and throughput
as seen from Perf Analyzer and also the average request latency on the server.

The server latency measures the total time from when the request is received at
the server until when the response is sent from the server. Because of the HTTP
and gRPC libraries used to implement the server endpoints, total server latency
is typically more accurate for HTTP requests as it measures time from the first
byte received until last byte sent. For both HTTP and gRPC the total server
latency is broken-down into the following components:

* *queue*: The average time spent in the inference schedule queue by a request
  waiting for an instance of the model to become available.
* *compute*: The average time spent performing the actual inference, including
  any time needed to copy data to/from the GPU.
* *overhead*: The average time spent in the endpoint that cannot be correctly
  captured in the send/receive time with the way the gRPC and HTTP libraries are
  structured.

The client latency time is broken-down further for HTTP and gRPC as follows:

* HTTP: *send/recv* indicates the time on the client spent sending the request
  and receiving the response. *response wait* indicates time waiting for the
  response from the server.
* gRPC: *(un)marshal request/response* indicates the time spent marshalling the
  request data into the gRPC protobuf and unmarshalling the response data from
  the gRPC protobuf. *response wait* indicates time writing the gRPC request to
  the network, waiting for the response, and reading the gRPC response from the
  network.

Use the verbose ([`-v`](cli.md#v)) option see more output, including the
stabilization passes run for each request concurrency level or request rate.

# Reports[#](#reports "Link to this heading")

## Visualizing Latency vs. Throughput[#](#visualizing-latency-vs-throughput "Link to this heading")

Perf Analyzer provides the [`-f`](cli.md#f-path) option to generate a file
containing CSV output of the results.

```
$ perf_analyzer -m inception_graphdef --concurrency-range 1:4 -f perf.csv
...
$ cat perf.csv
Concurrency,Inferences/Second,Client Send,Network+Server Send/Recv,Server Queue,Server Compute Input,Server Compute Infer,Server Compute Output,Client Recv,p50 latency,p90 latency,p95 latency,p99 latency
1,69.2,225,2148,64,206,11781,19,0,13891,18795,19753,21018
3,84.2,237,1768,21673,209,11742,17,0,35398,43984,47085,51701
4,84.2,279,1604,33669,233,11731,18,1,47045,56545,59225,64886
2,87.2,235,1973,9151,190,11346,17,0,21874,28557,29768,34766
```

NOTE: The rows in the CSV file are sorted in an increasing order of throughput
(Inferences/Second).

You can import the CSV file into a spreadsheet to help visualize the latency vs
inferences/second tradeoff as well as see some components of the latency.

## Server-side Prometheus metrics[#](#server-side-prometheus-metrics "Link to this heading")

Perf Analyzer can collect
[server-side metrics](../../user_guide/metrics.md#gpu-metrics),
such as GPU utilization and GPU power usage. To enable the collection of these
metrics, use the [`--collect-metrics`](cli.md#collect-metrics) option.

By default, Perf Analyzer queries the metrics endpoint at the URL
`localhost:8002/metrics`. If the metrics are accessible at a different url, use
the [`--metrics-url=<url>`](cli.md#metrics-url-url) option to specify that.

By default, Perf Analyzer queries the metrics endpoint every 1000 milliseconds.
To use a different querying interval, use the
[`--metrics-interval=<n>`](cli.md#metrics-interval-n) option (specify in
milliseconds).

Because Perf Analyzer can collect the server-side metrics multiple times per
run, these metrics are aggregated in specific ways to produce one final number
per searched concurrency or request rate. Here are how the metrics are
aggregated:

| Metric | Aggregation |
| --- | --- |
| GPU Utilization | Averaged from each collection taken during stable passes. We want a number representative of all stable passes. |
| GPU Power Usage | Averaged from each collection taken during stable passes. We want a number representative of all stable passes. |
| GPU Used Memory | Maximum from all collections taken during a stable pass. Users are typically curious what the peak memory usage is for determining model/hardware viability. |
| GPU Total Memory | First from any collection taken during a stable pass. All of the collections should produce the same value for total memory available on the GPU. |

Note that all metrics are per-GPU in the case of multi-GPU systems.

To output these server-side metrics to a CSV file, use the
[`-f <path>`](cli.md#f-path) and [`--verbose-csv`](cli.md#verbose-csv)
options. The output CSV will contain one column per metric. The value of each
column will be a `key:value` pair (`GPU UUID:metric value`). Each `key:value`
pair will be delimited by a semicolon (`;`) to indicate metric values for each
GPU accessible by the server. There is a trailing semicolon. See below:

`<gpu-uuid-0>:<metric-value>;<gpu-uuid-1>:<metric-value>;...;`

Here is a simplified CSV output:

```
$ perf_analyzer -m resnet50_libtorch --collect-metrics -f output.csv --verbose-csv
$ cat output.csv
Concurrency,...,Avg GPU Utilization,Avg GPU Power Usage,Max GPU Memory Usage,Total GPU Memory
1,...,gpu_uuid_0:0.33;gpu_uuid_1:0.5;,gpu_uuid_0:55.3;gpu_uuid_1:56.9;,gpu_uuid_0:10000;gpu_uuid_1:11000;,gpu_uuid_0:50000;gpu_uuid_1:75000;,
2,...,gpu_uuid_0:0.25;gpu_uuid_1:0.6;,gpu_uuid_0:25.6;gpu_uuid_1:77.2;,gpu_uuid_0:11000;gpu_uuid_1:17000;,gpu_uuid_0:50000;gpu_uuid_1:75000;,
3,...,gpu_uuid_0:0.87;gpu_uuid_1:0.9;,gpu_uuid_0:87.1;gpu_uuid_1:71.7;,gpu_uuid_0:15000;gpu_uuid_1:22000;,gpu_uuid_0:50000;gpu_uuid_1:75000;,
```

## Communication Protocol[#](#communication-protocol "Link to this heading")

By default, Perf Analyzer uses HTTP to communicate with Triton. The gRPC
protocol can be specified with the [`-i [http|grpc]`](cli.md#i-http-grpc)
option. If gRPC is selected the [`--streaming`](cli.md#streaming) option can
also be specified for gRPC streaming.

### SSL/TLS Support[#](#ssl-tls-support "Link to this heading")

Perf Analyzer can be used to benchmark Triton service behind SSL/TLS-enabled
endpoints. These options can help in establishing secure connection with the
endpoint and profile the server.

For gRPC, see the following options:

* [`--ssl-grpc-use-ssl`](cli.md#ssl-grpc-use-ssl)
* [`--ssl-grpc-root-certifications-file=<path>`](cli.md#ssl-grpc-root-certifications-file-path)
* [`--ssl-grpc-private-key-file=<path>`](cli.md#ssl-grpc-private-key-file-path)
* [`--ssl-grpc-certificate-chain-file=<path>`](cli.md#ssl-grpc-certificate-chain-file-path)

More details here:
https://grpc.github.io/grpc/cpp/structgrpc\_1\_1\_ssl\_credentials\_options.md

The
[inference protocol gRPC SSL/TLS section](../../customization_guide/inference_protocols.md#ssl-tls)
describes server-side options to configure SSL/TLS in Tritonâs gRPC endpoint.

For HTTPS, the following options are exposed:

* [`--ssl-https-verify-peer`](cli.md#ssl-https-verify-peer-0-1)
* [`--ssl-https-verify-host`](cli.md#ssl-https-verify-host-0-1-2)
* [`--ssl-https-ca-certificates-file`](cli.md#ssl-https-ca-certificates-file-path)
* [`--ssl-https-client-certificate-file`](cli.md#ssl-https-client-certificate-file-path)
* [`--ssl-https-client-certificate-type`](cli.md#ssl-https-client-certificate-type-pem-der)
* [`--ssl-https-private-key-file`](cli.md#ssl-https-private-key-file-path)
* [`--ssl-https-private-key-type`](cli.md#ssl-https-private-key-type-pem-der)

See [`--help`](cli.md#help) for full documentation.

Unlike gRPC, Tritonâs HTTP server endpoint can not be configured with SSL/TLS
support.

Note: Just providing these `--ssl-http-*` options to Perf Analyzer does not
ensure that SSL/TLS is used in communication. If SSL/TLS is not enabled on the
service endpoint, these options have no effect. The intent of exposing these
options to a user of Perf Analyzer is to allow them to configure Perf Analyzer
to benchmark a Triton service behind SSL/TLS-enabled endpoints. In other words,
if Triton is running behind a HTTPS server proxy, then these options would allow
Perf Analyzer to profile Triton via exposed HTTPS proxy.

