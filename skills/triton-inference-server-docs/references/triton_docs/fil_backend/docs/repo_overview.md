* Repo Overview

# Repo Overview[#](#repo-overview "Link to this heading")

The FIL backend repo is organized in the following directories:

## `ci`[#](#ci "Link to this heading")

This directory contains scripts and configuration files for working with CI.
Developers may invoke `ci/local/build.sh` to build and run tests locally or
`ci/gitlab/build.sh` to more precisely mirror the test environment run in
official CI. This directory is not intended for end users.

## `cmake`[#](#cmake "Link to this heading")

This directory contains CMake files required for the build, especially those
which are used to retrieve external dependencies. It is not intended for
end users.

## `conda`[#](#conda "Link to this heading")

This directory contains conda-related infrastructure including environment yaml
files used to construct build and test environments:

* `conda/environments/buildpy.yml`: Minimal environment for using Tritonâs
  `build.py` build script
* `conda/environments/rapids_triton_dev.yml`: Environment for building the FIL
  backend
* `conda/environments/triton_benchmark.yml`: Environment for running the FIL
  backendâs standard benchmarks
* `conda/environments/triton_test_no_client.yml`: Environment for running tests
  for the FIL backend. This file does not include Tritonâs Python client to
  facilitate testing on ARM machines, where the client cannot be correctly
  installed via pip.
* `conda/environments/triton_test.yml`: Environment for running tests for the
  FIL backend that includes Tritonâs Python client. Recommended environment for
  those wishing to run tests outside of Docker.

## `docs`[#](#docs "Link to this heading")

This directory contains markdown files for documentation.

## `notebooks`[#](#notebooks "Link to this heading")

This directory contains example Jupyter notebooks for using the FIL backend.

## `ops`[#](#ops "Link to this heading")

This directory contains files used for build-related tasks including the
Dockerfile for the FIL backendâs dockerized build. It is not intended for end
users.

## `qa`[#](#qa "Link to this heading")

This directory contains files for running tests and benchmarks. It is not
intended for end users.

## `scripts`[#](#scripts "Link to this heading")

This directory contains utility scripts for e.g. converting models to Treelite
checkpoint format. It also contains a conda environment file indicating the
necessary dependencies for running these scripts.

## `src`[#](#src "Link to this heading")

This directory contains the C++ source files for the FIL backend. It is not
intended for end users.

