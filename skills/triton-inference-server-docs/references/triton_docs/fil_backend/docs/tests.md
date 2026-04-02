* Running Tests

# Running Tests[#](#running-tests "Link to this heading")

For developers working on the FIL backend, the easiest way to run tests is to
invoke the `ci/local/build.sh` script, which will build the server image
and a test image then run a container based on that image which runs the
complete test suite.

One of the most time-consuming parts of running the test suite is
training the end-to-end test models. The `ci/local/build.sh` script will
cache trained models between runs in `qa/L0_e2e/model_repository` and
`qa/L0_e2e/cpu_model_repository`. Sometimes, you may make a change which
invalidates previously generated models. In such cases, you can clear these
directories in order to start fresh.

The `ci/local/build.sh` script uses the following environment variables to
control build and execution of tests:

* `RETRAIN`: If set to 1, retrain test models.
* `USE_CLIENT_WHEEL`: If set to 1, install the Triton client from a wheel
  copied from Tritonâs SDK image. This is useful for testing on ARM
  machines, where the Triton Python client is not available via pip.
* `SDK_IMAGE`: If set, copy the Triton client wheel from this specific Docker
  SDK image
* `HOST_BUILD`: Build on the host rather than via Docker. This can be useful
  for rapid iteration during development.
* `TEST_PROFILE`: Either âdevâ or âciâ. This variable supplies the name of the
  Hypothesis testing profile to use when running tests. The âciâ profile
  runs more examples while the âdevâ profile executes more quickly. Default
  is âdevâ.

## The CI Test Script[#](#the-ci-test-script "Link to this heading")

In addition to `ci/local/build.sh`, the repo contains a
`ci/gitlab/build.sh` script which is used to run tests in CI. It is
sometimes useful to invoke this script to more closely replicate the CI
environment. This script does *not* cache models in between runs and will
generally run more and slower tests than those used for the `local` script.

The `ci/gitlab/build.sh` script uses the following environment variables
to control build and execution of tests:

* `PREBUILT_SERVER_TAG`: Use this Docker image as the Triton server image
  to test rather than building it.
* `PREBUILT_TEST_TAG`: Use this Docker image as the Triton test image rather
  than building it on top of the server image.
* `MODEL_BUILDER_IMAGE`: Use this Docker image to train test models rather
  than building an image.
* `LOG_DIR`: A host directory used for storing test logs
* `NV_DOCKER_ARGS`: A bash expression that when evaluated returns Docker
  arguments used for controlling GPU access in CI
* `BUILDPY`: If set to 1, build with Tritonâs `build.py` script rather than
  the FIL backend Dockerfile.
* `CPU_ONLY`: If set to 1, build without GPU support.
* `NO_CACHE`: Set to 0 to enable Docker cache. **By default, caching is
  disabled.**
* `USE_CLIENT_WHEEL`: If set to 1, install the Triton client from a wheel
  copied from Tritonâs SDK image. This is useful for testing on ARM
  machines, where the Triton Python client is not available via pip.
* `SDK_IMAGE`: If set, copy the Triton client wheel from this specific Docker
  SDK image

## Running Tests Manually[#](#running-tests-manually "Link to this heading")

It is *strongly* recommended that you use the provided test scripts for running
tests. If you wish to run tests manually, you must generate test models using
the `qa/generate_example_models.sh` script, start the Triton server against
the generated model repository, and then run `pytest --repo qa/L0_e2e/model_repository qa/L0_e2e`.

This approach is not an officially supported testing method, and minimal
support will be provided for it. If you find it useful and wish to
contribute documentation to make this method easier, pull requests are
welcome.

