* Custom...

# Custom Metrics Example[#](#custom-metrics-example "Link to this heading")

In this section we demonstrate an end-to-end example for
[Custom Metrics API](../../README.md#custom-metrics) in Python backend. The
[model repository](../../../user_guide/model_repository.md)
should contain [custom\_metrics](https://github.com/triton-inference-server/python_backend/blob/main/examples/custom_metrics/model.py) model. The
[custom\_metrics](https://github.com/triton-inference-server/python_backend/blob/main/examples/custom_metrics/model.py) model uses
[Custom Metrics API](../../README.md#custom-metrics) to register and collect
custom metrics.

## Deploying the Custom Metrics Models[#](#deploying-the-custom-metrics-models "Link to this heading")

1. Create the model repository:

```
mkdir -p models/custom_metrics/1/

# Copy the Python models
cp examples/custom_metrics/model.py models/custom_metrics/1/model.py
cp examples/custom_metrics/config.pbtxt models/custom_metrics/config.pbtxt
```

2. Start the tritonserver:

```
tritonserver --model-repository `pwd`/models
```

3. Send inference requests to server:

```
python3 examples/custom_metrics/client.py
```

You should see an output similar to the output below in the client terminal:

```
custom_metrics example: found pattern '# HELP requests_process_latency_ns Cumulative time spent processing requests' in metrics
custom_metrics example: found pattern '# TYPE requests_process_latency_ns counter' in metrics
custom_metrics example: found pattern 'requests_process_latency_ns{model="custom_metrics",version="1"}' in metrics
PASS: custom_metrics
```

In the terminal that runs Triton Server, you should see an output similar to
the output below:

```
Cumulative requests processing latency: 223406.0
```

The [model.py](https://github.com/triton-inference-server/python_backend/blob/main/examples/custom_metrics/model.py) model file is heavily commented with
explanations about each of the function calls.

### Explanation of the Client Output[#](#explanation-of-the-client-output "Link to this heading")

The [client.py](https://github.com/triton-inference-server/python_backend/blob/main/examples/custom_metrics/client.py) sends a HTTP request with url
`http://localhost:8002/metrics` to fetch the metrics from Triton server. The
client then verifies if the custom metrics added in the model file are
correctly reported.

