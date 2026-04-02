* Performance Analyzer

# Performance Analyzer[#](#performance-analyzer "Link to this heading")

## Triton Performance Analyzer[#](#triton-performance-analyzer "Link to this heading")

Triton Performance Analyzer is CLI tool which can help you optimize the
inference performance of models running on Triton Inference Server by
measuring changes in performance as you experiment with different
optimization strategies.

## Features[#](#features "Link to this heading")

### Inference Load Modes[#](#inference-load-modes "Link to this heading")

* [Concurrency Mode](docs/inference_load_modes.md#concurrency-mode)
  simlulates load by maintaining a specific concurrency of outgoing
  requests to the server
* [Request Rate
  Mode](docs/inference_load_modes.md#request-rate-mode) simulates
  load by sending consecutive requests at a specific rate to the server
* [Custom Interval
  Mode](docs/inference_load_modes.md#custom-interval-mode) simulates
  load by sending consecutive requests at specific intervals to the
  server

### Performance Measurement Modes[#](#performance-measurement-modes "Link to this heading")

* [Time Windows Mode](docs/measurements_metrics.md#time-windows)
  measures model performance repeatedly over a specific time interval
  until performance has stabilized
* [Count Windows Mode](docs/measurements_metrics.md#count-windows)
  measures model performance repeatedly over a specific number of
  requests until performance has stabilized

### Other Features[#](#other-features "Link to this heading")

* [Sequence Models](../user_guide/architecture.md#stateful-models),
  [Ensemble Models](../user_guide/architecture.md#ensemble-models),
  and [Decoupled Models](../user_guide/decoupled_models.md) can be
  profiled in addition to standard/stateless/coupled models
* [Input Data](docs/input_data.md) to model inferences can be
  auto-generated or specified as well as verifying output

## Quick Start[#](#quick-start "Link to this heading")

The steps below will guide you on how to start using Perf Analyzer.

### Step 1: Start Triton Container[#](#step-1-start-triton-container "Link to this heading")

```
export RELEASE=<yy.mm> # e.g. to use the release from the end of February of 2023, do `export RELEASE=23.02`

docker pull nvcr.io/nvidia/tritonserver:${RELEASE}-py3

docker run --gpus all --rm -it --net host nvcr.io/nvidia/tritonserver:${RELEASE}-py3
```

### Step 2: Download `simple` Model[#](#step-2-download-simple-model "Link to this heading")

```
# inside triton container
git clone --depth 1 https://github.com/triton-inference-server/server

mkdir model_repository ; cp -r server/docs/examples/model_repository/simple model_repository
```

### Step 3: Start Triton Server[#](#step-3-start-triton-server "Link to this heading")

```
# inside triton container
tritonserver --model-repository $(pwd)/model_repository &> server.log &

# confirm server is ready, look for 'HTTP/1.1 200 OK'
curl -v localhost:8000/v2/health/ready

# detach (CTRL-p CTRL-q)
```

### Step 4: Start Triton SDK Container[#](#step-4-start-triton-sdk-container "Link to this heading")

```
docker pull nvcr.io/nvidia/tritonserver:${RELEASE}-py3-sdk

docker run --gpus all --rm -it --net host nvcr.io/nvidia/tritonserver:${RELEASE}-py3-sdk
```

### Step 5: Run Perf Analyzer[#](#step-5-run-perf-analyzer "Link to this heading")

```
# inside sdk container
perf_analyzer -m simple
```

See the full [quick start guide](docs/quick_start.md) for additional
tips on how to analyze output.

## Documentation[#](#documentation "Link to this heading")

* [Installation](docs/install.md)
* [Perf Analyzer CLI](docs/cli.md)
* [Inference Load Modes](docs/inference_load_modes.md)
* [Input Data](docs/input_data.md)
* [Measurements & Metrics](docs/measurements_metrics.md)
* [Benchmarking](docs/benchmarking.md)

## Contributing[#](#contributing "Link to this heading")

Contributions to Triton Perf Analyzer are more than welcome. To
contribute please review the [contribution
guidelines](https://github.com/triton-inference-server/server/blob/main/CONTRIBUTING.md),
then fork and create a pull request.

## Reporting problems, asking questions[#](#reporting-problems-asking-questions "Link to this heading")

We appreciate any feedback, questions or bug reporting regarding this
project. When help with code is needed, follow the process outlined in
the Stack Overflow (<https://stackoverflow.com/help/mcve>) document.
Ensure posted examples are:

* minimal - use as little code as possible that still produces the same
  problem
* complete - provide all parts needed to reproduce the problem. Check
  if you can strip external dependency and still show the problem. The
  less time we spend on reproducing problems the more time we have to
  fix it
* verifiable - test the code youâre about to provide to make sure it
  reproduces the problem. Remove all other problems that are not
  related to your request/question.

