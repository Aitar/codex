* Deploying...

# Deploying Stable Diffusion Models with Triton and TensorRT[#](#deploying-stable-diffusion-models-with-triton-and-tensorrt "Link to this heading")

This example demonstrates how to deploy Stable Diffusion models in
Triton by leveraging the [TensorRT demo](https://github.com/NVIDIA/TensorRT/tree/release/10.4/demo/Diffusion)
pipeline and utilities.

Using the TensorRT demo as a base this example contains a reusable
[python based backend](../../../backend/docs/python_based_backends.md), [`/backend/diffusion/model.py`](https://github.com/triton-inference-server/tutorials/blob/main/Popular_Models_Guide/StableDiffusion/backend/diffusion/model.py),
suitable for deploying multiple versions and configurations of
Diffusion models.

For more information on Stable Diffusion please visit
[stable-diffusion-v1-5](https://huggingface.co/benjamin-paine/stable-diffusion-v1-5),
[stable-diffusion-xl](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0). For
more information on the TensorRT implementation please see the [TensorRT demo](https://github.com/NVIDIA/TensorRT/tree/release/10.4/demo/Diffusion).

> [!Note]
> This example is given as sample code and should be reviewed before use in production settings.

| [Requirements](#requirements) | [Building Server Image](#building-the-triton-inference-server-image) | [Stable Diffusion v1.5](#building-and-running-stable-diffusion-v-1-5) | [Stable Diffusion XL](#building-and-running-stable-diffusion-xl) | [Sending an Inference Request](#sending-an-inference-request) | [Model Configuration](docs/model_configuration.md) | [Sample Client](#sample-client) | [Known Issues and Limitations](#known-issues-and-limitations) |

## Requirements[#](#requirements "Link to this heading")

The following instructions require a Linux system with Docker
installed. For CUDA support, make sure your CUDA driver meets the
requirements in the âNVIDIA Driverâ section of [Deep Learning Framework
support matrix](https://docs.nvidia.com/deeplearning/frameworks/support-matrix/index.md).

## Building the Triton Inference Server Image[#](#building-the-triton-inference-server-image "Link to this heading")

The example is designed based on the
`nvcr.io/nvidia/tritonserver:24.08-py3` docker image and [TensorRT OSS v10.4](https://github.com/NVIDIA/TensorRT/releases/tag/v10.4).

A set of convenience scripts are provided to create a docker image
based on the `nvcr.io/nvidia/tritonserver:24.01-py3` image with the
dependencies for the TensorRT Stable Diffusion demo installed.

### Triton Inference Server + TensorRT OSS[#](#triton-inference-server-tensorrt-oss "Link to this heading")

#### Clone Repository[#](#clone-repository "Link to this heading")

```
git clone https://github.com/triton-inference-server/tutorials.git --single-branch
cd tutorials/Popular_Models_Guide/StableDiffusion
```

#### Build Tritonserver Diffusion Docker Image[#](#build-tritonserver-diffusion-docker-image "Link to this heading")

```
./build.sh
```

#### Included Models[#](#included-models "Link to this heading")

The `default` build includes model configuration files located in the
`/diffusion-models` folder. Example configurations are provided for
[`stable_diffusion_1_5`](https://github.com/triton-inference-server/tutorials/blob/main/Popular_Models_Guide/StableDiffusion/diffusion-models/stable_diffustion_1_5) and
[`stable_diffusion_xl`](https://github.com/triton-inference-server/tutorials/blob/main/Popular_Models_Guide/StableDiffusion/diffusion-models/stable_diffustion_xl).

Model artifacts and engine files are not included in the image but are
built into a volume mounted directory as a separate step.

## Building and Running Stable Diffusion v 1.5[#](#building-and-running-stable-diffusion-v-1-5 "Link to this heading")

### Start Tritonserver Diffusion Container[#](#start-tritonserver-diffusion-container "Link to this heading")

The following command starts a container and volume mounts the current
directory as `workspace`.

```
./run.sh
```

### Build Stable Diffusion v 1.5 Engine[#](#build-stable-diffusion-v-1-5-engine "Link to this heading")

> [!Note]
>
> The model
> [stable-diffusion-v1-5](https://huggingface.co/benjamin-paine/stable-diffusion-v1-5)
> requires login in to huggingface and acceptance of terms and
> conditions of use. Please set the environment variable HF\_TOKEN
> accordingly.

```
./scripts/build_models.sh --model stable_diffusion_1_5
```

#### Expected Output[#](#expected-output "Link to this heading")

```
 diffusion-models
|-- stable_diffusion_1_5
|   |-- 1
|   |   |-- 1.5-engine-batch-size-1
|   |   |-- 1.5-onnx
|   |   |-- 1.5-pytorch_model
|   `-- config.pbtxt
```

### Start a Server Instance[#](#start-a-server-instance "Link to this heading")

> [!Note]
> We use `EXPLICIT` model control mode for demonstration purposes to
> control which stable diffusion version is loaded. For production
> deployments please refer to [Secure Deployment Considerations](https://github.com/triton-inference-server/server/blob/main/docs/customization_guide/deploy.md)
> for more information on the risks associated with `EXPLICIT` mode.

```
tritonserver --model-repository diffusion-models --model-control-mode explicit --load-model stable_diffusion_1_5
```

#### Expected Output[#](#id1 "Link to this heading")

```
<SNIP>
I0229 20:15:52.125050 749 server.cc:676]
+----------------------+---------+--------+
| Model                | Version | Status |
+----------------------+---------+--------+
| stable_diffusion_1_5 | 1       | READY  |
+----------------------+---------+--------+

<SNIP>
```

## Building and Running Stable Diffusion XL[#](#building-and-running-stable-diffusion-xl "Link to this heading")

### Start Tritonserver Diffusion Container[#](#id2 "Link to this heading")

The following command starts a container and volume mounts the current
directory as `workspace`.

```
./run.sh
```

### Build Stable Diffusion XL Engine[#](#build-stable-diffusion-xl-engine "Link to this heading")

```
./scripts/build_models.sh --model stable_diffusion_xl
```

#### Expected Output[#](#id3 "Link to this heading")

```
 diffusion-models
 |-- stable_diffusion_xl
    |-- 1
    |   |-- xl-1.0-engine-batch-size-1
    |   |-- xl-1.0-onnx
    |   `-- xl-1.0-pytorch_model
    `-- config.pbtxt
```

### Start a Server Instance[#](#id4 "Link to this heading")

> [!Note]
> We use `EXPLICIT` model control mode for demonstration purposes to
> control which stable diffusion version is loaded. For production
> deployments please refer to [Secure Deployment Considerations](https://github.com/triton-inference-server/server/blob/main/docs/customization_guide/deploy.md)
> for more information on the risks associated with `EXPLICIT` mode.

```
tritonserver --model-repository diffusion-models --model-control-mode explicit --load-model stable_diffusion_xl
```

#### Expected Output[#](#id5 "Link to this heading")

```
<SNIP>
I0229 20:22:22.912465 1440 server.cc:676]
+---------------------+---------+--------+
| Model               | Version | Status |
+---------------------+---------+--------+
| stable_diffusion_xl | 1       | READY  |
+---------------------+---------+--------+

<SNIP>
```

## Sending an Inference Request[#](#sending-an-inference-request "Link to this heading")

Weâve provided a sample [client](https://github.com/triton-inference-server/tutorials/blob/main/Popular_Models_Guide/StableDiffusion/client.py) application to make
sending and receiving requests simpler.

### Start Tritonserver Diffusion Container[#](#id6 "Link to this heading")

In a separate terminal from the server start a new container.

The following command starts a container and volume mounts the current
directory as `workspace`.

```
./run.sh
```

### Send Prompt to Stable Diffusion 1.5[#](#send-prompt-to-stable-diffusion-1-5 "Link to this heading")

```
python3 client.py --model stable_diffusion_1_5 --prompt "butterfly in new york, 4k, realistic" --save-image
```

#### Example Output[#](#example-output "Link to this heading")

```
Client: 0 Throughput: 0.7201335361144658 Avg. Latency: 1.3677194118499756
Throughput: 0.7163933558221957 Total Time: 1.395881175994873
```

If `--save-image` is given then output images will be saved as jpegs.

`client_0_generated_image_0.jpg`

![sample_generated_image](../../../_images/client_0_generated_image_0_1_5.jpg)

### Send Prompt to Stable Diffusion XL[#](#send-prompt-to-stable-diffusion-xl "Link to this heading")

```
python3 client.py --model stable_diffusion_xl --prompt "butterfly in new york, 4k, realistic" --save-image
```

#### Example Output[#](#id7 "Link to this heading")

```
Client: 0 Throughput: 0.1825067711674996 Avg. Latency: 5.465569257736206
Throughput: 0.18224859609447058 Total Time: 5.487010717391968
```

If `--save-image` is given then output images will be saved as jpegs.

`client_0_generated_image_0.jpg`

![sample_generated_image](../../../_images/client_0_generated_image_0_xl.jpg)

## Sample Client[#](#sample-client "Link to this heading")

The sample [client](https://github.com/triton-inference-server/tutorials/blob/main/Popular_Models_Guide/StableDiffusion/client.py) application enables users to quickly
test the diffusion models under different concurrency scenarios. For a
full list and description of the client applicationâs options use:

```
python3 client.py --help
```

### Sending Concurrent Requests[#](#sending-concurrent-requests "Link to this heading")

To increase load and concurrency users can use the `clients` and
`requests` options to control the number of client processes and the
number of requests sent by each client.

#### Example: Ten Clients Sending Ten Requests Each[#](#example-ten-clients-sending-ten-requests-each "Link to this heading")

The following command enables ten clients each sending ten
requests. Each client is an independent process that sends its
requests one after the other in parallel with the other nine clients.

```
python3 client.py --model stable_diffusion_xl --requests 10 --clients 10
```

## Known Issues and Limitations[#](#known-issues-and-limitations "Link to this heading")

1. The diffusion backend doesnât yet support using an optional refiner
   model unlike the [demo](https://github.com/NVIDIA/TensorRT/tree/release/10.4/demo/Diffusion#generate-an-image-with-stable-diffusion-xl-guided-by-a-single-text-prompt) itâs based on. See also
   [demo\_txt2img\_xl.py](https://github.com/NVIDIA/TensorRT/blob/release/10.4/demo/Diffusion/demo_txt2img_xl.py)

