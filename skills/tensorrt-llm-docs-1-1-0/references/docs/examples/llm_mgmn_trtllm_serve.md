Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/examples/llm_mgmn_trtllm_serve.md

* [LLM Examples](llm_api_examples.md)
* Run trtllm-serve with pytorch backend on Slurm

# Run trtllm-serve with pytorch backend on Slurm[#](#run-trtllm-serve-with-pytorch-backend-on-slurm "Link to this heading")

Source [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM/blob/48b7b5d8b7ed1e6bff57aecc6ff7d1533288bed8/examples/llm-api/llm_mgmn_trtllm_serve.sh).

```
 1#!/bin/bash
 2#SBATCH -A <account>
 3#SBATCH -p <partition>
 4#SBATCH -t 01:00:00
 5#SBATCH -N 2
 6#SBATCH --ntasks-per-node=8
 7#SBATCH -o logs/trtllm-serve.out
 8#SBATCH -e logs/trtllm-serve.err
 9#SBATCH -J trtllm-serve
10
11##############################################################################
12# OVERVIEW:
13# This script launches trtllm-serve (OpenAI-compatible API server) on SLURM
14# with multi-node, multi-GPU support. The server will start on all allocated
15# nodes and serve the model with tensor parallelism.
16#
17# WHAT TO MODIFY:
18# 1. SLURM Parameters (lines 2-9):
19#    - Replace <account> with your SLURM account name
20#    - Replace <partition> with your SLURM partition name
21#    - Adjust -N (number of nodes) based on your TP size
22#    - Adjust --ntasks-per-node (GPUs per node) to match your setup
23#
24# 2. Environment Variables (set before running sbatch):
25#    - CONTAINER_IMAGE: Docker image with TensorRT-LLM installed
26#    - MOUNT_DIR: Host directory to mount in container
27#    - MOUNT_DEST: Container mount destination path
28#    - WORKDIR: Working directory inside container
29#    - SOURCE_ROOT: Path to TensorRT-LLM source code
30#    - PROLOGUE: Commands to run before main task (e.g., module loads)
31#    - LOCAL_MODEL: Path to your pre-downloaded model directory
32#    - ADDITIONAL_OPTIONS: (Optional) Extra trtllm-serve options
33#
34# 3. Server Configuration (lines 51-55):
35#    - --tp_size 16: Adjust tensor parallelism to match your node/GPU setup
36#    - --host 0.0.0.0: Server bind address (0.0.0.0 allows external access)
37#
38# EXAMPLE USAGE:
39#   export CONTAINER_IMAGE="nvcr.io/nvidia/tensorrt_llm:latest"
40#   export LOCAL_MODEL="/path/to/llama-model"
41#   sbatch llm_mgmn_trtllm_serve.sh
42#
43# NOTE: After the server starts, you can send requests to it using curl or
44#       the OpenAI Python client. Check the output logs for the server address.
45##############################################################################
46
47
48# NOTE, this feature is experimental and may not work on all systems.
49# The trtllm-llmapi-launch is a script that launches the LLM-API code on
50# Slurm-like systems, and can support multi-node and multi-GPU setups.
51
52# IMPORTANT: Total MPI processes (nodes × ntasks-per-node) must equal tp_size.
53# e.g. For tensor_parallel_size=16, you may use 2 nodes with 8 gpus for
54# each, or 4 nodes with 4 gpus for each or other combinations.
55
56# This docker image should have tensorrt_llm installed, or you need to install
57# it in the task.
58
59# The following variables are expected to be set in the environment:
60# You can set them via --export in the srun/sbatch command.
61#   CONTAINER_IMAGE: the docker image to use, you'd better install tensorrt_llm in it, or install it in the task.
62#   MOUNT_DIR: the directory to mount in the container
63#   MOUNT_DEST: the destination directory in the container
64#   WORKDIR: the working directory in the container
65#   SOURCE_ROOT: the path to the TensorRT LLM source
66#   PROLOGUE: the prologue to run before the script
67#   LOCAL_MODEL: the local model directory to use, NOTE: downloading from HF is
68#      not supported in Slurm mode, you need to download the model and put it in
69#      the LOCAL_MODEL directory.
70
71echo "Starting trtllm-serve..."
72# Just launch trtllm-serve job with trtllm-llmapi-launch command.
73srun -l \
74    --container-image=${CONTAINER_IMAGE} \
75    --container-mounts=${MOUNT_DIR}:${MOUNT_DEST} \
76    --container-workdir=${WORKDIR} \
77    --export=ALL,PYTHONPATH=${SOURCE_ROOT} \
78    --mpi=pmix \
79    bash -c "
80        set -ex
81        $PROLOGUE
82        export PATH=$PATH:~/.local/bin
83
84        trtllm-llmapi-launch \
85         trtllm-serve $LOCAL_MODEL \
86            --tp_size 16 \
87            --host 0.0.0.0 \
88            ${ADDITIONAL_OPTIONS}
89    "
```

[previous

Run trtllm-bench with pytorch backend on Slurm](llm_mgmn_trtllm_bench.md "previous page")
[next

Online Serving Examples](trtllm_serve_examples.md "next page")