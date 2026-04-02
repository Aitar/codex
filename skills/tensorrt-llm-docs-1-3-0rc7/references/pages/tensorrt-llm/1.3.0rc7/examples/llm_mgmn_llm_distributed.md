# Run LLM-API with pytorch backend on Slurm — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/examples/llm_mgmn_llm_distributed.html

Run LLM-API with pytorch backend on Slurm#

Source NVIDIA/TensorRT-LLM.

```text
 1#!/bin/bash
 2#SBATCH -A <account>    # parameter
 3#SBATCH -p <partition>  # parameter
 4#SBATCH -t 01:00:00
 5#SBATCH -N 1
 6#SBATCH --ntasks-per-node=2
 7#SBATCH -o logs/llmapi-distributed.out
 8#SBATCH -e logs/llmapi-distributed.err
 9#SBATCH -J llmapi-distributed-task
10
11##############################################################################
12# OVERVIEW:
13# This script demonstrates running a custom LLM API Python script on SLURM
14# with distributed inference support. It executes quickstart_advanced.py with
15# tensor parallelism across multiple GPUs/nodes.
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
32#
33# 3. Script Configuration (lines 39, 51-54):
34#    - Line 39: Change $script to point to your own Python script
35#    - Line 52: Modify --model_dir to use your model path
36#    - Line 53: Customize --prompt with your test prompt
37#    - Line 54: Adjust --tp_size to match your node/GPU setup
38#
39# EXAMPLE USAGE:
40#   export CONTAINER_IMAGE="nvcr.io/nvidia/tensorrt_llm:latest"
41#   export LOCAL_MODEL="/path/to/llama-model"
42#   sbatch llm_mgmn_llm_distributed.sh
43#
44# NOTE: This is a template - you can replace quickstart_advanced.py with any
45#       LLM API Python script. The trtllm-llmapi-launch wrapper handles the
46#       distributed execution setup automatically.
47##############################################################################
48
49
50# NOTE, this feature is experimental and may not work on all systems.
51# The trtllm-llmapi-launch is a script that launches the LLM-API code on
52# Slurm-like systems, and can support multi-node and multi-GPU setups.
53
54# IMPORTANT: Total MPI processes (nodes × ntasks-per-node) must equal tp_size.
55# e.g. For tensor_parallel_size=16, you may use 2 nodes with 8 gpus for
56# each, or 4 nodes with 4 gpus for each or other combinations.
57
58# This docker image should have tensorrt_llm installed, or you need to install
59# it in the task.
60
61# The following variables are expected to be set in the environment:
62# You can set them via --export in the srun/sbatch command.
63#   CONTAINER_IMAGE: the docker image to use, you'd better install tensorrt_llm in it, or install it in the task.
64#   MOUNT_DIR: the directory to mount in the container
65#   MOUNT_DEST: the destination directory in the container
66#   WORKDIR: the working directory in the container
67#   SOURCE_ROOT: the path to the TensorRT LLM source
68#   PROLOGUE: the prologue to run before the script
69#   LOCAL_MODEL: the local model directory to use, NOTE: downloading from HF is
70#      not supported in Slurm mode, you need to download the model and put it in
71#      the LOCAL_MODEL directory.
72
73# Adjust the paths to run
74export script=$SOURCE_ROOT/examples/llm-api/quickstart_advanced.py
75
76# Just launch the PyTorch example with trtllm-llmapi-launch command.
77srun -l \
78    --container-image=${CONTAINER_IMAGE} \
79    --container-mounts=${MOUNT_DIR}:${MOUNT_DEST} \
80    --container-workdir=${WORKDIR} \
81    --export=ALL \
82    --mpi=pmix \
83    bash -c "
84        $PROLOGUE
85        export PATH=$PATH:~/.local/bin
86        trtllm-llmapi-launch python3 $script \
87            --model_dir $LOCAL_MODEL \
88            --prompt 'Hello, how are you?' \
89            --tp_size 2 \
90            --max_batch_size 256
91    "
```
