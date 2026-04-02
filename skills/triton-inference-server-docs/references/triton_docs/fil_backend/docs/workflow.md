* Development Workflow

# Development Workflow[#](#development-workflow "Link to this heading")

The `ci/local/build.sh` script is intended to help automate build and testing
during development. Usually it is sufficient to make a change and then run
this script without arguments to validate the change.

For tasks which require frequent rebuilds, it is sometimes slightly faster
to build on the host rather than in the container. In this case, running
`HOST_BUILD=1 ./ci/local/build.sh` using the [rapids\_triton\_dev conda environment](https://github.com/triton-inference-server/fil_backend/blob/main/conda/environments/rapids_triton_dev.yml) will perform the build of the FIL backend on the host but then use Docker to execute the tests in a controlled environment.

For complete information on other options that can be used with this script,
see the [documentation on running tests](https://github.com/triton-inference-server/fil_backend/blob/main/conda/environments/rapids_triton_dev.yml).