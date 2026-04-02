* Quick Start

# Quick Start[#](#quick-start "Link to this heading")

The steps below will guide you on how to start using Perf Analyzer.

## Step 1: Start Triton Container[#](#step-1-start-triton-container "Link to this heading")

```
export RELEASE=<yy.mm> # e.g. to use the release from the end of February of 2023, do `export RELEASE=23.02`

docker pull nvcr.io/nvidia/tritonserver:${RELEASE}-py3

docker run --gpus all --rm -it --net host nvcr.io/nvidia/tritonserver:${RELEASE}-py3
```

## Step 2: Download `simple` Model[#](#step-2-download-simple-model "Link to this heading")

```
# inside triton container
git clone --depth 1 https://github.com/triton-inference-server/server

mkdir model_repository ; cp -r server/docs/examples/model_repository/simple model_repository
```

## Step 3: Start Triton Server[#](#step-3-start-triton-server "Link to this heading")

```
# inside triton container
tritonserver --model-repository $(pwd)/model_repository &> server.log &

# confirm server is ready, look for 'HTTP/1.1 200 OK'
curl -v localhost:8000/v2/health/ready

# detach (CTRL-p CTRL-q)
```

## Step 4: Start Triton SDK Container[#](#step-4-start-triton-sdk-container "Link to this heading")

```
docker pull nvcr.io/nvidia/tritonserver:${RELEASE}-py3-sdk

docker run --gpus all --rm -it --net host nvcr.io/nvidia/tritonserver:${RELEASE}-py3-sdk
```

## Step 5: Run Perf Analyzer[#](#step-5-run-perf-analyzer "Link to this heading")

```
# inside sdk container
perf_analyzer -m simple
```

## Step 6: Observe and Analyze Output[#](#step-6-observe-and-analyze-output "Link to this heading")

```
$ perf_analyzer -m simple
*** Measurement Settings ***
  Batch size: 1
  Service Kind: Triton
  Using "time_windows" mode for stabilization
  Measurement window: 5000 msec
  Using synchronous calls for inference
  Stabilizing using average latency

Request concurrency: 1
  Client:
    Request count: 25348
    Throughput: 1407.84 infer/sec
    Avg latency: 708 usec (standard deviation 663 usec)
    p50 latency: 690 usec
    p90 latency: 881 usec
    p95 latency: 926 usec
    p99 latency: 1031 usec
    Avg HTTP time: 700 usec (send/recv 102 usec + response wait 598 usec)
  Server:
    Inference count: 25348
    Execution count: 25348
    Successful request count: 25348
    Avg request latency: 382 usec (overhead 41 usec + queue 41 usec + compute input 26 usec + compute infer 257 usec + compute output 16 usec)

Inferences/Second vs. Client Average Batch Latency
Concurrency: 1, throughput: 1407.84 infer/sec, latency 708 usec
```

We can see from the output that the model was able to complete approximately
1407.84 inferences per second, with an average latency of 708 microseconds per
inference request. Concurrency of 1 meant that Perf Analyzer attempted to always
have 1 outgoing request at all times.

