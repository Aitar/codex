* [In-Process Triton Server API](../../../../client_guide/in_process.md)
* [Python](../../../../client_guide/python.md)
* Triton...

# Triton Inference Server Ray Serve Deployment[#](#triton-inference-server-ray-serve-deployment "Link to this heading")

Using the Triton Inference Server In-Process Python API you can
integrate triton server based models into any Python framework
including FastAPI and Ray Serve.

This directory contains an example Triton Inference Server Ray Serve
deployment based on FastAPI.

| [Installation](#installation) | [Run Deployment](#run-ray-serve-deployment) | [Send Requests](#send-requests-to-deployment) |

## Installation[#](#installation "Link to this heading")

The stable diffusion pipeline is based on the
[Popular\_Models\_Guide/StableDiffusion](https://github.com/triton-inference-server/tutorials/blob/main/Popular_Models_Guide/StableDiffusion)
tutorial.

### Clone Repository[#](#clone-repository "Link to this heading")

```
git clone https://github.com/triton-inference-server/tutorials.git
cd tutorials/Triton_Inference_Server_Python_API
```

### Build Tritonserver Image and Stable Diffusion Models[#](#build-tritonserver-image-and-stable-diffusion-models "Link to this heading")

Please note the following command will take many minutes depending on
your hardware configuration and network connection.

```
./build.sh --framework diffusion --build-models
```

## Run Ray Serve Deployment[#](#run-ray-serve-deployment "Link to this heading")

### Start Container[#](#start-container "Link to this heading")

The following command starts a container and volume mounts the current
directory as `workspace`.

```
./run.sh --framework diffusion
cd examples/rayserve
```

### Start Local Ray Cluster[#](#start-local-ray-cluster "Link to this heading")

The following command starts a local Ray cluster. It also starts
prometheus and grafana instances with default Ray and Ray Serve
metrics and dashboards enabled.

```
./start_ray.sh
```

### Run Deployment[#](#run-deployment "Link to this heading")

```
serve run tritonserver_deployment:deployment
```

## Send Requests to Deployment[#](#send-requests-to-deployment "Link to this heading")

The deployment includes two endpoints:

### `/identity`[#](#identity "Link to this heading")

The identity endpoint accepts a string and returns the same string.

#### Example Request[#](#example-request "Link to this heading")

```
curl --request GET "http://127.0.0.1:8000/identity?string_input=hello_world!"
```

#### Example Output[#](#example-output "Link to this heading")

```
"hello_world!"
```

### `/generate`[#](#generate "Link to this heading")

The generate endpoint accepts a prompt, generates an image based on
the prompt using stable diffusion, and saves the image to a file.

#### Example Request[#](#id1 "Link to this heading")

```
curl --request GET "http://127.0.0.1:8000/generate?prompt=car,model-t,realistic,4k&filename=/workspace/examples/rayserve/car_sample.jpg"
```

#### Example Output[#](#id2 "Link to this heading")

![car_sample](../../../../_images/car_sample.jpg)

## View Ray and Ray Serve Dashboards[#](#view-ray-and-ray-serve-dashboards "Link to this heading")

The Ray and Ray Serve dashboards are hosted on the default port and
can be used to visualize various metrics:

```
<IP_ADDRESS>:8265
```

## Stop the Ray Serve Cluster[#](#stop-the-ray-serve-cluster "Link to this heading")

The following command stops the local Ray cluster and also stops
prometheus and grafana instances.

```
./stop_ray.sh
```

