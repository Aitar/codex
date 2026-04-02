* Model...

# Model Instance Kind Example[#](#model-instance-kind-example "Link to this heading")

Triton model configuration allows users to provide kind to [instance group
settings.](../../../user_guide/model_configuration.md#instance-groups)
A python backend model can be written to respect the kind setting to control
the execution of a model instance either on CPU or GPU.

In this example, we demonstrate how this can be achieved for your python model.
We will use a `ResNet50` model as our base model for this example.

## Create a ResNet50 model repository[#](#create-a-resnet50-model-repository "Link to this heading")

We will use the files that come with this example to create the model
repository.

First, download the [client.py](https://github.com/triton-inference-server/python_backend/blob/main/examples/instance_kind/client.py), [config.pbtxt](https://github.com/triton-inference-server/python_backend/blob/main/examples/instance_kind/config.pbtxt),
[resnet50\_labels.txt](https://github.com/triton-inference-server/python_backend/blob/main/examples/instance_kind/resnet50_labels.txt), and [model.py](https://github.com/triton-inference-server/python_backend/blob/main/examples/instance_kind/model.py)
to your local machine.

Next, in the same directory with the four aforementioned files, create the model
repository with the following commands:

```
mkdir -p models/resnet50/1 &&
mv model.py models/resnet50/1/ &&
mv config.pbtxt models/resnet50/
```

## Pull the Triton Docker images[#](#pull-the-triton-docker-images "Link to this heading")

We need to install Docker and NVIDIA Container Toolkit before proceeding, refer
to the
[installation steps](https://github.com/triton-inference-server/server/tree/main/docs#installation).

To pull the latest containers, run the following commands:

```
docker pull nvcr.io/nvidia/tritonserver:<yy.mm>-py3
docker pull nvcr.io/nvidia/tritonserver:<yy.mm>-py3-sdk
```

See the installation steps above for the `<yy.mm>` version.

For example, if the latest version is `23.01`, the above commands translate
to the following:

```
docker pull nvcr.io/nvidia/tritonserver:23.01-py3
docker pull nvcr.io/nvidia/tritonserver:23.01-py3-sdk
```

Be sure to replace the `<yy.mm>` with the version pulled for all the remaining
parts of this example.

## Start the Triton Server[#](#start-the-triton-server "Link to this heading")

At the directory where we copied our resnet50 model (at where the âmodelsâ
folder is located), run the following command:

```
docker run --gpus all --shm-size 1G -it --rm -p 8000:8000 -v `pwd`:/instance_kind nvcr.io/nvidia/tritonserver:<yy.mm>-py3 /bin/bash
```

Inside the container, we need to install `torch`, `torchvision` and `pillow` to run
this example. We recommend to use `pip` method for the installation:

```
pip3 install torch==1.13.0+cu117 -f https://download.pytorch.org/whl/torch_stable.md torchvision==0.14.0+cu117 pillow
```

Finally, we need to start the Triton Server:

```
tritonserver --model-repository /instance_kind/models
```

To leave the container for the next step, press: `CTRL + P + Q`.

## Start the Triton SDK Container and Test Inference[#](#start-the-triton-sdk-container-and-test-inference "Link to this heading")

To start the sdk container, run the following command:

```
docker run --gpus all --network=host --pid=host --ipc=host -v `pwd`:/instance_kind -ti nvcr.io/nvidia/tritonserver:<yy.mm>-py3-sdk /bin/bash
```

The `client.py` requires the following packages to be installed: `torch`,
`torchvision`, `pillow` and `validators`. Similarly, we recommend to use `pip`
method for the installation:

```
pip3 install torch==1.13.0+cu117 -f https://download.pytorch.org/whl/torch_stable.md torchvision==0.14.0+cu117 pillow validators
```

Finally, letâs test an inference call with the following command:

```
python client.py
```

On a first run, a successful inference will print the following at the end:

```
Downloading: "https://github.com/NVIDIA/DeepLearningExamples/zipball/torchhub" to /root/.cache/torch/hub/torchhub.zip
Results is class: TABBY
PASS: ResNet50
```

It may take some time due to `torchhub` downloads, but any future calls
will be quicker, since the client will use already downloaded artifacts.

## Test Instance Kind[#](#test-instance-kind "Link to this heading")

Provided `config.pbtxt` sets the instance group setting to `KIND_CPU`,
which enables the execution of a model on the CPU.
To test that your model is actually loaded onto CPU, run the following:

```
python client.py -v
```

The `-v` argument asks the client to request modelâs confiuration from
the server and prints it in your console:

```
{
    ...,
    "instance_group": [
        {
            "name": "resnet50_0",
            "kind": "KIND_CPU",
            "count": 1,
            "gpus": [],
            "secondary_devices": [],
            "profile": [],
            "passive": false,
            "host_policy": ""
        }
    ],
    ...
}
Results is class: TABBY
PASS: ResNet50 instance kind
```

Based on the printed model config, we can see that `instance_group` field
has `kind` entry, which is set to `KIND_CPU`.

To change an `instance_group` parameter to `KIND_GPU`, a user can simply replace
`KIND_CPU` with `KIND_GPU` in the `config.pbtxt`. After restarting the server
with an updated config file, a successful inference request with `-v` argument
will result into the similar output, but with an updated `instance_group` entry:

```
{
    ...,
    "instance_group": [
        {
            "name": "resnet50_0",
            "kind": "KIND_GPU",
            "count": 1,
            "gpus": [
                0
            ],
            "secondary_devices": [],
            "profile": [],
            "passive": false,
            "host_policy": ""
        }
    ],
    ...
}
Results is class: TABBY
PASS: ResNet50 instance kind
```

It is also possible to load multiple model instances on CPU and GPU
if necessary.

Below the instance group setting will create two model instances,
one on CPU and other on GPU.

```
instance_group [{ kind: KIND_CPU }, { kind: KIND_GPU}]
```

For more information on possible model configurations,
check out the Triton Server documentation [here](../../../user_guide/model_configuration.md#model-configuration)

