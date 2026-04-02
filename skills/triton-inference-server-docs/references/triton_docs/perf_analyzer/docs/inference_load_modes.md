* [Performance Analyzer](../../perf_benchmark/perf_analyzer.md)
* Inference Load Modes

# Inference Load Modes[#](#inference-load-modes "Link to this heading")

Perf Analyzer has several modes for generating inference request load for a
model.

## Concurrency Mode[#](#concurrency-mode "Link to this heading")

In concurrency mode, Perf Analyzer attempts to send inference requests to the
server such that N requests are always outstanding during profiling. For
example, when using
[`--concurrency-range=4`](cli.md#concurrency-range-start-end-step), Perf Analyzer
will to attempt to have 4 outgoing inference requests at all times during
profiling.

## Periodic Concurrency Mode[#](#periodic-concurrency-mode "Link to this heading")

In periodic concurrency mode, Perf Analyzer will periodically launch a new set
of inference requests until the total number of inference requests that has been
launched since the beginning reaches N requests.

For example, when using `--periodic-concurrency-range 10:100:30`, Perf Analyzer
will start with 10 concurrent requests and for every step, it will launch 30 new
inference requests until the total number of requests launched since the
beginning reaches 100. Additionally, the user can also specify *when* to launch
the new requests by specifying `--request-period M`. This will set Perf Analyzer
to launch a new set of requests whenever *all* of the latest set of launched
concurrent requests received M number of responses back from the server.

The user can also specify custom parameters to the model using
`--request-parameter <name:value:type>` option.
For instance, passing `--request-parameter max_tokens:256:uint` will set an
additional parameter `max_tokens` of type `int` to 256 as part of the request.

```
perf_analyzer -m <model_name> -i grpc --async --streaming \
    --profile-export-file profile.json \
    --periodic-concurrency-range 10:100:30 \
    --request-period 10 \
    --request-parameter max_tokens:256:int
```

> **Note**
>
> The periodic concurrency mode is currently supported only by gRPC protocol and
> with [decoupled models](../../user_guide/decoupled_models.md).
> Additionally, the user must also specify a file where Perf Analyzer could dump all the
> profiled data using `--profile-export-file`.

## Request Rate Mode[#](#request-rate-mode "Link to this heading")

In request rate mode, Perf Analyzer attempts to send N inference requests per
second to the server during profiling. For example, when using
[`--request-rate-range=20`](cli.md#request-rate-range-start-end-step), Perf
Analyzer will attempt to send 20 requests per second during profiling.

## Custom Interval Mode[#](#custom-interval-mode "Link to this heading")

In custom interval mode, Perf Analyzer attempts to send inference requests
according to intervals (between requests, looping if necessary) provided by the
user in the form of a text file with one time interval (in microseconds) per
line. For example, when using
[`--request-intervals=my_intervals.txt`](cli.md#request-intervals-path),
where `my_intervals.txt` contains:

```
100000
200000
500000
```

Perf Analyzer will attempt to send requests at the following times: 0.1s, 0.3s,
0.8s, 0.9s, 1.1s, 1.6s, and so on, during profiling.

## Fixed Schedule Mode[#](#fixed-schedule-mode "Link to this heading")

In fixed schedule inference load mode, Perf Analyzer runs through the
[`--input-data`](cli.md#input-data-zero-random-path) JSON once. Each entry
represents a request and must have a `timestamp` âinputâ, which tells Perf
Analyzer when to send that request. A timestamp of `N` means Perf Analyzer will
send that request `N` milliseconds after the start of the benchmark. For
example:

```
# input_data.json
{
  "data": [
    {
      "payload": [{
          "model": "facebook/opt-125m",
          "messages": [{"role": "user","content": "What is the capital of France?"}],
          "max_completion_tokens": 1
        }],
      "timestamp": [1000]
    },
    {
      "payload": [{
          "model": "facebook/opt-125m",
          "messages": [{"role": "user","content": "What is 1+1?"}],
          "max_completion_tokens": 1
        }],
      "timestamp": [2000]
    }
  ]
}
```

Using this `input_data.json` with fixed schedule mode will run a benchmark that
sends 2 requests total.

The first request gets sent 1000ms after the start of the benchmark with the
prompt `What is the capital of France?`.

The second request gets sent 2000ms after the start of the benchmark with the
prompt `What is 1+1?`.

