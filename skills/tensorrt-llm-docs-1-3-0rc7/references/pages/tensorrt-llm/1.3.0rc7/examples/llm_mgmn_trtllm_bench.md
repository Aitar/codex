# Run trtllm-bench with pytorch backend on Slurm — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/examples/llm_mgmn_trtllm_bench.html

Run trtllm-bench with pytorch backend on Slurm#

Source NVIDIA/TensorRT-LLM.

```text
  1#!/bin/bash
  2#SBATCH -A <account>
  3#SBATCH -p <partition>
  4#SBATCH -t 01:00:00
  5#SBATCH -N 2
  6#SBATCH --ntasks-per-node=8
  7#SBATCH -o logs/trtllm-bench.out
  8#SBATCH -e logs/trtllm-bench.err
  9#SBATCH -J trtllm-bench
 10
 11##############################################################################
 12# OVERVIEW:
 13# This script runs trtllm-bench throughput benchmarking on SLURM with multi-node,
 14# multi-GPU setup. It prepares a synthetic dataset and then benchmarks the model
 15# using the PyTorch backend with tensor parallelism.
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
 32#    - MODEL_NAME: Name of the model to benchmark
 33#    - EXTRA_ARGS: (Optional) Additional benchmark arguments
 34#
 35# 3. Model Configuration (lines 87-94):
 36#    - --tp 16: Adjust tensor parallelism size to match your node/GPU setup
 37#    - --num-requests (line 56): Change number of benchmark requests
 38#    - --input-mean/output-mean (lines 57-58): Adjust token lengths
 39#
 40# EXAMPLE USAGE:
 41#   export CONTAINER_IMAGE="nvcr.io/nvidia/tensorrt_llm:latest"
 42#   export LOCAL_MODEL="/path/to/llama-model"
 43#   export MODEL_NAME="meta-llama/Llama-2-7b-hf"
 44#   sbatch llm_mgmn_trtllm_bench.sh
 45##############################################################################
 46
 47
 48# NOTE, this feature is experimental and may not work on all systems.
 49# The trtllm-llmapi-launch is a script that launches the LLM-API code on
 50# Slurm-like systems, and can support multi-node and multi-GPU setups.
 51
 52# IMPORTANT: Total MPI processes (nodes × ntasks-per-node) must equal tensor_parallel_size.
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
 71export data_path="$WORKDIR/token-norm-dist.txt"
 72
 73echo "Preparing dataset..."
 74srun -l \
 75    -N 1 \
 76    -n 1 \
 77    --container-image=${CONTAINER_IMAGE} \
 78    --container-name="prepare-name" \
 79    --container-mounts=${MOUNT_DIR}:${MOUNT_DEST} \
 80    --container-workdir=${WORKDIR} \
 81    --export=ALL \
 82    --mpi=pmix \
 83    bash -c "
 84        $PROLOGUE
 85        trtllm-bench --model=$LOCAL_MODEL prepare-dataset \
 86            --output $data_path \
 87            token-norm-dist \
 88            --num-requests=100 \
 89            --input-mean=128 \
 90            --output-mean=128 \
 91            --input-stdev=0 \
 92            --output-stdev=0
 93    "
 94
 95echo "Running benchmark..."
 96# Just launch trtllm-bench job with trtllm-llmapi-launch command.
 97
 98srun -l \
 99    --container-image=${CONTAINER_IMAGE} \
100    --container-mounts=${MOUNT_DIR}:${MOUNT_DEST} \
101    --container-workdir=${WORKDIR} \
102    --export=ALL,PYTHONPATH=${SOURCE_ROOT} \
103    --mpi=pmix \
104    bash -c "
105        set -ex
106        $PROLOGUE
107        export PATH=$PATH:~/.local/bin
108
109        # This is optional
110        cat > /tmp/pytorch_extra_args.txt << EOF
111cuda_graph_config: null
112print_iter_log: true
113enable_attention_dp: false
114EOF
115
116        # launch the benchmark
117        trtllm-llmapi-launch \
118         trtllm-bench \
119            --model $MODEL_NAME \
120            --model_path $LOCAL_MODEL \
121            throughput \
122            --dataset $data_path \
123            --backend pytorch \
124            --tp 16 \
125            --config /tmp/pytorch_extra_args.txt \
126            $EXTRA_ARGS
127    "
```
