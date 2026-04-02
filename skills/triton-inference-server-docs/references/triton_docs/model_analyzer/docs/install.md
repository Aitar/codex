* Recommended...

# Recommended Installation Method[#](#recommended-installation-method "Link to this heading")

  

## Triton SDK Container with Docker Launch Mode[#](#triton-sdk-container-with-docker-launch-mode "Link to this heading")

---

The recommended way to install Model Analyzer is from the Triton SDK docker
container available on the [NVIDIA GPU Cloud
Catalog](https://ngc.nvidia.com/catalog/containers/nvidia:tritonserver).

**1. Choose a release version**
The format is `<rYY.MM>` where, `YY`=year and `MM`=month

For example, the release from May of 2022 is `<r22.05>`

```
export RELEASE=<rYY:MM>
```

**2. Pull the SDK container**

```
docker pull nvcr.io/nvidia/tritonserver:${RELEASE}-py3-sdk
```

**3. Run the SDK container**

```
docker run -it --gpus all \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v <path-to-output-model-repo>:<path-to-output-model-repo> \
    --net=host nvcr.io/nvidia/tritonserver:${RELEASE}-py3-sdk
```

**Replacing** `<path-to-output-model-repo>` with the
***absolute* *path*** to the directory where the output model repository
will be located.
This ensures the Triton SDK container has access to the model
config variants that Model Analyzer creates.  
  
**Important:** You must ensure the `<path-to-output-model-repo>` is identical on both sides of the mount (or else Tritonserver cannot load the model)

**4. Run Model Analyzer with Docker Launch Mode**
Be sure to use `--triton-launch-mode=docker`, when running Model Analyzer.

# Alternative Installation Methods[#](#alternative-installation-methods "Link to this heading")

* [Specific Version with Local Launch Mode](#specific-version-with-local-launch-mode)
* [Main with Local Launch Mode](#main-branch-with-local-launch-mode)
* [Using Pip](#pip)
* [From the Source](#from-the-source)

  

## Specific Version with Local Launch Mode[#](#specific-version-with-local-launch-mode "Link to this heading")

---

This method allows you build a specific version of Model Analyzerâs
docker.
This installation method uses `--triton-launch-mode=local` by
default, as all the dependencies will be available.

**1. Clone Model Analyzerâs Git Repository**

```
git clone https://github.com/triton-inference-server/model_analyzer.git -b <rYY.MM>
```

**Replacing** `<rYY.MM>` with the version of Model Analyzer you want to install.
For example, `r22.05` is the release for May of 2022

**2. Build the Docker Image**

```
cd ./model_analyzer

docker build --pull -t model-analyzer .
```

Model Analyzerâs Dockerfile bases the container on the corresponding `tritonserver` (from step 1)
containers from NGC.

**3. Run the Container**

```
docker run -it --rm --gpus all \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v <path-to-triton-model-repo>:<path-to-triton-model-repo> \
    -v <path-to-output-model-repo>:<path-to-output-model-repo> \
    --net=host model-analyzer
```

**Replacing** `<path-to-triton-model-repo>` with the
***absolute* *path*** to the directory where the `Triton` model repository
will be located.
**Replacing** `<path-to-output-model-repo>` with the
***absolute* *path*** to the directory where the `output` model repository
will be located.

## Main Branch with Local Launch Mode[#](#main-branch-with-local-launch-mode "Link to this heading")

---

This method allows you build a docker container using the `main` branch of Model Analyzer.
This installation method uses `--triton-launch-mode=local` by
default, as all the dependencies will be available.

**1. Build Triton SDK Container from Main**
Follow the instructions found at
[Build SDK Image](../../customization_guide/test.md#build-sdk-image)

**2. Build Model Analyzerâs Main Docker Image**

```
git clone https://github.com/triton-inference-server/model_analyzer.git -b main

cd ./model_analyzer

docker build -t model-analyzer --build-arg TRITONSDK_BASE_IMAGE=<built-sdk-image> .
```

**Replacing** `<built-sdk-image>` with the ***absolute* *path*** to the directory where the Triton SDK image is located

**3. Run the Container**

```
docker run -it --rm --gpus all \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v <path-to-triton-model-repo>:<path-to-triton-model-repo> \
    -v <path-to-output-model-repo>:<path-to-output-model-repo> \
    --net=host model-analyzer
```

**Replacing** `<path-to-triton-model-repo>` with the
***absolute* *path*** to the directory where the `Triton` model repository
will be located.
**Replacing** `<path-to-output-model-repo>` with the
***absolute* *path*** to the directory where the `output` model repository
will be located.

## Pip[#](#pip "Link to this heading")

---

You can install pip using:

```
sudo apt-get update && sudo apt-get install python3-pip
```

Model analyzer can be installed with:

```
pip3 install triton-model-analyzer
```

If you encounter any errors installing dependencies like `numba`, make sure that
you have the latest version of `pip` using:

```
pip3 install --upgrade pip
```

You can then try installing model analyzer again.

Optionally, if you want Model Analyzer to generate PDF reports instead of HTML,
you should also run the following:

```
sudo apt-get update && sudo apt-get install wkhtmltopdf
```

## From the Source[#](#from-the-source "Link to this heading")

---

To build model analyzer from the source. Youâll need to install the same
dependencies (tritonclient) mentioned in [Pip Install](#pip).  
After that, you can use the following commands:

```
git clone https://github.com/triton-inference-server/model_analyzer
cd model_analyzer
./build_wheel.sh <path to perf_analyzer> true
```

In the final command above we are building the triton-model-analyzer wheel. You
will need to provide the `build_wheel.sh` script with two arguments. The first
is the path to the `perf_analyzer` binary that you would like Model Analyzer to
use. The second is whether you want this wheel to be linux specific. Currently,
this argument must be set to `true` as perf analyzer is supported only on linux.
This will create a wheel file in the `wheels` directory named
`triton-model-analyzer-<version>-py3-none-manylinux1_x86_64.whl`. We can now
install this with:

```
pip3 install wheels/triton-model-analyzer-*.whl
```

After these steps, `model-analyzer` executable should be available in `$PATH`.

**Notes:**

* Triton Model Analyzer supports all the GPUs supported by the DCGM library. See
  [DCGM Supported
  GPUs](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/getting-started.md#supported-platforms)
  for more information.

