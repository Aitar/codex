* Using...

# Using Triton Inference Server as a shared library for execution on Jetson[#](#using-triton-inference-server-as-a-shared-library-for-execution-on-jetson "Link to this heading")

## Overview[#](#overview "Link to this heading")

This project demonstrates how to run C API applications using Triton Inference Server as a shared library. We also show how to build and execute such applications on Jetson.

### Prerequisites[#](#prerequisites "Link to this heading")

* JetPack >= 4.6
* OpenCV >= 4.1.1
* TensorRT >= 8.0.1.6

### Installation[#](#installation "Link to this heading")

Follow the installation instructions from the GitHub release page ([triton-inference-server/server](https://github.com/triton-inference-server/server/releases/)).

In our example, we placed the contents of downloaded release directory under `/opt/tritonserver`.

## Part 1. Concurrent inference and dynamic batching[#](#part-1-concurrent-inference-and-dynamic-batching "Link to this heading")

The purpose of the sample located under [concurrency\_and\_dynamic\_batching](concurrency_and_dynamic_batching/README.md)
is to demonstrate the important features of Triton Inference Server such as concurrent model execution and
dynamic batching. In order to do that, we implemented a people detection application using C API and Triton
Inference Server as a shared library.

## Part 2. Analyzing model performance with perf\_analyzer[#](#part-2-analyzing-model-performance-with-perf-analyzer "Link to this heading")

To analyze model performance on Jetson,
[perf\_analyzer](../../perf_analyzer/README.md)
tool is used. The `perf_analyzer` is included in the release tar file or can be
compiled from source.

From this directory of the repository, execute the following to evaluate model performance:

```
./perf_analyzer -m peoplenet -b 2 --service-kind=triton_c_api --model-repo=$(pwd)/concurrency_and_dynamic_batching/trtis_model_repo_sample_1 --triton-server-directory=/opt/tritonserver --concurrency-range 1:6 -f perf_c_api.csv
```

In the example above we saved the results as a `.csv` file. To visualize these
results, follow the steps described
[here](../../perf_analyzer/README.md).

