* Building Triton

# Building Triton[#](#building-triton "Link to this heading")

This section describes how to build the Triton server from source. For
information on building the Triton client libraries and examples see
[Client Libraries and
Examples](https://github.com/triton-inference-server/client). For
information on building the Triton SDK container see [Build SDK
Image](test.md#build-sdk-image). For information on testing your
Triton build see [Testing Triton](test.md).

You can create a customized Triton Docker image that contains a subset
of the released backends without building from source. For example,
you may want a Triton image that contains only the TensorRT and Python
backends. For this type of customization you donât need to build
Triton from source and instead can use [the *compose*
utility](compose.md).

The Triton source is distributed across multiple GitHub repositories
that together can be built and installed to create a complete Triton
installation. Triton server is built using CMake and (optionally)
Docker. To simplify the build process, Triton provides a
[build.py](https://github.com/triton-inference-server/server/blob/main/build.py) script.
The build.py script will generate the CMake and Docker build steps required to
build Triton, and will optionally invoke those steps or leave the invocation to
you, as described below.

The build.py script currently supports building Triton for the
following platforms. See [Building on Unsupported
Platforms](#building-on-unsupported-platforms) if you are attempting
to build Triton on a platform that is not listed here.

* [Ubuntu 22.04, x86-64](#building-for-ubuntu-22-04)
* [Jetpack 4.x, NVIDIA Jetson (Xavier, Nano, TX2)](#building-for-jetpack-4x)
* [Windows 10, x86-64](#building-for-windows-10)

If you are developing or debugging Triton, see [Development and
Incremental Builds](#development-and-incremental-builds) for information
on how to perform incremental build.

## Building for Ubuntu 22.04[#](#building-for-ubuntu-22-04 "Link to this heading")

For Ubuntu-22.04, build.py supports both a Docker build and a
non-Docker build.

* [Build using Docker](#building-with-docker) and the PyTorch
  Docker image from [NVIDIA GPU Cloud (NGC)](https://ngc.nvidia.com).
* [Build without Docker](#building-without-docker).

### Building With Docker[#](#building-with-docker "Link to this heading")

The easiest way to build Triton is to use Docker. The result of the
build will be a Docker image called *tritonserver* that will contain
the tritonserver executable in /opt/tritonserver/bin and the required
shared libraries in /opt/tritonserver/lib. The backends and
repository-agents built for Triton will be in
/opt/tritonserver/backends and /opt/tritonserver/repoagents,
respectively.

The first step for the build is to clone the
[triton-inference-server/server](https://github.com/triton-inference-server/server)
repo branch for the release you are interested in building (or the
*main* branch to build from the development branch). Then run build.py
as described below. The build.py script performs these steps when
building with Docker.

* In the *build* subdirectory of the server repo, generate the
  docker\_build script, the cmake\_build script and the Dockerfiles
  needed to build Triton. If you use the âdryrun flag, build.py will
  stop here so that you can examine these files.
* Run the docker\_build script to perform the Docker-based build. The
  docker\_build script performs the following steps.

  + Build the *tritonserver\_buildbase* Docker image that collects all
    the build dependencies needed to build Triton. The
    *tritonserver\_buildbase* image is based on a minimal/base
    image. When building with GPU support (âenable-gpu), the *min*
    image is the
    [<xx.yy>-py3-min](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/tritonserver)
    image pulled from [NGC](https://ngc.nvidia.com) that contains the
    CUDA, cuDNN, TensorRT and other dependencies that are required to
    build Triton. When building without GPU support, the *min* image
    is the standard ubuntu:22.04 image.
  + Run the cmake\_build script within the *tritonserver\_buildbase*
    image to actually build Triton. The cmake\_build script performs
    the following steps.

    - Invoke CMake in the server repo to build Tritonâs core shared
      library and *tritonserver* executable.
    - Clone each requested backend and build it using CMake. For
      example, the ONNX Runtime backend is built using
      [triton-inference-server/onnxruntime\_backend/CMakeLists.txt](https://github.com/triton-inference-server/onnxruntime_backend/blob/main/CMakeLists.txt). Some
      of the backends may use Docker as part of their build (for
      example [ONNX
      Runtime](https://github.com/triton-inference-server/onnxruntime_backend)
      and
      [OpenVINO](https://github.com/triton-inference-server/openvino_backend)). If
      you donât want to use Docker in those cases you must consult the
      build process for those backends.
    - Clone each repository agent and build it using the CMake file
      from the corresponding repo. For example, the
      [Checksum](https://github.com/triton-inference-server/checksum_repository_agent)
      repository agent is built using
      [triton-inference-server/checksum\_repository\_agent/CMakeLists.txt](https://github.com/triton-inference-server/checksum_repository_agent/blob/main/CMakeLists.txt).
  + Copy the built artifacts out of the container and into the build
    subdirectory on the host system.
  + Create the final *tritonserver* Docker image that contains the
    libraries, executables and other artifacts from the build.
  + Create a *tritonserver\_cibase* Docker image that contains the QA
    artifacts needed for testing, as described in [Testing
    Triton](test.md).

By default, build.py does not enable any of Tritonâs optional features
but you can enable all features, backends, and repository agents with
the âenable-all flag. The -v flag turns on verbose output.

```
$ ./build.py -v --enable-all
```

If you want to enable only certain Triton features, backends and
repository agents, do not specify âenable-all. Instead you must
specify the individual flags as documented by âhelp.

#### Building With Specific GitHub Branches[#](#building-with-specific-github-branches "Link to this heading")

As described above, the build is performed in the server repo, but
source from several other repos is fetched during the build
process. Typically you do not need to specify anything about these
other repos, but if you want to control which branch is used in these
other repos you can as shown in the following example.

```
$ ./build.py ... --repo-tag=common:<container tag> --repo-tag=core:<container tag> --repo-tag=backend:<container tag> --repo-tag=thirdparty:<container tag> ... --backend=tensorrt:<container tag> ... --repoagent=checksum:<container tag> ...
```

If you are building on a release branch then `<container tag>` will
default to the branch name. For example, if you are building on the
r24.12 branch, `<container tag>` will default to r24.12. If you are
building on any other branch (including the *main* branch) then
`<container tag>` will default to âmainâ. Therefore, you typically do
not need to provide `<container tag>` at all (nor the preceding
colon). You can use a different `<container tag>` for a component to
instead use the corresponding branch/tag in the build. For example, if
you have a branch called âmybranchâ in the
[onnxruntime\_backend](https://github.com/triton-inference-server/onnxruntime_backend)
repo that you want to use in the build, you would specify
âbackend=onnxruntime:mybranch.

#### CPU-Only Build[#](#cpu-only-build "Link to this heading")

If you want to build without GPU support you must specify individual
feature flags and not include the `--enable-gpu` and
`--enable-gpu-metrics` flags. Only the following backends are
available for a non-GPU / CPU-only build: `identity`, `repeat`, `ensemble`,
`square`, `pytorch`, `onnxruntime`, `openvino`,
`python` and `fil`.

CPU-only builds of the PyTorch backends require some CUDA stubs
and runtime dependencies that are not present in the CPU-only base container.
These are retrieved from a GPU base container, which can be changed with the
`--image=gpu-base,nvcr.io/nvidia/tritonserver:<xx.yy>-py3-min` flag.

### Building Without Docker[#](#building-without-docker "Link to this heading")

To build Triton without using Docker you must install the build
dependencies that are handled automatically when building with Docker.

The first step for the build is to clone the
[triton-inference-server/server](https://github.com/triton-inference-server/server)
repo branch for the release you are interested in building (or the
*main* branch to build from the development branch).

To determine what dependencies are required by the build, run build.py
with the âdryrun flag, and then looking in the build subdirectory at
Dockerfile.buildbase.

```
$ ./build.py -v --enable-all
```

From Dockerfile.buildbase you can see what dependencies you need to
install on your host system. Note that when building with âenable-gpu
(or âenable-all), Dockerfile.buildbase depends on the
[<xx.yy>-py3-min](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/tritonserver)
image pulled from [NGC](https://ngc.nvidia.com). Unfortunately, a
Dockerfile is not currently available for the
[<xx.yy>-py3-min](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/tritonserver)
image. Instead, you must manually install [CUDA and
cuDNN](#cuda-cublas-cudnn) and [TensorRT](#tensorrt) dependencies as
described below.

Once you have installed these dependencies on your build system you
can then use build.py with the âno-container-build flag to build
Triton.

```
$ ./build.py -v --no-container-build --build-dir=`pwd`/build --enable-all
```

See [Building with Docker](#building-with-docker) for more details on how the
cmake\_build script is used to perform the build.

#### CUDA, cuBLAS, cuDNN[#](#cuda-cublas-cudnn "Link to this heading")

For Triton to support NVIDIA GPUs you must install CUDA, cuBLAS and
cuDNN. These libraries must be installed on the system include and
library paths so that they are available for the build. The version of
the libraries used for a given release can be found in the [Framework
Containers Support
Matrix](https://docs.nvidia.com/deeplearning/frameworks/support-matrix/index.md).

For a given version of Triton you can attempt to build with
non-supported versions of the libraries but you may have build or
execution issues since non-supported versions are not tested.

#### TensorRT[#](#tensorrt "Link to this heading")

The TensorRT headers and libraries must be installed on system include
and library paths so that they are available for the build. The
version of TensorRT used in a given release can be found in the
[Framework Containers Support
Matrix](https://docs.nvidia.com/deeplearning/frameworks/support-matrix/index.md).

For a given version of Triton you can attempt to build with
non-supported versions of TensorRT but you may have build or execution
issues since non-supported versions are not tested.

## Building for Windows 10[#](#building-for-windows-10 "Link to this heading")

For Windows 10, build.py supports both a Docker build and a non-Docker
build in a similar way as described for [Ubuntu](#building-for-ubuntu-22-04). The primary
difference is that the minimal/base image used as the base of
Dockerfile.buildbase image can be built from the provided
[Dockerfile.win10.min](https://github.com/triton-inference-server/server/blob/main/Dockerfile.win10.min)
file as described in [Windows 10 âMinâ Image](#windows-10-min-image). When running build.py
use the âimage flag to specify the tag that you assigned to this
image. For example, âimage=base,win10-py3-min.

### Windows and Docker[#](#windows-and-docker "Link to this heading")

Depending on your version of Windows 10 and your version of Docker you
may need to perform these additional steps before any of the following
step.

* Set your Docker to work with âWindows containersâ. Right click on
  the whale icon in the lower-right status area and select âSwitch to
  Windows containersâ.

### Windows 10 âMinâ Image[#](#windows-10-min-image "Link to this heading")

The âminâ container describes the base dependencies needed to perform
the Windows build. The Windows min container is
[Dockerfile.win10.min](https://github.com/triton-inference-server/server/blob/main/Dockerfile.win10.min).

Before building the min container you must download the appropriate
cuDNN and TensorRT versions and place them in the same directory as
Dockerfile.win10.min.

* For cuDNN the CUDNN\_VERSION and CUDNN\_ZIP arguments defined in
  Dockerfile.win10.min indicate the version of cuDNN that your should
  download from https://developer.nvidia.com/rdp/cudnn-download.
* For TensorRT the TENSORRT\_VERSION and TENSORRT\_ZIP arguments defined
  in Dockerfile.win10.min indicate the version of TensorRT that your
  should download from
  https://developer.nvidia.com/nvidia-tensorrt-download.

After downloading the zip files for cuDNN and TensorRT, you build the
min container using the following command.

```
$ docker build -t win10-py3-min -f Dockerfile.win10.min .
```

### Build Triton Server[#](#build-triton-server "Link to this heading")

Triton is built using the build.py script. The build system must have
Docker, Python3 (plus pip installed *docker* module) and git installed
so that it can execute build.py and perform a docker build. By
default, build.py does not enable any of Tritonâs optional features
and so you must enable them explicitly. The following build.py
invocation builds all features and backends available on windows.

```
python build.py --cmake-dir=<path/to/repo>/build --build-dir=/tmp/citritonbuild --no-container-pull --image=base,win10-py3-min --enable-logging --enable-stats --enable-tracing --enable-gpu --endpoint=grpc --endpoint=http --repo-tag=common:<container tag> --repo-tag=core:<container tag> --repo-tag=backend:<container tag> --repo-tag=thirdparty:<container tag> --backend=ensemble --backend=tensorrt:<container tag> --backend=onnxruntime:<container tag> --backend=openvino:<container tag> --backend=python:<container tag>
```

If you are building on *main* branch then `<container tag>` will
default to âmainâ. If you are building on a release branch then
`<container tag>` will default to the branch name. For example, if you
are building on the r24.12 branch, `<container tag>` will default to
r24.12. Therefore, you typically do not need to provide `<container tag>` at all (nor the preceding colon). You can use a different
`<container tag>` for a component to instead use the corresponding
branch/tag in the build. For example, if you have a branch called
âmybranchâ in the
[onnxruntime\_backend](https://github.com/triton-inference-server/onnxruntime_backend)
repo that you want to use in the build, you would specify
âbackend=onnxruntime:mybranch.

### Extract Build Artifacts[#](#extract-build-artifacts "Link to this heading")

When build.py completes, a Docker image called *tritonserver* will
contain the built Triton Server executable, libraries and other
artifacts. Windows containers do not support GPU access so you likely
want to extract the necessary files from the tritonserver image and
run them directly on your host system. All the Triton artifacts can be
found in /opt/tritonserver directory of the tritonserver image. Your
host system will need to install the CUDA, cuDNN, TensorRT and other
dependencies that were used for the build.

## Building on Unsupported Platforms[#](#building-on-unsupported-platforms "Link to this heading")

Building for an unsupported OS and/or hardware platform is
possible. All of the build scripting, Dockerfiles and CMake
invocations are included in the public repos or are generated by
build.py as described in [Building with Docker](#building-with-docker). From
these files you can find the required dependencies and CMake
invocations. However, due to differences in compilers, libraries,
package management, etc. you may have to make changes in the build
scripts, Dockerfiles, CMake files and the source code.

To see the generated build scripts and Dockerfiles referred to below,
use:

```
$ ./build.py -v --enable-all --dryrun
```

You should familiarize yourself with the build process for supported
platforms by reading the above documentation and then follow the
process for the supported platform that most closely matches the
platform you are interested in (for example, if you are trying to
build for RHEL/x86-64 then follow the [Building for Ubuntu
22.04](#building-for-ubuntu-22-04) process. You will likely need to
make changes in the following areas and then manually run docker\_build
and cmake\_build or the equivalent commands to perform a build.

* The generated Dockerfiles install dependencies for the build using
  platform-specific packaging tools, for example, apt-get for
  Ubuntu. You will need to change build.py to use the packaging tool
  appropriate for your platform.
* The package and libraries names for your platform may differ from
  those used by the generated Dockerfiles. You will need to find the
  corresponding packages on libraries on your platform.
* Your platform may use a different compiler or compiler version than
  the support platforms. As a result you may encounter build errors
  that need to be fixed by editing the source code or changing the
  compilation flags.
* Triton depends on a large number of open-source packages that it
  builds from source. If one of these packages does not support your
  platform then you may need to disable the Triton feature that
  depends on that package. For example, Triton supports the S3
  filesystem by building the aws-sdk-cpp package. If aws-sdk-cpp
  doesnât build for your platform then you can remove the need for
  that package by not specifying âfilesystem=s3 when you run
  build.py. In general, you should start by running build.py with the
  minimal required feature set.
* By default, the
  [PyTorch](https://github.com/triton-inference-server/pytorch_backend)
  backend build extracts pre-built shared libraries from The PyTorch
  NGC container. But the build can also use PyTorch shared libraries
  that you build separately for your platform. See the pytorch\_backend
  build process for details.

## Development and Incremental Builds[#](#development-and-incremental-builds "Link to this heading")

### Development Builds Without Docker[#](#development-builds-without-docker "Link to this heading")

If you are [building without Docker](#building-without-docker) use the
CMake invocation steps in cmake\_build to invoke CMake to set-up a
build environment where you can invoke make/msbuild.exe to incremental
build the Triton core, a backend, or a repository agent.

### Development Builds With Docker[#](#development-builds-with-docker "Link to this heading")

If you are [building with Docker](#building-with-docker), the generated
*tritonserver\_buildbase* image contains all the dependencies needed to
perform a full or incremental build. Within *tritonserver\_buildbase*,
/workspace/build/cmake\_build contains the CMake invocations that are
used to build the Triton core, the backends, and the repository
agents.

To perform an incremental build within the *tritonserver\_buildbase*
container, map your source into the container and then run the
appropriate CMake and `make` (or `msbuild.exe`) steps from cmake\_build
within the container.

#### Development Build of Triton Core[#](#development-build-of-triton-core "Link to this heading")

Assuming you have a clone of the [server
repo](https://github.com/triton-inference-server/server) on your host
system where you are making changes and you want to perform
incremental builds to test those changes. Your source code is in
/home/me/server. Run the *tritonserver\_buildbase* container and map
your server source directory into the container at /server.

```
$ docker run -it --rm -v/home/me/server:/server tritonserver_buildbase bash
```

Look at /workspace/build/cmake\_build within the container for the
section of commands that build âTriton core libraryâ. You can follow
those command exactly, or you can modify them to change the build
directory or the CMake options. You **must** change the CMake command
to use /server instead of /workspace as the location for the
CMakeLists.txt file and source:

```
$ cmake <options> /server
```

Then you can change directory into the build directory and run `make`
(or `msbuild.exe`) as shown in cmake\_build. As you make changes to the
source on your host system, you can perform incremental builds by
re-running `make` (or `msbuild.exe`).

#### Development Build of Backend or Repository Agent[#](#development-build-of-backend-or-repository-agent "Link to this heading")

Performing a full or incremental build of a backend or repository
agent is similar to building the Triton core. As an example we will
use the TensorRT backend. Assuming you have a clone of the [TensorRT
backend
repo](https://github.com/triton-inference-server/tensorrt_backend) on
your host system where you are making changes and you want to perform
incremental builds to test those changes. Your source code is in
/home/me/tritonserver\_backend. Run the *tritonserver\_buildbase*
container and map your TensorRT backend source directory into the
container at /tensorrt\_backend. Note that some backends will use
Docker as part of their build, and so the hostâs Docker registry must
be made available within the *tritonserver\_buildbase* by mounting
docker.sock (on Windows use
-v.\pipe\docker\_engine:.\pipe\docker\_engine).

```
$ docker run -it --rm -v/var/run/docker.sock:/var/run/docker.sock -v/home/me/tensorrt_backend:/tensorrt_backend tritonserver_buildbase bash
```

Look at /workspace/build/cmake\_build within the container for the
section of commands that build âTensorRT backendâ. You can follow
those command exactly, or you can modify them to change the build
directory or the CMake options. You **must** change the CMake command
to use /tensorrt\_backend instead of /workspace as the location for the
CMakeLists.txt file and source:

```
$ cmake <options> /tensorrt_backend
```

Then you can change directory into the build directory and run `make`
(or `msbuild.exe`) as shown in cmake\_build. As you make changes to the
source on your host system, you can perform incremental builds by
re-running `make` (or `msbuild.exe`).

### Building with Debug Symbols[#](#building-with-debug-symbols "Link to this heading")

To build with Debug symbols, use the âbuild-type=Debug argument while
launching build.py. If building directly with CMake use
-DCMAKE\_BUILD\_TYPE=Debug. You can then launch the built server with
gdb and see the debug symbols/information in the gdb trace.

