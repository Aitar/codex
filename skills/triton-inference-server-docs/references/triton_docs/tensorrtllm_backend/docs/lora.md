* Running...

# Running LoRA inference with inflight batching[#](#running-lora-inference-with-inflight-batching "Link to this heading")

Below is an example of how to run LoRA inference with inflight batching. See the
[LoRA documentation](https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/advanced/lora.md)
in the TensorRT-LLM repository for more information about running gpt-2b with
LoRA using inflight batching.

## Launch Triton TensorRT-LLM container[#](#launch-triton-tensorrt-llm-container "Link to this heading")

```
docker run --rm -it --net host --shm-size=2g \
    --ulimit memlock=-1 --ulimit stack=67108864 --gpus all \
    -v </path/to/tensorrtllm_backend>:/tensorrtllm_backend \
    -v ${HOME}/.cache/huggingface:/root/.cache/huggingface \
    -v </path/to/engines>:/engines \
    nvcr.io/nvidia/tritonserver:<xx.yy>-trtllm-python-py3
```

## Prepare TensorRT-LLM engines with LoRA enable[#](#prepare-tensorrt-llm-engines-with-lora-enable "Link to this heading")

(Optional) Download the LLaMa model from HuggingFace if you havenât already.

```
huggingface-cli login
huggingface-cli download meta-llama/Llama-2-7b-hf
```

> **NOTE**
>
> Make sure that you have access to https://huggingface.co/meta-llama/Llama-2-7b-hf.

```
cd /tensorrtllm_backend/tensorrt_llm/examples/models/core/llama
BASE_LLAMA_MODEL=/path/to/llama-7b-hf

python3 convert_checkpoint.py --model_dir ${BASE_LLAMA_MODEL} \
                            --output_dir ./c-model/llama/fp16/1-gpu \
                            --dtype float16

trtllm-build --checkpoint_dir ./c-model/llama/fp16/1-gpu \
            --output_dir /engines/llama_7b_with_lora_qkv/fp16/1-gpu \
            --gemm_plugin float16 \
            --max_batch_size 8 \
            --max_seq_len 562 \
            --gpt_attention_plugin float16 \
            --kv_cache_type paged \
            --remove_input_padding enable \
            --use_paged_context_fmha enable \
            --lora_plugin float16 \
            --lora_target_modules attn_q attn_k attn_v \
            --max_lora_rank 8
```

Note that you still need to use `hf_lora_convert.py` to convert the lora weights and store in `/tmp/lora_prefetch`. But users donât need to send the `--lora-path` when you run the inference at the first time.

## Generate LoRA tensors[#](#generate-lora-tensors "Link to this heading")

Now generate LoRA tensors that will be passed in with each request to triton.

```
git-lfs clone https://huggingface.co/silk-road/luotuo-lora-7b-0.1
git-lfs clone https://huggingface.co/kunishou/Japanese-Alpaca-LoRA-7b-v0

python3 ../../../hf_lora_convert.py -i luotuo-lora-7b-0.1 -o luotuo-lora-7b-0.1-weights --storage-type float16
python3 ../../../hf_lora_convert.py -i Japanese-Alpaca-LoRA-7b-v0 -o Japanese-Alpaca-LoRA-7b-v0-weights --storage-type float16
```

## Create a Triton model repository and launch the Triton server[#](#create-a-triton-model-repository-and-launch-the-triton-server "Link to this heading")

Create a Triton model repository following the instructions
[here](../README.md#prepare-the-model-repository), and modify the model
configuration following the steps
[here](../README.md#modify-the-model-configuration).

## LoRA Cache[#](#lora-cache "Link to this heading")

As LoRA weights are passed to the backend they will be cached in a host cache.
As requests are scheduled, those weights with be prefetched to a gpu cache.
After a LoRA is loaded into the cache, only `lora_task_id` is needed for inference.

### lora\_cache\_optimal\_adapter\_size[#](#lora-cache-optimal-adapter-size "Link to this heading")

Optimal adapter size used to size cache pages. Typically optimally sized
adapters will fix exactly into 1 cache page. (default: 8)

```
parameters: {
  key: "lora_cache_optimal_adapter_size"
  value: {
    string_value: "${lora_cache_optimal_adapter_size}"
  }
}
```

### lora\_cache\_max\_adapter\_size[#](#lora-cache-max-adapter-size "Link to this heading")

Used to set the minimum size of a cache page. Pages must be at least large enough to fit a single module, single later adapter\_size `maxAdapterSize` row of weights. (default: 64)

```
parameters: {
  key: "lora_cache_max_adapter_size"
  value: {
    string_value: "${lora_cache_max_adapter_size}"
  }
}
```

### lora\_cache\_gpu\_memory\_fraction[#](#lora-cache-gpu-memory-fraction "Link to this heading")

Fraction of GPU memory used for LoRA cache. Computed as a fraction of left over memory after engine load, and after KV cache is loaded (default: 0.05)

```
parameters: {
  key: "lora_cache_gpu_memory_fraction"
  value: {
    string_value: "${lora_cache_gpu_memory_fraction}"
  }
}
```

### lora\_cache\_host\_memory\_bytes[#](#lora-cache-host-memory-bytes "Link to this heading")

Size of host LoRA cache in bytes (default: 1G)

```
parameters: {
  key: "lora_cache_host_memory_bytes"
  value: {
    string_value: "${lora_cache_host_memory_bytes}"
  }
}
```

### prefetch lora cache during initializing the model instance[#](#prefetch-lora-cache-during-initializing-the-model-instance "Link to this heading")

If users want to load the lora models during initializing the model instance,
instead of passing the lora weight as input, users can store the lora weights in `<lora_prefetch_dir>`
and pass it as a parameter to initialize the model instance.
Then, the model instance will try to load the lora weights from the folder.
In the folder, users can put many folders for different lora tasks.
For example, assume we want to store lora weights in `/tmp/lora_prefetch` and
there are three lora tasks `0`, `1` and `3`, then the architecture of the folder would be like

```
/tmp/lora_prefetch
âââ 0
â   âââ model.lora_config.npy
â   âââ model.lora_weights.npy
âââ 1
â   âââ model.lora_config.npy
â   âââ model.lora_weights.npy
âââ 3
    âââ model.lora_config.npy
    âââ model.lora_weights.npy
```

Note that you must name the folder by digit because the lora cache manager will view these name as lora task ids.

```
parameters: {
  key: "lora_prefetch_dir"
  value: {
    string_value: "${lora_prefetch_dir}"
  }
}
```

## Launch tritonserver[#](#launch-tritonserver "Link to this heading")

```
MODEL_FOLDER=/path/to/triton_model_repo
# 'world_size' is the number of GPUs you want to use for serving. This should
# be aligned with the number of GPUs used to build the TensorRT-LLM engine.
python3 /tensorrtllm_backend/tensorrt_llm/triton_backend/scripts/launch_triton_server.py --world_size=1 --model_repo=${MODEL_FOLDER}
```

Run Multi-LoRA example by issuing multiple concurrent requests.
The inflight batcher will execute mixed batches with multiple LoRAs in the same batch.

First we cache the LoRAs by sending dummy requests for each adapter. The TASK\_IDS are uniq to the adapter

```
pip3 install tritonclient[all]

TASK_IDS=("1" "2")
LORA_PATHS=("luotuo-lora-7b-0.1-weights" "Japanese-Alpaca-LoRA-7b-v0-weights")
INFLIGHT_BATCHER_LLM_CLIENT=/tensorrtllm_backend/tensorrt_llm/triton_backend/tools/inflight_batcher_llm/inflight_batcher_llm_client.py

for index in ${!TASK_IDS[@]}; do
    text="dummy"
    lora_path=${LORA_PATHS[$index]}
    task_id=${TASK_IDS[$index]}
    lora_arg="--lora-path ${lora_path} --lora-task-id ${task_id}"

    python3 ${INFLIGHT_BATCHER_LLM_CLIENT} \
        --top-k 0 \
        --top-p 0.5 \
        --request-output-len 10 \
        --text "${text}" \
        --tokenizer-dir /path/to/llama-7b-hf \
        ${lora_arg} &
done
```

Now perform inference with just `--lora-task-id`

```
INPUT_TEXT=("ç¾å½çé¦é½å¨åªé? \nç­æ¡:" "ç¾å½çé¦é½å¨åªé? \nç­æ¡:" "ç¾å½çé¦é½å¨åªé? \nç­æ¡:" "ã¢ã¡ãªã«åè¡å½ã®é¦é½ã¯ã©ãã§ãã? \nç­ã:" "ã¢ã¡ãªã«åè¡å½ã®é¦é½ã¯ã©ãã§ãã? \nç­ã:" "ã¢ã¡ãªã«åè¡å½ã®é¦é½ã¯ã©ãã§ãã? \nç­ã:")
TASK_IDS=("" "1" "2" "" "1" "2")

for index in ${!INPUT_TEXT[@]}; do
    text=${INPUT_TEXT[$index]}
    task_id=${TASK_IDS[$index]}
    lora_arg=""
    if [ "${task_id}" != "" ]; then
        lora_arg="--lora-task-id ${task_id}"
    fi

    python3 inflight_batcher_llm/client/inflight_batcher_llm_client.py \
        --top-k 0 \
        --top-p 0.5 \
        --request-output-len 10 \
        --text "${text}" \
        --tokenizer-dir /home/scratch.trt_llm_data/llm-models/llama-models/llama-7b-hf \
        ${lora_arg} &
done

wait
```

Example Output:

```
Input sequence:  [1, 29871, 30310, 30604, 30303, 30439, 30733, 235, 164, 137, 30356, 30199, 31688, 30769, 30449, 31250, 30589, 30499, 30427, 30412, 29973, 320, 29876, 234, 176, 151, 30914, 29901]
Input sequence:  [1, 29871, 30630, 30356, 30210, 31688, 30769, 30505, 232, 150, 173, 30755, 29973, 320, 29876, 234, 176, 151, 233, 164, 139, 29901]
Input sequence:  [1, 29871, 30630, 30356, 30210, 31688, 30769, 30505, 232, 150, 173, 30755, 29973, 320, 29876, 234, 176, 151, 233, 164, 139, 29901]
Input sequence:  [1, 29871, 30310, 30604, 30303, 30439, 30733, 235, 164, 137, 30356, 30199, 31688, 30769, 30449, 31250, 30589, 30499, 30427, 30412, 29973, 320, 29876, 234, 176, 151, 30914, 29901]
Input sequence:  [1, 29871, 30310, 30604, 30303, 30439, 30733, 235, 164, 137, 30356, 30199, 31688, 30769, 30449, 31250, 30589, 30499, 30427, 30412, 29973, 320, 29876, 234, 176, 151, 30914, 29901]
Input sequence:  [1, 29871, 30630, 30356, 30210, 31688, 30769, 30505, 232, 150, 173, 30755, 29973, 320, 29876, 234, 176, 151, 233, 164, 139, 29901]
Got completed request
Input: ã¢ã¡ãªã«åè¡å½ã®é¦é½ã¯ã©ãã§ãã? \nç­ã:
Output beam 0: ã¯ã·ã³ãã³ D.C.
Output sequence:  [1, 29871, 30310, 30604, 30303, 30439, 30733, 235, 164, 137, 30356, 30199, 31688, 30769, 30449, 31250, 30589, 30499, 30427, 30412, 29973, 320, 29876, 234, 176, 151, 30914, 29901, 29871, 31028, 30373, 30203, 30279, 30203, 360, 29889, 29907, 29889]
Got completed request
Input: ç¾å½çé¦é½å¨åªé? \nç­æ¡:
Output beam 0: Washington, D.C.
What is the
Output sequence:  [1, 29871, 30630, 30356, 30210, 31688, 30769, 30505, 232, 150, 173, 30755, 29973, 320, 29876, 234, 176, 151, 233, 164, 139, 29901, 7660, 29892, 360, 29889, 29907, 29889, 13, 5618, 338, 278]
Got completed request
Input: ç¾å½çé¦é½å¨åªé? \nç­æ¡:
Output beam 0: Washington D.C.
Washington D.
Output sequence:  [1, 29871, 30630, 30356, 30210, 31688, 30769, 30505, 232, 150, 173, 30755, 29973, 320, 29876, 234, 176, 151, 233, 164, 139, 29901, 7660, 360, 29889, 29907, 29889, 13, 29956, 7321, 360, 29889]
Got completed request
Input: ã¢ã¡ãªã«åè¡å½ã®é¦é½ã¯ã©ãã§ãã? \nç­ã:
Output beam 0: Washington, D.C.
Which of
Output sequence:  [1, 29871, 30310, 30604, 30303, 30439, 30733, 235, 164, 137, 30356, 30199, 31688, 30769, 30449, 31250, 30589, 30499, 30427, 30412, 29973, 320, 29876, 234, 176, 151, 30914, 29901, 7660, 29892, 360, 29889, 29907, 29889, 13, 8809, 436, 310]
Got completed request
Input: ã¢ã¡ãªã«åè¡å½ã®é¦é½ã¯ã©ãã§ãã? \nç­ã:
Output beam 0: Washington D.C.
1. ã¢
Output sequence:  [1, 29871, 30310, 30604, 30303, 30439, 30733, 235, 164, 137, 30356, 30199, 31688, 30769, 30449, 31250, 30589, 30499, 30427, 30412, 29973, 320, 29876, 234, 176, 151, 30914, 29901, 7660, 360, 29889, 29907, 29889, 13, 29896, 29889, 29871, 30310]
Got completed request
Input: ç¾å½çé¦é½å¨åªé? \nç­æ¡:
Output beam 0: åçé¡¿
W
Output sequence:  [1, 29871, 30630, 30356, 30210, 31688, 30769, 30505, 232, 150, 173, 30755, 29973, 320, 29876, 234, 176, 151, 233, 164, 139, 29901, 29871, 31266, 234, 158, 158, 236, 164, 194, 13, 29956]
```

