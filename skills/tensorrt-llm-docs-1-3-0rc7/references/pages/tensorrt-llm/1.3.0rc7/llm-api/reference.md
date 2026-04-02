# API Reference — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/llm-api/reference.html

API Reference#

Note

Since version 1.0, we have attached a status label to LLM, LlmArgs and TorchLlmArgs Classes.

`stable` - The item is stable and will keep consistent.

`prototype` - The item is a prototype and is subject to change.

`beta` - The item is in beta and approaching stability.

`deprecated` - The item is deprecated and will be removed in a future release.

classtensorrt_llm.llmapi.LLM(

model:str|Path,

tokenizer:str|Path|TokenizerBase|PreTrainedTokenizerBase|None=None,

tokenizer_mode:Literal['auto','slow']='auto',

skip_tokenizer_init:bool=False,

trust_remote_code:bool=False,

tensor_parallel_size:int=1,

dtype:str='auto',

revision:str|None=None,

tokenizer_revision:str|None=None,

**kwargs:Any,

)[source]#

Bases: `_TorchLLM`

LLM class is the main class for running a LLM model.

For more details about the arguments, please refer to `TorchLlmArgs`.

Parameters:

model (Union[str, pathlib.Path]) – `stable` The path to the model checkpoint or the model name from the Hugging Face Hub.

tokenizer (Union[str, pathlib.Path, transformers.tokenization_utils_base.PreTrainedTokenizerBase, tensorrt_llm.tokenizer.tokenizer.TokenizerBase, NoneType]) – `stable` The path to the tokenizer checkpoint or the tokenizer name from the Hugging Face Hub. Defaults to None.

tokenizer_mode (Literal['auto', 'slow']) – `stable` The mode to initialize the tokenizer. Defaults to auto.

custom_tokenizer (Optional[str]) – `prototype` Specify a custom tokenizer implementation. Accepts either: (1) a built-in alias (e.g., ‘deepseek_v32’), or (2) a Python import path (e.g., ‘tensorrt_llm.tokenizer.deepseek_v32.DeepseekV32Tokenizer’). The tokenizer class must implement ‘from_pretrained(path, **kwargs)’ and the TokenizerBase interface. Defaults to None.

skip_tokenizer_init (bool) – `stable` Whether to skip the tokenizer initialization. Defaults to False.

trust_remote_code (bool) – `stable` Whether to trust the remote code. Defaults to False.

tensor_parallel_size (int) – `stable` The tensor parallel size. Defaults to 1.

dtype (str) – `stable` The data type to use for the model. Defaults to auto.

revision (Optional[str]) – `stable` The revision to use for the model. Defaults to None.

tokenizer_revision (Optional[str]) – `stable` The revision to use for the tokenizer. Defaults to None.

model_kwargs (Optional[Dict[str, Any]]) – `prototype` Optional parameters overriding model config defaults. Precedence: (1) model_kwargs, (2) model config file, (3) model config class defaults. Unknown keys are ignored Defaults to None.

pipeline_parallel_size (int) – `stable` The pipeline parallel size. Defaults to 1.

context_parallel_size (int) – `stable` The context parallel size. Defaults to 1.

gpus_per_node (Optional[int]) – `beta` The number of GPUs per node. Defaults to None.

moe_cluster_parallel_size (Optional[int]) – `beta` The cluster parallel size for MoE model’s expert weights. Defaults to None.

moe_tensor_parallel_size (Optional[int]) – `stable` The tensor parallel size for MoE model’s expert weights. Defaults to None.

moe_expert_parallel_size (Optional[int]) – `stable` The expert parallel size for MoE model’s expert weights. Defaults to None.

enable_attention_dp (bool) – `beta` Enable attention data parallel. Defaults to False.

enable_lm_head_tp_in_adp (bool) – `prototype` Enable LM head TP in attention dp. Defaults to False.

pp_partition (Optional[List[int]]) – `prototype` Pipeline parallel partition, a list of each rank’s layer number. Defaults to None.

cp_config (Optional[tensorrt_llm.llmapi.llm_args.CpConfig]) – `prototype` Context parallel config. Defaults to None.

load_format (Union[str, tensorrt_llm.llmapi.llm_args.LoadFormat]) – `stable` How to load the model weights. By default, detect the weight type from the model checkpoint. Defaults to 0.

enable_lora (bool) – `stable` Enable LoRA. Defaults to False.

lora_config (Optional[tensorrt_llm.lora_helper.LoraConfig]) – `stable` LoRA configuration for the model. Defaults to None.

kv_cache_config (tensorrt_llm.llmapi.llm_args.KvCacheConfig) – `stable` KV cache config. Defaults to None.

enable_chunked_prefill (bool) – `stable` Enable chunked prefill. Defaults to False.

guided_decoding_backend (Optional[Literal['xgrammar', 'llguidance']]) – `stable` Guided decoding backend. llguidance is supported in PyTorch backend only. Defaults to None.

batched_logits_processor (Optional[tensorrt_llm.sampling_params.BatchedLogitsProcessor]) – `stable` Batched logits processor. Defaults to None.

iter_stats_max_iterations (Optional[int]) – `prototype` The maximum number of iterations for iter stats. Defaults to None.

request_stats_max_iterations (Optional[int]) – `prototype` The maximum number of iterations for request stats. Defaults to None.

peft_cache_config (Optional[tensorrt_llm.llmapi.llm_args.PeftCacheConfig]) – `prototype` PEFT cache config. Defaults to None.

scheduler_config (tensorrt_llm.llmapi.llm_args.SchedulerConfig) – `prototype` Scheduler config. Defaults to None.

cache_transceiver_config (Optional[tensorrt_llm.llmapi.llm_args.CacheTransceiverConfig]) – `prototype` Cache transceiver config. Defaults to None.

sparse_attention_config (Union[tensorrt_llm.llmapi.llm_args.RocketSparseAttentionConfig, tensorrt_llm.llmapi.llm_args.DeepSeekSparseAttentionConfig, tensorrt_llm.llmapi.llm_args.SkipSoftmaxAttentionConfig, NoneType]) – `prototype` Sparse attention config. Defaults to None.

speculative_config (Union[tensorrt_llm.llmapi.llm_args.DraftTargetDecodingConfig, tensorrt_llm.llmapi.llm_args.EagleDecodingConfig, tensorrt_llm.llmapi.llm_args.Eagle3DecodingConfig, tensorrt_llm.llmapi.llm_args.LookaheadDecodingConfig, tensorrt_llm.llmapi.llm_args.MedusaDecodingConfig, tensorrt_llm.llmapi.llm_args.MTPDecodingConfig, tensorrt_llm.llmapi.llm_args.NGramDecodingConfig, tensorrt_llm.llmapi.llm_args.SADecodingConfig, tensorrt_llm.llmapi.llm_args.UserProvidedDecodingConfig, tensorrt_llm.llmapi.llm_args.SaveHiddenStatesDecodingConfig, tensorrt_llm.llmapi.llm_args.PARDDecodingConfig, tensorrt_llm.llmapi.llm_args.AutoDecodingConfig, NoneType]) – `stable` Speculative decoding config. Defaults to None.

max_batch_size (Optional[int]) – `stable` The maximum batch size. Defaults to 2048.

max_input_len (Optional[int]) – `stable` The maximum input length. Defaults to 1024.

max_seq_len (Optional[int]) – `stable` The maximum sequence length. Defaults to None.

max_beam_width (Optional[int]) – `stable` The maximum beam width. Defaults to 1.

max_num_tokens (Optional[int]) – `stable` The maximum number of tokens. Defaults to 8192.

gather_generation_logits (bool) – `prototype` Gather generation logits. Defaults to False.

num_postprocess_workers (int) – `prototype` The number of processes used for postprocessing the generated tokens, including detokenization. Defaults to 0.

postprocess_tokenizer_dir (Optional[str]) – `prototype` The path to the tokenizer directory for postprocessing. Defaults to None.

reasoning_parser (Optional[str]) – `prototype` The parser to separate reasoning content from output. Defaults to None.

otlp_traces_endpoint (Optional[str]) – `prototype` Target URL to which OpenTelemetry traces will be sent. Defaults to None.

return_perf_metrics (bool) – `prototype` Return perf metrics. Defaults to False.

perf_metrics_max_requests (int) – `prototype` The maximum number of requests for perf metrics. Must also set return_perf_metrics to true to get perf metrics. Defaults to 0.

orchestrator_type (Optional[Literal['rpc', 'ray']]) – `prototype` The orchestrator type to use. Defaults to None, which uses MPI. Defaults to None.

env_overrides (Optional[Dict[str, str]]) – `prototype` [EXPERIMENTAL] Environment variable overrides. NOTE: import-time-cached env vars in the code won’t update unless the code fetches them from os.environ on demand. Defaults to None.

garbage_collection_gen0_threshold (int) – `beta` Threshold for Python garbage collection of generation 0 objects. Lower values trigger more frequent garbage collection. Defaults to 20000.

cuda_graph_config (Optional[tensorrt_llm.llmapi.llm_args.CudaGraphConfig]) – `beta` CUDA graph config. If true, use CUDA graphs for decoding. CUDA graphs are only created for the batch sizes in cuda_graph_config.batch_sizes, and are enabled for batches that consist of decoding requests only (the reason is that it’s hard to capture a single graph with prefill requests since the input shapes are a function of the sequence lengths). Note that each CUDA graph can use up to 200 MB of extra memory. Defaults to None.

attention_dp_config (Optional[tensorrt_llm.llmapi.llm_args.AttentionDpConfig]) – `beta` Optimized load-balancing for the DP Attention scheduler. Defaults to None.

disable_overlap_scheduler (bool) – `beta` Disable the overlap scheduler. Defaults to False.

moe_config (tensorrt_llm.llmapi.llm_args.MoeConfig) – `beta` MoE config. Defaults to None.

nvfp4_gemm_config (tensorrt_llm.llmapi.llm_args.Nvfp4GemmConfig) – `beta` NVFP4 GEMM backend config. Defaults to None.

attn_backend (str) – `beta` Attention backend to use. Defaults to TRTLLM.

sampler_type (Union[str, tensorrt_llm.llmapi.llm_args.SamplerType]) – `beta` The type of sampler to use. Options are TRTLLMSampler, TorchSampler or auto. Defaults to auto, which will use TorchSampler unless BeamSearch is requested. Defaults to auto.

sampler_force_async_worker (bool) – `prototype` Force usage of the async worker in the sampler for D2H copies, even if confidential compute is not active. Normally, the async worker should only be used when confidential compute is active. This argument is provided to enable it for testing purposes, irrespective of confidential compute state. Defaults to False.

enable_iter_perf_stats (bool) – `prototype` Enable iteration performance statistics. Defaults to False.

enable_iter_req_stats (bool) – `prototype` If true, enables per request stats per iteration. Must also set enable_iter_perf_stats to true to get request stats. Defaults to False.

print_iter_log (bool) – `beta` Print iteration logs. Defaults to False.

batch_wait_timeout_ms (float) – `prototype` If greater than 0, the request queue might wait up to batch_wait_timeout_ms to receive max_batch_size requests, if fewer than max_batch_size requests are currently available. If 0, no waiting occurs. Defaults to 0.

batch_wait_timeout_iters (int) – `prototype` Maximum number of iterations the scheduler will wait to accumulate new coming requests for improved GPU utilization efficiency. If greater than 0, the scheduler will delay batch processing to gather more requests up to the specified iteration limit. If 0, disables timeout-iters-based batching delays. Defaults to 0.

batch_wait_max_tokens_ratio (float) – `prototype` Token accumulation threshold ratio for batch scheduling optimization. If greater than 0, the scheduler will accumulate requests locally until the total token count reaches batch_wait_max_tokens_ratio * max_num_tokens. This mechanism enhances GPU utilization efficiency by ensuring adequate batch sizes. If 0, disables token-based batching delays. Defaults to 0.

torch_compile_config (Optional[tensorrt_llm.llmapi.llm_args.TorchCompileConfig]) – `prototype` Torch compile config. Defaults to None.

enable_autotuner (bool) – `prototype` Enable autotuner for all tunable ops. This flag is for debugging purposes only, and the performance may significantly degrade if set to false. Defaults to True.

enable_layerwise_nvtx_marker (bool) – `beta` If true, enable layerwise nvtx marker. Defaults to False.

enable_min_latency (bool) – `beta` If true, enable min-latency mode. Currently only used for Llama4. Defaults to False.

stream_interval (int) – `stable` The iteration interval to create responses under the streaming mode. Set this to a larger value when the batch size is large, which helps reduce the streaming overhead. Defaults to 1.

force_dynamic_quantization (bool) – `prototype` If true, force dynamic quantization. Defaults to False. Defaults to False.

allreduce_strategy (Optional[Literal['AUTO', 'NCCL', 'UB', 'MINLATENCY', 'ONESHOT', 'TWOSHOT', 'LOWPRECISION', 'MNNVL', 'NCCL_SYMMETRIC']]) – `beta` Allreduce strategy to use. Defaults to AUTO.

checkpoint_loader (Optional[tensorrt_llm._torch.models.checkpoints.BaseCheckpointLoader]) – `prototype` The checkpoint loader to use for this LLM instance. You may use a custom checkpoint loader by subclassing BaseCheckpointLoader and providing an instance of the subclass here to load weights from a custom checkpoint format.
If neither checkpoint_format nor checkpoint_loader are provided, checkpoint_format will be set to HF and the default HfCheckpointLoader will be used.
If checkpoint_format and checkpoint_loader are both provided, checkpoint_loader will be ignored. Defaults to None.

checkpoint_format (Optional[str]) – `prototype` The format of the provided checkpoint. You may use a custom checkpoint format by subclassing BaseCheckpointLoader and registering it with register_checkpoint_loader.
If neither checkpoint_format nor checkpoint_loader are provided, checkpoint_format will be set to HF and the default HfCheckpointLoader will be used.
If checkpoint_format and checkpoint_loader are both provided, checkpoint_loader will be ignored. Defaults to None.

kv_connector_config (Optional[tensorrt_llm.llmapi.llm_args.KvCacheConnectorConfig]) – `prototype` The config for KV cache connector. Defaults to None.

mm_encoder_only (bool) – `prototype` Only load/execute the vision encoder part of the full model. Defaults to False. Defaults to False.

ray_worker_extension_cls (Optional[str]) – `prototype` The full worker extension class name including module path. Allows users to extend the functions of the RayGPUWorker class. Defaults to None.

ray_placement_config (Optional[tensorrt_llm.llmapi.llm_args.RayPlacementConfig]) – `prototype` Placement config for RayGPUWorker. Only used with AsyncLLM and orchestrator_type=’ray’. Defaults to None.

ray_worker_nsight_options (Optional[dict[str, str]]) – `prototype` Nsight options. Defaults to None.

enable_sleep (bool) – `prototype` Enable LLM sleep feature. Sleep feature requires extra setup that may slow down model loading. Only enable it if you intend to use this feature. Defaults to False.

use_cute_dsl_blockscaling_mm (bool) – `prototype` If true, use CuTe DSL fp8 blockscaling mm implementation. Defaults to False.

use_cute_dsl_blockscaling_bmm (bool) – `prototype` If true, use CuTe DSL fp8 blockscaling bmm implementation. Defaults to False.

disable_flashinfer_sampling (bool) – `prototype` Disable the use of FlashInfer.sampling. This option is likely to be removed in the future. Defaults to False.

max_stats_len (int) – `prototype` The max number of performance statistic entries. Defaults to 1000.

layer_wise_benchmarks_config (tensorrt_llm.llmapi.llm_args.LayerwiseBenchmarksConfig) – `prototype` Defaults to None.

tokenizer#

The tokenizer loaded by LLM instance, if any.

Type:

tensorrt_llm.llmapi.tokenizer.TokenizerBase, optional

llm_id#

The unique ID of the LLM instance.

Type:

str

disaggregated_params#

The disaggregated parameters of the LLM instance.

Type:

dict

__init__(

model:str|Path,

tokenizer:str|Path|TokenizerBase|PreTrainedTokenizerBase|None=None,

tokenizer_mode:Literal['auto','slow']='auto',

skip_tokenizer_init:bool=False,

trust_remote_code:bool=False,

tensor_parallel_size:int=1,

dtype:str='auto',

revision:str|None=None,

tokenizer_revision:str|None=None,

**kwargs:Any,

)→None[source]#

generate(

inputs:str|List[int]|TextPrompt|TokensPrompt|Sequence[str|List[int]|TextPrompt|TokensPrompt],

sampling_params:SamplingParams|List[SamplingParams]|None=None,

use_tqdm:bool=True,

lora_request:LoRARequest|Sequence[LoRARequest]|None=None,

prompt_adapter_request:PromptAdapterRequest|Sequence[PromptAdapterRequest]|None=None,

kv_cache_retention_config:KvCacheRetentionConfig|Sequence[KvCacheRetentionConfig]|None=None,

disaggregated_params:DisaggregatedParams|Sequence[DisaggregatedParams]|None=None,

scheduling_params:SchedulingParams|List[SchedulingParams]|None=None,

cache_salt:str|Sequence[str]|None=None,

)→RequestOutput|List[RequestOutput]#

Generate output for the given prompts in the synchronous mode.
Synchronous generation accepts either single prompt or batched prompts.

Parameters:

inputs (tensorrt_llm.inputs.data.PromptInputs, Sequence[tensorrt_llm.inputs.data.PromptInputs]) – The prompt text or token ids.
It can be single prompt or batched prompts.

sampling_params (tensorrt_llm.sampling_params.SamplingParams, List[tensorrt_llm.sampling_params.SamplingParams], optional) – The sampling params for the generation. Defaults to None.
A default one will be used if not provided.

use_tqdm (bool) – Whether to use tqdm to display the progress bar. Defaults to True.

lora_request (tensorrt_llm.executor.request.LoRARequest, Sequence[tensorrt_llm.executor.request.LoRARequest], optional) – LoRA request to use for generation, if any. Defaults to None.

prompt_adapter_request (tensorrt_llm.executor.request.PromptAdapterRequest, Sequence[tensorrt_llm.executor.request.PromptAdapterRequest], optional) – Prompt Adapter request to use for generation, if any. Defaults to None.

kv_cache_retention_config (tensorrt_llm.bindings.executor.KvCacheRetentionConfig, Sequence[tensorrt_llm.bindings.executor.KvCacheRetentionConfig], optional) – Configuration for the request’s retention in the KV Cache. Defaults to None.

disaggregated_params (tensorrt_llm.disaggregated_params.DisaggregatedParams, Sequence[tensorrt_llm.disaggregated_params.DisaggregatedParams], optional) – Disaggregated parameters. Defaults to None.

scheduling_params (tensorrt_llm.scheduling_params.SchedulingParams, List[tensorrt_llm.scheduling_params.SchedulingParams], optional) – Scheduling parameters. Defaults to None.

cache_salt (str, Sequence[str], optional) – If specified, KV cache will be salted with the provided string to limit the kv cache reuse to the requests with the same string. Defaults to None.

Returns:

The output data of the completion request to the LLM.

Return type:

Union[tensorrt_llm.llmapi.RequestOutput, List[tensorrt_llm.llmapi.RequestOutput]]

generate_async(

inputs:str|List[int]|TextPrompt|TokensPrompt|PreprocessedInputs,

sampling_params:SamplingParams|None=None,

lora_request:LoRARequest|None=None,

prompt_adapter_request:PromptAdapterRequest|None=None,

streaming:bool=False,

kv_cache_retention_config:KvCacheRetentionConfig|None=None,

disaggregated_params:DisaggregatedParams|None=None,

trace_headers:Mapping[str,str]|None=None,

_postproc_params:PostprocParams|None=None,

scheduling_params:SchedulingParams|None=None,

cache_salt:str|None=None,

)→RequestOutput#

Generate output for the given prompt in the asynchronous mode.
Asynchronous generation accepts single prompt only.

Parameters:

inputs (Union[tensorrt_llm.inputs.data.PromptInputs, tensorrt_llm.llmapi.llm.PreprocessedInputs]) – The prompt text or token ids, or a PreprocessedInputs returned by preprocess. If the latter, preprocessing will be skipped by this method.

sampling_params (tensorrt_llm.sampling_params.SamplingParams, optional) – The sampling params for the generation. Defaults to None.
A default one will be used if not provided.

lora_request (tensorrt_llm.executor.request.LoRARequest, optional) – LoRA request to use for generation, if any. Defaults to None.

prompt_adapter_request (tensorrt_llm.executor.request.PromptAdapterRequest, optional) – Prompt Adapter request to use for generation, if any. Defaults to None.

streaming (bool) – Whether to use the streaming mode for the generation. Defaults to False.

kv_cache_retention_config (tensorrt_llm.bindings.executor.KvCacheRetentionConfig, optional) – Configuration for the request’s retention in the KV Cache. Defaults to None.

disaggregated_params (tensorrt_llm.disaggregated_params.DisaggregatedParams, optional) – Disaggregated parameters. Defaults to None.

trace_headers (Mapping[str, str], optional) – Trace headers. Defaults to None.

scheduling_params (tensorrt_llm.scheduling_params.SchedulingParams, optional) – Scheduling parameters. Defaults to None.

cache_salt (str, optional) – If specified, KV cache will be salted with the provided string to limit the kv cache reuse to the requests with the same string. Defaults to None.

Returns:

The output data of the completion request to the LLM.

Return type:

tensorrt_llm.llmapi.RequestOutput

get_kv_cache_events(

timeout:float|None=2,

)→List[dict]#

`beta` Get iteration KV events from the runtime.

KV events are used to track changes and operations within the KV Cache. Types of events:

KVCacheCreatedData: Indicates the creation of cache blocks.

KVCacheStoredData: Represents a sequence of stored blocks.

KVCacheRemovedData: Contains the hashes of blocks that are being removed from the cache.

KVCacheUpdatedData: Captures updates to existing cache blocks.

To enable KV events:

set event_buffer_max_size to a positive integer in the KvCacheConfig.

set enable_block_reuse to True in the KvCacheConfig.

Parameters:

timeout (float, optional) – Max wait time in seconds when retrieving events from queue. Defaults to 2.

Returns:

A list of runtime events as dict.

Return type:

List[dict]

get_kv_cache_events_async(

timeout:float|None=2,

)→IterationResult#

`beta` Get iteration KV events from the runtime.

KV events are used to track changes and operations within the KV Cache. Types of events:

KVCacheCreatedData: Indicates the creation of cache blocks.

KVCacheStoredData: Represents a sequence of stored blocks.

KVCacheRemovedData: Contains the hashes of blocks that are being removed from the cache.

KVCacheUpdatedData: Captures updates to existing cache blocks.

To enable KV events:

set event_buffer_max_size to a positive integer in the KvCacheConfig.

set enable_block_reuse to True in the KvCacheConfig.

Parameters:

timeout (float, optional) – Max wait time in seconds when retrieving events from queue. Defaults to 2.

Returns:

An async iterable object containing runtime events.

Return type:

tensorrt_llm.executor.result.IterationResult

get_stats(timeout:float|None=2)→List[dict]#

`beta` Get iteration statistics from the runtime.
To collect statistics, call this function after prompts have been submitted with LLM().generate().

Parameters:

timeout (float, optional) – Max wait time in seconds when retrieving stats from queue. Defaults to 2.

Returns:

A list of runtime stats as dicts.

e.g., [{“cpuMemUsage”: …, “iter”: 0, …}, {“cpuMemUsage”: …, “iter”: 1, …}]

Return type:

List[dict]

get_stats_async(

timeout:float|None=2,

)→IterationResult#

`beta` Get iteration statistics from the runtime.
To collect statistics, you can call this function in an async coroutine or the /metrics endpoint (if you’re using trtllm-serve)
after prompts have been submitted.

Parameters:

timeout (float, optional) – Max wait time in seconds when retrieving stats from queue. Defaults to 2.

Returns:

An async iterable object containing runtime stats.

Return type:

tensorrt_llm.executor.result.IterationResult

preprocess(

inputs:str|List[int]|TextPrompt|TokensPrompt,

sampling_params:SamplingParams|None=None,

disaggregated_params:DisaggregatedParams|None=None,

)→PreprocessedInputs#

`prototype` Preprocess raw prompts into token IDs and multimodal params.

Parameters:

inputs (tensorrt_llm.inputs.data.PromptInputs) – The prompt text or token ids; it must be single prompt.

sampling_params (tensorrt_llm.sampling_params.SamplingParams, optional) – The sampling params for the generation. Defaults to None.
A default one will be used if not provided.

disaggregated_params (tensorrt_llm.disaggregated_params.DisaggregatedParams, optional) – Disaggregated parameters. Defaults to None.

Returns:

A preprocessed-inputs object that can be

passed directly to `generate_async()` as `inputs`.

Return type:

tensorrt_llm.llmapi.llm.PreprocessedInputs

shutdown()→None#

`beta` None

propertydisaggregated_params:dict#

`beta` None

propertyllm_id:str#

`beta` None

propertytokenizer:TokenizerBase|None#

classtensorrt_llm.llmapi.AsyncLLM(

placement_groups:List[Any]|None=None,

placement_bundle_indices:List[List[int]]|None=None,

per_worker_gpu_share:float|None=None,

*args,

**kwargs,

)[source]#

Bases: `LLM`

AsyncLLM is a subclass of LLM that supports asynchronous setup, release and
resume operations that are necessary for RL or agentic scenarios.

Currently, RL APIs are only supported with Ray orchestrator.

__init__(

placement_groups:List[Any]|None=None,

placement_bundle_indices:List[List[int]]|None=None,

per_worker_gpu_share:float|None=None,

*args,

**kwargs,

)[source]#

asynccollective_rpc(

method:str,

args:tuple[Any,...]=(),

kwargs:dict|None=None,

unique_reply_rank:int|None=None,

target_ranks:int|list[int]|None=None,

)→list[Any][source]#

Execute an asynchronous RPC call on all GPU workers. Currently, this is only supported for RayExecutor.

Parameters:

method (str) – The name of the worker method to execute.

args (tuple[Any, ...]) – Positional arguments to pass to the worker method. Defaults to ().

kwargs (dict, optional) – Keyword arguments to pass to the worker method. Defaults to None.

unique_reply_rank (int, optional) – The rank of the worker that will be used to send the reply.

target_ranks (int | list[int] | None) – The ranks of the workers that will be used to send the reply.

Returns:

A list of results from each worker.

Return type:

list[Any]

generate(

inputs:str|List[int]|TextPrompt|TokensPrompt|Sequence[str|List[int]|TextPrompt|TokensPrompt],

sampling_params:SamplingParams|List[SamplingParams]|None=None,

use_tqdm:bool=True,

lora_request:LoRARequest|Sequence[LoRARequest]|None=None,

prompt_adapter_request:PromptAdapterRequest|Sequence[PromptAdapterRequest]|None=None,

kv_cache_retention_config:KvCacheRetentionConfig|Sequence[KvCacheRetentionConfig]|None=None,

disaggregated_params:DisaggregatedParams|Sequence[DisaggregatedParams]|None=None,

scheduling_params:SchedulingParams|List[SchedulingParams]|None=None,

cache_salt:str|Sequence[str]|None=None,

)→RequestOutput|List[RequestOutput]#

Generate output for the given prompts in the synchronous mode.
Synchronous generation accepts either single prompt or batched prompts.

Parameters:

inputs (tensorrt_llm.inputs.data.PromptInputs, Sequence[tensorrt_llm.inputs.data.PromptInputs]) – The prompt text or token ids.
It can be single prompt or batched prompts.

sampling_params (tensorrt_llm.sampling_params.SamplingParams, List[tensorrt_llm.sampling_params.SamplingParams], optional) – The sampling params for the generation. Defaults to None.
A default one will be used if not provided.

use_tqdm (bool) – Whether to use tqdm to display the progress bar. Defaults to True.

lora_request (tensorrt_llm.executor.request.LoRARequest, Sequence[tensorrt_llm.executor.request.LoRARequest], optional) – LoRA request to use for generation, if any. Defaults to None.

prompt_adapter_request (tensorrt_llm.executor.request.PromptAdapterRequest, Sequence[tensorrt_llm.executor.request.PromptAdapterRequest], optional) – Prompt Adapter request to use for generation, if any. Defaults to None.

kv_cache_retention_config (tensorrt_llm.bindings.executor.KvCacheRetentionConfig, Sequence[tensorrt_llm.bindings.executor.KvCacheRetentionConfig], optional) – Configuration for the request’s retention in the KV Cache. Defaults to None.

disaggregated_params (tensorrt_llm.disaggregated_params.DisaggregatedParams, Sequence[tensorrt_llm.disaggregated_params.DisaggregatedParams], optional) – Disaggregated parameters. Defaults to None.

scheduling_params (tensorrt_llm.scheduling_params.SchedulingParams, List[tensorrt_llm.scheduling_params.SchedulingParams], optional) – Scheduling parameters. Defaults to None.

cache_salt (str, Sequence[str], optional) – If specified, KV cache will be salted with the provided string to limit the kv cache reuse to the requests with the same string. Defaults to None.

Returns:

The output data of the completion request to the LLM.

Return type:

Union[tensorrt_llm.llmapi.RequestOutput, List[tensorrt_llm.llmapi.RequestOutput]]

generate_async(

inputs:str|List[int]|TextPrompt|TokensPrompt|PreprocessedInputs,

sampling_params:SamplingParams|None=None,

lora_request:LoRARequest|None=None,

prompt_adapter_request:PromptAdapterRequest|None=None,

streaming:bool=False,

kv_cache_retention_config:KvCacheRetentionConfig|None=None,

disaggregated_params:DisaggregatedParams|None=None,

trace_headers:Mapping[str,str]|None=None,

_postproc_params:PostprocParams|None=None,

scheduling_params:SchedulingParams|None=None,

cache_salt:str|None=None,

)→RequestOutput#

Generate output for the given prompt in the asynchronous mode.
Asynchronous generation accepts single prompt only.

Parameters:

inputs (Union[tensorrt_llm.inputs.data.PromptInputs, tensorrt_llm.llmapi.llm.PreprocessedInputs]) – The prompt text or token ids, or a PreprocessedInputs returned by preprocess. If the latter, preprocessing will be skipped by this method.

sampling_params (tensorrt_llm.sampling_params.SamplingParams, optional) – The sampling params for the generation. Defaults to None.
A default one will be used if not provided.

lora_request (tensorrt_llm.executor.request.LoRARequest, optional) – LoRA request to use for generation, if any. Defaults to None.

prompt_adapter_request (tensorrt_llm.executor.request.PromptAdapterRequest, optional) – Prompt Adapter request to use for generation, if any. Defaults to None.

streaming (bool) – Whether to use the streaming mode for the generation. Defaults to False.

kv_cache_retention_config (tensorrt_llm.bindings.executor.KvCacheRetentionConfig, optional) – Configuration for the request’s retention in the KV Cache. Defaults to None.

disaggregated_params (tensorrt_llm.disaggregated_params.DisaggregatedParams, optional) – Disaggregated parameters. Defaults to None.

trace_headers (Mapping[str, str], optional) – Trace headers. Defaults to None.

scheduling_params (tensorrt_llm.scheduling_params.SchedulingParams, optional) – Scheduling parameters. Defaults to None.

cache_salt (str, optional) – If specified, KV cache will be salted with the provided string to limit the kv cache reuse to the requests with the same string. Defaults to None.

Returns:

The output data of the completion request to the LLM.

Return type:

tensorrt_llm.llmapi.RequestOutput

get_kv_cache_events(

timeout:float|None=2,

)→List[dict]#

`beta` Get iteration KV events from the runtime.

KV events are used to track changes and operations within the KV Cache. Types of events:

KVCacheCreatedData: Indicates the creation of cache blocks.

KVCacheStoredData: Represents a sequence of stored blocks.

KVCacheRemovedData: Contains the hashes of blocks that are being removed from the cache.

KVCacheUpdatedData: Captures updates to existing cache blocks.

To enable KV events:

set event_buffer_max_size to a positive integer in the KvCacheConfig.

set enable_block_reuse to True in the KvCacheConfig.

Parameters:

timeout (float, optional) – Max wait time in seconds when retrieving events from queue. Defaults to 2.

Returns:

A list of runtime events as dict.

Return type:

List[dict]

get_kv_cache_events_async(

timeout:float|None=2,

)→IterationResult#

`beta` Get iteration KV events from the runtime.

KV events are used to track changes and operations within the KV Cache. Types of events:

KVCacheCreatedData: Indicates the creation of cache blocks.

KVCacheStoredData: Represents a sequence of stored blocks.

KVCacheRemovedData: Contains the hashes of blocks that are being removed from the cache.

KVCacheUpdatedData: Captures updates to existing cache blocks.

To enable KV events:

set event_buffer_max_size to a positive integer in the KvCacheConfig.

set enable_block_reuse to True in the KvCacheConfig.

Parameters:

timeout (float, optional) – Max wait time in seconds when retrieving events from queue. Defaults to 2.

Returns:

An async iterable object containing runtime events.

Return type:

tensorrt_llm.executor.result.IterationResult

get_stats(timeout:float|None=2)→List[dict]#

`beta` Get iteration statistics from the runtime.
To collect statistics, call this function after prompts have been submitted with LLM().generate().

Parameters:

timeout (float, optional) – Max wait time in seconds when retrieving stats from queue. Defaults to 2.

Returns:

A list of runtime stats as dicts.

e.g., [{“cpuMemUsage”: …, “iter”: 0, …}, {“cpuMemUsage”: …, “iter”: 1, …}]

Return type:

List[dict]

get_stats_async(

timeout:float|None=2,

)→IterationResult#

`beta` Get iteration statistics from the runtime.
To collect statistics, you can call this function in an async coroutine or the /metrics endpoint (if you’re using trtllm-serve)
after prompts have been submitted.

Parameters:

timeout (float, optional) – Max wait time in seconds when retrieving stats from queue. Defaults to 2.

Returns:

An async iterable object containing runtime stats.

Return type:

tensorrt_llm.executor.result.IterationResult

preprocess(

inputs:str|List[int]|TextPrompt|TokensPrompt,

sampling_params:SamplingParams|None=None,

disaggregated_params:DisaggregatedParams|None=None,

)→PreprocessedInputs#

`prototype` Preprocess raw prompts into token IDs and multimodal params.

Parameters:

inputs (tensorrt_llm.inputs.data.PromptInputs) – The prompt text or token ids; it must be single prompt.

sampling_params (tensorrt_llm.sampling_params.SamplingParams, optional) – The sampling params for the generation. Defaults to None.
A default one will be used if not provided.

disaggregated_params (tensorrt_llm.disaggregated_params.DisaggregatedParams, optional) – Disaggregated parameters. Defaults to None.

Returns:

A preprocessed-inputs object that can be

passed directly to `generate_async()` as `inputs`.

Return type:

tensorrt_llm.llmapi.llm.PreprocessedInputs

asyncrelease(tags:list[str])[source]#

Release the GPU memory used by the LLM asynchronously.

Parameters:

tags – List of memory tag strings to release (e.g., [“model”, “kv_cache”]).

asyncresume(tags:list[str])[source]#

Resume the GPU memory used by the LLM asynchronously.

Parameters:

tags – List of memory tag strings to resume (e.g., [“model”, “kv_cache”]).

asyncsetup_async()[source]#

Setup the LLM asynchronously.

shutdown()→None#

`beta` None

asyncupdate_weights(weights:dict[str,str])[source]#

Update the weights of the LLM asynchronously.

Parameters:

weights – Dictionary mapping device UUIDs to IPC handles for weight tensors.

propertydisaggregated_params:dict#

`beta` None

propertyllm_id:str#

`beta` None

propertytokenizer:TokenizerBase|None#

classtensorrt_llm.llmapi.VisualGen(

model_path:str|Path,

diffusion_args:VisualGenArgs|None=None,

)[source]#

Bases: `object`

High-level API for visual generation.

__init__(

model_path:str|Path,

diffusion_args:VisualGenArgs|None=None,

)[source]#

`prototype` None

generate(

inputs:str|List[int]|VisualGenTextPrompt|VisualGenTokensPrompt|Sequence[str|List[int]|VisualGenTextPrompt|VisualGenTokensPrompt],

params:VisualGenParams,

)→MediaOutput[source]#

`prototype` Synchronous generation. Blocks until complete.

Parameters:

params – Generation parameters.

Returns:

Generated media with model-specific fields populated:

FLUX2: MediaOutput(image=torch.Tensor)

WAN: MediaOutput(video=torch.Tensor)

LTX2: MediaOutput(video=torch.Tensor, audio=torch.Tensor)

Return type:

MediaOutput

generate_async(

inputs:str|List[int]|VisualGenTextPrompt|VisualGenTokensPrompt|Sequence[str|List[int]|VisualGenTextPrompt|VisualGenTokensPrompt],

params:VisualGenParams,

)→DiffusionGenerationResult[source]#

`prototype` Async generation. Returns immediately with future-like object.

Parameters:

params – Generation parameters.

Returns:

Call result() to get output dict.

Return type:

DiffusionGenerationResult

shutdown()[source]#

`prototype` Shutdown executor and cleanup.

classtensorrt_llm.llmapi.VisualGenParams(

height:int=720,

width:int=1280,

num_inference_steps:int=50,

guidance_scale:float=5.0,

max_sequence_length:int=512,

seed:int=42,

num_frames:int=81,

frame_rate:float=24.0,

input_reference:str|None=None,

num_images_per_prompt:int=1,

image:List[str]|None=None,

mask:str|None=None,

guidance_rescale:float=0.0,

output_type:str='pt',

guidance_scale_2:float|None=None,

boundary_ratio:float|None=None,

last_image:str|None=None,

)[source]#

Bases: `object`

`prototype` Parameters for visual generation.

height#

Output height in pixels

Type:

int

width#

Output width in pixels

Type:

int

num_inference_steps#

Number of denoising steps

Type:

int

guidance_scale#

Classifier-free guidance scale

Type:

float

max_sequence_length#

Maximum sequence length for text encoding

Type:

int

seed#

Random seed for reproducibility

Type:

int

#Video-specificparameters

num_frames#

Number of video frames to generate

Type:

int

frame_rate#

Frame rate for video output in fps

Type:

float

#Image-specificparameters

num_images_per_prompt#

Number of images to generate per prompt (for image models)

Type:

int

#Advancedparameters

guidance_rescale#

Guidance rescale factor (for some models)

Type:

float

output_type#

Output type (“pt” for PyTorch tensors, “pil” for PIL images)

Type:

str

__init__(

height:int=720,

width:int=1280,

num_inference_steps:int=50,

guidance_scale:float=5.0,

max_sequence_length:int=512,

seed:int=42,

num_frames:int=81,

frame_rate:float=24.0,

input_reference:str|None=None,

num_images_per_prompt:int=1,

image:List[str]|None=None,

mask:str|None=None,

guidance_rescale:float=0.0,

output_type:str='pt',

guidance_scale_2:float|None=None,

boundary_ratio:float|None=None,

last_image:str|None=None,

)→None#

boundary_ratio:float|None=None#

frame_rate:float=24.0#

guidance_rescale:float=0.0#

guidance_scale:float=5.0#

guidance_scale_2:float|None=None#

height:int=720#

image:List[str]|None=None#

input_reference:str|None=None#

last_image:str|None=None#

mask:str|None=None#

max_sequence_length:int=512#

num_frames:int=81#

num_images_per_prompt:int=1#

num_inference_steps:int=50#

output_type:str='pt'#

seed:int=42#

width:int=1280#

classtensorrt_llm.llmapi.MultimodalEncoder(

model:str|Path,

trust_remote_code:bool=False,

tensor_parallel_size:int=1,

dtype:Literal['auto','float16','float32','bfloat16']='auto',

**kwargs:Any,

)[source]#

Bases: `_TorchLLM`

MultimodalEncoder class is the main class for running a multimodal encoder model using PyTorch backend.

__init__(

model:str|Path,

trust_remote_code:bool=False,

tensor_parallel_size:int=1,

dtype:Literal['auto','float16','float32','bfloat16']='auto',

**kwargs:Any,

)→None[source]#

generate(

inputs:str|List[int]|TextPrompt|TokensPrompt|Sequence[str|List[int]|TextPrompt|TokensPrompt],

use_tqdm:bool=True,

)→RequestOutput|List[RequestOutput][source]#

Generate output for the given prompts in the synchronous mode.
Synchronous generation accepts either single prompt or batched prompts.

Parameters:

inputs (tensorrt_llm.inputs.data.PromptInputs, Sequence[tensorrt_llm.inputs.data.PromptInputs]) – The prompt text or token ids.
It can be single prompt or batched prompts.

Returns:

The output data of the completion request to the LLM.

Return type:

Union[tensorrt_llm.llmapi.RequestOutput, List[tensorrt_llm.llmapi.RequestOutput]]

generate_async(

inputs:str|List[int]|TextPrompt|TokensPrompt,

sampling_params:SamplingParams|None=None,

)→RequestOutput[source]#

Generate output for the given multimodal request in the asynchronous mode.
Asynchronous generation accepts single multimodal request only.

Returns:

Future that resolves to tensorrt_llm.llmapi.RequestOutput containing mm_embeddings

get_kv_cache_events(

timeout:float|None=2,

)→List[dict]#

`beta` Get iteration KV events from the runtime.

KV events are used to track changes and operations within the KV Cache. Types of events:

KVCacheCreatedData: Indicates the creation of cache blocks.

KVCacheStoredData: Represents a sequence of stored blocks.

KVCacheRemovedData: Contains the hashes of blocks that are being removed from the cache.

KVCacheUpdatedData: Captures updates to existing cache blocks.

To enable KV events:

set event_buffer_max_size to a positive integer in the KvCacheConfig.

set enable_block_reuse to True in the KvCacheConfig.

Parameters:

timeout (float, optional) – Max wait time in seconds when retrieving events from queue. Defaults to 2.

Returns:

A list of runtime events as dict.

Return type:

List[dict]

get_kv_cache_events_async(

timeout:float|None=2,

)→IterationResult#

`beta` Get iteration KV events from the runtime.

KV events are used to track changes and operations within the KV Cache. Types of events:

KVCacheCreatedData: Indicates the creation of cache blocks.

KVCacheStoredData: Represents a sequence of stored blocks.

KVCacheRemovedData: Contains the hashes of blocks that are being removed from the cache.

KVCacheUpdatedData: Captures updates to existing cache blocks.

To enable KV events:

set event_buffer_max_size to a positive integer in the KvCacheConfig.

set enable_block_reuse to True in the KvCacheConfig.

Parameters:

timeout (float, optional) – Max wait time in seconds when retrieving events from queue. Defaults to 2.

Returns:

An async iterable object containing runtime events.

Return type:

tensorrt_llm.executor.result.IterationResult

get_stats(

timeout:float|None=2,

)→List[dict]#

`beta` Get iteration statistics from the runtime.
To collect statistics, call this function after prompts have been submitted with LLM().generate().

Parameters:

timeout (float, optional) – Max wait time in seconds when retrieving stats from queue. Defaults to 2.

Returns:

A list of runtime stats as dicts.

e.g., [{“cpuMemUsage”: …, “iter”: 0, …}, {“cpuMemUsage”: …, “iter”: 1, …}]

Return type:

List[dict]

get_stats_async(

timeout:float|None=2,

)→IterationResult#

`beta` Get iteration statistics from the runtime.
To collect statistics, you can call this function in an async coroutine or the /metrics endpoint (if you’re using trtllm-serve)
after prompts have been submitted.

Parameters:

timeout (float, optional) – Max wait time in seconds when retrieving stats from queue. Defaults to 2.

Returns:

An async iterable object containing runtime stats.

Return type:

tensorrt_llm.executor.result.IterationResult

preprocess(

inputs:str|List[int]|TextPrompt|TokensPrompt,

sampling_params:SamplingParams|None=None,

disaggregated_params:DisaggregatedParams|None=None,

)→PreprocessedInputs#

`prototype` Preprocess raw prompts into token IDs and multimodal params.

Parameters:

inputs (tensorrt_llm.inputs.data.PromptInputs) – The prompt text or token ids; it must be single prompt.

sampling_params (tensorrt_llm.sampling_params.SamplingParams, optional) – The sampling params for the generation. Defaults to None.
A default one will be used if not provided.

disaggregated_params (tensorrt_llm.disaggregated_params.DisaggregatedParams, optional) – Disaggregated parameters. Defaults to None.

Returns:

A preprocessed-inputs object that can be

passed directly to `generate_async()` as `inputs`.

Return type:

tensorrt_llm.llmapi.llm.PreprocessedInputs

shutdown()→None#

`beta` None

propertydisaggregated_params:dict#

`beta` None

propertyllm_id:str#

`beta` None

propertytokenizer:TokenizerBase|None#

classtensorrt_llm.llmapi.CompletionOutput(

index:int,

text:str='',

token_ids:~typing.List[int]|None=<factory>,

cumulative_logprob:float|None=None,

logprobs:list[dict[int,

~tensorrt_llm.executor.result.Logprob]]|~typing.List[float]|None=<factory>,

prompt_logprobs:list[dict[int,

~tensorrt_llm.executor.result.Logprob]]|None=<factory>,

finish_reason:~typing.Literal['stop',

'length',

'timeout',

'cancelled']|None=None,

stop_reason:int|str|None=None,

generation_logits:~torch.Tensor|None=None,

additional_context_outputs:~typing.Dict[str,

~torch.Tensor]|None=None,

additional_generation_outputs:~typing.Dict[str,

~torch.Tensor]|None=None,

disaggregated_params:~tensorrt_llm.disaggregated_params.DisaggregatedParams|None=None,

request_perf_metrics:~tensorrt_llm.bindings.executor.RequestPerfMetrics|None=None,

_postprocess_result:~typing.Any=None,

)[source]#

Bases: `object`

The output data of one completion output of a request.

Parameters:

index (int) – The index of the output in the request.

text (str) – The generated output text. Defaults to “”.

token_ids (List[int], optional) – The token ids of the generated output text. Defaults to [].

cumulative_logprob (float, optional) – The cumulative log probability of the generated output text. Defaults to None.

logprobs (TokenLogprobs | List[float], optional) – The log probabilities of the top probability words at each position if the logprobs are requested. Defaults to None.

prompt_logprobs (TokenLogprobs, optional) – The log probabilities per prompt token. Defaults to None.

finish_reason (Literal['stop', 'length', 'timeout', 'cancelled'], optional) – The reason why the sequence is finished. Defaults to None.

stop_reason (int, str, optional) – The stop string or token id that caused the completion to stop, None if the completion finished for some other reason. Defaults to None.

generation_logits (torch.Tensor, optional) – The logits on the generated output token ids. Defaults to None.

additional_context_outputs (Dict[str, torch.Tensor], optional) – The additional context outputs. Defaults to None.

additional_generation_outputs (Dict[str, torch.Tensor], optional) – The additional generation outputs. Defaults to None.

disaggregated_params (tensorrt_llm.disaggregated_params.DisaggregatedParams, optional) – Parameters needed for disaggregated serving. Includes the type of request, the first generated tokens, the context request id and the any additional state needing to be transferred from context and generation instances. Defaults to None.

request_perf_metrics (tensorrt_llm.bindings.executor.RequestPerfMetrics, optional) – Performance metrics for the request. Defaults to None.

length#

The number of generated tokens.

Type:

int

token_ids_diff#

Newly generated token ids.

Type:

List[int]

logprobs_diff#

Logprobs of newly generated tokens.

Type:

TokenLogprobs | List[float]

text_diff#

Newly generated tokens.

Type:

str

__init__(

index:int,

text:str='',

token_ids:~typing.List[int]|None=<factory>,

cumulative_logprob:float|None=None,

logprobs:list[dict[int,

~tensorrt_llm.executor.result.Logprob]]|~typing.List[float]|None=<factory>,

prompt_logprobs:list[dict[int,

~tensorrt_llm.executor.result.Logprob]]|None=<factory>,

finish_reason:~typing.Literal['stop',

'length',

'timeout',

'cancelled']|None=None,

stop_reason:int|str|None=None,

generation_logits:~torch.Tensor|None=None,

additional_context_outputs:~typing.Dict[str,

~torch.Tensor]|None=None,

additional_generation_outputs:~typing.Dict[str,

~torch.Tensor]|None=None,

disaggregated_params:~tensorrt_llm.disaggregated_params.DisaggregatedParams|None=None,

request_perf_metrics:~tensorrt_llm.bindings.executor.RequestPerfMetrics|None=None,

_postprocess_result:~typing.Any=None,

)→None#

additional_context_outputs:Dict[str,Tensor]|None#

additional_generation_outputs:Dict[str,Tensor]|None#

cumulative_logprob:float|None#

disaggregated_params:DisaggregatedParams|None#

finish_reason:Literal['stop','length','timeout','cancelled']|None#

generation_logits:Tensor|None#

index:int#

propertylength:int#

logprobs:list[dict[int,Logprob]]|List[float]|None#

propertylogprobs_diff:list[dict[int,Logprob]]|List[float]#

prompt_logprobs:list[dict[int,Logprob]]|None#

request_perf_metrics:RequestPerfMetrics|None#

stop_reason:int|str|None#

text:str#

propertytext_diff:str#

token_ids:List[int]|None#

propertytoken_ids_diff:List[int]#

classtensorrt_llm.llmapi.RequestOutput[source]#

Bases: `DetokenizedGenerationResultBase`, `GenerationResult`

The output data of a completion request to the LLM.

request_id#

The unique ID of the request.

Type:

int

prompt#

The prompt string of the request.

Type:

str, optional

prompt_token_ids#

The token ids of the prompt.

Type:

List[int]

outputs#

The output sequences of the request.

Type:

List[CompletionOutput]

context_logits#

The logits on the prompt token ids.

Type:

torch.Tensor, optional

disaggregated_params#

Parameters for disaggregated serving, including multimodal embedding handles.

Type:

DisaggregatedParams, optional

finished#

Whether the whole request is finished.

Type:

bool

classPostprocWorker(

pull_pipe_addr:tuple[str,bytes|None],

push_pipe_addr:tuple[str,bytes|None],

tokenizer_dir:str,

record_creator:Callable[[Input,TransformersTokenizer],Any],

Bases: `object`

The worker to postprocess the responses from the executor’s await_response.

classInput(

rsp:ForwardRef('tllm.Response')|ForwardRef('ResponseWrapper'),

sampling_params:tensorrt_llm.sampling_params.SamplingParams|None=None,

postproc_params:tensorrt_llm.executor.postproc_worker.PostprocParams|None=None,

streaming:bool|None=None,

Bases: `object`

__init__(

rsp:tllm.Response|ResponseWrapper,

sampling_params:SamplingParams|None=None,

postproc_params:PostprocParams|None=None,

streaming:bool|None=None,

)→None#

postproc_params:PostprocParams|None=None#

rsp:tllm.Response|ResponseWrapper#

sampling_params:SamplingParams|None=None#

streaming:bool|None=None#

classOutput(

client_id,

res,

is_final,

error,

metrics,

request_perf_metrics,

disaggregated_params,

Bases: `NamedTuple`

count(value, /)#

Return number of occurrences of value.

index(

value,

start=0,

stop=9223372036854775807,

Return first index of value.

Raises ValueError if the value is not present.

client_id:int#

Alias for field number 0

disaggregated_params:Any#

Alias for field number 6

error:str#

Alias for field number 3

is_final:bool#

Alias for field number 2

metrics:dict[str,float]|None#

Alias for field number 4

request_perf_metrics:Any#

Alias for field number 5

res:Any#

Alias for field number 1

__init__(

pull_pipe_addr:tuple[str,bytes|None],

push_pipe_addr:tuple[str,bytes|None],

tokenizer_dir:str,

record_creator:Callable[[Input,TransformersTokenizer],Any],

Parameters:

pull_pipe_addr (tuple[str, Optional[bytes]]) – The address and HMAC key of the input IPC.

push_pipe_addr (tuple[str, Optional[bytes]]) – The address and HMAC key of the output IPC.

tokenizer_dir (str) – The directory to load tokenizer.

record_creator (Callable[["ResponsePostprocessWorker.Input"], Any]) – A creator for creating a record for a request.

result_handler (Optional[Callable[[GenerationResultBase], Any]]) – A callback handles the final result.

staticdefault_record_creator(

inp:PostprocWorker.Input,

tokenizer:TransformersTokenizer,

)→DetokenizedGenerationResultBase#

start()#

Start the workflow in the current thread.

__init__()→None[source]#

abort()→None#

Abort the generation request.

aborted()→bool#

Return whether the generation request is aborted.

Returns:

whether the generation request is aborted.

Return type:

bool

asyncaresult()→GenerationResult#

Wait for the completion of the request, and return the result.

Returns:

generation result.

Return type:

tensorrt_llm.executor.result.GenerationResult

clear_logprob_params()→None#

do_tracing(

output:CompletionOutput,

req_perf_metrics_dict:dict[str,float]|None=None,

)→None#

Perform distributed tracing for the generation request.

Parameters:

output (CompletionOutput) – The output of the generation result.

req_perf_metrics_dict (Optional[dict[str, float]]) – Request performance metrics. Defaults to None.

record_stats(

output:CompletionOutput,

stats:dict[str,float]|None=None,

)→None#

Record the stats of the generation result.

Parameters:

output (CompletionOutput) – The output of the generation result.

stats (Optional[dict[str, float]]) – The stats of the generation result. Defaults to None.

result(

timeout:float|None=None,

)→GenerationResult#

Wait for the completion of the request, and return the result.

Parameters:

timeout (float, optional) – Timeout. Defaults to None.

Returns:

generation result.

Return type:

tensorrt_llm.executor.result.GenerationResult

propertycontext_logits:Tensor|None#

propertydisaggregated_params:DisaggregatedParams|None#

Returns the disaggregated params.

propertyfinished:bool#

propertyoutputs:List[CompletionOutput]#

propertyprompt:str|None#

propertyprompt_token_ids:List[int]#

propertyrequest_id:int#

classtensorrt_llm.llmapi.GuidedDecodingParams(

json:str|BaseModel|dict|None=None,

regex:str|None=None,

grammar:str|None=None,

json_object:bool=False,

structural_tag:str|None=None,

)[source]#

Bases: `object`

Guided decoding parameters for text generation. Only one of the fields could be effective.

Parameters:

json (str, pydantic.main.BaseModel, dict, optional) – The generated text is amenable to json format with additional user-specified restrictions, namely schema. Defaults to None.

regex (str, optional) – The generated text is amenable to the user-specified regular expression. Defaults to None.

grammar (str, optional) – The generated text is amenable to the user-specified extended Backus-Naur form (EBNF) grammar. Defaults to None.

json_object (bool) – If True, the generated text is amenable to json format. Defaults to False.

structural_tag (str, optional) – The generated text is amenable to the user-specified structural tag. Structural tag is supported by xgrammar backend only. Defaults to None.

__init__(

json:str|BaseModel|dict|None=None,

regex:str|None=None,

grammar:str|None=None,

json_object:bool=False,

structural_tag:str|None=None,

)→None#

grammar:str|None#

json:str|BaseModel|dict|None#

json_object:bool#

regex:str|None#

structural_tag:str|None#

classtensorrt_llm.llmapi.SamplingParams(

end_id:int|None=None,

pad_id:int|None=None,

max_tokens:int=32,

bad:str|List[str]|None=None,

bad_token_ids:List[int]|None=None,

stop:str|List[str]|None=None,

stop_token_ids:List[int]|None=None,

include_stop_str_in_output:bool=False,

embedding_bias:Tensor|None=None,

logits_processor:LogitsProcessor|List[LogitsProcessor]|None=None,

apply_batched_logits_processor:bool=False,

n:int=1,

best_of:int|None=None,

use_beam_search:bool=False,

logprobs_mode:LogprobMode=LogprobMode.RAW,

top_k:int|None=None,

top_p:float|None=None,

top_p_min:float|None=None,

top_p_reset_ids:int|None=None,

top_p_decay:float|None=None,

seed:int|None=None,

temperature:float|None=None,

min_tokens:int|None=None,

beam_search_diversity_rate:float|None=None,

repetition_penalty:float|None=None,

presence_penalty:float|None=None,

frequency_penalty:float|None=None,

prompt_ignore_length:int|None=None,

length_penalty:float|None=None,

early_stopping:int|None=None,

no_repeat_ngram_size:int|None=None,

min_p:float|None=None,

beam_width_array:List[int]|None=None,

logprobs:int|None=None,

prompt_logprobs:int|None=None,

return_context_logits:bool=False,

return_generation_logits:bool=False,

exclude_input_from_output:bool=True,

return_encoder_output:bool=False,

return_perf_metrics:bool=False,

additional_model_outputs:List[str]|None=None,

_context_logits_auto_enabled:bool=False,

_generation_logits_auto_enabled:bool=False,

_return_log_probs:bool=False,

lookahead_config:LookaheadDecodingConfig|None=None,

guided_decoding:GuidedDecodingParams|None=None,

ignore_eos:bool=False,

detokenize:bool=True,

add_special_tokens:bool=True,

truncate_prompt_tokens:int|None=None,

skip_special_tokens:bool=True,

spaces_between_special_tokens:bool=True,

)[source]#

Bases: `object`

Sampling parameters for text generation.

Usage Examples:

use_beam_search is False:

best_of is None: (top-p/top-k) sampling n responses and return n generations

best_of is not None: (top-p/top-k) sampling best_of responses and return n generations (best_of >= n must hold)

use_beam_search is True:

best_of is None: beam search with beam width of n, return n generations

best_of is not None: beam search with beam width of best_of, return n generations (best_of >= n must hold)

Parameters:

end_id (int, optional) – The end token id. Defaults to None.

pad_id (int, optional) – The pad token id. Defaults to None.

max_tokens (int) – The maximum number of tokens to generate. Defaults to 32.

bad (str, List[str], optional) – A string or a list of strings that redirect the generation when they are generated, so that the bad strings are excluded from the returned output. Defaults to None.

bad_token_ids (List[int], optional) – A list of token ids that redirect the generation when they are generated, so that the bad ids are excluded from the returned output. Defaults to None.

stop (str, List[str], optional) – A string or a list of strings that stop the generation when they are generated. The returned output will not contain the stop strings unless include_stop_str_in_output is True. Defaults to None.

stop_token_ids (List[int], optional) – A list of token ids that stop the generation when they are generated. Defaults to None.

include_stop_str_in_output (bool) – Whether to include the stop strings in output text. Defaults to False.

embedding_bias (torch.Tensor, optional) – The embedding bias tensor. Expected type is kFP32 and shape is [vocab_size]. Defaults to None.

logits_processor (tensorrt_llm.sampling_params.LogitsProcessor, List[tensorrt_llm.sampling_params.LogitsProcessor], optional) – The logits postprocessor callback(s). Defaults to None.
If a list, each processor is applied in order during generation (supported in PyTorch backend only).

apply_batched_logits_processor (bool) – Whether to apply batched logits postprocessor callback. Defaults to False.
The BatchedLogitsProcessor class is recommended for callback creation. The callback must be provided when initializing LLM.

n (int) – Number of sequences to generate. Defaults to 1.

best_of (int, optional) – Number of sequences to consider for best output. Defaults to None.

use_beam_search (bool) – Whether to use beam search. Defaults to False.

top_k (int, optional) – Controls number of logits to sample from. Can assume non-negative values, where 0 means ‘all logits’. Defaults to None.
The value None is treated as “not specified” in the following.
If neither temperature, top_p, nor top_k are specified, sampling is greedy.
If temperature > 0 and/or top_p < 1 are specified, sampling will proceed accordingly and top_k will default to top_k = 0.
Setting top_k = 1 results in greedy sampling.

top_p (float, optional) – Controls the top-P probability to sample from. Can have values between 0 and 1. Defaults to None.
The value None is treated as “not specified” in the following.
If neither temperature, top_p, nor top_k are specified, sampling is greedy.
If temperature > 0 and/or top_k > 1 are specified, sampling will proceed accordingly and top_p will default to top_p = 1.
Setting top_p = 0 should result in greedy sampling, but is currently disallowed in the backend.

top_p_min (float, optional) – Controls decay in the top-P algorithm. topPMin is lower-bound. None means using C++ runtime default 1.e-6. Defaults to None.

top_p_reset_ids (int, optional) – Controls decay in the top-P algorithm. Indicates where to reset the decay. None means using C++ runtime default 1. Defaults to None.

top_p_decay (float, optional) – Controls decay in the top-P algorithm. The decay value. None means using C++ runtime default 1.f. Defaults to None.

seed (int, optional) – Controls the random seed used by the random number generator in sampling. None means using C++ runtime default 0. Defaults to None.

temperature (float, optional) – Controls the modulation of logits when sampling new tokens. It can have values >= 0.f. Defaults to None.
The value None is treated as “not specified” in the following.
If neither temperature, top_p, nor top_k are specified, sampling is greedy.
If top_p < 1 and/or top_k > 1 are specified, sampling will proceed accordingly and temperature will default to temperature = 1.
Setting temperature = 0 results in greedy sampling.

min_tokens (int, optional) – Lower bound on the number of tokens to generate. Values < 1 have no effect. None means using C++ runtime default 1. Defaults to None.

beam_search_diversity_rate (float, optional) – Used to penalize tokens based on how often they appear in the sequence. It can have any value > 0.f. Values < 1.f encourages repetition, values > 1.f discourages it. None means using C++ runtime default 1.f. Defaults to None.

repetition_penalty (float, optional) – Used to penalize tokens based on how often they appear in the sequence. It can have any value > 0.f. Values < 1.f encourages repetition, values > 1.f discourages it. None means using C++ runtime default 1.f. Defaults to None.

presence_penalty (float, optional) – Used to penalize tokens already present in the sequence (irrespective of the number of appearances). It can have any values. Values < 0.f encourage repetition, values > 0.f discourage it. None means using C++ runtime default 0.f. Defaults to None.

frequency_penalty (float, optional) – Used to penalize tokens already present in the sequence (dependent on the number of appearances). It can have any values. Values < 0.f encourage repetition, values > 0.f discourage it. None means using C++ runtime default 0.f. Defaults to None.

prompt_ignore_length (int, optional) – Controls how many tokens to ignore from the prompt for presence and frequency penalties. Values <= 0 have no effect. Values > input (prompt) length will be clamped. None means using C++ runtime default 0. Defaults to None.

length_penalty (float, optional) – Controls how to penalize longer sequences in beam search. None means using C++ runtime default 0.f. Defaults to None.

early_stopping (int, optional) – Controls whether the generation process finishes once beamWidth sentences are generated (ends with end_token). None means using C++ runtime default 1. Defaults to None.

no_repeat_ngram_size (int, optional) – Controls how many repeat ngram size are acceptable. None means using C++ runtime default 1 << 30. Defaults to None.

min_p (float, optional) – scale the most likely token to determine the minimum token probability. None means using C++ runtime default 0.0. Defaults to None.

beam_width_array (List[int], optional) – The array of beam width using in Variable-Beam-Width-Search. Defaults to None.

logprobs (int, optional) – Number of log probabilities to return per output token. When set to 0, return only the sampled token’s log probability.
When set to K>0, return top-K log probabilities + the sampled token’s log probability (last entry) if it’s not in the Top-K. Defaults to None.

logprobs_mode (LogprobMode) – The mode of log probabilities to return. Defaults to LogprobMode.RAW.

prompt_logprobs (int, optional) – Number of log probabilities to return per prompt token. When set to 0, return only the actual prompt token’s log probability.
When set to K>0, return top-K log probabilities + the actual prompt token’s log probability (last entry) if it’s not in the Top-K. Defaults to None.

return_context_logits (bool) – Controls if Result should contain the context logits. Defaults to False.

return_generation_logits (bool) – Controls if Result should contain the generation logits. Defaults to False.

exclude_input_from_output (bool) – Controls if output tokens in Result should include the input tokens. Defaults to True.

return_encoder_output (bool) – Controls if Result should contain encoder output hidden states (for encoder-only and encoder-decoder models). Defaults to False.

return_perf_metrics (bool) – Controls if Result should contain the performance metrics for this request. Defaults to False.

additional_model_outputs (List[str], optional) – The additional outputs to gather from the model. Defaults to None.

lookahead_config (tensorrt_llm.bindings.executor.LookaheadDecodingConfig , optional) – Lookahead decoding config. Defaults to None.

guided_decoding (tensorrt_llm.sampling_params.GuidedDecodingParams, optional) – Guided decoding params. Defaults to None.

ignore_eos (bool) – Whether to ignore the EOS token and continue generating tokens after the EOS token is generated. Defaults to False.

detokenize (bool) – Whether to detokenize the output. Defaults to True.

add_special_tokens (bool) – Whether to add special tokens to the prompt. Defaults to True.

truncate_prompt_tokens (int, optional) – If set to an integer k, will use only the last k tokens from the prompt (i.e., left truncation). Defaults to None.

skip_special_tokens (bool) – Whether to skip special tokens in the output. Defaults to True.

spaces_between_special_tokens (bool) – Whether to add spaces between special tokens in the output. Defaults to True.

__init__(

end_id:int|None=None,

pad_id:int|None=None,

max_tokens:int=32,

bad:str|List[str]|None=None,

bad_token_ids:List[int]|None=None,

stop:str|List[str]|None=None,

stop_token_ids:List[int]|None=None,

include_stop_str_in_output:bool=False,

embedding_bias:Tensor|None=None,

logits_processor:LogitsProcessor|List[LogitsProcessor]|None=None,

apply_batched_logits_processor:bool=False,

n:int=1,

best_of:int|None=None,

use_beam_search:bool=False,

logprobs_mode:LogprobMode=LogprobMode.RAW,

top_k:int|None=None,

top_p:float|None=None,

top_p_min:float|None=None,

top_p_reset_ids:int|None=None,

top_p_decay:float|None=None,

seed:int|None=None,

temperature:float|None=None,

min_tokens:int|None=None,

beam_search_diversity_rate:float|None=None,

repetition_penalty:float|None=None,

presence_penalty:float|None=None,

frequency_penalty:float|None=None,

prompt_ignore_length:int|None=None,

length_penalty:float|None=None,

early_stopping:int|None=None,

no_repeat_ngram_size:int|None=None,

min_p:float|None=None,

beam_width_array:List[int]|None=None,

logprobs:int|None=None,

prompt_logprobs:int|None=None,

return_context_logits:bool=False,

return_generation_logits:bool=False,

exclude_input_from_output:bool=True,

return_encoder_output:bool=False,

return_perf_metrics:bool=False,

additional_model_outputs:List[str]|None=None,

_context_logits_auto_enabled:bool=False,

_generation_logits_auto_enabled:bool=False,

_return_log_probs:bool=False,

lookahead_config:LookaheadDecodingConfig|None=None,

guided_decoding:GuidedDecodingParams|None=None,

ignore_eos:bool=False,

detokenize:bool=True,

add_special_tokens:bool=True,

truncate_prompt_tokens:int|None=None,

skip_special_tokens:bool=True,

spaces_between_special_tokens:bool=True,

)→None#

staticparams_imply_greedy_decoding(

temperature:float|None,

top_p:float|None,

top_k:int|None,

use_beam_search:bool|None,

)[source]#

add_special_tokens:bool#

additional_model_outputs:List[str]|None#

apply_batched_logits_processor:bool#

bad:str|List[str]|None#

bad_token_ids:List[int]|None#

beam_width_array:List[int]|None#

best_of:int|None#

detokenize:bool#

early_stopping:int|None#

embedding_bias:Tensor|None#

end_id:int|None#

exclude_input_from_output:bool#

frequency_penalty:float|None#

guided_decoding:GuidedDecodingParams|None#

ignore_eos:bool#

include_stop_str_in_output:bool#

length_penalty:float|None#

logits_processor:LogitsProcessor|List[LogitsProcessor]|None#

logprobs:int|None#

logprobs_mode:LogprobMode#

lookahead_config:LookaheadDecodingConfig|None#

max_tokens:int#

min_p:float|None#

min_tokens:int|None#

n:int#

no_repeat_ngram_size:int|None#

pad_id:int|None#

presence_penalty:float|None#

prompt_ignore_length:int|None#

prompt_logprobs:int|None#

repetition_penalty:float|None#

return_context_logits:bool#

return_encoder_output:bool#

return_generation_logits:bool#

return_perf_metrics:bool#

seed:int|None#

skip_special_tokens:bool#

spaces_between_special_tokens:bool#

stop:str|List[str]|None#

stop_token_ids:List[int]|None#

temperature:float|None#

top_k:int|None#

top_p:float|None#

top_p_decay:float|None#

top_p_min:float|None#

top_p_reset_ids:int|None#

truncate_prompt_tokens:int|None#

classtensorrt_llm.llmapi.DisaggregatedParams(

request_type:str|None=None,

first_gen_tokens:List[int]|None=None,

first_gen_log_probs:List|None=None,

first_gen_logits:List|None=None,

ctx_request_id:int|None=None,

opaque_state:bytes|None=None,

draft_tokens:List[int]|None=None,

disagg_request_id:int|None=None,

ctx_dp_rank:int|None=None,

ctx_info_endpoint:List[str]|None=None,

schedule_style:DisaggScheduleStyle|None=None,

multimodal_embedding_handles:List[Dict[str,Any]]|None=None,

multimodal_hashes:List[List[int]]|None=None,

mrope_position_ids_handle:Dict[str,Any]|None=None,

mrope_position_deltas_handle:Dict[str,Any]|None=None,

)[source]#

Bases: `object`

Disaggregated serving parameters.

Parameters:

request_type (str) – The type of request (“context_only” | “generation_only” | “context_and_generation”)

first_gen_tokens (List[int]) – The first tokens of the generation request

ctx_request_id (int) – The context request id

opaque_state (bytes) – Any additional state needing to be exchanged between context and gen instances

draft_tokens (List[int]) – The draft tokens of the generation request

disagg_request_id (int) – The disaggregated request id, if set, both context and generation requests will use it
as underlying request id.

first_gen_log_probs (List) – The logprobs for first_gen_tokens, produced during prefill.
Each entry is a list (one per beam) of TokenLogprobs (list of dict[int, Logprob]).

first_gen_logits (List) – The generation logits for first_gen_tokens, produced during prefill.
Each entry is a torch.Tensor of shape [num_tokens, vocab_size] (one per beam/sequence).

multimodal_embedding_handles (List[Dict[str, Any]]) – The resulting multimodal embedding handles from ViT.

multimodal_hashes (List[List[int]]) – The multimodal hashes of each multimodal item in the request.

__init__(

request_type:str|None=None,

first_gen_tokens:List[int]|None=None,

first_gen_log_probs:List|None=None,

first_gen_logits:List|None=None,

ctx_request_id:int|None=None,

opaque_state:bytes|None=None,

draft_tokens:List[int]|None=None,

disagg_request_id:int|None=None,

ctx_dp_rank:int|None=None,

ctx_info_endpoint:List[str]|None=None,

schedule_style:DisaggScheduleStyle|None=None,

multimodal_embedding_handles:List[Dict[str,Any]]|None=None,

multimodal_hashes:List[List[int]]|None=None,

mrope_position_ids_handle:Dict[str,Any]|None=None,

mrope_position_deltas_handle:Dict[str,Any]|None=None,

)→None#

get_context_phase_params()→ContextPhaseParams[source]#

get_request_type()→RequestType[source]#

ctx_dp_rank:int|None#

ctx_info_endpoint:List[str]|None#

ctx_request_id:int|None#

disagg_request_id:int|None#

draft_tokens:List[int]|None#

first_gen_log_probs:List|None#

first_gen_logits:List|None#

first_gen_tokens:List[int]|None#

mrope_position_deltas_handle:Dict[str,Any]|None#

mrope_position_ids_handle:Dict[str,Any]|None#

multimodal_embedding_handles:List[Dict[str,Any]]|None#

multimodal_hashes:List[List[int]]|None#

opaque_state:bytes|None#

request_type:str|None#

schedule_style:DisaggScheduleStyle|None#

classtensorrt_llm.llmapi.DisaggScheduleStyle(

value,

names=<notgiven>,

*values,

module=None,

qualname=None,

type=None,

start=1,

boundary=None,

)[source]#

Bases: `IntEnum`

__init__(*args, **kwds)#

as_integer_ratio()#

Return a pair of integers, whose ratio is equal to the original int.

The ratio is in lowest terms and has a positive denominator.

```text
>>> (10).as_integer_ratio()
(10, 1)
>>> (-10).as_integer_ratio()
(-10, 1)
>>> (0).as_integer_ratio()
(0, 1)
```

bit_count()#

Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

```text
>>> bin(13)
'0b1101'
>>> (13).bit_count()
3
```

bit_length()#

Number of bits necessary to represent self in binary.

```text
>>> bin(37)
'0b100101'
>>> (37).bit_length()
6
```

conjugate()#

Returns self, the complex conjugate of any int.

from_bytes(byteorder='big', *, signed=False)#

Return the integer represented by the given array of bytes.

bytes

Holds the array of bytes to convert. The argument must either
support the buffer protocol or be an iterable object producing bytes.
Bytes and bytearray are examples of built-in objects that support the
buffer protocol.

byteorder

The byte order used to represent the integer. If byteorder is ‘big’,
the most significant byte is at the beginning of the byte array. If
byteorder is ‘little’, the most significant byte is at the end of the
byte array. To request the native byte order of the host system, use
`sys.byteorder’ as the byte order value. Default is to use ‘big’.

signed

Indicates whether two’s complement is used to represent the integer.

is_integer()#

Returns True. Exists for duck type compatibility with float.is_integer.

to_bytes(

length=1,

byteorder='big',

signed=False,

Return an array of bytes representing an integer.

length

Length of bytes object to use. An OverflowError is raised if the
integer is not representable with the given number of bytes. Default
is length 1.

byteorder

The byte order used to represent the integer. If byteorder is ‘big’,
the most significant byte is at the beginning of the byte array. If
byteorder is ‘little’, the most significant byte is at the end of the
byte array. To request the native byte order of the host system, use
`sys.byteorder’ as the byte order value. Default is to use ‘big’.

signed

Determines whether two’s complement is used to represent the integer.
If signed is False and a negative integer is given, an OverflowError
is raised.

CONTEXT_FIRST=0#

GENERATION_FIRST=1#

denominator#

the denominator of a rational number in lowest terms

imag#

the imaginary part of a complex number

numerator#

the numerator of a rational number in lowest terms

real#

the real part of a complex number

classtensorrt_llm.llmapi.KvCacheConfig(

enable_block_reuse:bool=True,

max_tokens:int|None=None,

max_attention_window:Annotated[List[Annotated[int,Gt(gt=0)]]|None,MinLen(min_length=1)]=None,

sink_token_length:int|None=None,

free_gpu_memory_fraction:Annotated[float|None,Ge(ge=0),Le(le=1)]=0.9,

host_cache_size:int|None=None,

onboard_blocks:bool=True,

cross_kv_cache_fraction:float|None=None,

secondary_offload_min_priority:int|None=None,

event_buffer_max_size:int=0,

attention_dp_events_gather_period_ms:int=5,

enable_partial_reuse:bool=True,

copy_on_partial_reuse:bool=True,

use_uvm:bool=False,

max_gpu_total_bytes:Annotated[int,Ge(ge=0)]=0,

dtype:str='auto',

mamba_ssm_cache_dtype:Literal['auto','float16','bfloat16','float32']='auto',

tokens_per_block:int=32,

use_kv_cache_manager_v2:bool=False,

max_util_for_resume:Annotated[float,Ge(ge=0),Le(le=1)]=0.95,

)[source]#

Bases: `StrictBaseModel`, `PybindMirror`

Configuration for the KV cache.

fieldattention_dp_events_gather_period_ms:int=5#

The period in milliseconds to gather attention DP events across ranks.

fieldcopy_on_partial_reuse:bool=True#

Whether partially matched blocks that are in use can be reused after copying them.

fieldcross_kv_cache_fraction:float|None=None#

The fraction of the KV Cache memory should be reserved for cross attention. If set to p, self attention will use 1-p of KV Cache memory and cross attention will use p of KV Cache memory. Default is 50%. Should only be set when using encoder-decoder model.

fielddtype:str='auto'#

The data type to use for the KV cache. Use ‘auto’ to follow checkpoint metadata, otherwise force the specified dtype.

fieldenable_block_reuse:bool=True#

Controls if KV cache blocks can be reused for different requests.

fieldenable_partial_reuse:bool=True#

Whether blocks that are only partially matched can be reused.

fieldevent_buffer_max_size:int=0#

Maximum size of the event buffer. If set to 0, the event buffer will not be used.

fieldfree_gpu_memory_fraction:float|None=0.9#

The fraction of GPU memory fraction that should be allocated for the KV cache. Default is 90%. If both max_tokens and free_gpu_memory_fraction are specified, memory corresponding to the minimum will be used.

Constraints:

ge = 0

le = 1

fieldhost_cache_size:int|None=None#

Size of the host cache in bytes. If both max_tokens and host_cache_size are specified, memory corresponding to the minimum will be used.

fieldmamba_ssm_cache_dtype:Literal['auto','float16','bfloat16','float32']='auto'#

The data type to use for the Mamba SSM cache. If set to ‘auto’, the data type will be inferred from the model config.

fieldmax_attention_window:List[Annotated[int,Gt(gt=0)]]|None=None#

Size of the attention window for each sequence. Only the last tokens will be stored in the KV cache. If the number of elements in max_attention_window is less than the number of layers, max_attention_window will be repeated multiple times to the number of layers.

Constraints:

min_length = 1

fieldmax_gpu_total_bytes:Annotated[int,Ge(ge=0)]=0#

The maximum size in bytes of GPU memory that can be allocated for the KV cache. If both max_gpu_total_bytes and free_gpu_memory_fraction are specified, memory corresponding to the minimum will be allocated.

Constraints:

ge = 0

fieldmax_tokens:int|None=None#

The maximum number of tokens that should be stored in the KV cache. If both max_tokens and free_gpu_memory_fraction are specified, memory corresponding to the minimum will be used.

fieldmax_util_for_resume:float=0.95#

The maximum utilization of the KV cache for resume. Default is 95%. Only used when using KV cache manager v2 (experimental).

Constraints:

ge = 0

le = 1

fieldonboard_blocks:bool=True#

Controls if blocks are onboarded.

fieldsecondary_offload_min_priority:int|None=None#

Only blocks with priority > secondary_offload_min_priority can be offloaded to secondary memory.

fieldsink_token_length:int|None=None#

Number of sink tokens (tokens to always keep in attention window).

fieldtokens_per_block:int=32#

The number of tokens per block.

fielduse_kv_cache_manager_v2:bool=False#

Whether to use the KV cache manager v2 (experimental).

fielduse_uvm:bool=False#

Whether to use UVM for the KV cache.

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(obj:Any)→Self#

classmethodfrom_pybind(

pybind_instance:PybindMirror,

)→T#

Construct an instance of the given class from the fields in the given
pybind class instance.

Parameters:

cls – Type of the class to construct, must be a subclass of pydantic
BaseModel

pybind_instance – Instance of the pybind class to construct from its
fields

Notes

When a field value is None in the pybind class, but it’s not
optional and has a default value in the BaseModel class, it would
get the default value defined in the BaseModel class.

Returns:

Instance of the given class, populated with the fields of the given
pybind instance

staticget_pybind_enum_fields(pybind_class)#

Get all the enum fields from the pybind class.

staticget_pybind_variable_fields(config_cls)#

Get all the variable fields from the pybind class.

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

staticmaybe_to_pybind(ins)#

staticmirror_pybind_enum(pybind_class)#

Mirror the enum fields from the pybind class to the Python class.

staticmirror_pybind_fields(pybind_class)#

Class decorator that ensures Python class fields mirror those of a C++ class.

Parameters:

pybind_class – The C++ class whose fields should be mirrored

Returns:

A decorator function that validates field mirroring

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(context:Any, /)→None#

Override this method to perform additional initialization after __init__ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(obj:Any)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

staticpybind_equals(obj0, obj1)#

Check if two pybind objects are equal.

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

classmethodupdate_forward_refs(**localns:Any)→None#

classmethodvalidate(value:Any)→Self#

validatorvalidate_dtype»dtype[source]#

validatorvalidate_free_gpu_memory_fraction»free_gpu_memory_fraction[source]#

Validates that the fraction is between 0.0 and 1.0.

validatorvalidate_max_attention_window»max_attention_window[source]#

validatorvalidate_max_gpu_total_bytes»max_gpu_total_bytes[source]#

validatorvalidate_max_util_for_resume»max_util_for_resume[source]#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'attention_dp_events_gather_period_ms':FieldInfo(annotation=int,required=False,default=5,description='TheperiodinmillisecondstogatherattentionDPeventsacrossranks.'),'copy_on_partial_reuse':FieldInfo(annotation=bool,required=False,default=True,description='Whetherpartiallymatchedblocksthatareinusecanbereusedaftercopyingthem.'),'cross_kv_cache_fraction':FieldInfo(annotation=Union[float,NoneType],required=False,default=None,description='ThefractionoftheKVCachememoryshouldbereservedforcrossattention.Ifsettop,selfattentionwilluse1-pofKVCachememoryandcrossattentionwillusepofKVCachememory.Defaultis50%.Shouldonlybesetwhenusingencoder-decodermodel.'),'dtype':FieldInfo(annotation=str,required=False,default='auto',description="ThedatatypetousefortheKVcache.Use'auto'tofollowcheckpointmetadata,otherwiseforcethespecifieddtype."),'enable_block_reuse':FieldInfo(annotation=bool,required=False,default=True,description='ControlsifKVcacheblockscanbereusedfordifferentrequests.'),'enable_partial_reuse':FieldInfo(annotation=bool,required=False,default=True,description='Whetherblocksthatareonlypartiallymatchedcanbereused.'),'event_buffer_max_size':FieldInfo(annotation=int,required=False,default=0,description='Maximumsizeoftheeventbuffer.Ifsetto0,theeventbufferwillnotbeused.'),'free_gpu_memory_fraction':FieldInfo(annotation=Union[float,NoneType],required=False,default=0.9,description='ThefractionofGPUmemoryfractionthatshouldbeallocatedfortheKVcache.Defaultis90%.Ifboth`max_tokens`and`free_gpu_memory_fraction`arespecified,memorycorrespondingtotheminimumwillbeused.',metadata=[Ge(ge=0),Le(le=1)]),'host_cache_size':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description='Sizeofthehostcacheinbytes.Ifboth`max_tokens`and`host_cache_size`arespecified,memorycorrespondingtotheminimumwillbeused.'),'mamba_ssm_cache_dtype':FieldInfo(annotation=Literal['auto','float16','bfloat16','float32'],required=False,default='auto',description="ThedatatypetousefortheMambaSSMcache.Ifsetto'auto',thedatatypewillbeinferredfromthemodelconfig."),'max_attention_window':FieldInfo(annotation=Union[List[Annotated[int,Gt]],NoneType],required=False,default=None,description='Sizeoftheattentionwindowforeachsequence.OnlythelasttokenswillbestoredintheKVcache.Ifthenumberofelementsin`max_attention_window`islessthanthenumberoflayers,`max_attention_window`willberepeatedmultipletimestothenumberoflayers.',metadata=[MinLen(min_length=1)]),'max_gpu_total_bytes':FieldInfo(annotation=int,required=False,default=0,description='ThemaximumsizeinbytesofGPUmemorythatcanbeallocatedfortheKVcache.Ifboth`max_gpu_total_bytes`and`free_gpu_memory_fraction`arespecified,memorycorrespondingtotheminimumwillbeallocated.',metadata=[Ge(ge=0)]),'max_tokens':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description='ThemaximumnumberoftokensthatshouldbestoredintheKVcache.Ifboth`max_tokens`and`free_gpu_memory_fraction`arespecified,memorycorrespondingtotheminimumwillbeused.'),'max_util_for_resume':FieldInfo(annotation=float,required=False,default=0.95,description='ThemaximumutilizationoftheKVcacheforresume.Defaultis95%.OnlyusedwhenusingKVcachemanagerv2(experimental).',json_schema_extra={'status':'prototype'},metadata=[Ge(ge=0),Le(le=1)]),'onboard_blocks':FieldInfo(annotation=bool,required=False,default=True,description='Controlsifblocksareonboarded.'),'secondary_offload_min_priority':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description='Onlyblockswithpriority>secondary_offload_min_prioritycanbeoffloadedtosecondarymemory.'),'sink_token_length':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description='Numberofsinktokens(tokenstoalwayskeepinattentionwindow).'),'tokens_per_block':FieldInfo(annotation=int,required=False,default=32,description='Thenumberoftokensperblock.'),'use_kv_cache_manager_v2':FieldInfo(annotation=bool,required=False,default=False,description='WhethertousetheKVcachemanagerv2(experimental).',json_schema_extra={'status':'prototype'}),'use_uvm':FieldInfo(annotation=bool,required=False,default=False,description='WhethertouseUVMfortheKVcache.')}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

classtensorrt_llm.llmapi.KvCacheRetentionConfig(*args, **kwargs)#

Bases: `object`

classTokenRangeRetentionConfig(*args, **kwargs)#

Bases: `object`

__init__#

propertyduration_ms#

(self) -> datetime.timedelta | None

propertypriority#

(self) -> int

propertytoken_end#

(self) -> int | None

propertytoken_start#

(self) -> int

__init__#

propertydecode_duration_ms#

(self) -> datetime.timedelta | None

propertydecode_retention_priority#

(self) -> int

propertydirectory#

(self) -> str

propertytoken_range_retention_configs#

(self) -> list[tensorrt_llm.bindings.executor.KvCacheRetentionConfig.TokenRangeRetentionConfig]

propertytransfer_mode#

(self) -> tensorrt_llm.bindings.executor.KvCacheTransferMode

classtensorrt_llm.llmapi.CudaGraphConfig(

batch_sizes:List[int]|None=None,

max_batch_size:Annotated[int,Ge(ge=0)]=0,

enable_padding:bool=False,

)[source]#

Bases: `StrictBaseModel`

Configuration for CUDA graphs.

fieldbatch_sizes:List[int]|None=None#

List of batch sizes to create CUDA graphs for.

fieldenable_padding:bool=False#

If true, batches are rounded up to the nearest cuda_graph_batch_size. This is usually a net win for performance.

fieldmax_batch_size:Annotated[int,Ge(ge=0)]=0#

Maximum batch size for CUDA graphs.

Constraints:

ge = 0

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(obj:Any)→Self#

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(context:Any, /)→None#

Override this method to perform additional initialization after __init__ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(obj:Any)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

classmethodupdate_forward_refs(**localns:Any)→None#

classmethodvalidate(value:Any)→Self#

validatorvalidate_cuda_graph_config»allfields[source]#

Validate CUDA graph configuration.

Ensures that:
1. If batch_sizes is provided, max_batch_size is derived as max(batch_sizes).

If max_batch_size was already set it must be compatible (equal to max(batch_sizes));
otherwise an error is raised.

If only max_batch_size is provided, batch_sizes is generated from it.

If neither is provided, a default max_batch_size of 128 is used.

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'batch_sizes':FieldInfo(annotation=Union[List[int],NoneType],required=False,default=None,description='ListofbatchsizestocreateCUDAgraphsfor.'),'enable_padding':FieldInfo(annotation=bool,required=False,default=False,description='Iftrue,batchesareroundeduptothenearestcuda_graph_batch_size.Thisisusuallyanetwinforperformance.'),'max_batch_size':FieldInfo(annotation=int,required=False,default=0,description='MaximumbatchsizeforCUDAgraphs.',metadata=[Ge(ge=0)])}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

classtensorrt_llm.llmapi.MoeConfig(

backend:Literal['AUTO','CUTLASS','CUTEDSL','WIDEEP','TRTLLM','DEEPGEMM','VANILLA','TRITON']='AUTO',

max_num_tokens:int|None=None,

load_balancer:object|str|None=None,

disable_finalize_fusion:bool=False,

use_low_precision_moe_combine:bool=False,

)[source]#

Bases: `StrictBaseModel`

Configuration for MoE.

fieldbackend:Literal['AUTO','CUTLASS','CUTEDSL','WIDEEP','TRTLLM','DEEPGEMM','VANILLA','TRITON']='AUTO'#

MoE backend to use. AUTO selects default backend based on model. It currently doesn’t always give the best choice for all scenarios. The capabilities of auto selection will be improved in future releases.

fielddisable_finalize_fusion:bool=False#

Disable FC2+finalize kernel fusion in CUTLASS MoE backend. Setting this to True recovers deterministic numerical behavior with top-k > 2.

fieldload_balancer:object|str|None=None#

Configuration for MoE load balancing.

fieldmax_num_tokens:int|None=None#

If set, at most max_num_tokens tokens will be sent to torch.ops.trtllm.fused_moe at the same time. If the number of tokens exceeds max_num_tokens, the input tensors will be split into chunks and a for loop will be used.

fielduse_low_precision_moe_combine:bool=False#

Use low precision combine in MoE operations (only for NVFP4 quantization). When enabled, uses lower precision for combining expert outputs to improve performance.

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(obj:Any)→Self#

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(context:Any, /)→None#

Override this method to perform additional initialization after __init__ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(obj:Any)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

classmethodupdate_forward_refs(**localns:Any)→None#

classmethodvalidate(value:Any)→Self#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'backend':FieldInfo(annotation=Literal['AUTO','CUTLASS','CUTEDSL','WIDEEP','TRTLLM','DEEPGEMM','VANILLA','TRITON'],required=False,default='AUTO',description="MoEbackendtouse.AUTOselectsdefaultbackendbasedonmodel.Itcurrentlydoesn'talwaysgivethebestchoiceforallscenarios.Thecapabilitiesofautoselectionwillbeimprovedinfuturereleases."),'disable_finalize_fusion':FieldInfo(annotation=bool,required=False,default=False,description='DisableFC2+finalizekernelfusioninCUTLASSMoEbackend.SettingthistoTruerecoversdeterministicnumericalbehaviorwithtop-k>2.'),'load_balancer':FieldInfo(annotation=Union[object,str,NoneType],required=False,default=None,description='ConfigurationforMoEloadbalancing.',json_schema_extra={'type':'Union[MoeLoadBalancerConfig,dict,str]'}),'max_num_tokens':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description='Ifset,atmostmax_num_tokenstokenswillbesenttotorch.ops.trtllm.fused_moeatthesametime.Ifthenumberoftokensexceedsmax_num_tokens,theinputtensorswillbesplitintochunksandaforloopwillbeused.'),'use_low_precision_moe_combine':FieldInfo(annotation=bool,required=False,default=False,description='UselowprecisioncombineinMoEoperations(onlyforNVFP4quantization).Whenenabled,useslowerprecisionforcombiningexpertoutputstoimproveperformance.')}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

classtensorrt_llm.llmapi.LookaheadDecodingConfig(

max_draft_len:Annotated[int,Ge(ge=0)]|None=None,

max_total_draft_tokens:int|None=None,

speculative_model:str|Path|None=None,

max_concurrency:Annotated[int,Ge(ge=0)]|None=None,

draft_len_schedule:dict[int,int]|None=None,

load_format:str|None=None,

acceptance_window:Annotated[int,Ge(ge=0)]|None=None,

acceptance_length_threshold:Annotated[float,Ge(ge=0)]|None=None,

allow_advanced_sampling:bool=False,

decoding_type:Literal['Lookahead']='Lookahead',

max_window_size:Annotated[int,Gt(gt=0)]=4,

max_ngram_size:Annotated[int,Gt(gt=0)]=3,

max_verification_set_size:Annotated[int,Gt(gt=0)]=4,

)[source]#

Bases: `DecodingBaseConfig`, `PybindMirror`

Configuration for lookahead speculative decoding.

fieldacceptance_length_threshold:NonNegativeFloat|None=None#

The threshold for average acceptance length; speculation will be disabled permanently once the rolling average over the last N completed requests (N = acceptance_window) drops below this value. PyTorch backend only.

fieldacceptance_window:NonNegativeInt|None=None#

The rolling average window size (N) for acceptance length across completed requests. If not set or set to 0, the feature is disabled. PyTorch backend only.

fieldallow_advanced_sampling:bool=False#

If true, allows non-greedy sampling when speculation is used. Only applicable to 1-model code paths; non-greedy sampling is always enabled on 2-model paths.

fielddecoding_type:Literal['Lookahead']='Lookahead'#

fielddraft_len_schedule:dict[int,int]|None=None#

Developer interface: dynamically adjust draft length based on active batch size in runtime. Maps batch size to draft lengths. For example, {1: 4, 4: 2, 8: 0} means: batch_size >= 1 uses draft_len=4, batch_size >= 4 uses draft_len=2, batch_size >= 8 uses draft_len=0 (disable speculation). draft_len_schedule is enforced to contain batch_size=1 and its according draft_len equals max_draft_len for consistency; for example, if max_draft_len=4, the schedule must contain {1: 4}.

fieldload_format:str|None=None#

The load format of the speculative model.

fieldmax_concurrency:NonNegativeInt|None=None#

When specified, speculation will be disabled at batch sizes above this value. Otherwise, speculation will always be on. PyTorch backend only.

fieldmax_draft_len:NonNegativeInt|None=None#

The maximum number of draft tokens.

fieldmax_ngram_size:Annotated[int,Gt(gt=0)]=3#

Number of tokens per NGram.

Constraints:

gt = 0

fieldmax_total_draft_tokens:int|None=None#

The number of draft tokens in the draft tokens tree. If it’s a linear tree, each draft layer will only generate one draft token. In this case, max_draft_len == max_total_draft_tokens. If it’s a static or dynamic tree, each draft layer may generate more than one draft token. In this case, max_total_draft_tokens >= max_draft_len.

fieldmax_verification_set_size:Annotated[int,Gt(gt=0)]=4#

Number of NGrams in verification branch per step.

Constraints:

gt = 0

fieldmax_window_size:Annotated[int,Gt(gt=0)]=4#

Number of NGrams in lookahead branch per step.

Constraints:

gt = 0

fieldspeculative_model:str|Path|None=None#

The speculative (draft) model. Accepts either (1) a HuggingFace Hub model ID (e.g. ‘yuhuili/EAGLE3-LLaMA3.1-Instruct-8B’), which will be automatically downloaded, or (2) a local filesystem path to a downloaded model directory.

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

calculate_speculative_resource()[source]#

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(obj:Any)→Self#

classmethodfrom_pybind(

pybind_instance:PybindMirror,

)→T#

Construct an instance of the given class from the fields in the given
pybind class instance.

Parameters:

cls – Type of the class to construct, must be a subclass of pydantic
BaseModel

pybind_instance – Instance of the pybind class to construct from its
fields

Notes

When a field value is None in the pybind class, but it’s not
optional and has a default value in the BaseModel class, it would
get the default value defined in the BaseModel class.

Returns:

Instance of the given class, populated with the fields of the given
pybind instance

staticget_pybind_enum_fields(pybind_class)#

Get all the enum fields from the pybind class.

staticget_pybind_variable_fields(config_cls)#

Get all the variable fields from the pybind class.

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

staticmaybe_to_pybind(ins)#

staticmirror_pybind_enum(pybind_class)#

Mirror the enum fields from the pybind class to the Python class.

staticmirror_pybind_fields(pybind_class)#

Class decorator that ensures Python class fields mirror those of a C++ class.

Parameters:

pybind_class – The C++ class whose fields should be mirrored

Returns:

A decorator function that validates field mirroring

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(context:Any, /)→None#

This function is meant to behave like a BaseModel method to initialise private attributes.

It takes context as an argument since that’s what pydantic-core passes when calling it.

Parameters:

self – The BaseModel instance.

context – The context.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

num_capture_layers()→int#

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(obj:Any)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

staticpybind_equals(obj0, obj1)#

Check if two pybind objects are equal.

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

validatorset_max_total_draft_tokens»allfields[source]#

supports_backend(backend:str)→bool[source]#

Override if the speculation algorithm does not support
a subset of the possible backends.

classmethodupdate_forward_refs(

**localns:Any,

)→None#

classmethodvalidate(value:Any)→Self#

validatorvalidate_draft_len_schedule_and_sort»draft_len_schedule#

Validate and sort draft_len_schedule by batch size thresholds.

propertyis_linear_tree:bool#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'acceptance_length_threshold':FieldInfo(annotation=Union[Annotated[float,Ge],NoneType],required=False,default=None,description='Thethresholdforaverageacceptancelength;speculationwillbedisabledpermanentlyoncetherollingaverageoverthelastNcompletedrequests(N=acceptance_window)dropsbelowthisvalue.PyTorchbackendonly.'),'acceptance_window':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Therollingaveragewindowsize(N)foracceptancelengthacrosscompletedrequests.Ifnotsetorsetto0,thefeatureisdisabled.PyTorchbackendonly.'),'allow_advanced_sampling':FieldInfo(annotation=bool,required=False,default=False,description='Iftrue,allowsnon-greedysamplingwhenspeculationisused.Onlyapplicableto1-modelcodepaths;non-greedysamplingisalwaysenabledon2-modelpaths.',json_schema_extra={'status':'prototype'}),'decoding_type':FieldInfo(annotation=Literal['Lookahead'],required=False,default='Lookahead'),'draft_len_schedule':FieldInfo(annotation=Union[dict[int,int],NoneType],required=False,default=None,description='Developerinterface:dynamicallyadjustdraftlengthbasedonactivebatchsizeinruntime.Mapsbatchsizetodraftlengths.Forexample,{1:4,4:2,8:0}means:batch_size>=1usesdraft_len=4,batch_size>=4usesdraft_len=2,batch_size>=8usesdraft_len=0(disablespeculation).draft_len_scheduleisenforcedtocontainbatch_size=1anditsaccordingdraft_lenequalsmax_draft_lenforconsistency;forexample,ifmax_draft_len=4,theschedulemustcontain{1:4}.'),'load_format':FieldInfo(annotation=Union[str,NoneType],required=False,default=None,description='Theloadformatofthespeculativemodel.'),'max_concurrency':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Whenspecified,speculationwillbedisabledatbatchsizesabovethisvalue.Otherwise,speculationwillalwaysbeon.PyTorchbackendonly.'),'max_draft_len':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Themaximumnumberofdrafttokens.'),'max_ngram_size':FieldInfo(annotation=int,required=False,default=3,description='NumberoftokensperNGram.',metadata=[Gt(gt=0)]),'max_total_draft_tokens':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description="Thenumberofdrafttokensinthedrafttokenstree.Ifit'salineartree,eachdraftlayerwillonlygenerateonedrafttoken.Inthiscase,max_draft_len==max_total_draft_tokens.Ifit'sastaticordynamictree,eachdraftlayermaygeneratemorethanonedrafttoken.Inthiscase,max_total_draft_tokens>=max_draft_len."),'max_verification_set_size':FieldInfo(annotation=int,required=False,default=4,description='NumberofNGramsinverificationbranchperstep.',metadata=[Gt(gt=0)]),'max_window_size':FieldInfo(annotation=int,required=False,default=4,description='NumberofNGramsinlookaheadbranchperstep.',metadata=[Gt(gt=0)]),'speculative_model':FieldInfo(annotation=Union[str,Path,NoneType],required=False,default=None,alias_priority=2,validation_alias=AliasChoices(choices=['speculative_model','speculative_model_dir']),description="Thespeculative(draft)model.Acceptseither(1)aHuggingFaceHubmodelID(e.g.'yuhuili/EAGLE3-LLaMA3.1-Instruct-8B'),whichwillbeautomaticallydownloaded,or(2)alocalfilesystempathtoadownloadedmodeldirectory.")}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

propertyspec_dec_mode#

propertytokens_per_gen_step:int#

Total tokens per gen request in one spec dec iteration (including golden token).

classtensorrt_llm.llmapi.MedusaDecodingConfig(

max_draft_len:Annotated[int,Ge(ge=0)]|None=None,

max_total_draft_tokens:int|None=None,

speculative_model:str|Path|None=None,

max_concurrency:Annotated[int,Ge(ge=0)]|None=None,

draft_len_schedule:dict[int,int]|None=None,

load_format:str|None=None,

acceptance_window:Annotated[int,Ge(ge=0)]|None=None,

acceptance_length_threshold:Annotated[float,Ge(ge=0)]|None=None,

allow_advanced_sampling:bool=False,

decoding_type:Literal['Medusa']='Medusa',

medusa_choices:List[List[int]]|None=None,

num_medusa_heads:int|None=None,

)[source]#

Bases: `DecodingBaseConfig`

fieldacceptance_length_threshold:NonNegativeFloat|None=None#

The threshold for average acceptance length; speculation will be disabled permanently once the rolling average over the last N completed requests (N = acceptance_window) drops below this value. PyTorch backend only.

fieldacceptance_window:NonNegativeInt|None=None#

The rolling average window size (N) for acceptance length across completed requests. If not set or set to 0, the feature is disabled. PyTorch backend only.

fieldallow_advanced_sampling:bool=False#

If true, allows non-greedy sampling when speculation is used. Only applicable to 1-model code paths; non-greedy sampling is always enabled on 2-model paths.

fielddecoding_type:Literal['Medusa']='Medusa'#

fielddraft_len_schedule:dict[int,int]|None=None#

Developer interface: dynamically adjust draft length based on active batch size in runtime. Maps batch size to draft lengths. For example, {1: 4, 4: 2, 8: 0} means: batch_size >= 1 uses draft_len=4, batch_size >= 4 uses draft_len=2, batch_size >= 8 uses draft_len=0 (disable speculation). draft_len_schedule is enforced to contain batch_size=1 and its according draft_len equals max_draft_len for consistency; for example, if max_draft_len=4, the schedule must contain {1: 4}.

fieldload_format:str|None=None#

The load format of the speculative model.

fieldmax_concurrency:NonNegativeInt|None=None#

When specified, speculation will be disabled at batch sizes above this value. Otherwise, speculation will always be on. PyTorch backend only.

fieldmax_draft_len:NonNegativeInt|None=None#

The maximum number of draft tokens.

fieldmax_total_draft_tokens:int|None=None#

The number of draft tokens in the draft tokens tree. If it’s a linear tree, each draft layer will only generate one draft token. In this case, max_draft_len == max_total_draft_tokens. If it’s a static or dynamic tree, each draft layer may generate more than one draft token. In this case, max_total_draft_tokens >= max_draft_len.

fieldmedusa_choices:List[List[int]]|None=None#

Tree structure for Medusa draft token generation. Each sublist represents a path in the tree where elements are token indices at each level. For example, [[0], [0, 0], [1], [0, 1]] defines multiple branches.

fieldnum_medusa_heads:int|None=None#

Number of Medusa prediction heads to use. Each head predicts a draft token at a different position in parallel. If not specified, defaults to the ‘medusa_num_heads’ value from the Medusa model’s config.json.

fieldspeculative_model:str|Path|None=None#

The speculative (draft) model. Accepts either (1) a HuggingFace Hub model ID (e.g. ‘yuhuili/EAGLE3-LLaMA3.1-Instruct-8B’), which will be automatically downloaded, or (2) a local filesystem path to a downloaded model directory.

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(obj:Any)→Self#

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(context:Any, /)→None#

This function is meant to behave like a BaseModel method to initialise private attributes.

It takes context as an argument since that’s what pydantic-core passes when calling it.

Parameters:

self – The BaseModel instance.

context – The context.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

num_capture_layers()→int#

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(obj:Any)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

validatorset_max_total_draft_tokens»allfields[source]#

supports_backend(backend:str)→bool[source]#

Override if the speculation algorithm does not support
a subset of the possible backends.

classmethodupdate_forward_refs(

**localns:Any,

)→None#

classmethodvalidate(value:Any)→Self#

validatorvalidate_draft_len_schedule_and_sort»draft_len_schedule#

Validate and sort draft_len_schedule by batch size thresholds.

propertyis_linear_tree:bool#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'acceptance_length_threshold':FieldInfo(annotation=Union[Annotated[float,Ge],NoneType],required=False,default=None,description='Thethresholdforaverageacceptancelength;speculationwillbedisabledpermanentlyoncetherollingaverageoverthelastNcompletedrequests(N=acceptance_window)dropsbelowthisvalue.PyTorchbackendonly.'),'acceptance_window':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Therollingaveragewindowsize(N)foracceptancelengthacrosscompletedrequests.Ifnotsetorsetto0,thefeatureisdisabled.PyTorchbackendonly.'),'allow_advanced_sampling':FieldInfo(annotation=bool,required=False,default=False,description='Iftrue,allowsnon-greedysamplingwhenspeculationisused.Onlyapplicableto1-modelcodepaths;non-greedysamplingisalwaysenabledon2-modelpaths.',json_schema_extra={'status':'prototype'}),'decoding_type':FieldInfo(annotation=Literal['Medusa'],required=False,default='Medusa'),'draft_len_schedule':FieldInfo(annotation=Union[dict[int,int],NoneType],required=False,default=None,description='Developerinterface:dynamicallyadjustdraftlengthbasedonactivebatchsizeinruntime.Mapsbatchsizetodraftlengths.Forexample,{1:4,4:2,8:0}means:batch_size>=1usesdraft_len=4,batch_size>=4usesdraft_len=2,batch_size>=8usesdraft_len=0(disablespeculation).draft_len_scheduleisenforcedtocontainbatch_size=1anditsaccordingdraft_lenequalsmax_draft_lenforconsistency;forexample,ifmax_draft_len=4,theschedulemustcontain{1:4}.'),'load_format':FieldInfo(annotation=Union[str,NoneType],required=False,default=None,description='Theloadformatofthespeculativemodel.'),'max_concurrency':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Whenspecified,speculationwillbedisabledatbatchsizesabovethisvalue.Otherwise,speculationwillalwaysbeon.PyTorchbackendonly.'),'max_draft_len':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Themaximumnumberofdrafttokens.'),'max_total_draft_tokens':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description="Thenumberofdrafttokensinthedrafttokenstree.Ifit'salineartree,eachdraftlayerwillonlygenerateonedrafttoken.Inthiscase,max_draft_len==max_total_draft_tokens.Ifit'sastaticordynamictree,eachdraftlayermaygeneratemorethanonedrafttoken.Inthiscase,max_total_draft_tokens>=max_draft_len."),'medusa_choices':FieldInfo(annotation=Union[List[List[int]],NoneType],required=False,default=None,description='TreestructureforMedusadrafttokengeneration.Eachsublistrepresentsapathinthetreewhereelementsaretokenindicesateachlevel.Forexample,[[0],[0,0],[1],[0,1]]definesmultiplebranches.'),'num_medusa_heads':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description="NumberofMedusapredictionheadstouse.Eachheadpredictsadrafttokenatadifferentpositioninparallel.Ifnotspecified,defaultstothe'medusa_num_heads'valuefromtheMedusamodel'sconfig.json."),'speculative_model':FieldInfo(annotation=Union[str,Path,NoneType],required=False,default=None,alias_priority=2,validation_alias=AliasChoices(choices=['speculative_model','speculative_model_dir']),description="Thespeculative(draft)model.Acceptseither(1)aHuggingFaceHubmodelID(e.g.'yuhuili/EAGLE3-LLaMA3.1-Instruct-8B'),whichwillbeautomaticallydownloaded,or(2)alocalfilesystempathtoadownloadedmodeldirectory.")}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

propertyspec_dec_mode#

propertytokens_per_gen_step:int#

Total tokens per gen request in one spec dec iteration (including golden token).

classtensorrt_llm.llmapi.EagleDecodingConfig(

max_draft_len:Annotated[int,Ge(ge=0)]|None=None,

max_total_draft_tokens:int|None=None,

speculative_model:str|Path|None=None,

max_concurrency:Annotated[int,Ge(ge=0)]|None=None,

draft_len_schedule:dict[int,int]|None=None,

load_format:str|None=None,

acceptance_window:Annotated[int,Ge(ge=0)]|None=None,

acceptance_length_threshold:Annotated[float,Ge(ge=0)]|None=None,

allow_advanced_sampling:bool=False,

decoding_type:Literal['Eagle']='Eagle',

eagle_choices:List[List[int]]|None=None,

greedy_sampling:bool|None=True,

posterior_threshold:float|None=None,

use_dynamic_tree:bool|None=False,

dynamic_tree_max_topK:int|None=None,

num_eagle_layers:int|None=None,

max_non_leaves_per_layer:int|None=None,

eagle3_one_model:bool|None=True,

eagle3_layers_to_capture:Set[int]|None=None,

eagle3_model_arch:Literal['llama3','mistral_large3']='llama3',

)[source]#

Bases: `DecodingBaseConfig`

fieldacceptance_length_threshold:NonNegativeFloat|None=None#

The threshold for average acceptance length; speculation will be disabled permanently once the rolling average over the last N completed requests (N = acceptance_window) drops below this value. PyTorch backend only.

fieldacceptance_window:NonNegativeInt|None=None#

The rolling average window size (N) for acceptance length across completed requests. If not set or set to 0, the feature is disabled. PyTorch backend only.

fieldallow_advanced_sampling:bool=False#

If true, allows non-greedy sampling when speculation is used. Only applicable to 1-model code paths; non-greedy sampling is always enabled on 2-model paths.

fielddecoding_type:Literal['Eagle']='Eagle'#

fielddraft_len_schedule:dict[int,int]|None=None#

Developer interface: dynamically adjust draft length based on active batch size in runtime. Maps batch size to draft lengths. For example, {1: 4, 4: 2, 8: 0} means: batch_size >= 1 uses draft_len=4, batch_size >= 4 uses draft_len=2, batch_size >= 8 uses draft_len=0 (disable speculation). draft_len_schedule is enforced to contain batch_size=1 and its according draft_len equals max_draft_len for consistency; for example, if max_draft_len=4, the schedule must contain {1: 4}.

fielddynamic_tree_max_topK:int|None=None#

The topK value for each layer when dynamic tree is enabled.

fieldeagle3_layers_to_capture:Set[int]|None=None#

Target model layer indices to capture hidden states from for the EAGLE3 draft model. Defaults to {1, num_layers//2-1, num_layers-4}.

fieldeagle3_model_arch:Literal['llama3','mistral_large3']='llama3'#

The model architecture of the eagle3 model.

fieldeagle3_one_model:bool|None=True#

Whether to use the faster one-model implementation (draft as submodule) or the two-model implementation.

fieldeagle_choices:List[List[int]]|None=None#

Static tree structure for draft token generation. Each sublist represents a path in the tree. Mutually exclusive with use_dynamic_tree.

fieldgreedy_sampling:bool|None=True#

Whether to use greedy sampling (Top-1 with token equality acceptance) or typical acceptance with multinomial sampling.

fieldload_format:str|None=None#

The load format of the speculative model.

fieldmax_concurrency:NonNegativeInt|None=None#

When specified, speculation will be disabled at batch sizes above this value. Otherwise, speculation will always be on. PyTorch backend only.

fieldmax_draft_len:NonNegativeInt|None=None#

The maximum number of draft tokens.

fieldmax_non_leaves_per_layer:int|None=None#

The number of non-leaves in each layer.

fieldmax_total_draft_tokens:int|None=None#

The number of draft tokens in the draft tokens tree. If it’s a linear tree, each draft layer will only generate one draft token. In this case, max_draft_len == max_total_draft_tokens. If it’s a static or dynamic tree, each draft layer may generate more than one draft token. In this case, max_total_draft_tokens >= max_draft_len.

fieldnum_eagle_layers:int|None=None#

The number of eagle layers. Will not be used in pytorch flow, just for compatibility with TRT flow.

fieldposterior_threshold:float|None=None#

Minimum token probability threshold for typical acceptance. Corresponds to epsilon in https://arxiv.org/pdf/2401.10774.

fieldspeculative_model:str|Path|None=None#

The speculative (draft) model. Accepts either (1) a HuggingFace Hub model ID (e.g. ‘yuhuili/EAGLE3-LLaMA3.1-Instruct-8B’), which will be automatically downloaded, or (2) a local filesystem path to a downloaded model directory.

fielduse_dynamic_tree:bool|None=False#

Whether to use dynamic tree (Eagle-2 algorithm). Mutually exclusive with eagle_choices.

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

check_eagle_choices()[source]#

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(obj:Any)→Self#

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(context:Any, /)→None#

This function is meant to behave like a BaseModel method to initialise private attributes.

It takes context as an argument since that’s what pydantic-core passes when calling it.

Parameters:

self – The BaseModel instance.

context – The context.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(obj:Any)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

supports_backend(backend:str)→bool#

Override if the speculation algorithm does not support
a subset of the possible backends.

classmethodupdate_forward_refs(

**localns:Any,

)→None#

classmethodvalidate(value:Any)→Self#

validatorvalidate_draft_len_schedule_and_sort»draft_len_schedule#

Validate and sort draft_len_schedule by batch size thresholds.

validatorvalidate_eagle_choices»eagle_choices[source]#

validatorvalidate_eagle_config»allfields[source]#

validatorvalidate_speculative_model»allfields[source]#

propertyis_linear_tree:bool#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'acceptance_length_threshold':FieldInfo(annotation=Union[Annotated[float,Ge],NoneType],required=False,default=None,description='Thethresholdforaverageacceptancelength;speculationwillbedisabledpermanentlyoncetherollingaverageoverthelastNcompletedrequests(N=acceptance_window)dropsbelowthisvalue.PyTorchbackendonly.'),'acceptance_window':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Therollingaveragewindowsize(N)foracceptancelengthacrosscompletedrequests.Ifnotsetorsetto0,thefeatureisdisabled.PyTorchbackendonly.'),'allow_advanced_sampling':FieldInfo(annotation=bool,required=False,default=False,description='Iftrue,allowsnon-greedysamplingwhenspeculationisused.Onlyapplicableto1-modelcodepaths;non-greedysamplingisalwaysenabledon2-modelpaths.',json_schema_extra={'status':'prototype'}),'decoding_type':FieldInfo(annotation=Literal['Eagle'],required=False,default='Eagle'),'draft_len_schedule':FieldInfo(annotation=Union[dict[int,int],NoneType],required=False,default=None,description='Developerinterface:dynamicallyadjustdraftlengthbasedonactivebatchsizeinruntime.Mapsbatchsizetodraftlengths.Forexample,{1:4,4:2,8:0}means:batch_size>=1usesdraft_len=4,batch_size>=4usesdraft_len=2,batch_size>=8usesdraft_len=0(disablespeculation).draft_len_scheduleisenforcedtocontainbatch_size=1anditsaccordingdraft_lenequalsmax_draft_lenforconsistency;forexample,ifmax_draft_len=4,theschedulemustcontain{1:4}.'),'dynamic_tree_max_topK':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description='ThetopKvalueforeachlayerwhendynamictreeisenabled.'),'eagle3_layers_to_capture':FieldInfo(annotation=Union[Set[int],NoneType],required=False,default=None,description='TargetmodellayerindicestocapturehiddenstatesfromfortheEAGLE3draftmodel.Defaultsto{1,num_layers//2-1,num_layers-4}.'),'eagle3_model_arch':FieldInfo(annotation=Literal['llama3','mistral_large3'],required=False,default='llama3',description='Themodelarchitectureoftheeagle3model.'),'eagle3_one_model':FieldInfo(annotation=Union[bool,NoneType],required=False,default=True,description='Whethertousethefasterone-modelimplementation(draftassubmodule)orthetwo-modelimplementation.'),'eagle_choices':FieldInfo(annotation=Union[List[List[int]],NoneType],required=False,default=None,description='Statictreestructurefordrafttokengeneration.Eachsublistrepresentsapathinthetree.Mutuallyexclusivewithuse_dynamic_tree.'),'greedy_sampling':FieldInfo(annotation=Union[bool,NoneType],required=False,default=True,description='Whethertousegreedysampling(Top-1withtokenequalityacceptance)ortypicalacceptancewithmultinomialsampling.'),'load_format':FieldInfo(annotation=Union[str,NoneType],required=False,default=None,description='Theloadformatofthespeculativemodel.'),'max_concurrency':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Whenspecified,speculationwillbedisabledatbatchsizesabovethisvalue.Otherwise,speculationwillalwaysbeon.PyTorchbackendonly.'),'max_draft_len':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Themaximumnumberofdrafttokens.'),'max_non_leaves_per_layer':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description='Thenumberofnon-leavesineachlayer.'),'max_total_draft_tokens':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description="Thenumberofdrafttokensinthedrafttokenstree.Ifit'salineartree,eachdraftlayerwillonlygenerateonedrafttoken.Inthiscase,max_draft_len==max_total_draft_tokens.Ifit'sastaticordynamictree,eachdraftlayermaygeneratemorethanonedrafttoken.Inthiscase,max_total_draft_tokens>=max_draft_len."),'num_eagle_layers':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description='Thenumberofeaglelayers.Willnotbeusedinpytorchflow,justforcompatibilitywithTRTflow.'),'posterior_threshold':FieldInfo(annotation=Union[float,NoneType],required=False,default=None,description='Minimumtokenprobabilitythresholdfortypicalacceptance.Correspondstoepsiloninhttps://arxiv.org/pdf/2401.10774.'),'speculative_model':FieldInfo(annotation=Union[str,Path,NoneType],required=False,default=None,alias_priority=2,validation_alias=AliasChoices(choices=['speculative_model','speculative_model_dir']),description="Thespeculative(draft)model.Acceptseither(1)aHuggingFaceHubmodelID(e.g.'yuhuili/EAGLE3-LLaMA3.1-Instruct-8B'),whichwillbeautomaticallydownloaded,or(2)alocalfilesystempathtoadownloadedmodeldirectory."),'use_dynamic_tree':FieldInfo(annotation=Union[bool,NoneType],required=False,default=False,description='Whethertousedynamictree(Eagle-2algorithm).Mutuallyexclusivewitheagle_choices.')}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

propertynum_capture_layers:int#

Returns the number of layers to capture of the target model.
If eagle3_layers_to_capture is not None, return the length of the set.
Otherwise, assume Eagle3 base set and return 3.

propertyspec_dec_mode#

propertytokens_per_gen_step:int#

Total tokens per gen request in one spec dec iteration (including golden token).

classtensorrt_llm.llmapi.Eagle3DecodingConfig(

max_draft_len:Annotated[int,Ge(ge=0)]|None=None,

max_total_draft_tokens:int|None=None,

speculative_model:str|Path|None=None,

max_concurrency:Annotated[int,Ge(ge=0)]|None=None,

draft_len_schedule:dict[int,int]|None=None,

load_format:str|None=None,

acceptance_window:Annotated[int,Ge(ge=0)]|None=None,

acceptance_length_threshold:Annotated[float,Ge(ge=0)]|None=None,

allow_advanced_sampling:bool=False,

decoding_type:Literal['Eagle3']='Eagle3',

eagle_choices:List[List[int]]|None=None,

greedy_sampling:bool|None=True,

posterior_threshold:float|None=None,

use_dynamic_tree:bool|None=False,

dynamic_tree_max_topK:int|None=None,

num_eagle_layers:int|None=None,

max_non_leaves_per_layer:int|None=None,

eagle3_one_model:bool|None=True,

eagle3_layers_to_capture:Set[int]|None=None,

eagle3_model_arch:Literal['llama3','mistral_large3']='llama3',

use_sa_spec:bool|None=False,

sa_spec_threshold:Annotated[int,Gt(gt=0)]=4,

)[source]#

Bases: `EagleDecodingConfig`

fieldacceptance_length_threshold:NonNegativeFloat|None=None#

The threshold for average acceptance length; speculation will be disabled permanently once the rolling average over the last N completed requests (N = acceptance_window) drops below this value. PyTorch backend only.

fieldacceptance_window:NonNegativeInt|None=None#

The rolling average window size (N) for acceptance length across completed requests. If not set or set to 0, the feature is disabled. PyTorch backend only.

fieldallow_advanced_sampling:bool=False#

If true, allows non-greedy sampling when speculation is used. Only applicable to 1-model code paths; non-greedy sampling is always enabled on 2-model paths.

fielddecoding_type:Literal['Eagle3']='Eagle3'#

fielddraft_len_schedule:dict[int,int]|None=None#

Developer interface: dynamically adjust draft length based on active batch size in runtime. Maps batch size to draft lengths. For example, {1: 4, 4: 2, 8: 0} means: batch_size >= 1 uses draft_len=4, batch_size >= 4 uses draft_len=2, batch_size >= 8 uses draft_len=0 (disable speculation). draft_len_schedule is enforced to contain batch_size=1 and its according draft_len equals max_draft_len for consistency; for example, if max_draft_len=4, the schedule must contain {1: 4}.

fielddynamic_tree_max_topK:int|None=None#

The topK value for each layer when dynamic tree is enabled.

fieldeagle3_layers_to_capture:Set[int]|None=None#

Target model layer indices to capture hidden states from for the EAGLE3 draft model. Defaults to {1, num_layers//2-1, num_layers-4}.

fieldeagle3_model_arch:Literal['llama3','mistral_large3']='llama3'#

The model architecture of the eagle3 model.

fieldeagle3_one_model:bool|None=True#

Whether to use the faster one-model implementation (draft as submodule) or the two-model implementation.

fieldeagle_choices:List[List[int]]|None=None#

Static tree structure for draft token generation. Each sublist represents a path in the tree. Mutually exclusive with use_dynamic_tree.

fieldgreedy_sampling:bool|None=True#

Whether to use greedy sampling (Top-1 with token equality acceptance) or typical acceptance with multinomial sampling.

fieldload_format:str|None=None#

The load format of the speculative model.

fieldmax_concurrency:NonNegativeInt|None=None#

When specified, speculation will be disabled at batch sizes above this value. Otherwise, speculation will always be on. PyTorch backend only.

fieldmax_draft_len:NonNegativeInt|None=None#

The maximum number of draft tokens.

fieldmax_non_leaves_per_layer:int|None=None#

The number of non-leaves in each layer.

fieldmax_total_draft_tokens:int|None=None#

The number of draft tokens in the draft tokens tree. If it’s a linear tree, each draft layer will only generate one draft token. In this case, max_draft_len == max_total_draft_tokens. If it’s a static or dynamic tree, each draft layer may generate more than one draft token. In this case, max_total_draft_tokens >= max_draft_len.

fieldnum_eagle_layers:int|None=None#

The number of eagle layers. Will not be used in pytorch flow, just for compatibility with TRT flow.

fieldposterior_threshold:float|None=None#

Minimum token probability threshold for typical acceptance. Corresponds to epsilon in https://arxiv.org/pdf/2401.10774.

fieldsa_spec_threshold:Annotated[int,Gt(gt=0)]=4#

The threshold for the Suffix Automaton Decoding. If the length of the suffix match exceeds the threshold, use the suffix automaton output for the next draft tokens.

Constraints:

gt = 0

fieldspeculative_model:str|Path|None=None#

The speculative (draft) model. Accepts either (1) a HuggingFace Hub model ID (e.g. ‘yuhuili/EAGLE3-LLaMA3.1-Instruct-8B’), which will be automatically downloaded, or (2) a local filesystem path to a downloaded model directory.

fielduse_dynamic_tree:bool|None=False#

Whether to use dynamic tree (Eagle-2 algorithm). Mutually exclusive with eagle_choices.

fielduse_sa_spec:bool|None=False#

Combine with Suffix Automaton Decoding

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

check_eagle_choices()#

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(obj:Any)→Self#

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(context:Any, /)→None#

This function is meant to behave like a BaseModel method to initialise private attributes.

It takes context as an argument since that’s what pydantic-core passes when calling it.

Parameters:

self – The BaseModel instance.

context – The context.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(obj:Any)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

supports_backend(backend:str)→bool#

Override if the speculation algorithm does not support
a subset of the possible backends.

classmethodupdate_forward_refs(

**localns:Any,

)→None#

classmethodvalidate(value:Any)→Self#

validatorvalidate_draft_len_schedule_and_sort»draft_len_schedule#

Validate and sort draft_len_schedule by batch size thresholds.

validatorvalidate_eagle_choices»eagle_choices#

validatorvalidate_eagle_config»allfields#

validatorvalidate_speculative_model»allfields#

propertyis_linear_tree:bool#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'acceptance_length_threshold':FieldInfo(annotation=Union[Annotated[float,Ge],NoneType],required=False,default=None,description='Thethresholdforaverageacceptancelength;speculationwillbedisabledpermanentlyoncetherollingaverageoverthelastNcompletedrequests(N=acceptance_window)dropsbelowthisvalue.PyTorchbackendonly.'),'acceptance_window':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Therollingaveragewindowsize(N)foracceptancelengthacrosscompletedrequests.Ifnotsetorsetto0,thefeatureisdisabled.PyTorchbackendonly.'),'allow_advanced_sampling':FieldInfo(annotation=bool,required=False,default=False,description='Iftrue,allowsnon-greedysamplingwhenspeculationisused.Onlyapplicableto1-modelcodepaths;non-greedysamplingisalwaysenabledon2-modelpaths.',json_schema_extra={'status':'prototype'}),'decoding_type':FieldInfo(annotation=Literal['Eagle3'],required=False,default='Eagle3'),'draft_len_schedule':FieldInfo(annotation=Union[dict[int,int],NoneType],required=False,default=None,description='Developerinterface:dynamicallyadjustdraftlengthbasedonactivebatchsizeinruntime.Mapsbatchsizetodraftlengths.Forexample,{1:4,4:2,8:0}means:batch_size>=1usesdraft_len=4,batch_size>=4usesdraft_len=2,batch_size>=8usesdraft_len=0(disablespeculation).draft_len_scheduleisenforcedtocontainbatch_size=1anditsaccordingdraft_lenequalsmax_draft_lenforconsistency;forexample,ifmax_draft_len=4,theschedulemustcontain{1:4}.'),'dynamic_tree_max_topK':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description='ThetopKvalueforeachlayerwhendynamictreeisenabled.'),'eagle3_layers_to_capture':FieldInfo(annotation=Union[Set[int],NoneType],required=False,default=None,description='TargetmodellayerindicestocapturehiddenstatesfromfortheEAGLE3draftmodel.Defaultsto{1,num_layers//2-1,num_layers-4}.'),'eagle3_model_arch':FieldInfo(annotation=Literal['llama3','mistral_large3'],required=False,default='llama3',description='Themodelarchitectureoftheeagle3model.'),'eagle3_one_model':FieldInfo(annotation=Union[bool,NoneType],required=False,default=True,description='Whethertousethefasterone-modelimplementation(draftassubmodule)orthetwo-modelimplementation.'),'eagle_choices':FieldInfo(annotation=Union[List[List[int]],NoneType],required=False,default=None,description='Statictreestructurefordrafttokengeneration.Eachsublistrepresentsapathinthetree.Mutuallyexclusivewithuse_dynamic_tree.'),'greedy_sampling':FieldInfo(annotation=Union[bool,NoneType],required=False,default=True,description='Whethertousegreedysampling(Top-1withtokenequalityacceptance)ortypicalacceptancewithmultinomialsampling.'),'load_format':FieldInfo(annotation=Union[str,NoneType],required=False,default=None,description='Theloadformatofthespeculativemodel.'),'max_concurrency':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Whenspecified,speculationwillbedisabledatbatchsizesabovethisvalue.Otherwise,speculationwillalwaysbeon.PyTorchbackendonly.'),'max_draft_len':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Themaximumnumberofdrafttokens.'),'max_non_leaves_per_layer':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description='Thenumberofnon-leavesineachlayer.'),'max_total_draft_tokens':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description="Thenumberofdrafttokensinthedrafttokenstree.Ifit'salineartree,eachdraftlayerwillonlygenerateonedrafttoken.Inthiscase,max_draft_len==max_total_draft_tokens.Ifit'sastaticordynamictree,eachdraftlayermaygeneratemorethanonedrafttoken.Inthiscase,max_total_draft_tokens>=max_draft_len."),'num_eagle_layers':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description='Thenumberofeaglelayers.Willnotbeusedinpytorchflow,justforcompatibilitywithTRTflow.'),'posterior_threshold':FieldInfo(annotation=Union[float,NoneType],required=False,default=None,description='Minimumtokenprobabilitythresholdfortypicalacceptance.Correspondstoepsiloninhttps://arxiv.org/pdf/2401.10774.'),'sa_spec_threshold':FieldInfo(annotation=int,required=False,default=4,description='ThethresholdfortheSuffixAutomatonDecoding.Ifthelengthofthesuffixmatchexceedsthethreshold,usethesuffixautomatonoutputforthenextdrafttokens.',metadata=[Gt(gt=0)]),'speculative_model':FieldInfo(annotation=Union[str,Path,NoneType],required=False,default=None,alias_priority=2,validation_alias=AliasChoices(choices=['speculative_model','speculative_model_dir']),description="Thespeculative(draft)model.Acceptseither(1)aHuggingFaceHubmodelID(e.g.'yuhuili/EAGLE3-LLaMA3.1-Instruct-8B'),whichwillbeautomaticallydownloaded,or(2)alocalfilesystempathtoadownloadedmodeldirectory."),'use_dynamic_tree':FieldInfo(annotation=Union[bool,NoneType],required=False,default=False,description='Whethertousedynamictree(Eagle-2algorithm).Mutuallyexclusivewitheagle_choices.'),'use_sa_spec':FieldInfo(annotation=Union[bool,NoneType],required=False,default=False,description='CombinewithSuffixAutomatonDecoding',json_schema_extra={'status':'beta'})}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

propertynum_capture_layers:int#

Returns the number of layers to capture of the target model.
If eagle3_layers_to_capture is not None, return the length of the set.
Otherwise, assume Eagle3 base set and return 3.

propertyspec_dec_mode#

propertytokens_per_gen_step:int#

Total tokens per gen request in one spec dec iteration (including golden token).

classtensorrt_llm.llmapi.MTPDecodingConfig(

max_draft_len:Annotated[int,Ge(ge=0)]|None=None,

max_total_draft_tokens:int|None=None,

speculative_model:str|Path|None=None,

max_concurrency:Annotated[int,Ge(ge=0)]|None=None,

draft_len_schedule:dict[int,int]|None=None,

load_format:str|None=None,

acceptance_window:Annotated[int,Ge(ge=0)]|None=None,

acceptance_length_threshold:Annotated[float,Ge(ge=0)]|None=None,

allow_advanced_sampling:bool=False,

decoding_type:Literal['MTP']='MTP',

num_nextn_predict_layers:Annotated[int,Gt(gt=0)]=1,

use_relaxed_acceptance_for_thinking:bool=False,

relaxed_topk:int=1,

relaxed_delta:float=0.0,

use_mtp_vanilla:bool=False,

mtp_eagle_one_model:bool=True,

use_sa_spec:bool|None=False,

sa_spec_threshold:Annotated[int,Gt(gt=0)]=4,

num_nextn_predict_layers_from_model_config:int=1,

begin_thinking_phase_token:int=128798,

end_thinking_phase_token:int=128799,

)[source]#

Bases: `DecodingBaseConfig`

fieldacceptance_length_threshold:NonNegativeFloat|None=None#

The threshold for average acceptance length; speculation will be disabled permanently once the rolling average over the last N completed requests (N = acceptance_window) drops below this value. PyTorch backend only.

fieldacceptance_window:NonNegativeInt|None=None#

The rolling average window size (N) for acceptance length across completed requests. If not set or set to 0, the feature is disabled. PyTorch backend only.

fieldallow_advanced_sampling:bool=False#

If true, allows non-greedy sampling when speculation is used. Only applicable to 1-model code paths; non-greedy sampling is always enabled on 2-model paths.

fieldbegin_thinking_phase_token:int=128798#

Token ID marking start of thinking phase. Relaxed acceptance only applies within this phase.

fielddecoding_type:Literal['MTP']='MTP'#

fielddraft_len_schedule:dict[int,int]|None=None#

Developer interface: dynamically adjust draft length based on active batch size in runtime. Maps batch size to draft lengths. For example, {1: 4, 4: 2, 8: 0} means: batch_size >= 1 uses draft_len=4, batch_size >= 4 uses draft_len=2, batch_size >= 8 uses draft_len=0 (disable speculation). draft_len_schedule is enforced to contain batch_size=1 and its according draft_len equals max_draft_len for consistency; for example, if max_draft_len=4, the schedule must contain {1: 4}.

fieldend_thinking_phase_token:int=128799#

Token ID marking end of thinking phase. Strict acceptance resumes after this.

fieldload_format:str|None=None#

The load format of the speculative model.

fieldmax_concurrency:NonNegativeInt|None=None#

When specified, speculation will be disabled at batch sizes above this value. Otherwise, speculation will always be on. PyTorch backend only.

fieldmax_draft_len:NonNegativeInt|None=None#

The maximum number of draft tokens.

fieldmax_total_draft_tokens:int|None=None#

The number of draft tokens in the draft tokens tree. If it’s a linear tree, each draft layer will only generate one draft token. In this case, max_draft_len == max_total_draft_tokens. If it’s a static or dynamic tree, each draft layer may generate more than one draft token. In this case, max_total_draft_tokens >= max_draft_len.

fieldmtp_eagle_one_model:bool=True#

When using EAGLE-style MTP, use faster one-model implementation (drafter as submodule) vs two-model.

fieldnum_nextn_predict_layers:Annotated[int,Gt(gt=0)]=1#

Number of MTP modules. Each module predicts the next token, so N modules produce N draft tokens.

Constraints:

gt = 0

fieldnum_nextn_predict_layers_from_model_config:int=1#

Internal field storing MTP layer count from model config. Used to decide decoding mode: when model has 1 layer and use_mtp_vanilla=False, uses faster EAGLE-style MTP instead of vanilla MTP.

fieldrelaxed_delta:float=0.0#

Probability threshold for relaxed acceptance. Only candidates with prob >= (top-1 prob - delta) are kept.

fieldrelaxed_topk:int=1#

Number of top candidate tokens to consider for relaxed acceptance. Draft token is accepted if it matches any of these.

fieldsa_spec_threshold:Annotated[int,Gt(gt=0)]=4#

The threshold for the Suffix Automaton Decoding. If the length of the suffix match exceeds the threshold, use the suffix automaton output for the next draft tokens.

Constraints:

gt = 0

fieldspeculative_model:str|Path|None=None#

The speculative (draft) model. Accepts either (1) a HuggingFace Hub model ID (e.g. ‘yuhuili/EAGLE3-LLaMA3.1-Instruct-8B’), which will be automatically downloaded, or (2) a local filesystem path to a downloaded model directory.

fielduse_mtp_vanilla:bool=False#

Force vanilla MTP mode (sequential MTP layers). When False, uses EAGLE-style MTP for single-layer checkpoints.

fielduse_relaxed_acceptance_for_thinking:bool=False#

Enable relaxed acceptance during thinking phase for reasoning models. Accepts draft tokens matching any top-K candidate instead of exact top-1.

fielduse_sa_spec:bool|None=False#

Combine with Suffix Automaton Decoding

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(obj:Any)→Self#

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

validatorlog_two_model_deprecation_warning»allfields[source]#

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(context:Any, /)→None#

This function is meant to behave like a BaseModel method to initialise private attributes.

It takes context as an argument since that’s what pydantic-core passes when calling it.

Parameters:

self – The BaseModel instance.

context – The context.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(obj:Any)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

validatorset_max_total_draft_tokens»allfields[source]#

supports_backend(backend:str)→bool[source]#

Override if the speculation algorithm does not support
a subset of the possible backends.

classmethodupdate_forward_refs(**localns:Any)→None#

classmethodvalidate(value:Any)→Self#

validatorvalidate_draft_len_schedule_and_sort»draft_len_schedule#

Validate and sort draft_len_schedule by batch size thresholds.

propertyis_linear_tree:bool#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'acceptance_length_threshold':FieldInfo(annotation=Union[Annotated[float,Ge],NoneType],required=False,default=None,description='Thethresholdforaverageacceptancelength;speculationwillbedisabledpermanentlyoncetherollingaverageoverthelastNcompletedrequests(N=acceptance_window)dropsbelowthisvalue.PyTorchbackendonly.'),'acceptance_window':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Therollingaveragewindowsize(N)foracceptancelengthacrosscompletedrequests.Ifnotsetorsetto0,thefeatureisdisabled.PyTorchbackendonly.'),'allow_advanced_sampling':FieldInfo(annotation=bool,required=False,default=False,description='Iftrue,allowsnon-greedysamplingwhenspeculationisused.Onlyapplicableto1-modelcodepaths;non-greedysamplingisalwaysenabledon2-modelpaths.',json_schema_extra={'status':'prototype'}),'begin_thinking_phase_token':FieldInfo(annotation=int,required=False,default=128798,description='TokenIDmarkingstartofthinkingphase.Relaxedacceptanceonlyapplieswithinthisphase.'),'decoding_type':FieldInfo(annotation=Literal['MTP'],required=False,default='MTP'),'draft_len_schedule':FieldInfo(annotation=Union[dict[int,int],NoneType],required=False,default=None,description='Developerinterface:dynamicallyadjustdraftlengthbasedonactivebatchsizeinruntime.Mapsbatchsizetodraftlengths.Forexample,{1:4,4:2,8:0}means:batch_size>=1usesdraft_len=4,batch_size>=4usesdraft_len=2,batch_size>=8usesdraft_len=0(disablespeculation).draft_len_scheduleisenforcedtocontainbatch_size=1anditsaccordingdraft_lenequalsmax_draft_lenforconsistency;forexample,ifmax_draft_len=4,theschedulemustcontain{1:4}.'),'end_thinking_phase_token':FieldInfo(annotation=int,required=False,default=128799,description='TokenIDmarkingendofthinkingphase.Strictacceptanceresumesafterthis.'),'load_format':FieldInfo(annotation=Union[str,NoneType],required=False,default=None,description='Theloadformatofthespeculativemodel.'),'max_concurrency':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Whenspecified,speculationwillbedisabledatbatchsizesabovethisvalue.Otherwise,speculationwillalwaysbeon.PyTorchbackendonly.'),'max_draft_len':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Themaximumnumberofdrafttokens.'),'max_total_draft_tokens':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description="Thenumberofdrafttokensinthedrafttokenstree.Ifit'salineartree,eachdraftlayerwillonlygenerateonedrafttoken.Inthiscase,max_draft_len==max_total_draft_tokens.Ifit'sastaticordynamictree,eachdraftlayermaygeneratemorethanonedrafttoken.Inthiscase,max_total_draft_tokens>=max_draft_len."),'mtp_eagle_one_model':FieldInfo(annotation=bool,required=False,default=True,description='WhenusingEAGLE-styleMTP,usefasterone-modelimplementation(drafterassubmodule)vstwo-model.'),'num_nextn_predict_layers':FieldInfo(annotation=int,required=False,default=1,description='NumberofMTPmodules.Eachmodulepredictsthenexttoken,soNmodulesproduceNdrafttokens.',metadata=[Gt(gt=0)]),'num_nextn_predict_layers_from_model_config':FieldInfo(annotation=int,required=False,default=1,description='InternalfieldstoringMTPlayercountfrommodelconfig.Usedtodecidedecodingmode:whenmodelhas1layeranduse_mtp_vanilla=False,usesfasterEAGLE-styleMTPinsteadofvanillaMTP.',init=False),'relaxed_delta':FieldInfo(annotation=float,required=False,default=0.0,description='Probabilitythresholdforrelaxedacceptance.Onlycandidateswithprob>=(top-1prob-delta)arekept.'),'relaxed_topk':FieldInfo(annotation=int,required=False,default=1,description='Numberoftopcandidatetokenstoconsiderforrelaxedacceptance.Drafttokenisacceptedifitmatchesanyofthese.'),'sa_spec_threshold':FieldInfo(annotation=int,required=False,default=4,description='ThethresholdfortheSuffixAutomatonDecoding.Ifthelengthofthesuffixmatchexceedsthethreshold,usethesuffixautomatonoutputforthenextdrafttokens.',metadata=[Gt(gt=0)]),'speculative_model':FieldInfo(annotation=Union[str,Path,NoneType],required=False,default=None,alias_priority=2,validation_alias=AliasChoices(choices=['speculative_model','speculative_model_dir']),description="Thespeculative(draft)model.Acceptseither(1)aHuggingFaceHubmodelID(e.g.'yuhuili/EAGLE3-LLaMA3.1-Instruct-8B'),whichwillbeautomaticallydownloaded,or(2)alocalfilesystempathtoadownloadedmodeldirectory."),'use_mtp_vanilla':FieldInfo(annotation=bool,required=False,default=False,description='ForcevanillaMTPmode(sequentialMTPlayers).WhenFalse,usesEAGLE-styleMTPforsingle-layercheckpoints.'),'use_relaxed_acceptance_for_thinking':FieldInfo(annotation=bool,required=False,default=False,description='Enablerelaxedacceptanceduringthinkingphaseforreasoningmodels.Acceptsdrafttokensmatchinganytop-Kcandidateinsteadofexacttop-1.'),'use_sa_spec':FieldInfo(annotation=Union[bool,NoneType],required=False,default=False,description='CombinewithSuffixAutomatonDecoding',json_schema_extra={'status':'beta'})}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

propertynum_capture_layers:int#

propertyspec_dec_mode#

propertytokens_per_gen_step:int#

Total tokens per gen request in one spec dec iteration (including golden token).

classtensorrt_llm.llmapi.SchedulerConfig(

capacity_scheduler_policy:CapacitySchedulerPolicy=CapacitySchedulerPolicy.GUARANTEED_NO_EVICT,

context_chunking_policy:ContextChunkingPolicy|None=None,

dynamic_batch_config:DynamicBatchConfig|None=None,

waiting_queue_policy:WaitingQueuePolicy=WaitingQueuePolicy.FCFS,

use_python_scheduler:bool=False,

)[source]#

Bases: `StrictBaseModel`, `PybindMirror`

fieldcapacity_scheduler_policy:CapacitySchedulerPolicy=CapacitySchedulerPolicy.GUARANTEED_NO_EVICT#

The capacity scheduler policy to use

fieldcontext_chunking_policy:ContextChunkingPolicy|None=None#

The context chunking policy to use

fielddynamic_batch_config:DynamicBatchConfig|None=None#

The dynamic batch config to use. This only applies for the TensorRT backend and cannot currently be used with the PyTorch backend.

fielduse_python_scheduler:bool=False#

Use pure-Python scheduler instead of C++ scheduler.

fieldwaiting_queue_policy:WaitingQueuePolicy=WaitingQueuePolicy.FCFS#

The waiting queue scheduling policy

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(obj:Any)→Self#

classmethodfrom_pybind(

pybind_instance:PybindMirror,

)→T#

Construct an instance of the given class from the fields in the given
pybind class instance.

Parameters:

cls – Type of the class to construct, must be a subclass of pydantic
BaseModel

pybind_instance – Instance of the pybind class to construct from its
fields

Notes

When a field value is None in the pybind class, but it’s not
optional and has a default value in the BaseModel class, it would
get the default value defined in the BaseModel class.

Returns:

Instance of the given class, populated with the fields of the given
pybind instance

staticget_pybind_enum_fields(pybind_class)#

Get all the enum fields from the pybind class.

staticget_pybind_variable_fields(config_cls)#

Get all the variable fields from the pybind class.

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

staticmaybe_to_pybind(ins)#

staticmirror_pybind_enum(pybind_class)#

Mirror the enum fields from the pybind class to the Python class.

staticmirror_pybind_fields(pybind_class)#

Class decorator that ensures Python class fields mirror those of a C++ class.

Parameters:

pybind_class – The C++ class whose fields should be mirrored

Returns:

A decorator function that validates field mirroring

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(context:Any, /)→None#

Override this method to perform additional initialization after __init__ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(obj:Any)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

staticpybind_equals(obj0, obj1)#

Check if two pybind objects are equal.

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

classmethodupdate_forward_refs(**localns:Any)→None#

classmethodvalidate(value:Any)→Self#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'capacity_scheduler_policy':FieldInfo(annotation=CapacitySchedulerPolicy,required=False,default=<CapacitySchedulerPolicy.GUARANTEED_NO_EVICT:'GUARANTEED_NO_EVICT'>,description='Thecapacityschedulerpolicytouse'),'context_chunking_policy':FieldInfo(annotation=Union[ContextChunkingPolicy,NoneType],required=False,default=None,description='Thecontextchunkingpolicytouse'),'dynamic_batch_config':FieldInfo(annotation=Union[DynamicBatchConfig,NoneType],required=False,default=None,description='Thedynamicbatchconfigtouse.ThisonlyappliesfortheTensorRTbackendandcannotcurrentlybeusedwiththePyTorchbackend.'),'use_python_scheduler':FieldInfo(annotation=bool,required=False,default=False,description='Usepure-PythonschedulerinsteadofC++scheduler.'),'waiting_queue_policy':FieldInfo(annotation=WaitingQueuePolicy,required=False,default=<WaitingQueuePolicy.FCFS:'fcfs'>,description='Thewaitingqueueschedulingpolicy')}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

classtensorrt_llm.llmapi.CapacitySchedulerPolicy(

value,

names=<notgiven>,

*values,

module=None,

qualname=None,

type=None,

start=1,

boundary=None,

)[source]#

Bases: `StrEnum`

__init__(*args, **kwds)#

capitalize()#

Return a capitalized version of the string.

More specifically, make the first character have upper case and the rest lower
case.

casefold()#

Return a version of the string suitable for caseless comparisons.

center(width, fillchar='', /)#

Return a centered string of length width.

Padding is done using the specified fill character (default is a space).

count(sub[, start[, end]])→int#

Return the number of non-overlapping occurrences of substring sub in
string S[start:end]. Optional arguments start and end are
interpreted as in slice notation.

encode(encoding='utf-8', errors='strict')#

Encode the string using the codec registered for encoding.

encoding

The encoding in which to encode the string.

errors

The error handling scheme to use for encoding errors.
The default is ‘strict’ meaning that encoding errors raise a
UnicodeEncodeError. Other possible values are ‘ignore’, ‘replace’ and
‘xmlcharrefreplace’ as well as any other name registered with
codecs.register_error that can handle UnicodeEncodeErrors.

endswith(suffix[, start[, end]])→bool#

Return True if S ends with the specified suffix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
suffix can also be a tuple of strings to try.

expandtabs(tabsize=8)#

Return a copy where all tab characters are expanded using spaces.

If tabsize is not given, a tab size of 8 characters is assumed.

find(sub[, start[, end]])→int#

Return the lowest index in S where substring sub is found,
such that sub is contained within S[start:end]. Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure.

format(*args, **kwargs)→str#

Return a formatted version of S, using substitutions from args and kwargs.
The substitutions are identified by braces (‘{’ and ‘}’).

format_map(mapping)→str#

Return a formatted version of S, using substitutions from mapping.
The substitutions are identified by braces (‘{’ and ‘}’).

index(sub[, start[, end]])→int#

Return the lowest index in S where substring sub is found,
such that sub is contained within S[start:end]. Optional
arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

isalnum()#

Return True if the string is an alpha-numeric string, False otherwise.

A string is alpha-numeric if all characters in the string are alpha-numeric and
there is at least one character in the string.

isalpha()#

Return True if the string is an alphabetic string, False otherwise.

A string is alphabetic if all characters in the string are alphabetic and there
is at least one character in the string.

isascii()#

Return True if all characters in the string are ASCII, False otherwise.

ASCII characters have code points in the range U+0000-U+007F.
Empty string is ASCII too.

isdecimal()#

Return True if the string is a decimal string, False otherwise.

A string is a decimal string if all characters in the string are decimal and
there is at least one character in the string.

isdigit()#

Return True if the string is a digit string, False otherwise.

A string is a digit string if all characters in the string are digits and there
is at least one character in the string.

isidentifier()#

Return True if the string is a valid Python identifier, False otherwise.

Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
such as “def” or “class”.

islower()#

Return True if the string is a lowercase string, False otherwise.

A string is lowercase if all cased characters in the string are lowercase and
there is at least one cased character in the string.

isnumeric()#

Return True if the string is a numeric string, False otherwise.

A string is numeric if all characters in the string are numeric and there is at
least one character in the string.

isprintable()#

Return True if the string is printable, False otherwise.

A string is printable if all of its characters are considered printable in
repr() or if it is empty.

isspace()#

Return True if the string is a whitespace string, False otherwise.

A string is whitespace if all characters in the string are whitespace and there
is at least one character in the string.

istitle()#

Return True if the string is a title-cased string, False otherwise.

In a title-cased string, upper- and title-case characters may only
follow uncased characters and lowercase characters only cased ones.

isupper()#

Return True if the string is an uppercase string, False otherwise.

A string is uppercase if all cased characters in the string are uppercase and
there is at least one cased character in the string.

join(iterable, /)#

Concatenate any number of strings.

The string whose method is called is inserted in between each given string.
The result is returned as a new string.

Example: ‘.’.join([‘ab’, ‘pq’, ‘rs’]) -> ‘ab.pq.rs’

ljust(width, fillchar='', /)#

Return a left-justified string of length width.

Padding is done using the specified fill character (default is a space).

lower()#

Return a copy of the string converted to lowercase.

lstrip(chars=None, /)#

Return a copy of the string with leading whitespace removed.

If chars is given and not None, remove characters in chars instead.

staticmaketrans()#

Return a translation table usable for str.translate().

If there is only one argument, it must be a dictionary mapping Unicode
ordinals (integers) or characters to Unicode ordinals, strings or None.
Character keys will be then converted to ordinals.
If there are two arguments, they must be strings of equal length, and
in the resulting dictionary, each character in x will be mapped to the
character at the same position in y. If there is a third argument, it
must be a string, whose characters will be mapped to None in the result.

partition(sep, /)#

Partition the string into three parts using the given separator.

This will search for the separator in the string. If the separator is found,
returns a 3-tuple containing the part before the separator, the separator
itself, and the part after it.

If the separator is not found, returns a 3-tuple containing the original string
and two empty strings.

removeprefix(prefix, /)#

Return a str with the given prefix string removed if present.

If the string starts with the prefix string, return string[len(prefix):].
Otherwise, return a copy of the original string.

removesuffix(suffix, /)#

Return a str with the given suffix string removed if present.

If the string ends with the suffix string and that suffix is not empty,
return string[:-len(suffix)]. Otherwise, return a copy of the original
string.

replace(old, new, count=-1, /)#

Return a copy with all occurrences of substring old replaced by new.

count

Maximum number of occurrences to replace.
-1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are
replaced.

rfind(sub[, start[, end]])→int#

Return the highest index in S where substring sub is found,
such that sub is contained within S[start:end]. Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure.

rindex(sub[, start[, end]])→int#

Return the highest index in S where substring sub is found,
such that sub is contained within S[start:end]. Optional
arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

rjust(width, fillchar='', /)#

Return a right-justified string of length width.

Padding is done using the specified fill character (default is a space).

rpartition(sep, /)#

Partition the string into three parts using the given separator.

This will search for the separator in the string, starting at the end. If
the separator is found, returns a 3-tuple containing the part before the
separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing two empty strings
and the original string.

rsplit(sep=None, maxsplit=-1)#

Return a list of the substrings in the string, using sep as the separator string.

sep

The separator used to split the string.

When set to None (the default value), will split on any whitespace
character (including n r t f and spaces) and will discard
empty strings from the result.

maxsplit

Maximum number of splits.
-1 (the default value) means no limit.

Splitting starts at the end of the string and works to the front.

rstrip(chars=None, /)#

Return a copy of the string with trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

split(sep=None, maxsplit=-1)#

Return a list of the substrings in the string, using sep as the separator string.

sep

The separator used to split the string.

When set to None (the default value), will split on any whitespace
character (including n r t f and spaces) and will discard
empty strings from the result.

maxsplit

Maximum number of splits.
-1 (the default value) means no limit.

Splitting starts at the front of the string and works to the end.

Note, str.split() is mainly useful for data that has been intentionally
delimited. With natural text that includes punctuation, consider using
the regular expression module.

splitlines(keepends=False)#

Return a list of the lines in the string, breaking at line boundaries.

Line breaks are not included in the resulting list unless keepends is given and
true.

startswith(prefix[, start[, end]])→bool#

Return True if S starts with the specified prefix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
prefix can also be a tuple of strings to try.

strip(chars=None, /)#

Return a copy of the string with leading and trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

swapcase()#

Convert uppercase characters to lowercase and lowercase characters to uppercase.

title()#

Return a version of the string where each word is titlecased.

More specifically, words start with uppercased characters and all remaining
cased characters have lower case.

translate(table, /)#

Replace each character in the string using the given translation table.

table

Translation table, which must be a mapping of Unicode ordinals to
Unicode ordinals, strings, or None.

The table must implement lookup/indexing via __getitem__, for instance a
dictionary or list. If this operation raises LookupError, the character is
left untouched. Characters mapped to None are deleted.

upper()#

Return a copy of the string converted to uppercase.

zfill(width, /)#

Pad a numeric string with zeros on the left, to fill a field of the given width.

The string is never truncated.

GUARANTEED_NO_EVICT='GUARANTEED_NO_EVICT'#

MAX_UTILIZATION='MAX_UTILIZATION'#

STATIC_BATCH='STATIC_BATCH'#

classtensorrt_llm.llmapi.BuildConfig(

max_input_len:int=1024,

max_seq_len:int|None=None,

opt_batch_size:int=8,

max_batch_size:int=2048,

max_beam_width:int=1,

max_num_tokens:int=8192,

opt_num_tokens:int|None=None,

max_prompt_embedding_table_size:int=0,

kv_cache_type:~tensorrt_llm.llmapi.kv_cache_type.KVCacheType|None=None,

gather_context_logits:bool=False,

gather_generation_logits:bool=False,

strongly_typed:bool=True,

force_num_profiles:int|None=None,

profiling_verbosity:str='layer_names_only',

enable_debug_output:bool=False,

max_draft_len:int=0,

speculative_decoding_mode:~tensorrt_llm.models.modeling_utils.SpeculativeDecodingMode=<SpeculativeDecodingMode.NONE:1>,

use_refit:bool=False,

input_timing_cache:str|None=None,

output_timing_cache:str='model.cache',

lora_config:~tensorrt_llm.lora_helper.LoraConfig=<factory>,

weight_sparsity:bool=False,

weight_streaming:bool=False,

plugin_config:~tensorrt_llm.plugin.plugin.PluginConfig=<factory>,

use_strip_plan:bool=False,

max_encoder_input_len:int=1024,

dry_run:bool=False,

visualize_network:str|None=None,

monitor_memory:bool=False,

use_mrope:bool=False,

)[source]#

Bases: `StrictBaseModel`

Configuration class for TensorRT LLM engine building parameters.

This class contains all the configuration parameters needed to build a TensorRT LLM engine,
including sequence length limits, batch sizes, optimization settings, and various features.

fielddry_run:bool=False#

Whether to perform a dry run without actually building the engine.

fieldenable_debug_output:bool=False#

Whether to enable debug output during building.

fieldforce_num_profiles:int|None=None#

Force a specific number of optimization profiles. If None, auto-determined.

fieldgather_context_logits:bool=False#

Whether to gather logits during context phase.

fieldgather_generation_logits:bool=False#

Whether to gather logits during generation phase.

fieldinput_timing_cache:str|None=None#

Path to input timing cache file. If None, no input cache used.

fieldkv_cache_type:KVCacheType|None=None#

Type of KV cache to use (CONTINUOUS or PAGED). If None, defaults to PAGED.

fieldlora_config:LoraConfig[Optional]#

Configuration for LoRA (Low-Rank Adaptation) fine-tuning.

fieldmax_batch_size:int=2048#

Maximum batch size the engine can handle.

fieldmax_beam_width:int=1#

Maximum beam width for beam search decoding.

fieldmax_draft_len:int=0#

Maximum length of draft tokens for speculative decoding.

fieldmax_encoder_input_len:int=1024#

Maximum encoder input length for encoder-decoder models.

fieldmax_input_len:int=1024#

Maximum length of input sequences.

fieldmax_num_tokens:int=8192#

Maximum number of batched input tokens after padding is removed in each batch.

fieldmax_prompt_embedding_table_size:int=0#

Maximum size of prompt embedding table for prompt tuning.

fieldmax_seq_len:int|None=None#

The maximum possible sequence length for a single request, including both input and generated output tokens.

fieldmonitor_memory:bool=False#

Whether to monitor memory usage during building.

fieldopt_batch_size:int=8#

Optimal batch size for engine optimization.

fieldopt_num_tokens:int|None=None#

Optimal number of batched input tokens for engine optimization.

fieldoutput_timing_cache:str='model.cache'#

Path to output timing cache file.

fieldplugin_config:PluginConfig[Optional]#

Configuration for TensorRT LLM plugins.

fieldprofiling_verbosity:str='layer_names_only'#

Verbosity level for TensorRT profiling (‘layer_names_only’, ‘detailed’, ‘none’).

fieldspeculative_decoding_mode:SpeculativeDecodingMode=<SpeculativeDecodingMode.NONE:1>#

Mode for speculative decoding (NONE, MEDUSA, EAGLE, etc.).

fieldstrongly_typed:bool=True#

Whether to use strongly_typed.

fielduse_mrope:bool=False#

Whether to use Multi-RoPE (Rotary Position Embedding) optimization.

fielduse_refit:bool=False#

Whether to enable engine refitting capabilities.

fielduse_strip_plan:bool=False#

Whether to use stripped plan for engine building.

fieldvisualize_network:str|None=None#

Path to save network visualization. If None, no visualization generated.

fieldweight_sparsity:bool=False#

Whether to enable weight sparsity optimization.

fieldweight_streaming:bool=False#

Whether to enable weight streaming for large models.

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_json_file(config_file)[source]#

classmethodfrom_orm(obj:Any)→Self#

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(context:Any, /)→None#

Override this method to perform additional initialization after __init__ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(obj:Any)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

classmethodupdate_forward_refs(**localns:Any)→None#

update_kv_cache_type(model_architecture:str)[source]#

classmethodvalidate(value:Any)→Self#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'dry_run':FieldInfo(annotation=bool,required=False,default=False,description='Whethertoperformadryrunwithoutactuallybuildingtheengine.'),'enable_debug_output':FieldInfo(annotation=bool,required=False,default=False,description='Whethertoenabledebugoutputduringbuilding.'),'force_num_profiles':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description='Forceaspecificnumberofoptimizationprofiles.IfNone,auto-determined.'),'gather_context_logits':FieldInfo(annotation=bool,required=False,default=False,description='Whethertogatherlogitsduringcontextphase.'),'gather_generation_logits':FieldInfo(annotation=bool,required=False,default=False,description='Whethertogatherlogitsduringgenerationphase.'),'input_timing_cache':FieldInfo(annotation=Union[str,NoneType],required=False,default=None,description='Pathtoinputtimingcachefile.IfNone,noinputcacheused.'),'kv_cache_type':FieldInfo(annotation=Union[KVCacheType,NoneType],required=False,default=None,description='TypeofKVcachetouse(CONTINUOUSorPAGED).IfNone,defaultstoPAGED.'),'lora_config':FieldInfo(annotation=LoraConfig,required=False,default_factory=LoraConfig,description='ConfigurationforLoRA(Low-RankAdaptation)fine-tuning.'),'max_batch_size':FieldInfo(annotation=int,required=False,default=2048,description='Maximumbatchsizetheenginecanhandle.'),'max_beam_width':FieldInfo(annotation=int,required=False,default=1,description='Maximumbeamwidthforbeamsearchdecoding.'),'max_draft_len':FieldInfo(annotation=int,required=False,default=0,description='Maximumlengthofdrafttokensforspeculativedecoding.'),'max_encoder_input_len':FieldInfo(annotation=int,required=False,default=1024,description='Maximumencoderinputlengthforencoder-decodermodels.'),'max_input_len':FieldInfo(annotation=int,required=False,default=1024,description='Maximumlengthofinputsequences.'),'max_num_tokens':FieldInfo(annotation=int,required=False,default=8192,description='Maximumnumberofbatchedinputtokensafterpaddingisremovedineachbatch.'),'max_prompt_embedding_table_size':FieldInfo(annotation=int,required=False,default=0,description='Maximumsizeofpromptembeddingtableforprompttuning.'),'max_seq_len':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description='Themaximumpossiblesequencelengthforasinglerequest,includingbothinputandgeneratedoutputtokens.'),'monitor_memory':FieldInfo(annotation=bool,required=False,default=False,description='Whethertomonitormemoryusageduringbuilding.'),'opt_batch_size':FieldInfo(annotation=int,required=False,default=8,description='Optimalbatchsizeforengineoptimization.'),'opt_num_tokens':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description='Optimalnumberofbatchedinputtokensforengineoptimization.'),'output_timing_cache':FieldInfo(annotation=str,required=False,default='model.cache',description='Pathtooutputtimingcachefile.'),'plugin_config':FieldInfo(annotation=PluginConfig,required=False,default_factory=PluginConfig,description='ConfigurationforTensorRTLLMplugins.'),'profiling_verbosity':FieldInfo(annotation=str,required=False,default='layer_names_only',description="VerbositylevelforTensorRTprofiling('layer_names_only','detailed','none')."),'speculative_decoding_mode':FieldInfo(annotation=SpeculativeDecodingMode,required=False,default=<SpeculativeDecodingMode.NONE:1>,description='Modeforspeculativedecoding(NONE,MEDUSA,EAGLE,etc.).'),'strongly_typed':FieldInfo(annotation=bool,required=False,default=True,description='Whethertousestrongly_typed.'),'use_mrope':FieldInfo(annotation=bool,required=False,default=False,description='WhethertouseMulti-RoPE(RotaryPositionEmbedding)optimization.'),'use_refit':FieldInfo(annotation=bool,required=False,default=False,description='Whethertoenableenginerefittingcapabilities.'),'use_strip_plan':FieldInfo(annotation=bool,required=False,default=False,description='Whethertousestrippedplanforenginebuilding.'),'visualize_network':FieldInfo(annotation=Union[str,NoneType],required=False,default=None,description='Pathtosavenetworkvisualization.IfNone,novisualizationgenerated.'),'weight_sparsity':FieldInfo(annotation=bool,required=False,default=False,description='Whethertoenableweightsparsityoptimization.'),'weight_streaming':FieldInfo(annotation=bool,required=False,default=False,description='Whethertoenableweightstreamingforlargemodels.')}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

classtensorrt_llm.llmapi.QuantConfig(

quant_algo:QuantAlgo|None=None,

kv_cache_quant_algo:QuantAlgo|None=None,

group_size:int|None=128,

smoothquant_val:float=0.5,

clamp_val:List[float]|None=None,

use_meta_recipe:bool=False,

has_zero_point:bool=False,

pre_quant_scale:bool=False,

exclude_modules:List[str]|None=None,

mamba_ssm_cache_dtype:str|None=None,

)[source]#

Bases: `StrictBaseModel`

Serializable quantization configuration class, part of the PretrainedConfig.

fieldclamp_val:List[float]|None=None#

Clamp values used in FP8 rowwise quantization.

fieldexclude_modules:List[str]|None=None#

Module name patterns that are skipped in quantization.

fieldgroup_size:int|None=128#

Group size for group-wise quantization.

fieldhas_zero_point:bool=False#

Whether to use zero point for quantization.

fieldkv_cache_quant_algo:QuantAlgo|None=None#

KV cache quantization algorithm.

fieldmamba_ssm_cache_dtype:str|None=None#

Data type for mamba SSM cache.

fieldpre_quant_scale:bool=False#

Whether to use pre-quant scale for quantization.

fieldquant_algo:QuantAlgo|None=None#

Quantization algorithm.

fieldsmoothquant_val:float=0.5#

Smoothing parameter alpha used in smooth quant.

fielduse_meta_recipe:bool=False#

Whether to use Meta’s recipe for FP8 rowwise quantization.

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_dict(

config:dict,

)→QuantConfig[source]#

Create a QuantConfig instance from a dict.

Parameters:

config (dict) – The dict used to create QuantConfig.

Returns:

The QuantConfig created from dict.

Return type:

tensorrt_llm.models.modeling_utils.QuantConfig

classmethodfrom_orm(obj:Any)→Self#

is_module_excluded_from_quantization(name:str)→bool[source]#

Check if the module is excluded from quantization.

Parameters:

name (str) – The name of the module.

Returns:

True if the module is excluded from quantization, False otherwise.

Return type:

bool

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(context:Any, /)→None#

Override this method to perform additional initialization after __init__ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(obj:Any)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

classmethodupdate_forward_refs(**localns:Any)→None#

classmethodvalidate(value:Any)→Self#

propertylayer_quant_mode:QuantMode#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'clamp_val':FieldInfo(annotation=Union[List[float],NoneType],required=False,default=None,description='ClampvaluesusedinFP8rowwisequantization.'),'exclude_modules':FieldInfo(annotation=Union[List[str],NoneType],required=False,default=None,description='Modulenamepatternsthatareskippedinquantization.'),'group_size':FieldInfo(annotation=Union[int,NoneType],required=False,default=128,description='Groupsizeforgroup-wisequantization.'),'has_zero_point':FieldInfo(annotation=bool,required=False,default=False,description='Whethertousezeropointforquantization.'),'kv_cache_quant_algo':FieldInfo(annotation=Union[QuantAlgo,NoneType],required=False,default=None,description='KVcachequantizationalgorithm.'),'mamba_ssm_cache_dtype':FieldInfo(annotation=Union[str,NoneType],required=False,default=None,description='DatatypeformambaSSMcache.'),'pre_quant_scale':FieldInfo(annotation=bool,required=False,default=False,description='Whethertousepre-quantscaleforquantization.'),'quant_algo':FieldInfo(annotation=Union[QuantAlgo,NoneType],required=False,default=None,description='Quantizationalgorithm.'),'smoothquant_val':FieldInfo(annotation=float,required=False,default=0.5,description='Smoothingparameteralphausedinsmoothquant.'),'use_meta_recipe':FieldInfo(annotation=bool,required=False,default=False,description="WhethertouseMeta'srecipeforFP8rowwisequantization.")}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

propertyquant_mode:QuantModeWrapper#

classtensorrt_llm.llmapi.QuantAlgo(

value,

names=<notgiven>,

*values,

module=None,

qualname=None,

type=None,

start=1,

boundary=None,

)[source]#

Bases: `StrEnum`

__init__(*args, **kwds)#

capitalize()#

Return a capitalized version of the string.

More specifically, make the first character have upper case and the rest lower
case.

casefold()#

Return a version of the string suitable for caseless comparisons.

center(width, fillchar='', /)#

Return a centered string of length width.

Padding is done using the specified fill character (default is a space).

count(sub[, start[, end]])→int#

Return the number of non-overlapping occurrences of substring sub in
string S[start:end]. Optional arguments start and end are
interpreted as in slice notation.

encode(encoding='utf-8', errors='strict')#

Encode the string using the codec registered for encoding.

encoding

The encoding in which to encode the string.

errors

The error handling scheme to use for encoding errors.
The default is ‘strict’ meaning that encoding errors raise a
UnicodeEncodeError. Other possible values are ‘ignore’, ‘replace’ and
‘xmlcharrefreplace’ as well as any other name registered with
codecs.register_error that can handle UnicodeEncodeErrors.

endswith(suffix[, start[, end]])→bool#

Return True if S ends with the specified suffix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
suffix can also be a tuple of strings to try.

expandtabs(tabsize=8)#

Return a copy where all tab characters are expanded using spaces.

If tabsize is not given, a tab size of 8 characters is assumed.

find(sub[, start[, end]])→int#

Return the lowest index in S where substring sub is found,
such that sub is contained within S[start:end]. Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure.

format(*args, **kwargs)→str#

Return a formatted version of S, using substitutions from args and kwargs.
The substitutions are identified by braces (‘{’ and ‘}’).

format_map(mapping)→str#

Return a formatted version of S, using substitutions from mapping.
The substitutions are identified by braces (‘{’ and ‘}’).

index(sub[, start[, end]])→int#

Return the lowest index in S where substring sub is found,
such that sub is contained within S[start:end]. Optional
arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

isalnum()#

Return True if the string is an alpha-numeric string, False otherwise.

A string is alpha-numeric if all characters in the string are alpha-numeric and
there is at least one character in the string.

isalpha()#

Return True if the string is an alphabetic string, False otherwise.

A string is alphabetic if all characters in the string are alphabetic and there
is at least one character in the string.

isascii()#

Return True if all characters in the string are ASCII, False otherwise.

ASCII characters have code points in the range U+0000-U+007F.
Empty string is ASCII too.

isdecimal()#

Return True if the string is a decimal string, False otherwise.

A string is a decimal string if all characters in the string are decimal and
there is at least one character in the string.

isdigit()#

Return True if the string is a digit string, False otherwise.

A string is a digit string if all characters in the string are digits and there
is at least one character in the string.

isidentifier()#

Return True if the string is a valid Python identifier, False otherwise.

Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
such as “def” or “class”.

islower()#

Return True if the string is a lowercase string, False otherwise.

A string is lowercase if all cased characters in the string are lowercase and
there is at least one cased character in the string.

isnumeric()#

Return True if the string is a numeric string, False otherwise.

A string is numeric if all characters in the string are numeric and there is at
least one character in the string.

isprintable()#

Return True if the string is printable, False otherwise.

A string is printable if all of its characters are considered printable in
repr() or if it is empty.

isspace()#

Return True if the string is a whitespace string, False otherwise.

A string is whitespace if all characters in the string are whitespace and there
is at least one character in the string.

istitle()#

Return True if the string is a title-cased string, False otherwise.

In a title-cased string, upper- and title-case characters may only
follow uncased characters and lowercase characters only cased ones.

isupper()#

Return True if the string is an uppercase string, False otherwise.

A string is uppercase if all cased characters in the string are uppercase and
there is at least one cased character in the string.

join(iterable, /)#

Concatenate any number of strings.

The string whose method is called is inserted in between each given string.
The result is returned as a new string.

Example: ‘.’.join([‘ab’, ‘pq’, ‘rs’]) -> ‘ab.pq.rs’

ljust(width, fillchar='', /)#

Return a left-justified string of length width.

Padding is done using the specified fill character (default is a space).

lower()#

Return a copy of the string converted to lowercase.

lstrip(chars=None, /)#

Return a copy of the string with leading whitespace removed.

If chars is given and not None, remove characters in chars instead.

staticmaketrans()#

Return a translation table usable for str.translate().

If there is only one argument, it must be a dictionary mapping Unicode
ordinals (integers) or characters to Unicode ordinals, strings or None.
Character keys will be then converted to ordinals.
If there are two arguments, they must be strings of equal length, and
in the resulting dictionary, each character in x will be mapped to the
character at the same position in y. If there is a third argument, it
must be a string, whose characters will be mapped to None in the result.

partition(sep, /)#

Partition the string into three parts using the given separator.

This will search for the separator in the string. If the separator is found,
returns a 3-tuple containing the part before the separator, the separator
itself, and the part after it.

If the separator is not found, returns a 3-tuple containing the original string
and two empty strings.

removeprefix(prefix, /)#

Return a str with the given prefix string removed if present.

If the string starts with the prefix string, return string[len(prefix):].
Otherwise, return a copy of the original string.

removesuffix(suffix, /)#

Return a str with the given suffix string removed if present.

If the string ends with the suffix string and that suffix is not empty,
return string[:-len(suffix)]. Otherwise, return a copy of the original
string.

replace(old, new, count=-1, /)#

Return a copy with all occurrences of substring old replaced by new.

count

Maximum number of occurrences to replace.
-1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are
replaced.

rfind(sub[, start[, end]])→int#

Return the highest index in S where substring sub is found,
such that sub is contained within S[start:end]. Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure.

rindex(sub[, start[, end]])→int#

Return the highest index in S where substring sub is found,
such that sub is contained within S[start:end]. Optional
arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

rjust(width, fillchar='', /)#

Return a right-justified string of length width.

Padding is done using the specified fill character (default is a space).

rpartition(sep, /)#

Partition the string into three parts using the given separator.

This will search for the separator in the string, starting at the end. If
the separator is found, returns a 3-tuple containing the part before the
separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing two empty strings
and the original string.

rsplit(sep=None, maxsplit=-1)#

Return a list of the substrings in the string, using sep as the separator string.

sep

The separator used to split the string.

When set to None (the default value), will split on any whitespace
character (including n r t f and spaces) and will discard
empty strings from the result.

maxsplit

Maximum number of splits.
-1 (the default value) means no limit.

Splitting starts at the end of the string and works to the front.

rstrip(chars=None, /)#

Return a copy of the string with trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

split(sep=None, maxsplit=-1)#

Return a list of the substrings in the string, using sep as the separator string.

sep

The separator used to split the string.

When set to None (the default value), will split on any whitespace
character (including n r t f and spaces) and will discard
empty strings from the result.

maxsplit

Maximum number of splits.
-1 (the default value) means no limit.

Splitting starts at the front of the string and works to the end.

Note, str.split() is mainly useful for data that has been intentionally
delimited. With natural text that includes punctuation, consider using
the regular expression module.

splitlines(keepends=False)#

Return a list of the lines in the string, breaking at line boundaries.

Line breaks are not included in the resulting list unless keepends is given and
true.

startswith(prefix[, start[, end]])→bool#

Return True if S starts with the specified prefix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
prefix can also be a tuple of strings to try.

strip(chars=None, /)#

Return a copy of the string with leading and trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

swapcase()#

Convert uppercase characters to lowercase and lowercase characters to uppercase.

title()#

Return a version of the string where each word is titlecased.

More specifically, words start with uppercased characters and all remaining
cased characters have lower case.

translate(table, /)#

Replace each character in the string using the given translation table.

table

Translation table, which must be a mapping of Unicode ordinals to
Unicode ordinals, strings, or None.

The table must implement lookup/indexing via __getitem__, for instance a
dictionary or list. If this operation raises LookupError, the character is
left untouched. Characters mapped to None are deleted.

upper()#

Return a copy of the string converted to uppercase.

zfill(width, /)#

Pad a numeric string with zeros on the left, to fill a field of the given width.

The string is never truncated.

FP8='FP8'#

FP8_BLOCK_SCALES='FP8_BLOCK_SCALES'#

FP8_PER_CHANNEL_PER_TOKEN='FP8_PER_CHANNEL_PER_TOKEN'#

INT8='INT8'#

MIXED_PRECISION='MIXED_PRECISION'#

NO_QUANT='NO_QUANT'#

NVFP4='NVFP4'#

NVFP4_AWQ='NVFP4_AWQ'#

W4A16='W4A16'#

W4A16_AWQ='W4A16_AWQ'#

W4A16_GPTQ='W4A16_GPTQ'#

W4A16_MXFP4='W4A16_MXFP4'#

W4A8_AWQ='W4A8_AWQ'#

W4A8_MXFP4_FP8='W4A8_MXFP4_FP8'#

W4A8_MXFP4_MXFP8='W4A8_MXFP4_MXFP8'#

W4A8_NVFP4_FP8='W4A8_NVFP4_FP8'#

W4A8_QSERVE_PER_CHANNEL='W4A8_QSERVE_PER_CHANNEL'#

W4A8_QSERVE_PER_GROUP='W4A8_QSERVE_PER_GROUP'#

W8A16='W8A16'#

W8A16_GPTQ='W8A16_GPTQ'#

W8A8_SQ_PER_CHANNEL='W8A8_SQ_PER_CHANNEL'#

W8A8_SQ_PER_CHANNEL_PER_TENSOR_PLUGIN='W8A8_SQ_PER_CHANNEL_PER_TENSOR_PLUGIN'#

W8A8_SQ_PER_CHANNEL_PER_TOKEN_PLUGIN='W8A8_SQ_PER_CHANNEL_PER_TOKEN_PLUGIN'#

W8A8_SQ_PER_TENSOR_PER_TOKEN_PLUGIN='W8A8_SQ_PER_TENSOR_PER_TOKEN_PLUGIN'#

W8A8_SQ_PER_TENSOR_PLUGIN='W8A8_SQ_PER_TENSOR_PLUGIN'#

classtensorrt_llm.llmapi.CalibConfig(

device:Literal['cuda','cpu']='cuda',

calib_dataset:str='cnn_dailymail',

calib_batches:int=512,

calib_batch_size:int=1,

calib_max_seq_length:int=512,

random_seed:int=1234,

tokenizer_max_seq_length:int=2048,

)[source]#

Bases: `StrictBaseModel`

Calibration configuration.

fieldcalib_batch_size:int=1#

The batch size that the calibration runs.

fieldcalib_batches:int=512#

The number of batches that the calibration runs.

fieldcalib_dataset:str='cnn_dailymail'#

The name or local path of calibration dataset.

fieldcalib_max_seq_length:int=512#

The maximum sequence length that the calibration runs.

fielddevice:Literal['cuda','cpu']='cuda'#

The device to run calibration.

fieldrandom_seed:int=1234#

The random seed used for calibration.

fieldtokenizer_max_seq_length:int=2048#

The maximum sequence length to initialize tokenizer for calibration.

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(obj:Any)→Self#

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(context:Any, /)→None#

Override this method to perform additional initialization after __init__ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(obj:Any)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

classmethodupdate_forward_refs(**localns:Any)→None#

classmethodvalidate(value:Any)→Self#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'calib_batch_size':FieldInfo(annotation=int,required=False,default=1,description='Thebatchsizethatthecalibrationruns.'),'calib_batches':FieldInfo(annotation=int,required=False,default=512,description='Thenumberofbatchesthatthecalibrationruns.'),'calib_dataset':FieldInfo(annotation=str,required=False,default='cnn_dailymail',description='Thenameorlocalpathofcalibrationdataset.'),'calib_max_seq_length':FieldInfo(annotation=int,required=False,default=512,description='Themaximumsequencelengththatthecalibrationruns.'),'device':FieldInfo(annotation=Literal['cuda','cpu'],required=False,default='cuda',description='Thedevicetoruncalibration.'),'random_seed':FieldInfo(annotation=int,required=False,default=1234,description='Therandomseedusedforcalibration.'),'tokenizer_max_seq_length':FieldInfo(annotation=int,required=False,default=2048,description='Themaximumsequencelengthtoinitializetokenizerforcalibration.')}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

classtensorrt_llm.llmapi.BuildCacheConfig(

cache_root:Path|None=None,

max_records:Annotated[int,Gt(gt=0)]=10,

max_cache_storage_gb:float=256.0,

)[source]#

Bases: `StrictBaseModel`

Configuration for the build cache.

Note

The build-cache assumes the weights of the model are not changed during the execution. If the weights are
changed, you should remove the caches manually.

fieldcache_root:Path|None=None#

The root directory for the build cache. Falls back to env var if not provided.

fieldmax_cache_storage_gb:float=256.0#

The maximum amount of storage (in GB) to use for the cache.

fieldmax_records:int=10#

The maximum number of records to store in the cache.

Constraints:

gt = 0

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(obj:Any)→Self#

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(context:Any, /)→None#

Override this method to perform additional initialization after __init__ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(obj:Any)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

validatorset_default_cache_root»allfields[source]#

Set cache_root from environment variable if not provided.

classmethodupdate_forward_refs(**localns:Any)→None#

classmethodvalidate(value:Any)→Self#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'cache_root':FieldInfo(annotation=Union[Path,NoneType],required=False,default=None,description='Therootdirectoryforthebuildcache.Fallsbacktoenvvarifnotprovided.'),'max_cache_storage_gb':FieldInfo(annotation=float,required=False,default=256.0,description='Themaximumamountofstorage(inGB)touseforthecache.'),'max_records':FieldInfo(annotation=int,required=False,default=10,description='Themaximumnumberofrecordstostoreinthecache.',metadata=[Gt(gt=0)])}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

classtensorrt_llm.llmapi.RequestError[source]#

Bases: `RuntimeError`

The error raised when the request is failed.

__init__(*args, **kwargs)#

add_note()#

Exception.add_note(note) –
add a note to the exception

with_traceback()#

Exception.with_traceback(tb) –
set self.__traceback__ to tb and return self.

args#

classtensorrt_llm.llmapi.MpiCommSession(comm=None, n_workers:int=1)[source]#

Bases: `MpiSession`

__init__(comm=None, n_workers:int=1)[source]#

abort()[source]#

get_comm()[source]#

is_comm_session()→bool#

shutdown(wait=True)[source]#

shutdown_abort(grace:float=60, reason=None)#

submit(

task:Callable[[...],T],

*args,

**kwargs,

)→List[Future[T]][source]#

Submit a task to MPI workers.

Parameters:

task – The task to be submitted.

args – Positional arguments for the task.

kwargs – Keyword arguments for the task.

submit_sync(

task:Callable[[...],T],

*args,

**kwargs,

)→List[T][source]#

classtensorrt_llm.llmapi.ExtendedRuntimePerfKnobConfig(

multi_block_mode:bool=True,

enable_context_fmha_fp32_acc:bool=False,

cuda_graph_mode:bool=False,

cuda_graph_cache_size:int=0,

)[source]#

Bases: `StrictBaseModel`, `PybindMirror`

Configuration for extended runtime performance knobs.

fieldcuda_graph_cache_size:int=0#

Number of cuda graphs to be cached in the runtime. The larger the cache, the better the perf, but more GPU memory is consumed.

fieldcuda_graph_mode:bool=False#

Whether to use CUDA graph mode.

fieldenable_context_fmha_fp32_acc:bool=False#

Whether to enable context FMHA FP32 accumulation.

fieldmulti_block_mode:bool=True#

Whether to use multi-block mode.

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(

obj:Any,

)→Self#

classmethodfrom_pybind(

pybind_instance:PybindMirror,

)→T#

Construct an instance of the given class from the fields in the given
pybind class instance.

Parameters:

cls – Type of the class to construct, must be a subclass of pydantic
BaseModel

pybind_instance – Instance of the pybind class to construct from its
fields

Notes

When a field value is None in the pybind class, but it’s not
optional and has a default value in the BaseModel class, it would
get the default value defined in the BaseModel class.

Returns:

Instance of the given class, populated with the fields of the given
pybind instance

staticget_pybind_enum_fields(pybind_class)#

Get all the enum fields from the pybind class.

staticget_pybind_variable_fields(config_cls)#

Get all the variable fields from the pybind class.

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

staticmaybe_to_pybind(ins)#

staticmirror_pybind_enum(pybind_class)#

Mirror the enum fields from the pybind class to the Python class.

staticmirror_pybind_fields(pybind_class)#

Class decorator that ensures Python class fields mirror those of a C++ class.

Parameters:

pybind_class – The C++ class whose fields should be mirrored

Returns:

A decorator function that validates field mirroring

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(

context:Any,

)→None#

Override this method to perform additional initialization after __init__ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(

obj:Any,

)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

staticpybind_equals(obj0, obj1)#

Check if two pybind objects are equal.

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

classmethodupdate_forward_refs(

**localns:Any,

)→None#

classmethodvalidate(

value:Any,

)→Self#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'cuda_graph_cache_size':FieldInfo(annotation=int,required=False,default=0,description='Numberofcudagraphstobecachedintheruntime.Thelargerthecache,thebettertheperf,butmoreGPUmemoryisconsumed.'),'cuda_graph_mode':FieldInfo(annotation=bool,required=False,default=False,description='WhethertouseCUDAgraphmode.'),'enable_context_fmha_fp32_acc':FieldInfo(annotation=bool,required=False,default=False,description='WhethertoenablecontextFMHAFP32accumulation.'),'multi_block_mode':FieldInfo(annotation=bool,required=False,default=True,description='Whethertousemulti-blockmode.')}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

classtensorrt_llm.llmapi.BatchingType(

value,

names=<notgiven>,

*values,

module=None,

qualname=None,

type=None,

start=1,

boundary=None,

)[source]#

Bases: `StrEnum`

__init__(*args, **kwds)#

capitalize()#

Return a capitalized version of the string.

More specifically, make the first character have upper case and the rest lower
case.

casefold()#

Return a version of the string suitable for caseless comparisons.

center(width, fillchar='', /)#

Return a centered string of length width.

Padding is done using the specified fill character (default is a space).

count(sub[, start[, end]])→int#

Return the number of non-overlapping occurrences of substring sub in
string S[start:end]. Optional arguments start and end are
interpreted as in slice notation.

encode(encoding='utf-8', errors='strict')#

Encode the string using the codec registered for encoding.

encoding

The encoding in which to encode the string.

errors

The error handling scheme to use for encoding errors.
The default is ‘strict’ meaning that encoding errors raise a
UnicodeEncodeError. Other possible values are ‘ignore’, ‘replace’ and
‘xmlcharrefreplace’ as well as any other name registered with
codecs.register_error that can handle UnicodeEncodeErrors.

endswith(suffix[, start[, end]])→bool#

Return True if S ends with the specified suffix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
suffix can also be a tuple of strings to try.

expandtabs(tabsize=8)#

Return a copy where all tab characters are expanded using spaces.

If tabsize is not given, a tab size of 8 characters is assumed.

find(sub[, start[, end]])→int#

Return the lowest index in S where substring sub is found,
such that sub is contained within S[start:end]. Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure.

format(*args, **kwargs)→str#

Return a formatted version of S, using substitutions from args and kwargs.
The substitutions are identified by braces (‘{’ and ‘}’).

format_map(mapping)→str#

Return a formatted version of S, using substitutions from mapping.
The substitutions are identified by braces (‘{’ and ‘}’).

index(sub[, start[, end]])→int#

Return the lowest index in S where substring sub is found,
such that sub is contained within S[start:end]. Optional
arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

isalnum()#

Return True if the string is an alpha-numeric string, False otherwise.

A string is alpha-numeric if all characters in the string are alpha-numeric and
there is at least one character in the string.

isalpha()#

Return True if the string is an alphabetic string, False otherwise.

A string is alphabetic if all characters in the string are alphabetic and there
is at least one character in the string.

isascii()#

Return True if all characters in the string are ASCII, False otherwise.

ASCII characters have code points in the range U+0000-U+007F.
Empty string is ASCII too.

isdecimal()#

Return True if the string is a decimal string, False otherwise.

A string is a decimal string if all characters in the string are decimal and
there is at least one character in the string.

isdigit()#

Return True if the string is a digit string, False otherwise.

A string is a digit string if all characters in the string are digits and there
is at least one character in the string.

isidentifier()#

Return True if the string is a valid Python identifier, False otherwise.

Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
such as “def” or “class”.

islower()#

Return True if the string is a lowercase string, False otherwise.

A string is lowercase if all cased characters in the string are lowercase and
there is at least one cased character in the string.

isnumeric()#

Return True if the string is a numeric string, False otherwise.

A string is numeric if all characters in the string are numeric and there is at
least one character in the string.

isprintable()#

Return True if the string is printable, False otherwise.

A string is printable if all of its characters are considered printable in
repr() or if it is empty.

isspace()#

Return True if the string is a whitespace string, False otherwise.

A string is whitespace if all characters in the string are whitespace and there
is at least one character in the string.

istitle()#

Return True if the string is a title-cased string, False otherwise.

In a title-cased string, upper- and title-case characters may only
follow uncased characters and lowercase characters only cased ones.

isupper()#

Return True if the string is an uppercase string, False otherwise.

A string is uppercase if all cased characters in the string are uppercase and
there is at least one cased character in the string.

join(iterable, /)#

Concatenate any number of strings.

The string whose method is called is inserted in between each given string.
The result is returned as a new string.

Example: ‘.’.join([‘ab’, ‘pq’, ‘rs’]) -> ‘ab.pq.rs’

ljust(width, fillchar='', /)#

Return a left-justified string of length width.

Padding is done using the specified fill character (default is a space).

lower()#

Return a copy of the string converted to lowercase.

lstrip(chars=None, /)#

Return a copy of the string with leading whitespace removed.

If chars is given and not None, remove characters in chars instead.

staticmaketrans()#

Return a translation table usable for str.translate().

If there is only one argument, it must be a dictionary mapping Unicode
ordinals (integers) or characters to Unicode ordinals, strings or None.
Character keys will be then converted to ordinals.
If there are two arguments, they must be strings of equal length, and
in the resulting dictionary, each character in x will be mapped to the
character at the same position in y. If there is a third argument, it
must be a string, whose characters will be mapped to None in the result.

partition(sep, /)#

Partition the string into three parts using the given separator.

This will search for the separator in the string. If the separator is found,
returns a 3-tuple containing the part before the separator, the separator
itself, and the part after it.

If the separator is not found, returns a 3-tuple containing the original string
and two empty strings.

removeprefix(prefix, /)#

Return a str with the given prefix string removed if present.

If the string starts with the prefix string, return string[len(prefix):].
Otherwise, return a copy of the original string.

removesuffix(suffix, /)#

Return a str with the given suffix string removed if present.

If the string ends with the suffix string and that suffix is not empty,
return string[:-len(suffix)]. Otherwise, return a copy of the original
string.

replace(old, new, count=-1, /)#

Return a copy with all occurrences of substring old replaced by new.

count

Maximum number of occurrences to replace.
-1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are
replaced.

rfind(sub[, start[, end]])→int#

Return the highest index in S where substring sub is found,
such that sub is contained within S[start:end]. Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure.

rindex(sub[, start[, end]])→int#

Return the highest index in S where substring sub is found,
such that sub is contained within S[start:end]. Optional
arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

rjust(width, fillchar='', /)#

Return a right-justified string of length width.

Padding is done using the specified fill character (default is a space).

rpartition(sep, /)#

Partition the string into three parts using the given separator.

This will search for the separator in the string, starting at the end. If
the separator is found, returns a 3-tuple containing the part before the
separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing two empty strings
and the original string.

rsplit(sep=None, maxsplit=-1)#

Return a list of the substrings in the string, using sep as the separator string.

sep

The separator used to split the string.

When set to None (the default value), will split on any whitespace
character (including n r t f and spaces) and will discard
empty strings from the result.

maxsplit

Maximum number of splits.
-1 (the default value) means no limit.

Splitting starts at the end of the string and works to the front.

rstrip(chars=None, /)#

Return a copy of the string with trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

split(sep=None, maxsplit=-1)#

Return a list of the substrings in the string, using sep as the separator string.

sep

The separator used to split the string.

When set to None (the default value), will split on any whitespace
character (including n r t f and spaces) and will discard
empty strings from the result.

maxsplit

Maximum number of splits.
-1 (the default value) means no limit.

Splitting starts at the front of the string and works to the end.

Note, str.split() is mainly useful for data that has been intentionally
delimited. With natural text that includes punctuation, consider using
the regular expression module.

splitlines(keepends=False)#

Return a list of the lines in the string, breaking at line boundaries.

Line breaks are not included in the resulting list unless keepends is given and
true.

startswith(prefix[, start[, end]])→bool#

Return True if S starts with the specified prefix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
prefix can also be a tuple of strings to try.

strip(chars=None, /)#

Return a copy of the string with leading and trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

swapcase()#

Convert uppercase characters to lowercase and lowercase characters to uppercase.

title()#

Return a version of the string where each word is titlecased.

More specifically, words start with uppercased characters and all remaining
cased characters have lower case.

translate(table, /)#

Replace each character in the string using the given translation table.

table

Translation table, which must be a mapping of Unicode ordinals to
Unicode ordinals, strings, or None.

The table must implement lookup/indexing via __getitem__, for instance a
dictionary or list. If this operation raises LookupError, the character is
left untouched. Characters mapped to None are deleted.

upper()#

Return a copy of the string converted to uppercase.

zfill(width, /)#

Pad a numeric string with zeros on the left, to fill a field of the given width.

The string is never truncated.

INFLIGHT='INFLIGHT'#

STATIC='STATIC'#

classtensorrt_llm.llmapi.ContextChunkingPolicy(

value,

names=<notgiven>,

*values,

module=None,

qualname=None,

type=None,

start=1,

boundary=None,

)[source]#

Bases: `StrEnum`

Context chunking policy.

__init__(*args, **kwds)#

capitalize()#

Return a capitalized version of the string.

More specifically, make the first character have upper case and the rest lower
case.

casefold()#

Return a version of the string suitable for caseless comparisons.

center(width, fillchar='', /)#

Return a centered string of length width.

Padding is done using the specified fill character (default is a space).

count(sub[, start[, end]])→int#

Return the number of non-overlapping occurrences of substring sub in
string S[start:end]. Optional arguments start and end are
interpreted as in slice notation.

encode(encoding='utf-8', errors='strict')#

Encode the string using the codec registered for encoding.

encoding

The encoding in which to encode the string.

errors

The error handling scheme to use for encoding errors.
The default is ‘strict’ meaning that encoding errors raise a
UnicodeEncodeError. Other possible values are ‘ignore’, ‘replace’ and
‘xmlcharrefreplace’ as well as any other name registered with
codecs.register_error that can handle UnicodeEncodeErrors.

endswith(suffix[, start[, end]])→bool#

Return True if S ends with the specified suffix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
suffix can also be a tuple of strings to try.

expandtabs(tabsize=8)#

Return a copy where all tab characters are expanded using spaces.

If tabsize is not given, a tab size of 8 characters is assumed.

find(sub[, start[, end]])→int#

Return the lowest index in S where substring sub is found,
such that sub is contained within S[start:end]. Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure.

format(*args, **kwargs)→str#

Return a formatted version of S, using substitutions from args and kwargs.
The substitutions are identified by braces (‘{’ and ‘}’).

format_map(mapping)→str#

Return a formatted version of S, using substitutions from mapping.
The substitutions are identified by braces (‘{’ and ‘}’).

index(sub[, start[, end]])→int#

Return the lowest index in S where substring sub is found,
such that sub is contained within S[start:end]. Optional
arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

isalnum()#

Return True if the string is an alpha-numeric string, False otherwise.

A string is alpha-numeric if all characters in the string are alpha-numeric and
there is at least one character in the string.

isalpha()#

Return True if the string is an alphabetic string, False otherwise.

A string is alphabetic if all characters in the string are alphabetic and there
is at least one character in the string.

isascii()#

Return True if all characters in the string are ASCII, False otherwise.

ASCII characters have code points in the range U+0000-U+007F.
Empty string is ASCII too.

isdecimal()#

Return True if the string is a decimal string, False otherwise.

A string is a decimal string if all characters in the string are decimal and
there is at least one character in the string.

isdigit()#

Return True if the string is a digit string, False otherwise.

A string is a digit string if all characters in the string are digits and there
is at least one character in the string.

isidentifier()#

Return True if the string is a valid Python identifier, False otherwise.

Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
such as “def” or “class”.

islower()#

Return True if the string is a lowercase string, False otherwise.

A string is lowercase if all cased characters in the string are lowercase and
there is at least one cased character in the string.

isnumeric()#

Return True if the string is a numeric string, False otherwise.

A string is numeric if all characters in the string are numeric and there is at
least one character in the string.

isprintable()#

Return True if the string is printable, False otherwise.

A string is printable if all of its characters are considered printable in
repr() or if it is empty.

isspace()#

Return True if the string is a whitespace string, False otherwise.

A string is whitespace if all characters in the string are whitespace and there
is at least one character in the string.

istitle()#

Return True if the string is a title-cased string, False otherwise.

In a title-cased string, upper- and title-case characters may only
follow uncased characters and lowercase characters only cased ones.

isupper()#

Return True if the string is an uppercase string, False otherwise.

A string is uppercase if all cased characters in the string are uppercase and
there is at least one cased character in the string.

join(iterable, /)#

Concatenate any number of strings.

The string whose method is called is inserted in between each given string.
The result is returned as a new string.

Example: ‘.’.join([‘ab’, ‘pq’, ‘rs’]) -> ‘ab.pq.rs’

ljust(width, fillchar='', /)#

Return a left-justified string of length width.

Padding is done using the specified fill character (default is a space).

lower()#

Return a copy of the string converted to lowercase.

lstrip(chars=None, /)#

Return a copy of the string with leading whitespace removed.

If chars is given and not None, remove characters in chars instead.

staticmaketrans()#

Return a translation table usable for str.translate().

If there is only one argument, it must be a dictionary mapping Unicode
ordinals (integers) or characters to Unicode ordinals, strings or None.
Character keys will be then converted to ordinals.
If there are two arguments, they must be strings of equal length, and
in the resulting dictionary, each character in x will be mapped to the
character at the same position in y. If there is a third argument, it
must be a string, whose characters will be mapped to None in the result.

partition(sep, /)#

Partition the string into three parts using the given separator.

This will search for the separator in the string. If the separator is found,
returns a 3-tuple containing the part before the separator, the separator
itself, and the part after it.

If the separator is not found, returns a 3-tuple containing the original string
and two empty strings.

removeprefix(prefix, /)#

Return a str with the given prefix string removed if present.

If the string starts with the prefix string, return string[len(prefix):].
Otherwise, return a copy of the original string.

removesuffix(suffix, /)#

Return a str with the given suffix string removed if present.

If the string ends with the suffix string and that suffix is not empty,
return string[:-len(suffix)]. Otherwise, return a copy of the original
string.

replace(old, new, count=-1, /)#

Return a copy with all occurrences of substring old replaced by new.

count

Maximum number of occurrences to replace.
-1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are
replaced.

rfind(sub[, start[, end]])→int#

Return the highest index in S where substring sub is found,
such that sub is contained within S[start:end]. Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure.

rindex(sub[, start[, end]])→int#

Return the highest index in S where substring sub is found,
such that sub is contained within S[start:end]. Optional
arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

rjust(width, fillchar='', /)#

Return a right-justified string of length width.

Padding is done using the specified fill character (default is a space).

rpartition(sep, /)#

Partition the string into three parts using the given separator.

This will search for the separator in the string, starting at the end. If
the separator is found, returns a 3-tuple containing the part before the
separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing two empty strings
and the original string.

rsplit(sep=None, maxsplit=-1)#

Return a list of the substrings in the string, using sep as the separator string.

sep

The separator used to split the string.

When set to None (the default value), will split on any whitespace
character (including n r t f and spaces) and will discard
empty strings from the result.

maxsplit

Maximum number of splits.
-1 (the default value) means no limit.

Splitting starts at the end of the string and works to the front.

rstrip(chars=None, /)#

Return a copy of the string with trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

split(sep=None, maxsplit=-1)#

Return a list of the substrings in the string, using sep as the separator string.

sep

The separator used to split the string.

When set to None (the default value), will split on any whitespace
character (including n r t f and spaces) and will discard
empty strings from the result.

maxsplit

Maximum number of splits.
-1 (the default value) means no limit.

Splitting starts at the front of the string and works to the end.

Note, str.split() is mainly useful for data that has been intentionally
delimited. With natural text that includes punctuation, consider using
the regular expression module.

splitlines(keepends=False)#

Return a list of the lines in the string, breaking at line boundaries.

Line breaks are not included in the resulting list unless keepends is given and
true.

startswith(prefix[, start[, end]])→bool#

Return True if S starts with the specified prefix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
prefix can also be a tuple of strings to try.

strip(chars=None, /)#

Return a copy of the string with leading and trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

swapcase()#

Convert uppercase characters to lowercase and lowercase characters to uppercase.

title()#

Return a version of the string where each word is titlecased.

More specifically, words start with uppercased characters and all remaining
cased characters have lower case.

translate(table, /)#

Replace each character in the string using the given translation table.

table

Translation table, which must be a mapping of Unicode ordinals to
Unicode ordinals, strings, or None.

The table must implement lookup/indexing via __getitem__, for instance a
dictionary or list. If this operation raises LookupError, the character is
left untouched. Characters mapped to None are deleted.

upper()#

Return a copy of the string converted to uppercase.

zfill(width, /)#

Pad a numeric string with zeros on the left, to fill a field of the given width.

The string is never truncated.

EQUAL_PROGRESS='EQUAL_PROGRESS'#

FIRST_COME_FIRST_SERVED='FIRST_COME_FIRST_SERVED'#

classtensorrt_llm.llmapi.DynamicBatchConfig(

enable_batch_size_tuning:bool=True,

enable_max_num_tokens_tuning:bool=False,

dynamic_batch_moving_average_window:int=128,

)[source]#

Bases: `StrictBaseModel`, `PybindMirror`

Dynamic batch configuration.

Controls how batch size and token limits are dynamically adjusted at runtime.

fielddynamic_batch_moving_average_window:int=128#

The window size for moving average of input and output length which is used to calculate dynamic batch size and max num tokens

fieldenable_batch_size_tuning:bool=True#

Controls if the batch size should be tuned dynamically

fieldenable_max_num_tokens_tuning:bool=False#

Controls if the max num tokens should be tuned dynamically

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(obj:Any)→Self#

classmethodfrom_pybind(

pybind_instance:PybindMirror,

)→T#

Construct an instance of the given class from the fields in the given
pybind class instance.

Parameters:

cls – Type of the class to construct, must be a subclass of pydantic
BaseModel

pybind_instance – Instance of the pybind class to construct from its
fields

Notes

When a field value is None in the pybind class, but it’s not
optional and has a default value in the BaseModel class, it would
get the default value defined in the BaseModel class.

Returns:

Instance of the given class, populated with the fields of the given
pybind instance

staticget_pybind_enum_fields(pybind_class)#

Get all the enum fields from the pybind class.

staticget_pybind_variable_fields(config_cls)#

Get all the variable fields from the pybind class.

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

staticmaybe_to_pybind(ins)#

staticmirror_pybind_enum(pybind_class)#

Mirror the enum fields from the pybind class to the Python class.

staticmirror_pybind_fields(pybind_class)#

Class decorator that ensures Python class fields mirror those of a C++ class.

Parameters:

pybind_class – The C++ class whose fields should be mirrored

Returns:

A decorator function that validates field mirroring

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(context:Any, /)→None#

Override this method to perform additional initialization after __init__ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(obj:Any)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

staticpybind_equals(obj0, obj1)#

Check if two pybind objects are equal.

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

classmethodupdate_forward_refs(**localns:Any)→None#

classmethodvalidate(value:Any)→Self#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'dynamic_batch_moving_average_window':FieldInfo(annotation=int,required=False,default=128,description='Thewindowsizeformovingaverageofinputandoutputlengthwhichisusedtocalculatedynamicbatchsizeandmaxnumtokens'),'enable_batch_size_tuning':FieldInfo(annotation=bool,required=False,default=True,description='Controlsifthebatchsizeshouldbetuneddynamically'),'enable_max_num_tokens_tuning':FieldInfo(annotation=bool,required=False,default=False,description='Controlsifthemaxnumtokensshouldbetuneddynamically')}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

classtensorrt_llm.llmapi.CacheTransceiverConfig(

backend:Literal['DEFAULT','UCX','NIXL','MOONCAKE','MPI']|None=None,

transceiver_runtime:Literal['CPP','PYTHON']|None=None,

max_tokens_in_buffer:int|None=None,

kv_transfer_timeout_ms:Annotated[int,Gt(gt=0)]|None=None,

kv_transfer_sender_future_timeout_ms:Annotated[int,Gt(gt=0)]|None=1000,

)[source]#

Bases: `StrictBaseModel`, `PybindMirror`

Configuration for the cache transceiver.

fieldbackend:Literal['DEFAULT','UCX','NIXL','MOONCAKE','MPI']|None=None#

The communication backend type to use for the cache transceiver.

fieldkv_transfer_sender_future_timeout_ms:Annotated[int,Gt(gt=0)]|None=1000#

Timeout in milliseconds to wait for the sender future to be ready when scheduled batch size is 0. This allows the request to be eventually cancelled by the user or because of kv_transfer_timeout_ms

fieldkv_transfer_timeout_ms:Annotated[int,Gt(gt=0)]|None=None#

Timeout in milliseconds for KV cache transfer. Requests exceeding this timeout will be cancelled.

fieldmax_tokens_in_buffer:int|None=None#

The max number of tokens the transfer buffer can fit.

fieldtransceiver_runtime:Literal['CPP','PYTHON']|None=None#

The runtime implementation. ‘CPP’ for C++ transceiver (default when not set), ‘PYTHON’ for Python transceiver.

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(obj:Any)→Self#

classmethodfrom_pybind(

pybind_instance:PybindMirror,

)→T#

Construct an instance of the given class from the fields in the given
pybind class instance.

Parameters:

cls – Type of the class to construct, must be a subclass of pydantic
BaseModel

pybind_instance – Instance of the pybind class to construct from its
fields

Notes

When a field value is None in the pybind class, but it’s not
optional and has a default value in the BaseModel class, it would
get the default value defined in the BaseModel class.

Returns:

Instance of the given class, populated with the fields of the given
pybind instance

staticget_pybind_enum_fields(pybind_class)#

Get all the enum fields from the pybind class.

staticget_pybind_variable_fields(config_cls)#

Get all the variable fields from the pybind class.

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

staticmaybe_to_pybind(ins)#

staticmirror_pybind_enum(pybind_class)#

Mirror the enum fields from the pybind class to the Python class.

staticmirror_pybind_fields(pybind_class)#

Class decorator that ensures Python class fields mirror those of a C++ class.

Parameters:

pybind_class – The C++ class whose fields should be mirrored

Returns:

A decorator function that validates field mirroring

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(

context:Any,

)→None#

Override this method to perform additional initialization after __init__ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(obj:Any)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

staticpybind_equals(obj0, obj1)#

Check if two pybind objects are equal.

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

classmethodupdate_forward_refs(

**localns:Any,

)→None#

classmethodvalidate(value:Any)→Self#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'backend':FieldInfo(annotation=Union[Literal['DEFAULT','UCX','NIXL','MOONCAKE','MPI'],NoneType],required=False,default=None,description='Thecommunicationbackendtypetouseforthecachetransceiver.'),'kv_transfer_sender_future_timeout_ms':FieldInfo(annotation=Union[Annotated[int,Gt],NoneType],required=False,default=1000,description='Timeoutinmillisecondstowaitforthesenderfuturetobereadywhenscheduledbatchsizeis0.Thisallowstherequesttobeeventuallycancelledbytheuserorbecauseofkv_transfer_timeout_ms'),'kv_transfer_timeout_ms':FieldInfo(annotation=Union[Annotated[int,Gt],NoneType],required=False,default=None,description='TimeoutinmillisecondsforKVcachetransfer.Requestsexceedingthistimeoutwillbecancelled.'),'max_tokens_in_buffer':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description='Themaxnumberoftokensthetransferbuffercanfit.'),'transceiver_runtime':FieldInfo(annotation=Union[Literal['CPP','PYTHON'],NoneType],required=False,default=None,description="Theruntimeimplementation.'CPP'forC++transceiver(defaultwhennotset),'PYTHON'forPythontransceiver.")}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

classtensorrt_llm.llmapi.NGramDecodingConfig(

max_draft_len:Annotated[int,Ge(ge=0)]|None=None,

max_total_draft_tokens:int|None=None,

speculative_model:str|Path|None=None,

max_concurrency:Annotated[int,Ge(ge=0)]|None=None,

draft_len_schedule:dict[int,int]|None=None,

load_format:str|None=None,

acceptance_window:Annotated[int,Ge(ge=0)]|None=None,

acceptance_length_threshold:Annotated[float,Ge(ge=0)]|None=None,

allow_advanced_sampling:bool=False,

decoding_type:Literal['NGram']='NGram',

max_matching_ngram_size:Annotated[int,Gt(gt=0)]=2,

is_keep_all:bool=True,

is_use_oldest:bool=True,

is_public_pool:bool=True,

)[source]#

Bases: `DecodingBaseConfig`

Configuration for NGram drafter speculative decoding.

fieldacceptance_length_threshold:NonNegativeFloat|None=None#

The threshold for average acceptance length; speculation will be disabled permanently once the rolling average over the last N completed requests (N = acceptance_window) drops below this value. PyTorch backend only.

fieldacceptance_window:NonNegativeInt|None=None#

The rolling average window size (N) for acceptance length across completed requests. If not set or set to 0, the feature is disabled. PyTorch backend only.

fieldallow_advanced_sampling:bool=False#

If true, allows non-greedy sampling when speculation is used. Only applicable to 1-model code paths; non-greedy sampling is always enabled on 2-model paths.

fielddecoding_type:Literal['NGram']='NGram'#

fielddraft_len_schedule:dict[int,int]|None=None#

Developer interface: dynamically adjust draft length based on active batch size in runtime. Maps batch size to draft lengths. For example, {1: 4, 4: 2, 8: 0} means: batch_size >= 1 uses draft_len=4, batch_size >= 4 uses draft_len=2, batch_size >= 8 uses draft_len=0 (disable speculation). draft_len_schedule is enforced to contain batch_size=1 and its according draft_len equals max_draft_len for consistency; for example, if max_draft_len=4, the schedule must contain {1: 4}.

fieldis_keep_all:bool=True#

Whether to keep all candidate pattern-matches pairs, only one match is kept for each pattern if False.

fieldis_public_pool:bool=True#

Whether to use a common pool for all requests, or the pool is private for each request if False.

fieldis_use_oldest:bool=True#

Whether to provide the oldest match when pattern is hit, the newest one is provided if False.

fieldload_format:str|None=None#

The load format of the speculative model.

fieldmax_concurrency:NonNegativeInt|None=None#

When specified, speculation will be disabled at batch sizes above this value. Otherwise, speculation will always be on. PyTorch backend only.

fieldmax_draft_len:NonNegativeInt|None=None#

The maximum number of draft tokens.

fieldmax_matching_ngram_size:Annotated[int,Gt(gt=0)]=2#

The length maximum of searching tokens (can be understood as length maximum of input tokens to search).

Constraints:

gt = 0

fieldmax_total_draft_tokens:int|None=None#

The number of draft tokens in the draft tokens tree. If it’s a linear tree, each draft layer will only generate one draft token. In this case, max_draft_len == max_total_draft_tokens. If it’s a static or dynamic tree, each draft layer may generate more than one draft token. In this case, max_total_draft_tokens >= max_draft_len.

fieldspeculative_model:str|Path|None=None#

The speculative (draft) model. Accepts either (1) a HuggingFace Hub model ID (e.g. ‘yuhuili/EAGLE3-LLaMA3.1-Instruct-8B’), which will be automatically downloaded, or (2) a local filesystem path to a downloaded model directory.

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(obj:Any)→Self#

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(context:Any, /)→None#

This function is meant to behave like a BaseModel method to initialise private attributes.

It takes context as an argument since that’s what pydantic-core passes when calling it.

Parameters:

self – The BaseModel instance.

context – The context.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

num_capture_layers()→int#

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(obj:Any)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

supports_backend(backend:str)→bool[source]#

Override if the speculation algorithm does not support
a subset of the possible backends.

classmethodupdate_forward_refs(

**localns:Any,

)→None#

classmethodvalidate(value:Any)→Self#

validatorvalidate_draft_len_schedule_and_sort»draft_len_schedule#

Validate and sort draft_len_schedule by batch size thresholds.

validatorvalidate_ngram_config»allfields[source]#

propertyis_linear_tree:bool#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'acceptance_length_threshold':FieldInfo(annotation=Union[Annotated[float,Ge],NoneType],required=False,default=None,description='Thethresholdforaverageacceptancelength;speculationwillbedisabledpermanentlyoncetherollingaverageoverthelastNcompletedrequests(N=acceptance_window)dropsbelowthisvalue.PyTorchbackendonly.'),'acceptance_window':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Therollingaveragewindowsize(N)foracceptancelengthacrosscompletedrequests.Ifnotsetorsetto0,thefeatureisdisabled.PyTorchbackendonly.'),'allow_advanced_sampling':FieldInfo(annotation=bool,required=False,default=False,description='Iftrue,allowsnon-greedysamplingwhenspeculationisused.Onlyapplicableto1-modelcodepaths;non-greedysamplingisalwaysenabledon2-modelpaths.',json_schema_extra={'status':'prototype'}),'decoding_type':FieldInfo(annotation=Literal['NGram'],required=False,default='NGram'),'draft_len_schedule':FieldInfo(annotation=Union[dict[int,int],NoneType],required=False,default=None,description='Developerinterface:dynamicallyadjustdraftlengthbasedonactivebatchsizeinruntime.Mapsbatchsizetodraftlengths.Forexample,{1:4,4:2,8:0}means:batch_size>=1usesdraft_len=4,batch_size>=4usesdraft_len=2,batch_size>=8usesdraft_len=0(disablespeculation).draft_len_scheduleisenforcedtocontainbatch_size=1anditsaccordingdraft_lenequalsmax_draft_lenforconsistency;forexample,ifmax_draft_len=4,theschedulemustcontain{1:4}.'),'is_keep_all':FieldInfo(annotation=bool,required=False,default=True,description='Whethertokeepallcandidatepattern-matchespairs,onlyonematchiskeptforeachpatternifFalse.'),'is_public_pool':FieldInfo(annotation=bool,required=False,default=True,description='Whethertouseacommonpoolforallrequests,orthepoolisprivateforeachrequestifFalse.'),'is_use_oldest':FieldInfo(annotation=bool,required=False,default=True,description='Whethertoprovidetheoldestmatchwhenpatternishit,thenewestoneisprovidedifFalse.'),'load_format':FieldInfo(annotation=Union[str,NoneType],required=False,default=None,description='Theloadformatofthespeculativemodel.'),'max_concurrency':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Whenspecified,speculationwillbedisabledatbatchsizesabovethisvalue.Otherwise,speculationwillalwaysbeon.PyTorchbackendonly.'),'max_draft_len':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Themaximumnumberofdrafttokens.'),'max_matching_ngram_size':FieldInfo(annotation=int,required=False,default=2,description='Thelengthmaximumofsearchingtokens(canbeunderstoodaslengthmaximumofinputtokenstosearch).',metadata=[Gt(gt=0)]),'max_total_draft_tokens':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description="Thenumberofdrafttokensinthedrafttokenstree.Ifit'salineartree,eachdraftlayerwillonlygenerateonedrafttoken.Inthiscase,max_draft_len==max_total_draft_tokens.Ifit'sastaticordynamictree,eachdraftlayermaygeneratemorethanonedrafttoken.Inthiscase,max_total_draft_tokens>=max_draft_len."),'speculative_model':FieldInfo(annotation=Union[str,Path,NoneType],required=False,default=None,alias_priority=2,validation_alias=AliasChoices(choices=['speculative_model','speculative_model_dir']),description="Thespeculative(draft)model.Acceptseither(1)aHuggingFaceHubmodelID(e.g.'yuhuili/EAGLE3-LLaMA3.1-Instruct-8B'),whichwillbeautomaticallydownloaded,or(2)alocalfilesystempathtoadownloadedmodeldirectory.")}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

propertyspec_dec_mode#

propertytokens_per_gen_step:int#

Total tokens per gen request in one spec dec iteration (including golden token).

classtensorrt_llm.llmapi.PARDDecodingConfig(

max_draft_len:Annotated[int,Ge(ge=0)]|None=None,

max_total_draft_tokens:int|None=None,

speculative_model:str|Path|None=None,

max_concurrency:Annotated[int,Ge(ge=0)]|None=None,

draft_len_schedule:dict[int,int]|None=None,

load_format:str|None=None,

acceptance_window:Annotated[int,Ge(ge=0)]|None=None,

acceptance_length_threshold:Annotated[float,Ge(ge=0)]|None=None,

allow_advanced_sampling:bool=False,

mask_token_id:int|None=None,

decoding_type:Literal['PARD']='PARD',

use_sa_spec:bool|None=False,

sa_spec_threshold:Annotated[int,Gt(gt=0)]=4,

)[source]#

Bases: `DecodingBaseConfig`

Configuration for PARD (Parallel Draft) speculative decoding.

PARD is a target-independent speculative decoding method that uses
mask tokens to predict multiple draft tokens in parallel within a
single forward pass.

Key features:
- Target-independent: doesn’t use target model hidden states
- Parallel prediction: all K draft tokens in one forward pass
- Shared mask token: uses the same mask_token_id across all positions

Reference: https://arxiv.org/pdf/2504.18583

fieldacceptance_length_threshold:NonNegativeFloat|None=None#

The threshold for average acceptance length; speculation will be disabled permanently once the rolling average over the last N completed requests (N = acceptance_window) drops below this value. PyTorch backend only.

fieldacceptance_window:NonNegativeInt|None=None#

The rolling average window size (N) for acceptance length across completed requests. If not set or set to 0, the feature is disabled. PyTorch backend only.

fieldallow_advanced_sampling:bool=False#

If true, allows non-greedy sampling when speculation is used. Only applicable to 1-model code paths; non-greedy sampling is always enabled on 2-model paths.

fielddecoding_type:Literal['PARD']='PARD'#

fielddraft_len_schedule:dict[int,int]|None=None#

Developer interface: dynamically adjust draft length based on active batch size in runtime. Maps batch size to draft lengths. For example, {1: 4, 4: 2, 8: 0} means: batch_size >= 1 uses draft_len=4, batch_size >= 4 uses draft_len=2, batch_size >= 8 uses draft_len=0 (disable speculation). draft_len_schedule is enforced to contain batch_size=1 and its according draft_len equals max_draft_len for consistency; for example, if max_draft_len=4, the schedule must contain {1: 4}.

fieldload_format:str|None=None#

The load format of the speculative model.

fieldmask_token_id:int|None=None#

The token ID used as a mask token for parallel draft prediction. If None, it will be read from the draft model config (typically vocab_size).

fieldmax_concurrency:NonNegativeInt|None=None#

When specified, speculation will be disabled at batch sizes above this value. Otherwise, speculation will always be on. PyTorch backend only.

fieldmax_draft_len:NonNegativeInt|None=None#

The maximum number of draft tokens.

fieldmax_total_draft_tokens:int|None=None#

The number of draft tokens in the draft tokens tree. If it’s a linear tree, each draft layer will only generate one draft token. In this case, max_draft_len == max_total_draft_tokens. If it’s a static or dynamic tree, each draft layer may generate more than one draft token. In this case, max_total_draft_tokens >= max_draft_len.

fieldsa_spec_threshold:Annotated[int,Gt(gt=0)]=4#

The threshold for the Suffix Automaton Decoding. If the length of the suffix match exceeds the threshold, use the suffix automaton output for the next draft tokens.

Constraints:

gt = 0

fieldspeculative_model:str|Path|None=None#

The speculative (draft) model. Accepts either (1) a HuggingFace Hub model ID (e.g. ‘yuhuili/EAGLE3-LLaMA3.1-Instruct-8B’), which will be automatically downloaded, or (2) a local filesystem path to a downloaded model directory.

fielduse_sa_spec:bool|None=False#

Combine with Suffix Automaton Decoding

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(obj:Any)→Self#

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(context:Any, /)→None#

This function is meant to behave like a BaseModel method to initialise private attributes.

It takes context as an argument since that’s what pydantic-core passes when calling it.

Parameters:

self – The BaseModel instance.

context – The context.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

num_capture_layers()→int#

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(obj:Any)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

validatorset_max_total_draft_tokens»allfields[source]#

supports_backend(backend:str)→bool[source]#

Override if the speculation algorithm does not support
a subset of the possible backends.

classmethodupdate_forward_refs(**localns:Any)→None#

classmethodvalidate(value:Any)→Self#

validatorvalidate_draft_len_schedule_and_sort»draft_len_schedule#

Validate and sort draft_len_schedule by batch size thresholds.

propertyis_linear_tree:bool#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'acceptance_length_threshold':FieldInfo(annotation=Union[Annotated[float,Ge],NoneType],required=False,default=None,description='Thethresholdforaverageacceptancelength;speculationwillbedisabledpermanentlyoncetherollingaverageoverthelastNcompletedrequests(N=acceptance_window)dropsbelowthisvalue.PyTorchbackendonly.'),'acceptance_window':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Therollingaveragewindowsize(N)foracceptancelengthacrosscompletedrequests.Ifnotsetorsetto0,thefeatureisdisabled.PyTorchbackendonly.'),'allow_advanced_sampling':FieldInfo(annotation=bool,required=False,default=False,description='Iftrue,allowsnon-greedysamplingwhenspeculationisused.Onlyapplicableto1-modelcodepaths;non-greedysamplingisalwaysenabledon2-modelpaths.',json_schema_extra={'status':'prototype'}),'decoding_type':FieldInfo(annotation=Literal['PARD'],required=False,default='PARD'),'draft_len_schedule':FieldInfo(annotation=Union[dict[int,int],NoneType],required=False,default=None,description='Developerinterface:dynamicallyadjustdraftlengthbasedonactivebatchsizeinruntime.Mapsbatchsizetodraftlengths.Forexample,{1:4,4:2,8:0}means:batch_size>=1usesdraft_len=4,batch_size>=4usesdraft_len=2,batch_size>=8usesdraft_len=0(disablespeculation).draft_len_scheduleisenforcedtocontainbatch_size=1anditsaccordingdraft_lenequalsmax_draft_lenforconsistency;forexample,ifmax_draft_len=4,theschedulemustcontain{1:4}.'),'load_format':FieldInfo(annotation=Union[str,NoneType],required=False,default=None,description='Theloadformatofthespeculativemodel.'),'mask_token_id':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description='ThetokenIDusedasamasktokenforparalleldraftprediction.IfNone,itwillbereadfromthedraftmodelconfig(typicallyvocab_size).'),'max_concurrency':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Whenspecified,speculationwillbedisabledatbatchsizesabovethisvalue.Otherwise,speculationwillalwaysbeon.PyTorchbackendonly.'),'max_draft_len':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Themaximumnumberofdrafttokens.'),'max_total_draft_tokens':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description="Thenumberofdrafttokensinthedrafttokenstree.Ifit'salineartree,eachdraftlayerwillonlygenerateonedrafttoken.Inthiscase,max_draft_len==max_total_draft_tokens.Ifit'sastaticordynamictree,eachdraftlayermaygeneratemorethanonedrafttoken.Inthiscase,max_total_draft_tokens>=max_draft_len."),'sa_spec_threshold':FieldInfo(annotation=int,required=False,default=4,description='ThethresholdfortheSuffixAutomatonDecoding.Ifthelengthofthesuffixmatchexceedsthethreshold,usethesuffixautomatonoutputforthenextdrafttokens.',metadata=[Gt(gt=0)]),'speculative_model':FieldInfo(annotation=Union[str,Path,NoneType],required=False,default=None,alias_priority=2,validation_alias=AliasChoices(choices=['speculative_model','speculative_model_dir']),description="Thespeculative(draft)model.Acceptseither(1)aHuggingFaceHubmodelID(e.g.'yuhuili/EAGLE3-LLaMA3.1-Instruct-8B'),whichwillbeautomaticallydownloaded,or(2)alocalfilesystempathtoadownloadedmodeldirectory."),'use_sa_spec':FieldInfo(annotation=Union[bool,NoneType],required=False,default=False,description='CombinewithSuffixAutomatonDecoding',json_schema_extra={'status':'beta'})}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

propertyspec_dec_mode#

propertytokens_per_gen_step:int#

K+1 accepted + K-1 masks.

Type:

PARD needs 2K tokens per gen request

classtensorrt_llm.llmapi.SADecodingConfig(

max_draft_len:Annotated[int,Ge(ge=0)]|None=None,

max_total_draft_tokens:int|None=None,

speculative_model:str|Path|None=None,

max_concurrency:Annotated[int,Ge(ge=0)]|None=None,

draft_len_schedule:dict[int,int]|None=None,

load_format:str|None=None,

acceptance_window:Annotated[int,Ge(ge=0)]|None=None,

acceptance_length_threshold:Annotated[float,Ge(ge=0)]|None=None,

allow_advanced_sampling:bool=False,

decoding_type:Literal['SA']='SA',

max_matching_ngram_size:int=-1,

)[source]#

Bases: `DecodingBaseConfig`

Configuration for Suffix Automaton (SA) speculative decoding (one-model design).

Uses a GPU-native suffix automaton for pattern matching. Drafting runs inside
the target model forward; supports CUDA graph and overlap scheduler.

fieldacceptance_length_threshold:NonNegativeFloat|None=None#

The threshold for average acceptance length; speculation will be disabled permanently once the rolling average over the last N completed requests (N = acceptance_window) drops below this value. PyTorch backend only.

fieldacceptance_window:NonNegativeInt|None=None#

The rolling average window size (N) for acceptance length across completed requests. If not set or set to 0, the feature is disabled. PyTorch backend only.

fieldallow_advanced_sampling:bool=False#

If true, allows non-greedy sampling when speculation is used. Only applicable to 1-model code paths; non-greedy sampling is always enabled on 2-model paths.

fielddecoding_type:Literal['SA']='SA'#

fielddraft_len_schedule:dict[int,int]|None=None#

Developer interface: dynamically adjust draft length based on active batch size in runtime. Maps batch size to draft lengths. For example, {1: 4, 4: 2, 8: 0} means: batch_size >= 1 uses draft_len=4, batch_size >= 4 uses draft_len=2, batch_size >= 8 uses draft_len=0 (disable speculation). draft_len_schedule is enforced to contain batch_size=1 and its according draft_len equals max_draft_len for consistency; for example, if max_draft_len=4, the schedule must contain {1: 4}.

fieldload_format:str|None=None#

The load format of the speculative model.

fieldmax_concurrency:NonNegativeInt|None=None#

When specified, speculation will be disabled at batch sizes above this value. Otherwise, speculation will always be on. PyTorch backend only.

fieldmax_draft_len:NonNegativeInt|None=None#

The maximum number of draft tokens.

fieldmax_matching_ngram_size:int=-1#

Positive value (e.g., 3): fixed-size ngram matching. -1: longest possible match via suffix automaton. 0 is invalid.

fieldmax_total_draft_tokens:int|None=None#

The number of draft tokens in the draft tokens tree. If it’s a linear tree, each draft layer will only generate one draft token. In this case, max_draft_len == max_total_draft_tokens. If it’s a static or dynamic tree, each draft layer may generate more than one draft token. In this case, max_total_draft_tokens >= max_draft_len.

fieldspeculative_model:str|Path|None=None#

The speculative (draft) model. Accepts either (1) a HuggingFace Hub model ID (e.g. ‘yuhuili/EAGLE3-LLaMA3.1-Instruct-8B’), which will be automatically downloaded, or (2) a local filesystem path to a downloaded model directory.

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(obj:Any)→Self#

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(context:Any, /)→None#

This function is meant to behave like a BaseModel method to initialise private attributes.

It takes context as an argument since that’s what pydantic-core passes when calling it.

Parameters:

self – The BaseModel instance.

context – The context.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

num_capture_layers()→int#

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(obj:Any)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

supports_backend(backend:str)→bool[source]#

Override if the speculation algorithm does not support
a subset of the possible backends.

classmethodupdate_forward_refs(**localns:Any)→None#

classmethodvalidate(value:Any)→Self#

validatorvalidate_draft_len_schedule_and_sort»draft_len_schedule#

Validate and sort draft_len_schedule by batch size thresholds.

validatorvalidate_sa_config»allfields[source]#

propertyis_linear_tree:bool#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'acceptance_length_threshold':FieldInfo(annotation=Union[Annotated[float,Ge],NoneType],required=False,default=None,description='Thethresholdforaverageacceptancelength;speculationwillbedisabledpermanentlyoncetherollingaverageoverthelastNcompletedrequests(N=acceptance_window)dropsbelowthisvalue.PyTorchbackendonly.'),'acceptance_window':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Therollingaveragewindowsize(N)foracceptancelengthacrosscompletedrequests.Ifnotsetorsetto0,thefeatureisdisabled.PyTorchbackendonly.'),'allow_advanced_sampling':FieldInfo(annotation=bool,required=False,default=False,description='Iftrue,allowsnon-greedysamplingwhenspeculationisused.Onlyapplicableto1-modelcodepaths;non-greedysamplingisalwaysenabledon2-modelpaths.',json_schema_extra={'status':'prototype'}),'decoding_type':FieldInfo(annotation=Literal['SA'],required=False,default='SA'),'draft_len_schedule':FieldInfo(annotation=Union[dict[int,int],NoneType],required=False,default=None,description='Developerinterface:dynamicallyadjustdraftlengthbasedonactivebatchsizeinruntime.Mapsbatchsizetodraftlengths.Forexample,{1:4,4:2,8:0}means:batch_size>=1usesdraft_len=4,batch_size>=4usesdraft_len=2,batch_size>=8usesdraft_len=0(disablespeculation).draft_len_scheduleisenforcedtocontainbatch_size=1anditsaccordingdraft_lenequalsmax_draft_lenforconsistency;forexample,ifmax_draft_len=4,theschedulemustcontain{1:4}.'),'load_format':FieldInfo(annotation=Union[str,NoneType],required=False,default=None,description='Theloadformatofthespeculativemodel.'),'max_concurrency':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Whenspecified,speculationwillbedisabledatbatchsizesabovethisvalue.Otherwise,speculationwillalwaysbeon.PyTorchbackendonly.'),'max_draft_len':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Themaximumnumberofdrafttokens.'),'max_matching_ngram_size':FieldInfo(annotation=int,required=False,default=-1,description='Positivevalue(e.g.,3):fixed-sizengrammatching.-1:longestpossiblematchviasuffixautomaton.0isinvalid.'),'max_total_draft_tokens':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description="Thenumberofdrafttokensinthedrafttokenstree.Ifit'salineartree,eachdraftlayerwillonlygenerateonedrafttoken.Inthiscase,max_draft_len==max_total_draft_tokens.Ifit'sastaticordynamictree,eachdraftlayermaygeneratemorethanonedrafttoken.Inthiscase,max_total_draft_tokens>=max_draft_len."),'speculative_model':FieldInfo(annotation=Union[str,Path,NoneType],required=False,default=None,alias_priority=2,validation_alias=AliasChoices(choices=['speculative_model','speculative_model_dir']),description="Thespeculative(draft)model.Acceptseither(1)aHuggingFaceHubmodelID(e.g.'yuhuili/EAGLE3-LLaMA3.1-Instruct-8B'),whichwillbeautomaticallydownloaded,or(2)alocalfilesystempathtoadownloadedmodeldirectory.")}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

propertyspec_dec_mode#

propertytokens_per_gen_step:int#

Total tokens per gen request in one spec dec iteration (including golden token).

classtensorrt_llm.llmapi.UserProvidedDecodingConfig(

max_draft_len:Annotated[int,Ge(ge=0)]|None=None,

max_total_draft_tokens:int|None=None,

speculative_model:str|Path|None=None,

max_concurrency:Annotated[int,Ge(ge=0)]|None=None,

draft_len_schedule:dict[int,int]|None=None,

load_format:str|None=None,

acceptance_window:Annotated[int,Ge(ge=0)]|None=None,

acceptance_length_threshold:Annotated[float,Ge(ge=0)]|None=None,

allow_advanced_sampling:bool=False,

decoding_type:Literal['User_Provided']='User_Provided',

drafter:object,

resource_manager:object=None,

)[source]#

Bases: `DecodingBaseConfig`

fieldacceptance_length_threshold:NonNegativeFloat|None=None#

The threshold for average acceptance length; speculation will be disabled permanently once the rolling average over the last N completed requests (N = acceptance_window) drops below this value. PyTorch backend only.

fieldacceptance_window:NonNegativeInt|None=None#

The rolling average window size (N) for acceptance length across completed requests. If not set or set to 0, the feature is disabled. PyTorch backend only.

fieldallow_advanced_sampling:bool=False#

If true, allows non-greedy sampling when speculation is used. Only applicable to 1-model code paths; non-greedy sampling is always enabled on 2-model paths.

fielddecoding_type:Literal['User_Provided']='User_Provided'#

fielddraft_len_schedule:dict[int,int]|None=None#

Developer interface: dynamically adjust draft length based on active batch size in runtime. Maps batch size to draft lengths. For example, {1: 4, 4: 2, 8: 0} means: batch_size >= 1 uses draft_len=4, batch_size >= 4 uses draft_len=2, batch_size >= 8 uses draft_len=0 (disable speculation). draft_len_schedule is enforced to contain batch_size=1 and its according draft_len equals max_draft_len for consistency; for example, if max_draft_len=4, the schedule must contain {1: 4}.

fielddrafter:object[Required]#

User-provided Drafter instance implementing the prepare_draft_tokens() method for custom draft token generation. See tensorrt_llm/_torch/speculative/drafter.py for the Drafter base class interface.

fieldload_format:str|None=None#

The load format of the speculative model.

fieldmax_concurrency:NonNegativeInt|None=None#

When specified, speculation will be disabled at batch sizes above this value. Otherwise, speculation will always be on. PyTorch backend only.

fieldmax_draft_len:NonNegativeInt|None=None#

The maximum number of draft tokens.

fieldmax_total_draft_tokens:int|None=None#

The number of draft tokens in the draft tokens tree. If it’s a linear tree, each draft layer will only generate one draft token. In this case, max_draft_len == max_total_draft_tokens. If it’s a static or dynamic tree, each draft layer may generate more than one draft token. In this case, max_total_draft_tokens >= max_draft_len.

fieldresource_manager:object=None#

Optional user-provided BaseResourceManager instance for managing resources (memory, caches) during drafting. Called to prepare/free resources before/after target model forward passes.

fieldspeculative_model:str|Path|None=None#

The speculative (draft) model. Accepts either (1) a HuggingFace Hub model ID (e.g. ‘yuhuili/EAGLE3-LLaMA3.1-Instruct-8B’), which will be automatically downloaded, or (2) a local filesystem path to a downloaded model directory.

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(obj:Any)→Self#

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(context:Any, /)→None#

This function is meant to behave like a BaseModel method to initialise private attributes.

It takes context as an argument since that’s what pydantic-core passes when calling it.

Parameters:

self – The BaseModel instance.

context – The context.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

num_capture_layers()→int#

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(obj:Any)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

validatorset_max_total_draft_tokens»allfields[source]#

supports_backend(backend:str)→bool#

Override if the speculation algorithm does not support
a subset of the possible backends.

classmethodupdate_forward_refs(

**localns:Any,

)→None#

classmethodvalidate(

value:Any,

)→Self#

validatorvalidate_draft_len_schedule_and_sort»draft_len_schedule#

Validate and sort draft_len_schedule by batch size thresholds.

propertyis_linear_tree:bool#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'acceptance_length_threshold':FieldInfo(annotation=Union[Annotated[float,Ge],NoneType],required=False,default=None,description='Thethresholdforaverageacceptancelength;speculationwillbedisabledpermanentlyoncetherollingaverageoverthelastNcompletedrequests(N=acceptance_window)dropsbelowthisvalue.PyTorchbackendonly.'),'acceptance_window':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Therollingaveragewindowsize(N)foracceptancelengthacrosscompletedrequests.Ifnotsetorsetto0,thefeatureisdisabled.PyTorchbackendonly.'),'allow_advanced_sampling':FieldInfo(annotation=bool,required=False,default=False,description='Iftrue,allowsnon-greedysamplingwhenspeculationisused.Onlyapplicableto1-modelcodepaths;non-greedysamplingisalwaysenabledon2-modelpaths.',json_schema_extra={'status':'prototype'}),'decoding_type':FieldInfo(annotation=Literal['User_Provided'],required=False,default='User_Provided'),'draft_len_schedule':FieldInfo(annotation=Union[dict[int,int],NoneType],required=False,default=None,description='Developerinterface:dynamicallyadjustdraftlengthbasedonactivebatchsizeinruntime.Mapsbatchsizetodraftlengths.Forexample,{1:4,4:2,8:0}means:batch_size>=1usesdraft_len=4,batch_size>=4usesdraft_len=2,batch_size>=8usesdraft_len=0(disablespeculation).draft_len_scheduleisenforcedtocontainbatch_size=1anditsaccordingdraft_lenequalsmax_draft_lenforconsistency;forexample,ifmax_draft_len=4,theschedulemustcontain{1:4}.'),'drafter':FieldInfo(annotation=object,required=True,description='User-providedDrafterinstanceimplementingtheprepare_draft_tokens()methodforcustomdrafttokengeneration.Seetensorrt_llm/_torch/speculative/drafter.pyfortheDrafterbaseclassinterface.'),'load_format':FieldInfo(annotation=Union[str,NoneType],required=False,default=None,description='Theloadformatofthespeculativemodel.'),'max_concurrency':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Whenspecified,speculationwillbedisabledatbatchsizesabovethisvalue.Otherwise,speculationwillalwaysbeon.PyTorchbackendonly.'),'max_draft_len':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Themaximumnumberofdrafttokens.'),'max_total_draft_tokens':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description="Thenumberofdrafttokensinthedrafttokenstree.Ifit'salineartree,eachdraftlayerwillonlygenerateonedrafttoken.Inthiscase,max_draft_len==max_total_draft_tokens.Ifit'sastaticordynamictree,eachdraftlayermaygeneratemorethanonedrafttoken.Inthiscase,max_total_draft_tokens>=max_draft_len."),'resource_manager':FieldInfo(annotation=object,required=False,default=None,description='Optionaluser-providedBaseResourceManagerinstanceformanagingresources(memory,caches)duringdrafting.Calledtoprepare/freeresourcesbefore/aftertargetmodelforwardpasses.'),'speculative_model':FieldInfo(annotation=Union[str,Path,NoneType],required=False,default=None,alias_priority=2,validation_alias=AliasChoices(choices=['speculative_model','speculative_model_dir']),description="Thespeculative(draft)model.Acceptseither(1)aHuggingFaceHubmodelID(e.g.'yuhuili/EAGLE3-LLaMA3.1-Instruct-8B'),whichwillbeautomaticallydownloaded,or(2)alocalfilesystempathtoadownloadedmodeldirectory.")}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

propertyspec_dec_mode#

propertytokens_per_gen_step:int#

Total tokens per gen request in one spec dec iteration (including golden token).

classtensorrt_llm.llmapi.TorchCompileConfig(

enable_fullgraph:bool=True,

enable_inductor:bool=False,

enable_piecewise_cuda_graph:bool=False,

capture_num_tokens:List[Annotated[int,Gt(gt=0)]]|None=None,

enable_userbuffers:bool=True,

max_num_streams:Annotated[int,Gt(gt=0)]=1,

)[source]#

Bases: `StrictBaseModel`

Configuration for torch.compile.

fieldcapture_num_tokens:List[Annotated[int,Gt(gt=0)]]|None=None#

List of num of tokens to capture the piecewise CUDA graph for. If not provided, the number of tokens will be the same as cuda_graph_config.batch_sizes.

fieldenable_fullgraph:bool=True#

Enable full graph compilation in torch.compile.

fieldenable_inductor:bool=False#

Enable inductor backend in torch.compile.

fieldenable_piecewise_cuda_graph:bool=False#

Enable piecewise CUDA graph in torch.compile.

fieldenable_userbuffers:bool=True#

When torch compile is enabled, userbuffers is enabled by default.

fieldmax_num_streams:Annotated[int,Gt(gt=0)]=1#

The maximum number of CUDA streams to use for torch.compile.

Constraints:

gt = 0

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(obj:Any)→Self#

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(context:Any, /)→None#

Override this method to perform additional initialization after __init__ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(obj:Any)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

validatorset_default_capture_num_tokens»allfields[source]#

classmethodupdate_forward_refs(**localns:Any)→None#

classmethodvalidate(value:Any)→Self#

validatorvalidate_capture_num_tokens»capture_num_tokens[source]#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'capture_num_tokens':FieldInfo(annotation=Union[List[Annotated[int,Gt]],NoneType],required=False,default=None,description='ListofnumoftokenstocapturethepiecewiseCUDAgraphfor.Ifnotprovided,thenumberoftokenswillbethesameascuda_graph_config.batch_sizes.'),'enable_fullgraph':FieldInfo(annotation=bool,required=False,default=True,description='Enablefullgraphcompilationintorch.compile.'),'enable_inductor':FieldInfo(annotation=bool,required=False,default=False,description='Enableinductorbackendintorch.compile.'),'enable_piecewise_cuda_graph':FieldInfo(annotation=bool,required=False,default=False,description='EnablepiecewiseCUDAgraphintorch.compile.'),'enable_userbuffers':FieldInfo(annotation=bool,required=False,default=True,description='Whentorchcompileisenabled,userbuffersisenabledbydefault.'),'max_num_streams':FieldInfo(annotation=int,required=False,default=1,description='ThemaximumnumberofCUDAstreamstousefortorch.compile.',metadata=[Gt(gt=0)])}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

classtensorrt_llm.llmapi.DraftTargetDecodingConfig(

max_draft_len:Annotated[int,Ge(ge=0)]|None=None,

max_total_draft_tokens:int|None=None,

speculative_model:str|Path|None=None,

max_concurrency:Annotated[int,Ge(ge=0)]|None=None,

draft_len_schedule:dict[int,int]|None=None,

load_format:str|None=None,

acceptance_window:Annotated[int,Ge(ge=0)]|None=None,

acceptance_length_threshold:Annotated[float,Ge(ge=0)]|None=None,

allow_advanced_sampling:bool=False,

decoding_type:Literal['Draft_Target']='Draft_Target',

)[source]#

Bases: `DecodingBaseConfig`

fieldacceptance_length_threshold:NonNegativeFloat|None=None#

The threshold for average acceptance length; speculation will be disabled permanently once the rolling average over the last N completed requests (N = acceptance_window) drops below this value. PyTorch backend only.

fieldacceptance_window:NonNegativeInt|None=None#

The rolling average window size (N) for acceptance length across completed requests. If not set or set to 0, the feature is disabled. PyTorch backend only.

fieldallow_advanced_sampling:bool=False#

If true, allows non-greedy sampling when speculation is used. Only applicable to 1-model code paths; non-greedy sampling is always enabled on 2-model paths.

fielddecoding_type:Literal['Draft_Target']='Draft_Target'#

fielddraft_len_schedule:dict[int,int]|None=None#

Developer interface: dynamically adjust draft length based on active batch size in runtime. Maps batch size to draft lengths. For example, {1: 4, 4: 2, 8: 0} means: batch_size >= 1 uses draft_len=4, batch_size >= 4 uses draft_len=2, batch_size >= 8 uses draft_len=0 (disable speculation). draft_len_schedule is enforced to contain batch_size=1 and its according draft_len equals max_draft_len for consistency; for example, if max_draft_len=4, the schedule must contain {1: 4}.

fieldload_format:str|None=None#

The load format of the speculative model.

fieldmax_concurrency:NonNegativeInt|None=None#

When specified, speculation will be disabled at batch sizes above this value. Otherwise, speculation will always be on. PyTorch backend only.

fieldmax_draft_len:NonNegativeInt|None=None#

The maximum number of draft tokens.

fieldmax_total_draft_tokens:int|None=None#

The number of draft tokens in the draft tokens tree. If it’s a linear tree, each draft layer will only generate one draft token. In this case, max_draft_len == max_total_draft_tokens. If it’s a static or dynamic tree, each draft layer may generate more than one draft token. In this case, max_total_draft_tokens >= max_draft_len.

fieldspeculative_model:str|Path|None=None#

The speculative (draft) model. Accepts either (1) a HuggingFace Hub model ID (e.g. ‘yuhuili/EAGLE3-LLaMA3.1-Instruct-8B’), which will be automatically downloaded, or (2) a local filesystem path to a downloaded model directory.

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(obj:Any)→Self#

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(context:Any, /)→None#

This function is meant to behave like a BaseModel method to initialise private attributes.

It takes context as an argument since that’s what pydantic-core passes when calling it.

Parameters:

self – The BaseModel instance.

context – The context.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

num_capture_layers()→int#

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(obj:Any)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

supports_backend(backend:str)→bool[source]#

Override if the speculation algorithm does not support
a subset of the possible backends.

classmethodupdate_forward_refs(

**localns:Any,

)→None#

classmethodvalidate(value:Any)→Self#

validatorvalidate_draft_len_schedule_and_sort»draft_len_schedule#

Validate and sort draft_len_schedule by batch size thresholds.

validatorvalidate_draft_target_config»allfields[source]#

propertyis_linear_tree:bool#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'acceptance_length_threshold':FieldInfo(annotation=Union[Annotated[float,Ge],NoneType],required=False,default=None,description='Thethresholdforaverageacceptancelength;speculationwillbedisabledpermanentlyoncetherollingaverageoverthelastNcompletedrequests(N=acceptance_window)dropsbelowthisvalue.PyTorchbackendonly.'),'acceptance_window':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Therollingaveragewindowsize(N)foracceptancelengthacrosscompletedrequests.Ifnotsetorsetto0,thefeatureisdisabled.PyTorchbackendonly.'),'allow_advanced_sampling':FieldInfo(annotation=bool,required=False,default=False,description='Iftrue,allowsnon-greedysamplingwhenspeculationisused.Onlyapplicableto1-modelcodepaths;non-greedysamplingisalwaysenabledon2-modelpaths.',json_schema_extra={'status':'prototype'}),'decoding_type':FieldInfo(annotation=Literal['Draft_Target'],required=False,default='Draft_Target'),'draft_len_schedule':FieldInfo(annotation=Union[dict[int,int],NoneType],required=False,default=None,description='Developerinterface:dynamicallyadjustdraftlengthbasedonactivebatchsizeinruntime.Mapsbatchsizetodraftlengths.Forexample,{1:4,4:2,8:0}means:batch_size>=1usesdraft_len=4,batch_size>=4usesdraft_len=2,batch_size>=8usesdraft_len=0(disablespeculation).draft_len_scheduleisenforcedtocontainbatch_size=1anditsaccordingdraft_lenequalsmax_draft_lenforconsistency;forexample,ifmax_draft_len=4,theschedulemustcontain{1:4}.'),'load_format':FieldInfo(annotation=Union[str,NoneType],required=False,default=None,description='Theloadformatofthespeculativemodel.'),'max_concurrency':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Whenspecified,speculationwillbedisabledatbatchsizesabovethisvalue.Otherwise,speculationwillalwaysbeon.PyTorchbackendonly.'),'max_draft_len':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Themaximumnumberofdrafttokens.'),'max_total_draft_tokens':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description="Thenumberofdrafttokensinthedrafttokenstree.Ifit'salineartree,eachdraftlayerwillonlygenerateonedrafttoken.Inthiscase,max_draft_len==max_total_draft_tokens.Ifit'sastaticordynamictree,eachdraftlayermaygeneratemorethanonedrafttoken.Inthiscase,max_total_draft_tokens>=max_draft_len."),'speculative_model':FieldInfo(annotation=Union[str,Path,NoneType],required=False,default=None,alias_priority=2,validation_alias=AliasChoices(choices=['speculative_model','speculative_model_dir']),description="Thespeculative(draft)model.Acceptseither(1)aHuggingFaceHubmodelID(e.g.'yuhuili/EAGLE3-LLaMA3.1-Instruct-8B'),whichwillbeautomaticallydownloaded,or(2)alocalfilesystempathtoadownloadedmodeldirectory.")}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

propertyspec_dec_mode#

propertytokens_per_gen_step:int#

Total tokens per gen request in one spec dec iteration (including golden token).

tensorrt_llm.llmapi.LlmArgs#

alias of `TorchLlmArgs`

classtensorrt_llm.llmapi.TorchLlmArgs(

model:str|~pathlib.Path,

tokenizer:str|~pathlib.Path|~transformers.tokenization_utils_base.PreTrainedTokenizerBase|~tensorrt_llm.tokenizer.tokenizer.TokenizerBase|None=None,

tokenizer_mode:~typing.Literal['auto',

'slow']='auto',

custom_tokenizer:str|None=None,

skip_tokenizer_init:bool=False,

trust_remote_code:bool=False,

tensor_parallel_size:int=1,

dtype:str='auto',

revision:str|None=None,

tokenizer_revision:str|None=None,

model_kwargs:~typing.Dict[str,

~typing.Any]|None=None,

pipeline_parallel_size:int=1,

context_parallel_size:int=1,

gpus_per_node:int|None=None,

moe_cluster_parallel_size:int|None=None,

moe_tensor_parallel_size:int|None=None,

moe_expert_parallel_size:int|None=None,

enable_attention_dp:bool=False,

enable_lm_head_tp_in_adp:bool=False,

pp_partition:~typing.List[int]|None=None,

cp_config:~tensorrt_llm.llmapi.llm_args.CpConfig|None=None,

load_format:str|~tensorrt_llm.llmapi.llm_args.LoadFormat=LoadFormat.AUTO,

enable_lora:bool=False,

lora_config:~tensorrt_llm.lora_helper.LoraConfig|None=None,

kv_cache_config:~tensorrt_llm.llmapi.llm_args.KvCacheConfig=<factory>,

enable_chunked_prefill:bool=False,

guided_decoding_backend:~typing.Literal['xgrammar',

'llguidance']|None=None,

batched_logits_processor:object|None=None,

iter_stats_max_iterations:int|None=None,

request_stats_max_iterations:int|None=None,

peft_cache_config:~tensorrt_llm.llmapi.llm_args.PeftCacheConfig|None=None,

scheduler_config:~tensorrt_llm.llmapi.llm_args.SchedulerConfig=<factory>,

cache_transceiver_config:~tensorrt_llm.llmapi.llm_args.CacheTransceiverConfig|None=None,

sparse_attention_config:~typing.Annotated[~tensorrt_llm.llmapi.llm_args.RocketSparseAttentionConfig|~tensorrt_llm.llmapi.llm_args.DeepSeekSparseAttentionConfig|~tensorrt_llm.llmapi.llm_args.SkipSoftmaxAttentionConfig,

FieldInfo(annotation=NoneType,

required=True,

discriminator='algorithm')]|None=None,

speculative_config:~typing.Annotated[~tensorrt_llm.llmapi.llm_args.DraftTargetDecodingConfig|~tensorrt_llm.llmapi.llm_args.EagleDecodingConfig|~tensorrt_llm.llmapi.llm_args.Eagle3DecodingConfig|~tensorrt_llm.llmapi.llm_args.LookaheadDecodingConfig|~tensorrt_llm.llmapi.llm_args.MedusaDecodingConfig|~tensorrt_llm.llmapi.llm_args.MTPDecodingConfig|~tensorrt_llm.llmapi.llm_args.NGramDecodingConfig|~tensorrt_llm.llmapi.llm_args.SADecodingConfig|~tensorrt_llm.llmapi.llm_args.UserProvidedDecodingConfig|~tensorrt_llm.llmapi.llm_args.SaveHiddenStatesDecodingConfig|~tensorrt_llm.llmapi.llm_args.PARDDecodingConfig|~tensorrt_llm.llmapi.llm_args.AutoDecodingConfig,

FieldInfo(annotation=NoneType,

required=True,

discriminator='decoding_type')]|None=None,

max_batch_size:int|None=2048,

max_input_len:int|None=1024,

max_seq_len:int|None=None,

max_beam_width:int|None=1,

max_num_tokens:int|None=8192,

gather_generation_logits:bool=False,

num_postprocess_workers:int=0,

postprocess_tokenizer_dir:str|None=None,

reasoning_parser:str|None=None,

decoding_config:object|None=None,

_mpi_session:object|None=None,

otlp_traces_endpoint:str|None=None,

backend:~typing.Literal['pytorch']='pytorch',

return_perf_metrics:bool=False,

perf_metrics_max_requests:~typing.Annotated[int,

~annotated_types.Ge(ge=0)]=0,

orchestrator_type:~typing.Literal['rpc',

'ray']|None=None,

env_overrides:~typing.Dict[str,

str]|None=None,

garbage_collection_gen0_threshold:int=20000,

cuda_graph_config:~tensorrt_llm.llmapi.llm_args.CudaGraphConfig|None=<factory>,

attention_dp_config:~tensorrt_llm.llmapi.llm_args.AttentionDpConfig|None=None,

disable_overlap_scheduler:bool=False,

moe_config:~tensorrt_llm.llmapi.llm_args.MoeConfig=<factory>,

nvfp4_gemm_config:~tensorrt_llm.llmapi.llm_args.Nvfp4GemmConfig=<factory>,

attn_backend:str='TRTLLM',

sampler_type:str|~tensorrt_llm.llmapi.llm_args.SamplerType=SamplerType.auto,

sampler_force_async_worker:bool=False,

enable_iter_perf_stats:bool=False,

enable_iter_req_stats:bool=False,

print_iter_log:bool=False,

batch_wait_timeout_ms:~typing.Annotated[float,

~annotated_types.Ge(ge=0)]=0,

batch_wait_timeout_iters:~typing.Annotated[int,

~annotated_types.Ge(ge=0)]=0,

batch_wait_max_tokens_ratio:~typing.Annotated[float,

~annotated_types.Ge(ge=0),

~annotated_types.Le(le=1)]=0,

torch_compile_config:~tensorrt_llm.llmapi.llm_args.TorchCompileConfig|None=None,

enable_autotuner:bool=True,

enable_layerwise_nvtx_marker:bool=False,

enable_min_latency:bool=False,

stream_interval:~typing.Annotated[int,

~annotated_types.Gt(gt=0)]=1,

force_dynamic_quantization:bool=False,

allreduce_strategy:~typing.Literal['AUTO',

'NCCL',

'UB',

'MINLATENCY',

'ONESHOT',

'TWOSHOT',

'LOWPRECISION',

'MNNVL',

'NCCL_SYMMETRIC']|None='AUTO',

checkpoint_loader:object|None=None,

checkpoint_format:str|None=None,

kv_connector_config:~tensorrt_llm.llmapi.llm_args.KvCacheConnectorConfig|None=None,

mm_encoder_only:bool=False,

ray_worker_extension_cls:str|None=None,

ray_placement_config:~tensorrt_llm.llmapi.llm_args.RayPlacementConfig|None=None,

ray_worker_nsight_options:dict[str,

str]|None=None,

enable_sleep:bool=False,

use_cute_dsl_blockscaling_mm:bool=False,

use_cute_dsl_blockscaling_bmm:bool=False,

disable_flashinfer_sampling:bool=False,

max_stats_len:int=1000,

layer_wise_benchmarks_config:~tensorrt_llm.llmapi.llm_args.LayerwiseBenchmarksConfig=<factory>,

)[source]#

Bases: `BaseLlmArgs`

fieldallreduce_strategy:Literal['AUTO','NCCL','UB','MINLATENCY','ONESHOT','TWOSHOT','LOWPRECISION','MNNVL','NCCL_SYMMETRIC']|None='AUTO'#

`beta` Allreduce strategy to use.

fieldattention_dp_config:AttentionDpConfig|None=None#

`beta` Optimized load-balancing for the DP Attention scheduler.

fieldattn_backend:str='TRTLLM'#

`beta` Attention backend to use.

fieldbackend:Literal['pytorch']='pytorch'#

`deprecated` The backend to use for this LLM instance.

fieldbatch_wait_max_tokens_ratio:float=0#

`prototype` Token accumulation threshold ratio for batch scheduling optimization. If greater than 0, the scheduler will accumulate requests locally until the total token count reaches batch_wait_max_tokens_ratio * max_num_tokens. This mechanism enhances GPU utilization efficiency by ensuring adequate batch sizes. If 0, disables token-based batching delays.

Constraints:

ge = 0

le = 1

fieldbatch_wait_timeout_iters:Annotated[int,Ge(ge=0)]=0#

`prototype` Maximum number of iterations the scheduler will wait to accumulate new coming requests for improved GPU utilization efficiency. If greater than 0, the scheduler will delay batch processing to gather more requests up to the specified iteration limit. If 0, disables timeout-iters-based batching delays.

Constraints:

ge = 0

fieldbatch_wait_timeout_ms:Annotated[float,Ge(ge=0)]=0#

`prototype` If greater than 0, the request queue might wait up to batch_wait_timeout_ms to receive max_batch_size requests, if fewer than max_batch_size requests are currently available. If 0, no waiting occurs.

Constraints:

ge = 0

fieldbatched_logits_processor:object|None=None#

`stable` Batched logits processor.

fieldcache_transceiver_config:CacheTransceiverConfig|None=None#

`prototype` Cache transceiver config.

fieldcheckpoint_format:str|None=None#

`prototype` The format of the provided checkpoint. You may use a custom checkpoint format by subclassing BaseCheckpointLoader and registering it with register_checkpoint_loader.
If neither checkpoint_format nor checkpoint_loader are provided, checkpoint_format will be set to HF and the default HfCheckpointLoader will be used.
If checkpoint_format and checkpoint_loader are both provided, checkpoint_loader will be ignored.

fieldcheckpoint_loader:object|None=None#

`prototype` The checkpoint loader to use for this LLM instance. You may use a custom checkpoint loader by subclassing BaseCheckpointLoader and providing an instance of the subclass here to load weights from a custom checkpoint format.
If neither checkpoint_format nor checkpoint_loader are provided, checkpoint_format will be set to HF and the default HfCheckpointLoader will be used.
If checkpoint_format and checkpoint_loader are both provided, checkpoint_loader will be ignored.

fieldcontext_parallel_size:int=1#

`stable` The context parallel size.

fieldcp_config:CpConfig|None=None#

`prototype` Context parallel config.

fieldcuda_graph_config:CudaGraphConfig|None[Optional]#

`beta` CUDA graph config. If true, use CUDA graphs for decoding. CUDA graphs are only created for the batch sizes in cuda_graph_config.batch_sizes, and are enabled for batches that consist of decoding requests only (the reason is that it’s hard to capture a single graph with prefill requests since the input shapes are a function of the sequence lengths). Note that each CUDA graph can use up to 200 MB of extra memory.

fieldcustom_tokenizer:str|None=None#

`prototype` Specify a custom tokenizer implementation. Accepts either: (1) a built-in alias (e.g., ‘deepseek_v32’), or (2) a Python import path (e.g., ‘tensorrt_llm.tokenizer.deepseek_v32.DeepseekV32Tokenizer’). The tokenizer class must implement ‘from_pretrained(path, **kwargs)’ and the TokenizerBase interface.

fielddisable_flashinfer_sampling:bool=False#

`prototype` Disable the use of FlashInfer.sampling. This option is likely to be removed in the future.

fielddisable_overlap_scheduler:bool=False#

`beta` Disable the overlap scheduler.

fielddtype:str='auto'#

`stable` The data type to use for the model.

fieldenable_attention_dp:bool=False#

`beta` Enable attention data parallel.

fieldenable_autotuner:bool=True#

`prototype` Enable autotuner for all tunable ops. This flag is for debugging purposes only, and the performance may significantly degrade if set to false.

fieldenable_chunked_prefill:bool=False#

`stable` Enable chunked prefill.

fieldenable_iter_perf_stats:bool=False#

`prototype` Enable iteration performance statistics.

fieldenable_iter_req_stats:bool=False#

`prototype` If true, enables per request stats per iteration. Must also set enable_iter_perf_stats to true to get request stats.

fieldenable_layerwise_nvtx_marker:bool=False#

`beta` If true, enable layerwise nvtx marker.

fieldenable_lm_head_tp_in_adp:bool=False#

`prototype` Enable LM head TP in attention dp.

fieldenable_lora:bool=False#

`stable` Enable LoRA.

fieldenable_min_latency:bool=False#

`beta` If true, enable min-latency mode. Currently only used for Llama4.

fieldenable_sleep:bool=False#

`prototype` Enable LLM sleep feature. Sleep feature requires extra setup that may slow down model loading. Only enable it if you intend to use this feature.

fieldenv_overrides:Dict[str,str]|None=None#

`prototype` [EXPERIMENTAL] Environment variable overrides. NOTE: import-time-cached env vars in the code won’t update unless the code fetches them from os.environ on demand.

fieldforce_dynamic_quantization:bool=False#

`prototype` If true, force dynamic quantization. Defaults to False.

fieldgarbage_collection_gen0_threshold:int=20000#

`beta` Threshold for Python garbage collection of generation 0 objects. Lower values trigger more frequent garbage collection.

fieldgather_generation_logits:bool=False#

`prototype` Gather generation logits.

fieldgpus_per_node:int|None=None#

`beta` The number of GPUs per node.

fieldguided_decoding_backend:Literal['xgrammar','llguidance']|None=None#

`stable` Guided decoding backend. llguidance is supported in PyTorch backend only.

fielditer_stats_max_iterations:int|None=None#

`prototype` The maximum number of iterations for iter stats.

fieldkv_cache_config:KvCacheConfig[Optional]#

`stable` KV cache config.

fieldkv_connector_config:KvCacheConnectorConfig|None=None#

`prototype` The config for KV cache connector.

fieldlayer_wise_benchmarks_config:LayerwiseBenchmarksConfig[Optional]#

`prototype` Configuration for layer-wise benchmarks calibration.

fieldload_format:str|LoadFormat=LoadFormat.AUTO#

`stable` How to load the model weights. By default, detect the weight type from the model checkpoint.

fieldlora_config:LoraConfig|None=None#

`stable` LoRA configuration for the model.

fieldmax_batch_size:int|None=2048#

`stable` The maximum batch size.

fieldmax_beam_width:int|None=1#

`stable` The maximum beam width.

fieldmax_input_len:int|None=1024#

`stable` The maximum input length.

fieldmax_num_tokens:int|None=8192#

`stable` The maximum number of tokens.

fieldmax_seq_len:int|None=None#

`stable` The maximum sequence length.

fieldmax_stats_len:int=1000#

`prototype` The max number of performance statistic entries.

fieldmm_encoder_only:bool=False#

`prototype` Only load/execute the vision encoder part of the full model. Defaults to False.

fieldmodel:str|Path[Required]#

`stable` The path to the model checkpoint or the model name from the Hugging Face Hub.

fieldmodel_kwargs:Dict[str,Any]|None=None#

`prototype` Optional parameters overriding model config defaults. Precedence: (1) model_kwargs, (2) model config file, (3) model config class defaults. Unknown keys are ignored

fieldmoe_cluster_parallel_size:int|None=None#

`beta` The cluster parallel size for MoE model’s expert weights.

fieldmoe_config:MoeConfig[Optional]#

`beta` MoE config.

fieldmoe_expert_parallel_size:int|None=None#

`stable` The expert parallel size for MoE model’s expert weights.

fieldmoe_tensor_parallel_size:int|None=None#

`stable` The tensor parallel size for MoE model’s expert weights.

fieldmpi_session:object|None=None(alias'_mpi_session')#

`stable` The optional MPI session to use for this LLM instance.

fieldnum_postprocess_workers:int=0#

`prototype` The number of processes used for postprocessing the generated tokens, including detokenization.

fieldnvfp4_gemm_config:Nvfp4GemmConfig[Optional]#

`beta` NVFP4 GEMM backend config.

fieldorchestrator_type:Literal['rpc','ray']|None=None#

`prototype` The orchestrator type to use. Defaults to None, which uses MPI.

fieldotlp_traces_endpoint:str|None=None#

`prototype` Target URL to which OpenTelemetry traces will be sent.

fieldpeft_cache_config:PeftCacheConfig|None=None#

`prototype` PEFT cache config.

fieldperf_metrics_max_requests:NonNegativeInt=0#

`prototype` The maximum number of requests for perf metrics. Must also set return_perf_metrics to true to get perf metrics.

Constraints:

ge = 0

fieldpipeline_parallel_size:int=1#

`stable` The pipeline parallel size.

fieldpostprocess_tokenizer_dir:str|None=None#

`prototype` The path to the tokenizer directory for postprocessing.

fieldpp_partition:List[int]|None=None#

`prototype` Pipeline parallel partition, a list of each rank’s layer number.

fieldprint_iter_log:bool=False#

`beta` Print iteration logs.

fieldray_placement_config:RayPlacementConfig|None=None#

`prototype` Placement config for RayGPUWorker. Only used with AsyncLLM and orchestrator_type=’ray’.

fieldray_worker_extension_cls:str|None=None#

`prototype` The full worker extension class name including module path. Allows users to extend the functions of the RayGPUWorker class.

fieldray_worker_nsight_options:dict[str,str]|None=None#

`prototype` Nsight options.

fieldreasoning_parser:str|None=None#

`prototype` The parser to separate reasoning content from output.

fieldrequest_stats_max_iterations:int|None=None#

`prototype` The maximum number of iterations for request stats.

fieldreturn_perf_metrics:bool=False#

`prototype` Return perf metrics.

fieldrevision:str|None=None#

`stable` The revision to use for the model.

fieldsampler_force_async_worker:bool=False#

`prototype` Force usage of the async worker in the sampler for D2H copies, even if confidential compute is not active. Normally, the async worker should only be used when confidential compute is active. This argument is provided to enable it for testing purposes, irrespective of confidential compute state.

fieldsampler_type:str|SamplerType=SamplerType.auto#

`beta` The type of sampler to use. Options are TRTLLMSampler, TorchSampler or auto. Defaults to auto, which will use TorchSampler unless BeamSearch is requested.

fieldscheduler_config:SchedulerConfig[Optional]#

`prototype` Scheduler config.

fieldskip_tokenizer_init:bool=False#

`stable` Whether to skip the tokenizer initialization.

fieldsparse_attention_config:SparseAttentionConfig|None=None#

`prototype` Sparse attention config.

fieldspeculative_config:SpeculativeConfig|None=None#

`stable` Speculative decoding config.

fieldstream_interval:Annotated[int,Gt(gt=0)]=1#

`stable` The iteration interval to create responses under the streaming mode. Set this to a larger value when the batch size is large, which helps reduce the streaming overhead.

Constraints:

gt = 0

fieldtensor_parallel_size:int=1#

`stable` The tensor parallel size.

fieldtokenizer:str|Path|TokenizerBase|PreTrainedTokenizerBase|None=None#

`stable` The path to the tokenizer checkpoint or the tokenizer name from the Hugging Face Hub.

fieldtokenizer_mode:Literal['auto','slow']='auto'#

`stable` The mode to initialize the tokenizer.

fieldtokenizer_revision:str|None=None#

`stable` The revision to use for the tokenizer.

fieldtorch_compile_config:TorchCompileConfig|None=None#

`prototype` Torch compile config.

fieldtrust_remote_code:bool=False#

`stable` Whether to trust the remote code.

fielduse_cute_dsl_blockscaling_bmm:bool=False#

`prototype` If true, use CuTe DSL fp8 blockscaling bmm implementation.

fielduse_cute_dsl_blockscaling_mm:bool=False#

`prototype` If true, use CuTe DSL fp8 blockscaling mm implementation.

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

validatorcoerce_env_overrides_to_str»env_overrides#

Coerce env_overrides values to strings for os.environ compatibility.

validatorconvert_load_format»load_format[source]#

classmethodfrom_yaml(yaml_path:str|Path)#

get_executor_config(

_hf_model_dir:Path|None=None,

tokenizer:TokenizerBase|None=None,

)→ExecutorConfig[source]#

get_runtime_sizes()→Tuple[int,int,int,int]#

validatornormalize_optional_fields_to_defaults»allfields#

Normalize certain fields to their declared default values in case a user explicitly sets them to None.

This is necessary because downstream code expects these fields to be non-None.
At the same time, we still need to accept None as a valid value to avoid a breaking change.

validatorset_model_format»allfields[source]#

validatorsync_quant_config_with_kv_cache_config_dtype»allfields[source]#

validatorvalidate_and_init_tokenizer»allfields#

Initialize tokenizer based on configuration.

validatorvalidate_checkpoint_format»allfields[source]#

validatorvalidate_dtype»dtype#

validatorvalidate_gpus_per_node»gpus_per_node#

validatorvalidate_helix_tokens_per_block»allfields[source]#

Validate that cp_config.tokens_per_block matches kv_cache_config.tokens_per_block when HELIX parallelism is active.

validatorvalidate_load_balancer»allfields[source]#

validatorvalidate_lora_config_consistency»allfields#

validatorvalidate_parallel_config»allfields#

validatorvalidate_peft_cache_config»allfields#

validatorvalidate_ray_placement_config»allfields[source]#

validatorvalidate_ray_worker_extension_cls»allfields[source]#

validatorvalidate_runtime_args»allfields#

validatorvalidate_speculative_config»allfields[source]#

warn_on_unstable_feature_usage()→TorchLlmArgs[source]#

Warn on unstable feature usage.

decoding_config:object|None#

Read-only data descriptor used to emit a runtime deprecation warning before accessing a deprecated field.

msg#

The deprecation message to be emitted.

wrapped_property#

The property instance if the deprecated field is a computed field, or None.

field_name#

The name of the field being deprecated.

propertyextra_resource_managers:Dict[str,object]#

propertymodel_format:_ModelFormatKind#

propertyparallel_config:_ParallelConfig#

propertyquant_config:QuantConfig#

propertyspeculative_model:str|Path|None#

classtensorrt_llm.llmapi.TrtLlmArgs(

model:str|~pathlib.Path,

tokenizer:str|~pathlib.Path|~transformers.tokenization_utils_base.PreTrainedTokenizerBase|~tensorrt_llm.tokenizer.tokenizer.TokenizerBase|None=None,

tokenizer_mode:~typing.Literal['auto',

'slow']='auto',

custom_tokenizer:str|None=None,

skip_tokenizer_init:bool=False,

trust_remote_code:bool=False,

tensor_parallel_size:int=1,

dtype:str='auto',

revision:str|None=None,

tokenizer_revision:str|None=None,

model_kwargs:~typing.Dict[str,

~typing.Any]|None=None,

pipeline_parallel_size:int=1,

context_parallel_size:int=1,

gpus_per_node:int|None=None,

moe_cluster_parallel_size:int|None=None,

moe_tensor_parallel_size:int|None=None,

moe_expert_parallel_size:int|None=None,

enable_attention_dp:bool=False,

enable_lm_head_tp_in_adp:bool=False,

pp_partition:~typing.List[int]|None=None,

cp_config:~tensorrt_llm.llmapi.llm_args.CpConfig|None=None,

load_format:~typing.Literal['auto',

'dummy']='auto',

enable_lora:bool=False,

lora_config:~tensorrt_llm.lora_helper.LoraConfig|None=None,

kv_cache_config:~tensorrt_llm.llmapi.llm_args.KvCacheConfig=<factory>,

enable_chunked_prefill:bool=False,

guided_decoding_backend:~typing.Literal['xgrammar',

'llguidance']|None=None,

batched_logits_processor:object|None=None,

iter_stats_max_iterations:int|None=None,

request_stats_max_iterations:int|None=None,

peft_cache_config:~tensorrt_llm.llmapi.llm_args.PeftCacheConfig|None=None,

scheduler_config:~tensorrt_llm.llmapi.llm_args.SchedulerConfig=<factory>,

cache_transceiver_config:~tensorrt_llm.llmapi.llm_args.CacheTransceiverConfig|None=None,

sparse_attention_config:~typing.Annotated[~tensorrt_llm.llmapi.llm_args.RocketSparseAttentionConfig|~tensorrt_llm.llmapi.llm_args.DeepSeekSparseAttentionConfig|~tensorrt_llm.llmapi.llm_args.SkipSoftmaxAttentionConfig,

FieldInfo(annotation=NoneType,

required=True,

discriminator='algorithm')]|None=None,

speculative_config:~typing.Annotated[~tensorrt_llm.llmapi.llm_args.DraftTargetDecodingConfig|~tensorrt_llm.llmapi.llm_args.EagleDecodingConfig|~tensorrt_llm.llmapi.llm_args.Eagle3DecodingConfig|~tensorrt_llm.llmapi.llm_args.LookaheadDecodingConfig|~tensorrt_llm.llmapi.llm_args.MedusaDecodingConfig|~tensorrt_llm.llmapi.llm_args.MTPDecodingConfig|~tensorrt_llm.llmapi.llm_args.NGramDecodingConfig|~tensorrt_llm.llmapi.llm_args.SADecodingConfig|~tensorrt_llm.llmapi.llm_args.UserProvidedDecodingConfig|~tensorrt_llm.llmapi.llm_args.SaveHiddenStatesDecodingConfig|~tensorrt_llm.llmapi.llm_args.PARDDecodingConfig|~tensorrt_llm.llmapi.llm_args.AutoDecodingConfig,

FieldInfo(annotation=NoneType,

required=True,

discriminator='decoding_type')]|None=None,

max_batch_size:int|None=2048,

max_input_len:int|None=1024,

max_seq_len:int|None=None,

max_beam_width:int|None=1,

max_num_tokens:int|None=8192,

gather_generation_logits:bool=False,

num_postprocess_workers:int=0,

postprocess_tokenizer_dir:str|None=None,

reasoning_parser:str|None=None,

decoding_config:object|None=None,

_mpi_session:object|None=None,

otlp_traces_endpoint:str|None=None,

backend:str|None=None,

return_perf_metrics:bool=False,

perf_metrics_max_requests:~typing.Annotated[int,

~annotated_types.Ge(ge=0)]=0,

orchestrator_type:~typing.Literal['rpc',

'ray']|None=None,

env_overrides:~typing.Dict[str,

str]|None=None,

enable_tqdm:bool=False,

workspace:str|None=None,

fail_fast_on_attention_window_too_large:bool=False,

enable_build_cache:~tensorrt_llm.llmapi.build_cache.BuildCacheConfig|bool=False,

extended_runtime_perf_knob_config:~tensorrt_llm.llmapi.llm_args.ExtendedRuntimePerfKnobConfig|None=None,

calib_config:~tensorrt_llm.llmapi.llm_args.CalibConfig=<factory>,

quant_config:~tensorrt_llm.models.modeling_utils.QuantConfig=<factory>,

embedding_parallel_mode:~typing.Literal['NONE',

'SHARDING_ALONG_VOCAB',

'SHARDING_ALONG_HIDDEN']='SHARDING_ALONG_VOCAB',

fast_build:bool=False,

build_config:~tensorrt_llm.builder.BuildConfig|None=None,

enable_prompt_adapter:bool=False,

max_prompt_adapter_token:int=0,

batching_type:~tensorrt_llm.llmapi.llm_args.BatchingType|None=None,

normalize_log_probs:bool=False,

)[source]#

Bases: `BaseLlmArgs`

fieldbackend:str|None=None#

The backend to use for this LLM instance.

fieldbatched_logits_processor:object|None=None#

Batched logits processor.

fieldbatching_type:BatchingType|None=None#

Batching type.

fieldbuild_config:BuildConfig|None=None#

Build config.

fieldcache_transceiver_config:CacheTransceiverConfig|None=None#

Cache transceiver config.

fieldcalib_config:CalibConfig[Optional]#

Calibration config.

fieldcontext_parallel_size:int=1#

The context parallel size.

fieldcp_config:CpConfig|None=None#

Context parallel config.

fieldcustom_tokenizer:str|None=None#

Specify a custom tokenizer implementation. Accepts either: (1) a built-in alias (e.g., ‘deepseek_v32’), or (2) a Python import path (e.g., ‘tensorrt_llm.tokenizer.deepseek_v32.DeepseekV32Tokenizer’). The tokenizer class must implement ‘from_pretrained(path, **kwargs)’ and the TokenizerBase interface.

fielddtype:str='auto'#

The data type to use for the model.

fieldembedding_parallel_mode:Literal['NONE','SHARDING_ALONG_VOCAB','SHARDING_ALONG_HIDDEN']='SHARDING_ALONG_VOCAB'#

The embedding parallel mode.

fieldenable_attention_dp:bool=False#

Enable attention data parallel.

fieldenable_build_cache:BuildCacheConfig|bool=False#

Enable build cache.

fieldenable_chunked_prefill:bool=False#

Enable chunked prefill.

fieldenable_lm_head_tp_in_adp:bool=False#

Enable LM head TP in attention dp.

fieldenable_lora:bool=False#

Enable LoRA.

fieldenable_prompt_adapter:bool=False#

Enable prompt adapter.

fieldenable_tqdm:bool=False#

Enable tqdm for progress bar.

fieldenv_overrides:Dict[str,str]|None=None#

[EXPERIMENTAL] Environment variable overrides. NOTE: import-time-cached env vars in the code won’t update unless the code fetches them from os.environ on demand.

fieldextended_runtime_perf_knob_config:ExtendedRuntimePerfKnobConfig|None=None#

Extended runtime perf knob config.

fieldfail_fast_on_attention_window_too_large:bool=False#

Fail fast when attention window is too large to fit even a single sequence in the KV cache.

fieldfast_build:bool=False#

Enable fast build.

fieldgather_generation_logits:bool=False#

Gather generation logits.

fieldgpus_per_node:int|None=None#

The number of GPUs per node.

fieldguided_decoding_backend:Literal['xgrammar','llguidance']|None=None#

Guided decoding backend. llguidance is supported in PyTorch backend only.

fielditer_stats_max_iterations:int|None=None#

The maximum number of iterations for iter stats.

fieldkv_cache_config:KvCacheConfig[Optional]#

KV cache config.

fieldload_format:Literal['auto','dummy']='auto'#

The format to load the model.

fieldlora_config:LoraConfig|None=None#

LoRA configuration for the model.

fieldmax_batch_size:int|None=2048#

The maximum batch size.

fieldmax_beam_width:int|None=1#

The maximum beam width.

fieldmax_input_len:int|None=1024#

The maximum input length.

fieldmax_num_tokens:int|None=8192#

The maximum number of tokens.

fieldmax_prompt_adapter_token:int=0#

The maximum number of prompt adapter tokens.

fieldmax_seq_len:int|None=None#

The maximum sequence length.

fieldmodel:str|Path[Required]#

The path to the model checkpoint or the model name from the Hugging Face Hub.

fieldmodel_kwargs:Dict[str,Any]|None=None#

Optional parameters overriding model config defaults. Precedence: (1) model_kwargs, (2) model config file, (3) model config class defaults. Unknown keys are ignored

fieldmoe_cluster_parallel_size:int|None=None#

The cluster parallel size for MoE model’s expert weights.

fieldmoe_expert_parallel_size:int|None=None#

The expert parallel size for MoE model’s expert weights.

fieldmoe_tensor_parallel_size:int|None=None#

The tensor parallel size for MoE model’s expert weights.

fieldmpi_session:object|None=None(alias'_mpi_session')#

The optional MPI session to use for this LLM instance.

fieldnormalize_log_probs:bool=False#

Normalize log probabilities.

fieldnum_postprocess_workers:int=0#

The number of processes used for postprocessing the generated tokens, including detokenization.

fieldorchestrator_type:Literal['rpc','ray']|None=None#

The orchestrator type to use. Defaults to None, which uses MPI.

fieldotlp_traces_endpoint:str|None=None#

Target URL to which OpenTelemetry traces will be sent.

fieldpeft_cache_config:PeftCacheConfig|None=None#

PEFT cache config.

fieldperf_metrics_max_requests:NonNegativeInt=0#

The maximum number of requests for perf metrics. Must also set return_perf_metrics to true to get perf metrics.

Constraints:

ge = 0

fieldpipeline_parallel_size:int=1#

The pipeline parallel size.

fieldpostprocess_tokenizer_dir:str|None=None#

The path to the tokenizer directory for postprocessing.

fieldpp_partition:List[int]|None=None#

Pipeline parallel partition, a list of each rank’s layer number.

fieldquant_config:QuantConfig[Optional]#

Quantization config.

fieldreasoning_parser:str|None=None#

The parser to separate reasoning content from output.

fieldrequest_stats_max_iterations:int|None=None#

The maximum number of iterations for request stats.

fieldreturn_perf_metrics:bool=False#

Return perf metrics.

fieldrevision:str|None=None#

The revision to use for the model.

fieldscheduler_config:SchedulerConfig[Optional]#

Scheduler config.

fieldskip_tokenizer_init:bool=False#

Whether to skip the tokenizer initialization.

fieldsparse_attention_config:SparseAttentionConfig|None=None#

Sparse attention config.

fieldspeculative_config:SpeculativeConfig|None=None#

Speculative decoding config.

fieldtensor_parallel_size:int=1#

The tensor parallel size.

fieldtokenizer:str|Path|TokenizerBase|PreTrainedTokenizerBase|None=None#

The path to the tokenizer checkpoint or the tokenizer name from the Hugging Face Hub.

fieldtokenizer_mode:Literal['auto','slow']='auto'#

The mode to initialize the tokenizer.

fieldtokenizer_revision:str|None=None#

The revision to use for the tokenizer.

fieldtrust_remote_code:bool=False#

Whether to trust the remote code.

fieldworkspace:str|None=None#

The workspace for the model.

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

validatorcoerce_env_overrides_to_str»env_overrides#

Coerce env_overrides values to strings for os.environ compatibility.

classmethodfrom_yaml(yaml_path:str|Path)#

get_runtime_sizes()→Tuple[int,int,int,int]#

validatorinit_build_config»allfields[source]#

Creating a default BuildConfig if none is provided

validatornormalize_optional_fields_to_defaults»allfields#

Normalize certain fields to their declared default values in case a user explicitly sets them to None.

This is necessary because downstream code expects these fields to be non-None.
At the same time, we still need to accept None as a valid value to avoid a breaking change.

validatorsetup_embedding_parallel_mode»allfields[source]#

validatorvalidate_and_init_tokenizer»allfields#

Initialize tokenizer based on configuration.

validatorvalidate_build_config_remaining»allfields[source]#

validatorvalidate_build_config_with_runtime_params»allfields[source]#

Sync runtime parameters with build_config limits.

This validator runs AFTER validate_model_format_misc so that when
loading from an engine, we have the real build_config loaded.

validatorvalidate_dtype»dtype#

validatorvalidate_enable_build_cache»allfields[source]#

validatorvalidate_gpus_per_node»gpus_per_node#

validatorvalidate_kv_cache_dtype»allfields[source]#

validatorvalidate_lora_config_consistency»allfields#

validatorvalidate_model_format_misc»allfields[source]#

Load the model format, and do the following:

Load the build_config if got an engine.

Load the parallel_config if got a checkpoint.

validatorvalidate_parallel_config»allfields#

validatorvalidate_peft_cache_config»allfields#

validatorvalidate_runtime_args»allfields#

validatorvalidate_speculative_config»allfields[source]#

decoding_config:object|None#

Read-only data descriptor used to emit a runtime deprecation warning before accessing a deprecated field.

msg#

The deprecation message to be emitted.

wrapped_property#

The property instance if the deprecated field is a computed field, or None.

field_name#

The name of the field being deprecated.

propertymodel_format:_ModelFormatKind#

propertyparallel_config:_ParallelConfig#

propertyspeculative_model:str|Path|None#

classtensorrt_llm.llmapi.AutoDecodingConfig(

max_draft_len:Annotated[int,Ge(ge=0)]|None=None,

max_total_draft_tokens:int|None=None,

speculative_model:str|Path|None=None,

max_concurrency:Annotated[int,Ge(ge=0)]|None=None,

draft_len_schedule:dict[int,int]|None=None,

load_format:str|None=None,

acceptance_window:Annotated[int,Ge(ge=0)]|None=None,

acceptance_length_threshold:Annotated[float,Ge(ge=0)]|None=None,

allow_advanced_sampling:bool=False,

decoding_type:Literal['AUTO']='AUTO',

)[source]#

Bases: `DecodingBaseConfig`

Configuration for auto speculative decoding.

This config will automatically select a good, draft-model free
speculation algorithm with some heuristic.

Attributes that are inherited from the base class are ignored.

fieldacceptance_length_threshold:NonNegativeFloat|None=None#

The threshold for average acceptance length; speculation will be disabled permanently once the rolling average over the last N completed requests (N = acceptance_window) drops below this value. PyTorch backend only.

fieldacceptance_window:NonNegativeInt|None=None#

The rolling average window size (N) for acceptance length across completed requests. If not set or set to 0, the feature is disabled. PyTorch backend only.

fieldallow_advanced_sampling:bool=False#

If true, allows non-greedy sampling when speculation is used. Only applicable to 1-model code paths; non-greedy sampling is always enabled on 2-model paths.

fielddecoding_type:Literal['AUTO']='AUTO'#

fielddraft_len_schedule:dict[int,int]|None=None#

Developer interface: dynamically adjust draft length based on active batch size in runtime. Maps batch size to draft lengths. For example, {1: 4, 4: 2, 8: 0} means: batch_size >= 1 uses draft_len=4, batch_size >= 4 uses draft_len=2, batch_size >= 8 uses draft_len=0 (disable speculation). draft_len_schedule is enforced to contain batch_size=1 and its according draft_len equals max_draft_len for consistency; for example, if max_draft_len=4, the schedule must contain {1: 4}.

fieldload_format:str|None=None#

The load format of the speculative model.

fieldmax_concurrency:NonNegativeInt|None=None#

When specified, speculation will be disabled at batch sizes above this value. Otherwise, speculation will always be on. PyTorch backend only.

fieldmax_draft_len:NonNegativeInt|None=None#

The maximum number of draft tokens.

fieldmax_total_draft_tokens:int|None=None#

The number of draft tokens in the draft tokens tree. If it’s a linear tree, each draft layer will only generate one draft token. In this case, max_draft_len == max_total_draft_tokens. If it’s a static or dynamic tree, each draft layer may generate more than one draft token. In this case, max_total_draft_tokens >= max_draft_len.

fieldspeculative_model:str|Path|None=None#

The speculative (draft) model. Accepts either (1) a HuggingFace Hub model ID (e.g. ‘yuhuili/EAGLE3-LLaMA3.1-Instruct-8B’), which will be automatically downloaded, or (2) a local filesystem path to a downloaded model directory.

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(obj:Any)→Self#

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(context:Any, /)→None#

This function is meant to behave like a BaseModel method to initialise private attributes.

It takes context as an argument since that’s what pydantic-core passes when calling it.

Parameters:

self – The BaseModel instance.

context – The context.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

num_capture_layers()→int#

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(obj:Any)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

validatorset_max_total_draft_tokens»allfields[source]#

supports_backend(backend:str)→bool[source]#

Override if the speculation algorithm does not support
a subset of the possible backends.

classmethodupdate_forward_refs(**localns:Any)→None#

classmethodvalidate(value:Any)→Self#

validatorvalidate_draft_len_schedule_and_sort»draft_len_schedule#

Validate and sort draft_len_schedule by batch size thresholds.

propertyis_linear_tree:bool#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'acceptance_length_threshold':FieldInfo(annotation=Union[Annotated[float,Ge],NoneType],required=False,default=None,description='Thethresholdforaverageacceptancelength;speculationwillbedisabledpermanentlyoncetherollingaverageoverthelastNcompletedrequests(N=acceptance_window)dropsbelowthisvalue.PyTorchbackendonly.'),'acceptance_window':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Therollingaveragewindowsize(N)foracceptancelengthacrosscompletedrequests.Ifnotsetorsetto0,thefeatureisdisabled.PyTorchbackendonly.'),'allow_advanced_sampling':FieldInfo(annotation=bool,required=False,default=False,description='Iftrue,allowsnon-greedysamplingwhenspeculationisused.Onlyapplicableto1-modelcodepaths;non-greedysamplingisalwaysenabledon2-modelpaths.',json_schema_extra={'status':'prototype'}),'decoding_type':FieldInfo(annotation=Literal['AUTO'],required=False,default='AUTO'),'draft_len_schedule':FieldInfo(annotation=Union[dict[int,int],NoneType],required=False,default=None,description='Developerinterface:dynamicallyadjustdraftlengthbasedonactivebatchsizeinruntime.Mapsbatchsizetodraftlengths.Forexample,{1:4,4:2,8:0}means:batch_size>=1usesdraft_len=4,batch_size>=4usesdraft_len=2,batch_size>=8usesdraft_len=0(disablespeculation).draft_len_scheduleisenforcedtocontainbatch_size=1anditsaccordingdraft_lenequalsmax_draft_lenforconsistency;forexample,ifmax_draft_len=4,theschedulemustcontain{1:4}.'),'load_format':FieldInfo(annotation=Union[str,NoneType],required=False,default=None,description='Theloadformatofthespeculativemodel.'),'max_concurrency':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Whenspecified,speculationwillbedisabledatbatchsizesabovethisvalue.Otherwise,speculationwillalwaysbeon.PyTorchbackendonly.'),'max_draft_len':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Themaximumnumberofdrafttokens.'),'max_total_draft_tokens':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description="Thenumberofdrafttokensinthedrafttokenstree.Ifit'salineartree,eachdraftlayerwillonlygenerateonedrafttoken.Inthiscase,max_draft_len==max_total_draft_tokens.Ifit'sastaticordynamictree,eachdraftlayermaygeneratemorethanonedrafttoken.Inthiscase,max_total_draft_tokens>=max_draft_len."),'speculative_model':FieldInfo(annotation=Union[str,Path,NoneType],required=False,default=None,alias_priority=2,validation_alias=AliasChoices(choices=['speculative_model','speculative_model_dir']),description="Thespeculative(draft)model.Acceptseither(1)aHuggingFaceHubmodelID(e.g.'yuhuili/EAGLE3-LLaMA3.1-Instruct-8B'),whichwillbeautomaticallydownloaded,or(2)alocalfilesystempathtoadownloadedmodeldirectory.")}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

propertyspec_dec_mode#

propertytokens_per_gen_step:int#

Total tokens per gen request in one spec dec iteration (including golden token).

classtensorrt_llm.llmapi.AttentionDpConfig(

enable_balance:bool=False,

timeout_iters:int=50,

batching_wait_iters:int=10,

)[source]#

Bases: `StrictBaseModel`

Configuration for attention DP.

fieldbatching_wait_iters:int=10#

The number of iterations to wait for batching.

fieldenable_balance:bool=False#

Whether to enable balance.

fieldtimeout_iters:int=50#

The number of iterations to timeout.

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(obj:Any)→Self#

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(context:Any, /)→None#

Override this method to perform additional initialization after __init__ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(obj:Any)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

classmethodupdate_forward_refs(**localns:Any)→None#

classmethodvalidate(value:Any)→Self#

validatorvalidate_attention_dp_config»allfields[source]#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'batching_wait_iters':FieldInfo(annotation=int,required=False,default=10,description='Thenumberofiterationstowaitforbatching.'),'enable_balance':FieldInfo(annotation=bool,required=False,default=False,description='Whethertoenablebalance.'),'timeout_iters':FieldInfo(annotation=int,required=False,default=50,description='Thenumberofiterationstotimeout.')}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

classtensorrt_llm.llmapi.LoRARequest(

lora_name:str,

lora_int_id:int,

lora_path:str='',

lora_ckpt_source:str='hf',

)[source]#

Bases: `object`

Request for a LoRA adapter.

__init__(

lora_name:str,

lora_int_id:int,

lora_path:str='',

lora_ckpt_source:str='hf',

)→None#

propertyadapter_id#

propertyckpt_source#

lora_ckpt_source:str#

lora_int_id:int#

lora_name:str#

lora_path:str#

propertyname#

propertypath#

classtensorrt_llm.llmapi.SaveHiddenStatesDecodingConfig(

max_draft_len:Annotated[int,Ge(ge=0)]|None=None,

max_total_draft_tokens:int|None=1,

speculative_model:str|Path|None=None,

max_concurrency:Annotated[int,Ge(ge=0)]|None=None,

draft_len_schedule:dict[int,int]|None=None,

load_format:str|None=None,

acceptance_window:Annotated[int,Ge(ge=0)]|None=None,

acceptance_length_threshold:Annotated[float,Ge(ge=0)]|None=None,

allow_advanced_sampling:bool=False,

decoding_type:Literal['SaveState']='SaveState',

output_directory:str,

write_interval:int=20,

file_prefix:str='data',

eagle3_layers_to_capture:Set[int]|None=None,

eagle_choices:List[List[int]]|None=None,

)[source]#

Bases: `DecodingBaseConfig`

fieldacceptance_length_threshold:NonNegativeFloat|None=None#

The threshold for average acceptance length; speculation will be disabled permanently once the rolling average over the last N completed requests (N = acceptance_window) drops below this value. PyTorch backend only.

fieldacceptance_window:NonNegativeInt|None=None#

The rolling average window size (N) for acceptance length across completed requests. If not set or set to 0, the feature is disabled. PyTorch backend only.

fieldallow_advanced_sampling:bool=False#

If true, allows non-greedy sampling when speculation is used. Only applicable to 1-model code paths; non-greedy sampling is always enabled on 2-model paths.

fielddecoding_type:Literal['SaveState']='SaveState'#

fielddraft_len_schedule:dict[int,int]|None=None#

Developer interface: dynamically adjust draft length based on active batch size in runtime. Maps batch size to draft lengths. For example, {1: 4, 4: 2, 8: 0} means: batch_size >= 1 uses draft_len=4, batch_size >= 4 uses draft_len=2, batch_size >= 8 uses draft_len=0 (disable speculation). draft_len_schedule is enforced to contain batch_size=1 and its according draft_len equals max_draft_len for consistency; for example, if max_draft_len=4, the schedule must contain {1: 4}.

fieldeagle3_layers_to_capture:Set[int]|None=None#

Set of target model layer indices to capture hidden states from for EAGLE3 draft model training. Use -1 to indicate the final post-norm hidden state. If not provided, defaults to capturing 3 intermediate layers plus the post-norm hidden state. When provided, -1 is automatically added if not present.

fieldeagle_choices:List[List[int]]|None=None#

Internal field, not user-configurable. Always None since this mode does not use tree-based draft token structures.

fieldfile_prefix:str='data'#

Prefix for output filenames. Files are saved as ‘<file_prefix>_<iteration>.pt’ containing input_ids and hidden_state tensors.

fieldload_format:str|None=None#

The load format of the speculative model.

fieldmax_concurrency:NonNegativeInt|None=None#

When specified, speculation will be disabled at batch sizes above this value. Otherwise, speculation will always be on. PyTorch backend only.

fieldmax_draft_len:NonNegativeInt|None=None#

The maximum number of draft tokens.

fieldmax_total_draft_tokens:int|None=1#

Internal field, not user-configurable. Fixed to 1 since this mode captures hidden states without draft token generation.

fieldoutput_directory:str[Required]#

Directory path where hidden states data files will be saved. The directory is created if it does not exist.

fieldspeculative_model:str|Path|None=None#

The speculative (draft) model. Accepts either (1) a HuggingFace Hub model ID (e.g. ‘yuhuili/EAGLE3-LLaMA3.1-Instruct-8B’), which will be automatically downloaded, or (2) a local filesystem path to a downloaded model directory.

fieldwrite_interval:int=20#

Number of requests to process before writing accumulated hidden states to disk. Lower values write more frequently but may impact performance.

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(

obj:Any,

)→Self#

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(

_SaveHiddenStatesDecodingConfig__context,

)[source]#

This function is meant to behave like a BaseModel method to initialise private attributes.

It takes context as an argument since that’s what pydantic-core passes when calling it.

Parameters:

self – The BaseModel instance.

context – The context.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(

obj:Any,

)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

supports_backend(backend:str)→bool#

Override if the speculation algorithm does not support
a subset of the possible backends.

classmethodupdate_forward_refs(

**localns:Any,

)→None#

classmethodvalidate(

value:Any,

)→Self#

validatorvalidate_draft_len_schedule_and_sort»draft_len_schedule#

Validate and sort draft_len_schedule by batch size thresholds.

propertyis_linear_tree:bool#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'acceptance_length_threshold':FieldInfo(annotation=Union[Annotated[float,Ge],NoneType],required=False,default=None,description='Thethresholdforaverageacceptancelength;speculationwillbedisabledpermanentlyoncetherollingaverageoverthelastNcompletedrequests(N=acceptance_window)dropsbelowthisvalue.PyTorchbackendonly.'),'acceptance_window':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Therollingaveragewindowsize(N)foracceptancelengthacrosscompletedrequests.Ifnotsetorsetto0,thefeatureisdisabled.PyTorchbackendonly.'),'allow_advanced_sampling':FieldInfo(annotation=bool,required=False,default=False,description='Iftrue,allowsnon-greedysamplingwhenspeculationisused.Onlyapplicableto1-modelcodepaths;non-greedysamplingisalwaysenabledon2-modelpaths.',json_schema_extra={'status':'prototype'}),'decoding_type':FieldInfo(annotation=Literal['SaveState'],required=False,default='SaveState'),'draft_len_schedule':FieldInfo(annotation=Union[dict[int,int],NoneType],required=False,default=None,description='Developerinterface:dynamicallyadjustdraftlengthbasedonactivebatchsizeinruntime.Mapsbatchsizetodraftlengths.Forexample,{1:4,4:2,8:0}means:batch_size>=1usesdraft_len=4,batch_size>=4usesdraft_len=2,batch_size>=8usesdraft_len=0(disablespeculation).draft_len_scheduleisenforcedtocontainbatch_size=1anditsaccordingdraft_lenequalsmax_draft_lenforconsistency;forexample,ifmax_draft_len=4,theschedulemustcontain{1:4}.'),'eagle3_layers_to_capture':FieldInfo(annotation=Union[Set[int],NoneType],required=False,default=None,description='SetoftargetmodellayerindicestocapturehiddenstatesfromforEAGLE3draftmodeltraining.Use-1toindicatethefinalpost-normhiddenstate.Ifnotprovided,defaultstocapturing3intermediatelayersplusthepost-normhiddenstate.Whenprovided,-1isautomaticallyaddedifnotpresent.'),'eagle_choices':FieldInfo(annotation=Union[List[List[int]],NoneType],required=False,default=None,description='Internalfield,notuser-configurable.AlwaysNonesincethismodedoesnotusetree-baseddrafttokenstructures.',init=False),'file_prefix':FieldInfo(annotation=str,required=False,default='data',description="Prefixforoutputfilenames.Filesaresavedas'<file_prefix>_<iteration>.pt'containinginput_idsandhidden_statetensors."),'load_format':FieldInfo(annotation=Union[str,NoneType],required=False,default=None,description='Theloadformatofthespeculativemodel.'),'max_concurrency':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Whenspecified,speculationwillbedisabledatbatchsizesabovethisvalue.Otherwise,speculationwillalwaysbeon.PyTorchbackendonly.'),'max_draft_len':FieldInfo(annotation=Union[Annotated[int,Ge],NoneType],required=False,default=None,description='Themaximumnumberofdrafttokens.'),'max_total_draft_tokens':FieldInfo(annotation=Union[int,NoneType],required=False,default=1,description='Internalfield,notuser-configurable.Fixedto1sincethismodecaptureshiddenstateswithoutdrafttokengeneration.',init=False),'output_directory':FieldInfo(annotation=str,required=True,description='Directorypathwherehiddenstatesdatafileswillbesaved.Thedirectoryiscreatedifitdoesnotexist.'),'speculative_model':FieldInfo(annotation=Union[str,Path,NoneType],required=False,default=None,alias_priority=2,validation_alias=AliasChoices(choices=['speculative_model','speculative_model_dir']),description="Thespeculative(draft)model.Acceptseither(1)aHuggingFaceHubmodelID(e.g.'yuhuili/EAGLE3-LLaMA3.1-Instruct-8B'),whichwillbeautomaticallydownloaded,or(2)alocalfilesystempathtoadownloadedmodeldirectory."),'write_interval':FieldInfo(annotation=int,required=False,default=20,description='Numberofrequeststoprocessbeforewritingaccumulatedhiddenstatestodisk.Lowervalueswritemorefrequentlybutmayimpactperformance.')}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

propertynum_capture_layers#

Returns the number of layers to save.
The following hidden states are saved:
- If eagle3_layers_to_capture is None, save the eagle3 base set plus
the post norm last hidden state.
- Otherwise, save the specified layers plus the post norm last hidden state.

The saved data will contain two tensors, hidden_states and aux_hidden_states.
* hidden_states will contain the last post norm state.
* aux_hidden_states will contain all other captured layers. The last hidden state
will also be included in this tensor if you explicitly captured layer -1.

Note that if you set layers to capture to {-1}, aux_hidden_states won’t exist.

propertyspec_dec_mode#

propertytokens_per_gen_step:int#

Total tokens per gen request in one spec dec iteration (including golden token).

classtensorrt_llm.llmapi.RocketSparseAttentionConfig(

algorithm:Literal['rocket']='rocket',

seq_len_threshold:int|None=None,

window_size:int|None=32,

kernel_size:int|None=63,

topr:int|float|None=128,

topk:int|None=64,

prompt_budget:int|None=2048,

page_size:int|None=4,

kt_cache_dtype:str|None='float8_e5m2',

)[source]#

Bases: `BaseSparseAttentionConfig`

Configuration for RocketKV sparse attention.

fieldalgorithm:Literal['rocket']='rocket'#

fieldkernel_size:int|None=63#

The kernel size for RocketKV.

fieldkt_cache_dtype:str|None='float8_e5m2'#

KT cache dtype

fieldpage_size:int|None=4#

Page size

fieldprompt_budget:int|None=2048#

Prompt budget

fieldseq_len_threshold:int|None=None#

The sequence length threshold for separating short and long sequences.

fieldtopk:int|None=64#

Top-k

fieldtopr:int|float|None=128#

Top-r

fieldwindow_size:int|None=32#

The window size for RocketKV.

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(obj:Any)→Self#

get_indices_block_size()→int[source]#

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(

context:Any,

)→None#

Override this method to perform additional initialization after __init__ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

needs_separate_short_long_cuda_graphs()→bool#

Determines whether to capture a dedicated CUDA graph for batches consisting entirely of short sequences.
If True, capture distinct graphs for short-only batches and general cases (e.g., long or mixed batches).
If False, capture a single unified CUDA graph for all sequences regardless of length.
The seq_len_threshold parameter defines the cutoff boundary between short and long sequences.

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(

obj:Any,

)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

supports_backend(backend:str)→bool[source]#

Override if the sparse attention algorithm does not support
a subset of the possible backends.

classmethodupdate_forward_refs(

**localns:Any,

)→None#

classmethodvalidate(

value:Any,

)→Self#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'algorithm':FieldInfo(annotation=Literal['rocket'],required=False,default='rocket'),'kernel_size':FieldInfo(annotation=Union[int,NoneType],required=False,default=63,description='ThekernelsizeforRocketKV.'),'kt_cache_dtype':FieldInfo(annotation=Union[str,NoneType],required=False,default='float8_e5m2',description='KTcachedtype',json_schema_extra={'choices':['bfloat16','float8_e5m2']}),'page_size':FieldInfo(annotation=Union[int,NoneType],required=False,default=4,description='Pagesize'),'prompt_budget':FieldInfo(annotation=Union[int,NoneType],required=False,default=2048,description='Promptbudget'),'seq_len_threshold':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description='Thesequencelengththresholdforseparatingshortandlongsequences.'),'topk':FieldInfo(annotation=Union[int,NoneType],required=False,default=64,description='Top-k'),'topr':FieldInfo(annotation=Union[int,float,NoneType],required=False,default=128,description='Top-r'),'window_size':FieldInfo(annotation=Union[int,NoneType],required=False,default=32,description='ThewindowsizeforRocketKV.')}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

classtensorrt_llm.llmapi.DeepSeekSparseAttentionConfig(

algorithm:Literal['dsa']='dsa',

seq_len_threshold:int|None=None,

index_n_heads:int|None=None,

index_head_dim:int|None=None,

index_topk:int|None=None,

indexer_max_chunk_size:int|None=None,

skip_indexer_for_short_seqs:bool=True,

)[source]#

Bases: `BaseSparseAttentionConfig`

Configuration for DeepSeek Sparse Attention.

fieldalgorithm:Literal['dsa']='dsa'#

fieldindex_head_dim:int|None=None#

The dimension of the indexer heads.

fieldindex_n_heads:int|None=None#

The number of heads for the indexer.

fieldindex_topk:int|None=None#

The topk for the indexer.

fieldindexer_max_chunk_size:int|None=None#

The maximum chunk size for the indexer.

fieldseq_len_threshold:int|None=None#

The sequence length threshold for separating short and long sequences.

fieldskip_indexer_for_short_seqs:bool=True#

Whether to skip the MQA and Top-K in the indexer for short sequences.

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(

obj:Any,

)→Self#

get_indices_block_size()→int#

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(

context:Any,

)→None#

Override this method to perform additional initialization after __init__ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

needs_separate_short_long_cuda_graphs()→bool[source]#

Whether to capture separate CUDA graphs for short and long sequences.
Use seq_len_threshold to determine the threshold for separating short and long sequences.

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(

obj:Any,

)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

supports_backend(backend:str)→bool[source]#

Override if the sparse attention algorithm does not support
a subset of the possible backends.

classmethodupdate_forward_refs(

**localns:Any,

)→None#

classmethodvalidate(

value:Any,

)→Self#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'algorithm':FieldInfo(annotation=Literal['dsa'],required=False,default='dsa'),'index_head_dim':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description='Thedimensionoftheindexerheads.'),'index_n_heads':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description='Thenumberofheadsfortheindexer.'),'index_topk':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description='Thetopkfortheindexer.'),'indexer_max_chunk_size':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description='Themaximumchunksizefortheindexer.'),'seq_len_threshold':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description='Thesequencelengththresholdforseparatingshortandlongsequences.'),'skip_indexer_for_short_seqs':FieldInfo(annotation=bool,required=False,default=True,description='WhethertoskiptheMQAandTop-Kintheindexerforshortsequences.')}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

classtensorrt_llm.llmapi.SkipSoftmaxAttentionConfig(

algorithm:Literal['skip_softmax']='skip_softmax',

seq_len_threshold:int|None=None,

threshold_scale_factor:float|Dict[str,float]|None=None,

)[source]#

Bases: `BaseSparseAttentionConfig`

Configuration for skip softmax attention.

fieldalgorithm:Literal['skip_softmax']='skip_softmax'#

fieldseq_len_threshold:int|None=None#

The sequence length threshold for separating short and long sequences.

fieldthreshold_scale_factor:float|Dict[str,float]|None=None#

The threshold scale factor for skip softmax attention.

classConfig#

Bases: `object`

extra='forbid'#

__init__(**data:Any)→None#

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

classmethodconstruct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

copy(

include:AbstractSetIntStr|MappingIntStrAny|None=None,

exclude:AbstractSetIntStr|MappingIntStrAny|None=None,

update:Dict[str,Any]|None=None,

deep:bool=False,

)→Self#

Returns a copy of the model.

!!! warning “Deprecated”

This method is now deprecated; use model_copy instead.

If you need include or exclude, use:

``python{test="skip"lint="skip"}data=self.model_dump(include=include,exclude=exclude,round_trip=True)data={**data,**(updateor{})}copied=self.model_validate(data)``

Parameters:

include – Optional set or mapping specifying which fields to include in the copied model.

exclude – Optional set or mapping specifying which fields to exclude in the copied model.

update – Optional dictionary of field-value pairs to override field values in the copied model.

deep – If True, the values of fields that are Pydantic models will be deep-copied.

Returns:

A copy of the model with included, excluded and updated fields as specified.

dict(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

)→Dict[str,Any]#

classmethodfrom_orm(obj:Any)→Self#

get_indices_block_size()→int#

json(

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

by_alias:bool=False,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

encoder:Callable[[Any],Any]|None=PydanticUndefined,

models_as_dict:bool=PydanticUndefined,

**dumps_kwargs:Any,

)→str#

classmethodmodel_construct(

_fields_set:set[str]|None=None,

**values:Any,

)→Self#

Creates a new instance of the Model class with validated data.

Creates a new model setting __dict__ and __pydantic_fields_set__ from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note

model_construct() generally respects the model_config.extra setting on the provided model.
That is, if model_config.extra == ‘allow’, then all extra passed values are added to the model instance’s __dict__
and __pydantic_extra__ fields. If model_config.extra == ‘ignore’ (the default), then all extra passed values are ignored.
Because no validation is performed with a call to model_construct(), having model_config.extra == ‘forbid’ does not result in
an error if extra values are passed, but they will be ignored.

Parameters:

_fields_set – A set of field names that were originally explicitly set during instantiation. If provided,
this is directly used for the [model_fields_set][pydantic.BaseModel.model_fields_set] attribute.
Otherwise, the field names from the values argument will be used.

values – Trusted or pre-validated data dictionary.

Returns:

A new instance of the Model class with validated data.

model_copy(

update:Mapping[str,Any]|None=None,

deep:bool=False,

)→Self#

!!! abstract “Usage Documentation”

[model_copy](../concepts/serialization.md#model_copy)

Returns a copy of the model.

!!! note

The underlying instance’s [__dict__][object.__dict__] attribute is copied. This
might have unexpected side effects if you store anything in it, on top of the model
fields (e.g. the value of [cached properties][functools.cached_property]).

Parameters:

update – Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data.

deep – Set to True to make a deep copy of the model.

Returns:

New model instance.

model_dump(

mode:Literal['json','python']|str='python',

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→dict[str,Any]#

!!! abstract “Usage Documentation”

[model_dump](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Parameters:

mode – The mode in which to_python should run.
If mode is ‘json’, the output will only contain JSON serializable types.
If mode is ‘python’, the output may contain non-JSON-serializable Python objects.

include – A set of fields to include in the output.

exclude – A set of fields to exclude from the output.

context – Additional context to pass to the serializer.

by_alias – Whether to use the field’s alias in the dictionary key if defined.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A dictionary representation of the model.

model_dump_json(

indent:int|None=None,

include:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

exclude:set[int]|set[str]|Mapping[int,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|Mapping[str,set[int]|set[str]|Mapping[int,IncEx|bool]|Mapping[str,IncEx|bool]|bool]|None=None,

context:Any|None=None,

by_alias:bool|None=None,

exclude_unset:bool=False,

exclude_defaults:bool=False,

exclude_none:bool=False,

round_trip:bool=False,

warnings:bool|Literal['none','warn','error']=True,

fallback:Callable[[Any],Any]|None=None,

serialize_as_any:bool=False,

)→str#

!!! abstract “Usage Documentation”

[model_dump_json](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic’s to_json method.

Parameters:

indent – Indentation to use in the JSON output. If None is passed, the output will be compact.

include – Field(s) to include in the JSON output.

exclude – Field(s) to exclude from the JSON output.

context – Additional context to pass to the serializer.

by_alias – Whether to serialize using field aliases.

exclude_unset – Whether to exclude fields that have not been explicitly set.

exclude_defaults – Whether to exclude fields that are set to their default value.

exclude_none – Whether to exclude fields that have a value of None.

round_trip – If True, dumped values should be valid as input for non-idempotent types such as Json[T].

warnings – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
“error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

fallback – A function to call when an unknown value is encountered. If not provided,
a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.

serialize_as_any – Whether to serialize fields with duck-typing serialization behavior.

Returns:

A JSON string representation of the model.

classmethodmodel_json_schema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

schema_generator:type[~pydantic.json_schema.GenerateJsonSchema]=<class'pydantic.json_schema.GenerateJsonSchema'>,

mode:~typing.Literal['validation',

'serialization']='validation',

)→dict[str,Any]#

Generates a JSON schema for a model class.

Parameters:

by_alias – Whether to use attribute aliases or not.

ref_template – The reference template.

schema_generator – To override the logic used to generate the JSON schema, as a subclass of
GenerateJsonSchema with your desired modifications

mode – The mode in which to generate the schema.

Returns:

The JSON schema for the given model class.

classmethodmodel_parametrized_name(

params:tuple[type[Any],...],

)→str#

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Parameters:

params – Tuple of types of the class. Given a generic class
Model with 2 type variables and a concrete model Model[str, int],
the value (str, int) would be passed to params.

Returns:

String representing the new class where params are passed to cls as type variables.

Raises:

TypeError – Raised when trying to generate concrete names for non-generic models.

model_post_init(

context:Any,

)→None#

Override this method to perform additional initialization after __init__ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

classmethodmodel_rebuild(

force:bool=False,

raise_errors:bool=True,

_parent_namespace_depth:int=2,

_types_namespace:MappingNamespace|None=None,

)→bool|None#

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Parameters:

force – Whether to force the rebuilding of the model schema, defaults to False.

raise_errors – Whether to raise errors, defaults to True.

_parent_namespace_depth – The depth level of the parent namespace, defaults to 2.

_types_namespace – The types namespace, defaults to None.

Returns:

Returns None if the schema is already “complete” and rebuilding was not required.
If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.

classmethodmodel_validate(

obj:Any,

strict:bool|None=None,

from_attributes:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate a pydantic model instance.

Parameters:

obj – The object to validate.

strict – Whether to enforce types strictly.

from_attributes – Whether to extract data from object attributes.

context – Additional context to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Raises:

ValidationError – If the object could not be validated.

Returns:

The validated model instance.

classmethodmodel_validate_json(

json_data:str|bytes|bytearray,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

!!! abstract “Usage Documentation”

[JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

Parameters:

json_data – The JSON data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

Raises:

ValidationError – If json_data is not a JSON string or the object could not be validated.

classmethodmodel_validate_strings(

obj:Any,

strict:bool|None=None,

context:Any|None=None,

by_alias:bool|None=None,

by_name:bool|None=None,

)→Self#

Validate the given object with string data against the Pydantic model.

Parameters:

obj – The object containing string data to validate.

strict – Whether to enforce types strictly.

context – Extra variables to pass to the validator.

by_alias – Whether to use the field’s alias when validating against the provided input data.

by_name – Whether to use the field’s name when validating against the provided input data.

Returns:

The validated Pydantic model.

needs_separate_short_long_cuda_graphs()→bool#

Determines whether to capture a dedicated CUDA graph for batches consisting entirely of short sequences.
If True, capture distinct graphs for short-only batches and general cases (e.g., long or mixed batches).
If False, capture a single unified CUDA graph for all sequences regardless of length.
The seq_len_threshold parameter defines the cutoff boundary between short and long sequences.

classmethodparse_file(

path:str|Path,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodparse_obj(obj:Any)→Self#

classmethodparse_raw(

b:str|bytes,

content_type:str|None=None,

encoding:str='utf8',

proto:DeprecatedParseProtocol|None=None,

allow_pickle:bool=False,

)→Self#

classmethodschema(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

)→Dict[str,Any]#

classmethodschema_json(

by_alias:bool=True,

ref_template:str='#/$defs/{model}',

**dumps_kwargs:Any,

)→str#

supports_backend(backend:str)→bool[source]#

Override if the sparse attention algorithm does not support
a subset of the possible backends.

classmethodupdate_forward_refs(

**localns:Any,

)→None#

classmethodvalidate(

value:Any,

)→Self#

model_computed_fields={}#

model_config:ClassVar[ConfigDict]={'extra':'forbid'}#

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

propertymodel_extra:dict[str,Any]|None#

Get extra fields set during validation.

Returns:

A dictionary of extra fields, or None if config.extra is not set to “allow”.

model_fields={'algorithm':FieldInfo(annotation=Literal['skip_softmax'],required=False,default='skip_softmax'),'seq_len_threshold':FieldInfo(annotation=Union[int,NoneType],required=False,default=None,description='Thesequencelengththresholdforseparatingshortandlongsequences.'),'threshold_scale_factor':FieldInfo(annotation=Union[float,Dict[str,float],NoneType],required=False,default=None,description='Thethresholdscalefactorforskipsoftmaxattention.')}#

propertymodel_fields_set:set[str]#

Returns the set of fields that have been explicitly set on this model instance.

Returns:

A set of strings representing the fields that have been set,

i.e. that were not filled from defaults.

propertythreshold_scale_factor_decode:float|None#

propertythreshold_scale_factor_prefill:float|None#
