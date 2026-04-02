Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/examples/llm_mgmn_trtllm_bench.md

* [LLM Examples](llm_api_examples.md)
* Run trtllm-bench with pytorch backend on Slurm

# Run trtllm-bench with pytorch backend on Slurm[#](#run-trtllm-bench-with-pytorch-backend-on-slurm "Link to this heading")

Source [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM/blob/48b7b5d8b7ed1e6bff57aecc6ff7d1533288bed8/examples/llm-api/llm_mgmn_trtllm_bench.sh).

```
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
 71export prepare_dataset="$SOURCE_ROOT/benchmarks/cpp/prepare_dataset.py"
 72export data_path="$WORKDIR/token-norm-dist.txt"
 73
 74echo "Preparing dataset..."
 75srun -l \
 76    -N 1 \
 77    -n 1 \
 78    --container-image=${CONTAINER_IMAGE} \
 79    --container-name="prepare-name" \
 80    --container-mounts=${MOUNT_DIR}:${MOUNT_DEST} \
 81    --container-workdir=${WORKDIR} \
 82    --export=ALL \
 83    --mpi=pmix \
 84    bash -c "
 85        $PROLOGUE
 86        python3 $prepare_dataset \
 87            --tokenizer=$LOCAL_MODEL \
 88            --stdout token-norm-dist \
 89            --num-requests=100 \
 90            --input-mean=128 \
 91            --output-mean=128 \
 92            --input-stdev=0 \
 93            --output-stdev=0 > $data_path
 94    "
 95
 96echo "Running benchmark..."
 97# Just launch trtllm-bench job with trtllm-llmapi-launch command.
 98
 99srun -l \
100    --container-image=${CONTAINER_IMAGE} \
101    --container-mounts=${MOUNT_DIR}:${MOUNT_DEST} \
102    --container-workdir=${WORKDIR} \
103    --export=ALL,PYTHONPATH=${SOURCE_ROOT} \
104    --mpi=pmix \
105    bash -c "
106        set -ex
107        $PROLOGUE
108        export PATH=$PATH:~/.local/bin
109
110        # This is optional
111        cat > /tmp/pytorch_extra_args.txt << EOF
112cuda_graph_config: null
113print_iter_log: true
114enable_attention_dp: false
115EOF
116
117        # launch the benchmark
118        trtllm-llmapi-launch \
119         trtllm-bench \
120            --model $MODEL_NAME \
121            --model_path $LOCAL_MODEL \
122            throughput \
123            --dataset $data_path \
124            --backend pytorch \
125            --tp 16 \
126            --extra_llm_api_options /tmp/pytorch_extra_args.txt \
127            $EXTRA_ARGS
128    "
```

[previous

Run LLM-API with pytorch backend on Slurm](llm_mgmn_llm_distributed.md "previous page")
[next

Run trtllm-serve with pytorch backend on Slurm](llm_mgmn_trtllm_serve.md "next page")