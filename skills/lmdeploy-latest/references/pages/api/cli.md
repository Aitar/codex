# Command-line Tools — lmdeploy

Source: https://lmdeploy.readthedocs.io/en/latest/api/cli.html

Command-line Tools

Command-line Tools#

lmdeploy - CLI interface#

The CLI provides a unified API for converting, compressing and deploying large language models.

```text
lmdeploy [-h] [-v] {lite,serve,check_env,chat} ...
```

lmdeploy options#

`-h`, `--help` - show this help message and exit

`-v`, `--version` - show program’s version number and exit

lmdeploy lite#

Compressing and accelerating LLMs with lmdeploy.lite module

```text
lmdeploy lite [-h] {auto_awq,auto_gptq,calibrate,smooth_quant} ...
```

lmdeploy lite options#

`-h`, `--help` - show this help message and exit

lmdeploy lite auto_awq#

Perform weight quantization using AWQ algorithm.

```text
lmdeploy lite auto_awq [-h] [--revision REVISION] [--download-dir DOWNLOAD_DIR]
                       [--work-dir WORK_DIR]
                       [--calib-dataset {wikitext2,c4,pileval,gsm8k,neuralmagic_calibration,open-platypus,openwebtext}]
                       [--calib-samples CALIB_SAMPLES] [--calib-seqlen CALIB_SEQLEN]
                       [--batch-size BATCH_SIZE] [--search-scale]
                       [--dtype {auto,float16,bfloat16}] [--device DEVICE] [--w-bits W_BITS]
                       [--w-sym] [--w-group-size W_GROUP_SIZE]
                       model
```

lmdeploy lite auto_awq positional arguments#

`model` - The path of model in hf format (default: `None`)

lmdeploy lite auto_awq options#

`-h`, `--help` - show this help message and exit

`--revision``REVISION` - The specific model version to use. It can be a branch name, a tag name, or a commit id. If unspecified, will use the default version.

`--download-dir``DOWNLOAD_DIR` - Directory to download and load the weights, default to the default cache directory of huggingface.

`--work-dir``WORK_DIR` - The working directory to save results (default: `./work_dir`)

`--calib-dataset``CALIB_DATASET` - The calibration dataset name. (default: `wikitext2`)

`--calib-samples``CALIB_SAMPLES` - The number of samples for calibration (default: `128`)

`--calib-seqlen``CALIB_SEQLEN` - The sequence length for calibration (default: `2048`)

`--batch-size``BATCH_SIZE` - The batch size for running the calib samples. Low GPU mem requires small batch_size. Large batch_size reduces the calibration time while costs more VRAM (default: `1`)

`--dtype``DTYPE` - data type for model weights and activations. The `"auto"` option will use FP16 precision for FP32 and FP16 models, and BF16 precision for BF16 models. This option will be ignored if the model is a quantized model (default: `auto`)

`--device``DEVICE` - Device for weight quantization (cuda or npu) (default: `cuda`)

`--w-bits``W_BITS` - Bit number for weight quantization (default: `4`)

`--w-sym` - Whether to do symmetric quantization

`--w-group-size``W_GROUP_SIZE` - Group size for weight quantization statistics (default: `128`)

lmdeploy lite auto_gptq#

Perform weight quantization using GPTQ algorithm.

```text
lmdeploy lite auto_gptq [-h] [--revision REVISION] [--work-dir WORK_DIR]
                        [--calib-dataset {wikitext2,c4,pileval,gsm8k,neuralmagic_calibration,open-platypus,openwebtext}]
                        [--calib-samples CALIB_SAMPLES] [--calib-seqlen CALIB_SEQLEN]
                        [--batch-size BATCH_SIZE] [--dtype {auto,float16,bfloat16}]
                        [--w-bits W_BITS] [--w-group-size W_GROUP_SIZE]
                        model
```

lmdeploy lite auto_gptq positional arguments#

`model` - The path of model in hf format (default: `None`)

lmdeploy lite auto_gptq options#

`-h`, `--help` - show this help message and exit

`--revision``REVISION` - The specific model version to use. It can be a branch name, a tag name, or a commit id. If unspecified, will use the default version.

`--work-dir``WORK_DIR` - The working directory to save results (default: `./work_dir`)

`--calib-dataset``CALIB_DATASET` - The calibration dataset name. (default: `wikitext2`)

`--calib-samples``CALIB_SAMPLES` - The number of samples for calibration (default: `128`)

`--calib-seqlen``CALIB_SEQLEN` - The sequence length for calibration (default: `2048`)

`--batch-size``BATCH_SIZE` - The batch size for running the calib samples. Low GPU mem requires small batch_size. Large batch_size reduces the calibration time while costs more VRAM (default: `1`)

`--dtype``DTYPE` - data type for model weights and activations. The `"auto"` option will use FP16 precision for FP32 and FP16 models, and BF16 precision for BF16 models. This option will be ignored if the model is a quantized model (default: `auto`)

`--w-bits``W_BITS` - Bit number for weight quantization (default: `4`)

`--w-group-size``W_GROUP_SIZE` - Group size for weight quantization statistics (default: `128`)

lmdeploy lite calibrate#

Perform calibration on a given dataset.

```text
lmdeploy lite calibrate [-h] [--work-dir WORK_DIR]
                        [--calib-dataset {wikitext2,c4,pileval,gsm8k,neuralmagic_calibration,open-platypus,openwebtext}]
                        [--calib-samples CALIB_SAMPLES] [--calib-seqlen CALIB_SEQLEN]
                        [--batch-size BATCH_SIZE] [--search-scale]
                        [--dtype {auto,float16,bfloat16}]
                        model
```

lmdeploy lite calibrate positional arguments#

`model` - The name or path of the model to be loaded (default: `None`)

lmdeploy lite calibrate options#

`-h`, `--help` - show this help message and exit

`--work-dir``WORK_DIR` - The working directory to save results (default: `./work_dir`)

`--calib-dataset``CALIB_DATASET` - The calibration dataset name. (default: `wikitext2`)

`--calib-samples``CALIB_SAMPLES` - The number of samples for calibration (default: `128`)

`--calib-seqlen``CALIB_SEQLEN` - The sequence length for calibration (default: `2048`)

`--batch-size``BATCH_SIZE` - The batch size for running the calib samples. Low GPU mem requires small batch_size. Large batch_size reduces the calibration time while costs more VRAM (default: `1`)

`--dtype``DTYPE` - data type for model weights and activations. The `"auto"` option will use FP16 precision for FP32 and FP16 models, and BF16 precision for BF16 models. This option will be ignored if the model is a quantized model (default: `auto`)

lmdeploy lite smooth_quant#

Perform w8a8 quantization using SmoothQuant.

```text
lmdeploy lite smooth_quant [-h] [--work-dir WORK_DIR] [--device DEVICE]
                           [--calib-dataset {wikitext2,c4,pileval,gsm8k,neuralmagic_calibration,open-platypus,openwebtext}]
                           [--calib-samples CALIB_SAMPLES] [--calib-seqlen CALIB_SEQLEN]
                           [--batch-size BATCH_SIZE] [--search-scale]
                           [--dtype {auto,float16,bfloat16}]
                           [--quant-dtype {int8,float8_e4m3fn,float8_e5m2,fp8}]
                           [--revision REVISION] [--download-dir DOWNLOAD_DIR]
                           model
```

lmdeploy lite smooth_quant positional arguments#

`model` - The name or path of the model to be loaded (default: `None`)

lmdeploy lite smooth_quant options#

`-h`, `--help` - show this help message and exit

`--work-dir``WORK_DIR` - The working directory for outputs. defaults to `"./work_dir"`

`--device``DEVICE` - Device for weight quantization (cuda or npu) (default: `cuda`)

`--calib-dataset``CALIB_DATASET` - The calibration dataset name. (default: `wikitext2`)

`--calib-samples``CALIB_SAMPLES` - The number of samples for calibration (default: `128`)

`--calib-seqlen``CALIB_SEQLEN` - The sequence length for calibration (default: `2048`)

`--batch-size``BATCH_SIZE` - The batch size for running the calib samples. Low GPU mem requires small batch_size. Large batch_size reduces the calibration time while costs more VRAM (default: `1`)

`--dtype``DTYPE` - data type for model weights and activations. The `"auto"` option will use FP16 precision for FP32 and FP16 models, and BF16 precision for BF16 models. This option will be ignored if the model is a quantized model (default: `auto`)

`--quant-dtype``QUANT_DTYPE` - data type for the quantized model weights and activations.Note `"fp8"` is the short version of `"float8_e4m3fn"` (default: `int8`)

`--revision``REVISION` - The specific model version to use. It can be a branch name, a tag name, or a commit id. If unspecified, will use the default version.

`--download-dir``DOWNLOAD_DIR` - Directory to download and load the weights, default to the default cache directory of huggingface.

lmdeploy serve#

Serve LLMs with openai API

```text
lmdeploy serve [-h] {api_server,proxy} ...
```

lmdeploy serve options#

`-h`, `--help` - show this help message and exit

lmdeploy serve api_server#

Serve LLMs with restful api using fastapi.

```text
lmdeploy serve api_server [-h] [--server-name SERVER_NAME] [--server-port SERVER_PORT]
                          [--allow-origins ALLOW_ORIGINS [ALLOW_ORIGINS ...]]
                          [--allow-credentials]
                          [--allow-methods ALLOW_METHODS [ALLOW_METHODS ...]]
                          [--allow-headers ALLOW_HEADERS [ALLOW_HEADERS ...]]
                          [--proxy-url PROXY_URL]
                          [--max-concurrent-requests MAX_CONCURRENT_REQUESTS]
                          [--backend {pytorch,turbomind}]
                          [--log-level {CRITICAL,FATAL,ERROR,WARN,WARNING,INFO,DEBUG,NOTSET}]
                          [--api-keys [API_KEYS ...]] [--ssl] [--model-name MODEL_NAME]
                          [--max-log-len MAX_LOG_LEN] [--disable-fastapi-docs]
                          [--allow-terminate-by-client] [--enable-abort-handling]
                          [--chat-template CHAT_TEMPLATE]
                          [--tool-call-parser TOOL_CALL_PARSER]
                          [--reasoning-parser REASONING_PARSER] [--revision REVISION]
                          [--download-dir DOWNLOAD_DIR] [--adapters [ADAPTERS ...]]
                          [--device {cuda,ascend,maca,camb}] [--eager-mode]
                          [--disable-vision-encoder]
                          [--logprobs-mode {None,raw_logits,raw_logprobs}]
                          [--dllm-block-length DLLM_BLOCK_LENGTH]
                          [--dllm-unmasking-strategy {low_confidence_dynamic,low_confidence_static,sequential}]
                          [--dllm-denoising-steps DLLM_DENOISING_STEPS]
                          [--dllm-confidence-threshold DLLM_CONFIDENCE_THRESHOLD]
                          [--enable-return-routed-experts]
                          [--distributed-executor-backend {uni,mp,ray}]
                          [--dtype {auto,float16,bfloat16}] [--tp TP]
                          [--session-len SESSION_LEN] [--max-batch-size MAX_BATCH_SIZE]
                          [--cache-max-entry-count CACHE_MAX_ENTRY_COUNT]
                          [--cache-block-seq-len CACHE_BLOCK_SEQ_LEN]
                          [--enable-prefix-caching]
                          [--max-prefill-token-num MAX_PREFILL_TOKEN_NUM]
                          [--quant-policy {0,4,8}]
                          [--model-format {hf,awq,gptq,compressed-tensors,fp8,mxfp4}]
                          [--hf-overrides HF_OVERRIDES] [--disable-metrics] [--dp DP]
                          [--ep EP] [--enable-microbatch] [--enable-eplb]
                          [--role {Hybrid,Prefill,Decode}]
                          [--migration-backend {DLSlime,Mooncake}] [--node-rank NODE_RANK]
                          [--nnodes NNODES] [--cp CP]
                          [--rope-scaling-factor ROPE_SCALING_FACTOR]
                          [--num-tokens-per-iter NUM_TOKENS_PER_ITER]
                          [--max-prefill-iters MAX_PREFILL_ITERS] [--async {0,1}]
                          [--communicator {nccl,native,cuda-ipc}]
                          [--dist-init-addr DIST_INIT_ADDR]
                          [--vision-max-batch-size VISION_MAX_BATCH_SIZE]
                          [--speculative-algorithm {eagle,eagle3,deepseek_mtp}]
                          [--speculative-draft-model SPECULATIVE_DRAFT_MODEL]
                          [--speculative-num-draft-tokens SPECULATIVE_NUM_DRAFT_TOKENS]
                          model_path
```

lmdeploy serve api_server positional arguments#

`model_path` - The path of a model. it could be one of the following options: - i) a local directory path of a turbomind model which is converted by lmdeploy convert command or download from ii) and iii). - ii) the model_id of a lmdeploy-quantized model hosted inside a model repo on huggingface.co, such as `"internlm/internlm-chat-20b-4bit"`, `"lmdeploy/llama2-chat-70b-4bit"`, etc. - iii) the model_id of a model hosted inside a model repo on huggingface.co, such as `"internlm/internlm-chat-7b"`, `"qwen/qwen-7b-chat"`, `"baichuan-inc/baichuan2-7b-chat"` and so on (default: `None`)

lmdeploy serve api_server options#

`-h`, `--help` - show this help message and exit

`--server-name``SERVER_NAME` - Host ip for serving (default: `0.0.0.0`)

`--server-port``SERVER_PORT` - Server port (default: `23333`)

`--allow-origins``ALLOW_ORIGINS` - A list of allowed origins for cors (default: `['*']`)

`--allow-credentials` - Whether to allow credentials for cors

`--allow-methods``ALLOW_METHODS` - A list of allowed http methods for cors (default: `['*']`)

`--allow-headers``ALLOW_HEADERS` - A list of allowed http headers for cors (default: `['*']`)

`--proxy-url``PROXY_URL` - The proxy url for api server. (default: `None`)

`--max-concurrent-requests``MAX_CONCURRENT_REQUESTS` - This refers to the number of concurrent requests that the server can handle. The server is designed to process the engine’s tasks once the maximum number of concurrent requests is reached, regardless of any additional requests sent by clients concurrently during that time. Default to None. (default: `None`)

`--backend``BACKEND` - Set the inference backend (default: `turbomind`)

`--log-level``LOG_LEVEL` - Set the log level (default: `WARNING`)

`--api-keys``API_KEYS` - Optional list of space separated API keys (default: `None`)

`--ssl` - Enable SSL. Requires OS Environment variables `'SSL_KEYFILE'` and `'SSL_CERTFILE'`

`--model-name``MODEL_NAME` - The name of the served model. It can be accessed by the RESTful API /v1/models. If it is not specified, model_path will be adopted (default: `None`)

`--max-log-len``MAX_LOG_LEN` - Max number of prompt characters or prompt tokens being printed in log. Default: Unlimited (default: `None`)

`--disable-fastapi-docs` - Disable FastAPI’s OpenAPI schema, Swagger UI, and ReDoc endpoint

`--allow-terminate-by-client` - Enable server to be terminated by request from client

`--enable-abort-handling` - Enable server to handle client abort requests

`--chat-template``CHAT_TEMPLATE` - A JSON file or string that specifies the chat template configuration. Please refer to https://lmdeploy.readthedocs.io/en/latest/advance/chat_template.html for the specification (default: `None`)

`--tool-call-parser``TOOL_CALL_PARSER` - The registered tool parser name dict_keys([`'internlm'`, `'intern-s1'`, `'llama3'`, `'qwen2d5'`, `'qwen'`, `'qwen3'`, `'qwen3coder'`]). Default to None. (default: `None`)

`--reasoning-parser``REASONING_PARSER` - The registered reasoning parser name from dict_keys([`'deepseek-r1'`, `'qwen-qwq'`, `'intern-s1'`]). Default to None. (default: `None`)

`--revision``REVISION` - The specific model version to use. It can be a branch name, a tag name, or a commit id. If unspecified, will use the default version.

`--download-dir``DOWNLOAD_DIR` - Directory to download and load the weights, default to the default cache directory of huggingface.

lmdeploy serve api_server PyTorch engine arguments#

`--adapters``ADAPTERS` - Used to set path(s) of lora adapter(s). One can input key-value pairs in xxx=yyy format for multiple lora adapters. If only have one adapter, one can only input the path of the adapter. (default: `None`)

`--device``DEVICE` - The device type of running (default: `cuda`)

`--eager-mode` - Whether to enable eager mode. If True, cuda graph would be disabled

`--disable-vision-encoder` - disable multimodal encoder

`--logprobs-mode``LOGPROBS_MODE` - The mode of logprobs. (default: `None`)

`--dllm-block-length``DLLM_BLOCK_LENGTH` - Block length for dllm (default: `None`)

`--dllm-unmasking-strategy``DLLM_UNMASKING_STRATEGY` - The unmasking strategy for dllm. (default: `low_confidence_dynamic`)

`--dllm-denoising-steps``DLLM_DENOISING_STEPS` - The number of denoising steps for dllm. (default: `None`)

`--dllm-confidence-threshold``DLLM_CONFIDENCE_THRESHOLD` - The confidence threshold for dllm. (default: `0.85`)

`--enable-return-routed-experts` - Whether to output routed expert ids for replay

`--distributed-executor-backend``DISTRIBUTED_EXECUTOR_BACKEND` - The distributed executor backend for pytorch engine. (default: `None`)

`--dtype``DTYPE` - data type for model weights and activations. The `"auto"` option will use FP16 precision for FP32 and FP16 models, and BF16 precision for BF16 models. This option will be ignored if the model is a quantized model (default: `auto`)

`--tp``TP` - GPU number used in tensor parallelism. Should be 2^n (default: `1`)

`--session-len``SESSION_LEN` - The max session length of a sequence (default: `None`)

`--max-batch-size``MAX_BATCH_SIZE` - Maximum batch size. If not specified, the engine will automatically set it according to the device (default: `None`)

`--cache-max-entry-count``CACHE_MAX_ENTRY_COUNT` - The percentage of free gpu memory occupied by the k/v cache, excluding weights (default: `0.8`)

`--cache-block-seq-len``CACHE_BLOCK_SEQ_LEN` - The length of the token sequence in a k/v block. For Turbomind Engine, if the GPU compute capability is >= 8.0, it should be a multiple of 32, otherwise it should be a multiple of 64. For Pytorch Engine, if Lora Adapter is specified, this parameter will be ignored (default: `64`)

`--enable-prefix-caching` - Enable cache and match prefix

`--max-prefill-token-num``MAX_PREFILL_TOKEN_NUM` - the max number of tokens per iteration during prefill (default: `8192`)

`--quant-policy``QUANT_POLICY` - Quantize kv or not. 0: no quant; 4: 4bit kv; 8: 8bit kv (default: `0`)

`--model-format``MODEL_FORMAT` - The format of input model. hf means hf_llama, awq and gptq refer to 4-bit grouped quantization, compressed-tensors refers to pack-quantized grouped int4 checkpoints and is usually auto-detected from the model config, fp8 refers to blocked fp8 checkpoints, and mxfp4 refers to MXFP4 expert weights. (default: `None`)

`--hf-overrides``HF_OVERRIDES` - Extra arguments to be forwarded to the HuggingFace config. (default: `None`)

`--disable-metrics` - disable metrics system

`--dp``DP` - data parallelism. dp_rank is required when pytorch engine is used. (default: `1`)

`--ep``EP` - expert parallelism. dp is required when pytorch engine is used. (default: `1`)

`--enable-microbatch` - enable microbatch for specified model

`--enable-eplb` - enable eplb for specified model

`--role``ROLE` - Hybrid for Non-Disaggregated Engine; Prefill for Disaggregated Prefill Engine; Decode for Disaggregated Decode Engine (default: `Hybrid`)

`--migration-backend``MIGRATION_BACKEND` - kvcache migration management backend when PD disaggregation (default: `DLSlime`)

`--node-rank``NODE_RANK` - The current node rank. (default: `0`)

`--nnodes``NNODES` - The total node nums (default: `1`)

lmdeploy serve api_server TurboMind engine arguments#

`--dtype``DTYPE` - data type for model weights and activations. The `"auto"` option will use FP16 precision for FP32 and FP16 models, and BF16 precision for BF16 models. This option will be ignored if the model is a quantized model (default: `auto`)

`--tp``TP` - GPU number used in tensor parallelism. Should be 2^n (default: `1`)

`--session-len``SESSION_LEN` - The max session length of a sequence (default: `None`)

`--max-batch-size``MAX_BATCH_SIZE` - Maximum batch size. If not specified, the engine will automatically set it according to the device (default: `None`)

`--cache-max-entry-count``CACHE_MAX_ENTRY_COUNT` - The percentage of free gpu memory occupied by the k/v cache, excluding weights (default: `0.8`)

`--cache-block-seq-len``CACHE_BLOCK_SEQ_LEN` - The length of the token sequence in a k/v block. For Turbomind Engine, if the GPU compute capability is >= 8.0, it should be a multiple of 32, otherwise it should be a multiple of 64. For Pytorch Engine, if Lora Adapter is specified, this parameter will be ignored (default: `64`)

`--enable-prefix-caching` - Enable cache and match prefix

`--max-prefill-token-num``MAX_PREFILL_TOKEN_NUM` - the max number of tokens per iteration during prefill (default: `8192`)

`--quant-policy``QUANT_POLICY` - Quantize kv or not. 0: no quant; 4: 4bit kv; 8: 8bit kv (default: `0`)

`--model-format``MODEL_FORMAT` - The format of input model. hf means hf_llama, awq and gptq refer to 4-bit grouped quantization, compressed-tensors refers to pack-quantized grouped int4 checkpoints and is usually auto-detected from the model config, fp8 refers to blocked fp8 checkpoints, and mxfp4 refers to MXFP4 expert weights. (default: `None`)

`--nnodes``NNODES` - The total node nums (default: `1`)

`--node-rank``NODE_RANK` - The current node rank. (default: `0`)

`--hf-overrides``HF_OVERRIDES` - Extra arguments to be forwarded to the HuggingFace config. (default: `None`)

`--disable-metrics` - disable metrics system

`--dp``DP` - data parallelism. dp_rank is required when pytorch engine is used. (default: `1`)

`--cp``CP` - context parallelism size in attention for turbomind backend, tp must be a multiple of cp. (default: `1`)

`--rope-scaling-factor``ROPE_SCALING_FACTOR` - Rope scaling factor (default: `0.0`)

`--num-tokens-per-iter``NUM_TOKENS_PER_ITER` - the number of tokens processed in a forward pass (default: `0`)

`--max-prefill-iters``MAX_PREFILL_ITERS` - the max number of forward passes in prefill stage (default: `1`)

`--async``ASYNC_` - Enable async execution (default: 1, enabled). Set to 0 to disable async mode, 1 to enable it. (default: `1`)

`--communicator``COMMUNICATOR` - Communication backend for multi-GPU inference. The `"native"` option is deprecated and serves as an alias for `"cuda-ipc"` (default: `nccl`)

`--dist-init-addr``DIST_INIT_ADDR` (default: `None`)

lmdeploy serve api_server Vision model arguments#

`--vision-max-batch-size``VISION_MAX_BATCH_SIZE` - the vision model batch size (default: `1`)

lmdeploy serve api_server Speculative decoding arguments#

`--speculative-algorithm``SPECULATIVE_ALGORITHM` - The speculative algorithm to use. None means speculative decoding is disabled (default: `None`)

`--speculative-draft-model``SPECULATIVE_DRAFT_MODEL` - The path to speculative draft model (default: `None`)

`--speculative-num-draft-tokens``SPECULATIVE_NUM_DRAFT_TOKENS` - The number of speculative tokens to generate per step (default: `1`)

lmdeploy serve proxy#

Proxy server that manages distributed api_server nodes.

```text
lmdeploy serve proxy [-h] [--server-name SERVER_NAME] [--server-port SERVER_PORT]
                     [--serving-strategy {Hybrid,DistServe}] [--dummy-prefill]
                     [--routing-strategy {random,min_expected_latency,min_observed_latency}]
                     [--disable-cache-status] [--migration-protocol {RDMA,NVLINK}]
                     [--link-type {RoCE,IB}] [--disable-gdr] [--api-keys [API_KEYS ...]]
                     [--ssl]
                     [--log-level {CRITICAL,FATAL,ERROR,WARN,WARNING,INFO,DEBUG,NOTSET}]
```

lmdeploy serve proxy options#

`-h`, `--help` - show this help message and exit

`--server-name``SERVER_NAME` - Host ip for proxy serving (default: `0.0.0.0`)

`--server-port``SERVER_PORT` - Server port of the proxy (default: `8000`)

`--serving-strategy``SERVING_STRATEGY` - the strategy to serve, Hybrid for colocating Prefill and Decodeworkloads into same engine, DistServe for Prefill-Decode Disaggregation (default: `Hybrid`)

`--dummy-prefill` - dummy prefill for performance profiler

`--routing-strategy``ROUTING_STRATEGY` - the strategy to dispatch requests to nodes (default: `min_expected_latency`)

`--disable-cache-status` - Whether to disable cache status of the proxy. If set, the proxy will forget the status of the previous time

`--migration-protocol``MIGRATION_PROTOCOL` - transport protocol of KV migration (default: `RDMA`)

`--link-type``LINK_TYPE` - RDMA Link Type (default: `RoCE`)

`--disable-gdr` - with GPU Direct Memory Access

`--api-keys``API_KEYS` - Optional list of space separated API keys (default: `None`)

`--ssl` - Enable SSL. Requires OS Environment variables `'SSL_KEYFILE'` and `'SSL_CERTFILE'`

`--log-level``LOG_LEVEL` - Set the log level (default: `WARNING`)

lmdeploy check_env#

Check the environmental information.

```text
lmdeploy check_env [-h] [--dump-file DUMP_FILE]
```

lmdeploy check_env options#

`-h`, `--help` - show this help message and exit

`--dump-file``DUMP_FILE` - The file path to save env info. Only support file format in json, yml, pkl (default: `None`)

lmdeploy chat#

```text
lmdeploy chat [-h] [--backend {pytorch,turbomind}] [--chat-template CHAT_TEMPLATE]
              [--revision REVISION] [--download-dir DOWNLOAD_DIR] [--adapters [ADAPTERS ...]]
              [--device {cuda,ascend,maca,camb}] [--eager-mode]
              [--dllm-block-length DLLM_BLOCK_LENGTH] [--dtype {auto,float16,bfloat16}]
              [--tp TP] [--session-len SESSION_LEN]
              [--cache-max-entry-count CACHE_MAX_ENTRY_COUNT] [--enable-prefix-caching]
              [--quant-policy {0,4,8}]
              [--model-format {hf,awq,gptq,compressed-tensors,fp8,mxfp4}]
              [--rope-scaling-factor ROPE_SCALING_FACTOR]
              [--communicator {nccl,native,cuda-ipc}] [--cp CP] [--async {0,1}]
              [--speculative-algorithm {eagle,eagle3,deepseek_mtp}]
              [--speculative-draft-model SPECULATIVE_DRAFT_MODEL]
              [--speculative-num-draft-tokens SPECULATIVE_NUM_DRAFT_TOKENS]
              model_path
```

lmdeploy chat positional arguments#

`model_path` - The path of a model. it could be one of the following options: - i) a local directory path of a turbomind model which is converted by lmdeploy convert command or download from ii) and iii). - ii) the model_id of a lmdeploy-quantized model hosted inside a model repo on huggingface.co, such as `"internlm/internlm-chat-20b-4bit"`, `"lmdeploy/llama2-chat-70b-4bit"`, etc. - iii) the model_id of a model hosted inside a model repo on huggingface.co, such as `"internlm/internlm-chat-7b"`, `"qwen/qwen-7b-chat"`, `"baichuan-inc/baichuan2-7b-chat"` and so on (default: `None`)

lmdeploy chat options#

`-h`, `--help` - show this help message and exit

`--backend``BACKEND` - Set the inference backend (default: `turbomind`)

`--chat-template``CHAT_TEMPLATE` - A JSON file or string that specifies the chat template configuration. Please refer to https://lmdeploy.readthedocs.io/en/latest/advance/chat_template.html for the specification (default: `None`)

`--revision``REVISION` - The specific model version to use. It can be a branch name, a tag name, or a commit id. If unspecified, will use the default version.

`--download-dir``DOWNLOAD_DIR` - Directory to download and load the weights, default to the default cache directory of huggingface.

lmdeploy chat PyTorch engine arguments#

`--adapters``ADAPTERS` - Used to set path(s) of lora adapter(s). One can input key-value pairs in xxx=yyy format for multiple lora adapters. If only have one adapter, one can only input the path of the adapter. (default: `None`)

`--device``DEVICE` - The device type of running (default: `cuda`)

`--eager-mode` - Whether to enable eager mode. If True, cuda graph would be disabled

`--dllm-block-length``DLLM_BLOCK_LENGTH` - Block length for dllm (default: `None`)

`--dtype``DTYPE` - data type for model weights and activations. The `"auto"` option will use FP16 precision for FP32 and FP16 models, and BF16 precision for BF16 models. This option will be ignored if the model is a quantized model (default: `auto`)

`--tp``TP` - GPU number used in tensor parallelism. Should be 2^n (default: `1`)

`--session-len``SESSION_LEN` - The max session length of a sequence (default: `None`)

`--cache-max-entry-count``CACHE_MAX_ENTRY_COUNT` - The percentage of free gpu memory occupied by the k/v cache, excluding weights (default: `0.8`)

`--enable-prefix-caching` - Enable cache and match prefix

`--quant-policy``QUANT_POLICY` - Quantize kv or not. 0: no quant; 4: 4bit kv; 8: 8bit kv (default: `0`)

lmdeploy chat TurboMind engine arguments#

`--dtype``DTYPE` - data type for model weights and activations. The `"auto"` option will use FP16 precision for FP32 and FP16 models, and BF16 precision for BF16 models. This option will be ignored if the model is a quantized model (default: `auto`)

`--tp``TP` - GPU number used in tensor parallelism. Should be 2^n (default: `1`)

`--session-len``SESSION_LEN` - The max session length of a sequence (default: `None`)

`--cache-max-entry-count``CACHE_MAX_ENTRY_COUNT` - The percentage of free gpu memory occupied by the k/v cache, excluding weights (default: `0.8`)

`--enable-prefix-caching` - Enable cache and match prefix

`--quant-policy``QUANT_POLICY` - Quantize kv or not. 0: no quant; 4: 4bit kv; 8: 8bit kv (default: `0`)

`--model-format``MODEL_FORMAT` - The format of input model. hf means hf_llama, awq and gptq refer to 4-bit grouped quantization, compressed-tensors refers to pack-quantized grouped int4 checkpoints and is usually auto-detected from the model config, fp8 refers to blocked fp8 checkpoints, and mxfp4 refers to MXFP4 expert weights. (default: `None`)

`--rope-scaling-factor``ROPE_SCALING_FACTOR` - Rope scaling factor (default: `0.0`)

`--communicator``COMMUNICATOR` - Communication backend for multi-GPU inference. The `"native"` option is deprecated and serves as an alias for `"cuda-ipc"` (default: `nccl`)

`--cp``CP` - context parallelism size in attention for turbomind backend, tp must be a multiple of cp. (default: `1`)

`--async``ASYNC_` - Enable async execution (default: 1, enabled). Set to 0 to disable async mode, 1 to enable it. (default: `1`)

lmdeploy chat Speculative decoding arguments#

`--speculative-algorithm``SPECULATIVE_ALGORITHM` - The speculative algorithm to use. None means speculative decoding is disabled (default: `None`)

`--speculative-draft-model``SPECULATIVE_DRAFT_MODEL` - The path to speculative draft model (default: `None`)

`--speculative-num-draft-tokens``SPECULATIVE_NUM_DRAFT_TOKENS` - The number of speculative tokens to generate per step (default: `1`)
