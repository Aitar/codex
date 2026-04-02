# Inference pipeline — lmdeploy

Source: https://lmdeploy.readthedocs.io/en/latest/api/pipeline.html

Inference pipeline

Inference pipeline#

Pipeline#

lmdeploy.pipeline(model_path, backend_config=None, chat_template_config=None, log_level='WARNING', max_log_len=None, speculative_config=None, **kwargs)[source]#

Create a pipeline for inference.

Parameters:

model_path (`str`) –
the path of a model. It could be one of the following options:

i) A local directory path of a turbomind model which is
converted by `lmdeployconvert` command or download from
ii) and iii).

ii) The model_id of a lmdeploy-quantized model hosted
inside a model repo on huggingface.co, such as
`InternLM/internlm-chat-20b-4bit`,
`lmdeploy/llama2-chat-70b-4bit`, etc.

iii) The model_id of a model hosted inside a model repo
on huggingface.co, such as `internlm/internlm-chat-7b`,
`Qwen/Qwen-7B-Chat`, `baichuan-inc/Baichuan2-7B-Chat`
and so on.

backend_config (`Union`[`TurbomindEngineConfig`, `PytorchEngineConfig`, `None`]) – backend config instance. Default to None.

chat_template_config (`Optional`[`ChatTemplateConfig`]) – chat template configuration. Default to None.

log_level (`str`) – set log level whose value among [`CRITICAL`, `ERROR`,
`WARNING`, `INFO`, `DEBUG`]

max_log_len (`Optional`[`int`]) – Max number of prompt characters or prompt tokens
being printed in log.

speculative_config (`Optional`[`SpeculativeConfig`]) – speculative decoding configuration.

**kwargs – additional keyword arguments passed to the pipeline.

Returns:

a pipeline instance for inference.

Return type:

Pipeline

Examples

```text
# LLM
import lmdeploy
pipe = lmdeploy.pipeline('internlm/internlm-chat-7b')
response = pipe(['hi','say this is a test'])
print(response)

# VLM
from lmdeploy.vl import load_image
from lmdeploy import pipeline, TurbomindEngineConfig, ChatTemplateConfig
pipe = pipeline('liuhaotian/llava-v1.5-7b',
                backend_config=TurbomindEngineConfig(session_len=8192),
                chat_template_config=ChatTemplateConfig(model_name='vicuna'))
im = load_image('https://raw.githubusercontent.com/open-mmlab/mmdeploy/main/demo/resources/human-pose.jpg')
response = pipe([('describe this image', [im])])
print(response)
```

classlmdeploy.Pipeline(model_path, backend_config=None, chat_template_config=None, log_level='WARNING', max_log_len=None, speculative_config=None, **kwargs)[source]#

Bases: `object`

Pipeline - User-facing API layer for inference.

__init__(model_path, backend_config=None, chat_template_config=None, log_level='WARNING', max_log_len=None, speculative_config=None, **kwargs)[source]#

Initialize Pipeline.

Parameters:

model_path (`str`) – Path to the model.

backend_config (`Union`[`TurbomindEngineConfig`, `PytorchEngineConfig`, `None`]) – Backend configuration.

chat_template_config (`Optional`[`ChatTemplateConfig`]) – Chat template configuration.

log_level (`str`) – Log level.

max_log_len (`Optional`[`int`]) – Max number of prompt characters or prompt tokens being printed in log.

speculative_config (`Optional`[`SpeculativeConfig`]) – Speculative decoding configuration.

**kwargs – Additional keyword arguments.

infer(prompts, gen_config=None, do_preprocess=True, adapter_name=None, use_tqdm=False, **kwargs)[source]#

Inference prompts.

Parameters:

prompts (`list`[`str`] | `str` | `list`[`dict`] | `list`[`list`[`dict`]] | `tuple` | `list`[`tuple`]) – Prompts for inference. It can be a single prompt, a list of prompts, a list of tuples, or a tuple.
tuple can be (prompt, image or [images]) or (image or [images], prompt).

gen_config (`Union`[`GenerationConfig`, `list`[`GenerationConfig`], `None`]) – Generation configuration(s).

do_preprocess (`bool`) – Whether to pre-process messages.

adapter_name (`Optional`[`str`]) – Adapter name.

use_tqdm (`bool`) – Whether to use progress bar.

**kwargs – Additional keyword arguments.

Returns:

A single response or a list of responses.

Return type:

Response | list[Response]

stream_infer(prompts, sessions=None, gen_config=None, do_preprocess=True, adapter_name=None, stream_response=True, **kwargs)[source]#

Stream inference.

Parameters:

prompts (`list`[`str`] | `str` | `list`[`dict`] | `list`[`list`[`dict`]] | `tuple` | `list`[`tuple`]) – Prompts to inference. It can be a single prompt, a list of prompts, a list of tuples, or a tuple.
tuple can be (prompt, image or [images]) or (image or [images], prompt).

sessions (`Union`[`Session`, `list`[`Session`], `None`]) – Sessions. Each of which corresponds to a prompt.

gen_config (`Union`[`GenerationConfig`, `list`[`GenerationConfig`], `None`]) – Generation configuration(s).

do_preprocess (`bool`) – Whether to pre-process messages.

adapter_name (`Optional`[`str`]) – Adapter name.

stream_response (`bool`) – Whether to stream the response. If True, the generator will stream the response.
Otherwise, the generator will run until finish and return the final response. This argument
is introduced to support the streaming and non-streaming modes of Pipeline.chat.

**kwargs – Additional keyword arguments.

Returns:

A generator that yields the output (i.e. instance of class `Response`) of the inference.

Return type:

Iterator

chat(prompt, session=None, gen_config=None, stream_response=False, adapter_name=None, **kwargs)[source]#

Chat.

Parameters:

prompt (`str` | `tuple`[`str`, `Image` | `list`[`Image`]]) – prompt string or a tuple of (prompt, image or [images]).

session – the chat session.

gen_config (`Optional`[`GenerationConfig`]) – an instance of GenerationConfig. Default to None.

stream_response – whether to stream the response.

adapter_name – adapter name.

**kwargs – additional keyword arguments.

Returns:

the updated session, or a streaming iterator if stream_response is True.

Return type:

Session | Iterator

get_ppl(input_ids)[source]#

Get perplexity scores given a list of input tokens that have to be
of the same length.

Parameters:

input_ids (`list`[`int`] | `list`[`list`[`int`]]) – the batch of input token ids.

Returns:

A list of perplexity scores.

Return type:

list[float]

Config#

classlmdeploy.PytorchEngineConfig(dtype='auto', tp=1, dp=1, dp_rank=0, ep=1, session_len=None, max_batch_size=None, attn_tp_size=None, mlp_tp_size=None, moe_tp_size=None, cache_max_entry_count=0.8, prefill_interval=16, block_size=64, num_cpu_blocks=0, num_gpu_blocks=0, adapters=None, max_prefill_token_num=4096, thread_safe=False, enable_prefix_caching=False, device_type='cuda', eager_mode=False, custom_module_map=None, download_dir=None, revision=None, quant_policy=0, distributed_executor_backend=None, empty_init=False, enable_microbatch=False, enable_eplb=False, enable_mp_engine=False, mp_engine_backend='mp', model_format=None, enable_metrics=True, hf_overrides=None, disable_vision_encoder=False, logprobs_mode=None, enable_return_routed_experts=False, enable_transfer_obj_ref=False, dllm_block_length=None, dllm_unmasking_strategy='low_confidence_dynamic', dllm_denoising_steps=None, dllm_confidence_threshold=0.85, role=EngineRole.Hybrid, migration_backend=MigrationBackend.DLSlime)[source]#

PyTorch Engine Config.

Parameters:

dtype (`str`) – data type for model weights and activations. It can be
one of the following values, [‘auto’, ‘float16’, ‘bfloat16’]
The auto option will use FP16 precision for FP32 and FP16
models, and BF16 precision for BF16 models.

tp (`int`) – Tensor Parallelism. default 1.

dp (`int`) – Data Parallelism. default 1.

dp_rank (`int`) – rank of dp.

ep (`int`) – Expert Parallelism. default 1.

session_len (`Optional`[`int`]) – Max session length. Default None.

max_batch_size (`Optional`[`int`]) – Max batch size. If it is not specified,
the engine will automatically set it according to the device

attn_tp_size (`Optional`[`int`]) – tp size for attention, only works for dp>1

mlp_tp_size (`Optional`[`int`]) – tp size for mlp, only works for dp>1

moe_tp_size (`Optional`[`int`]) – tp size for moe, only works for dp>1

cache_max_entry_count (`float`) – the percentage of gpu memory occupied
by the k/v cache. For lmdeploy versions greater than v0.2.1,
it defaults to 0.8, signifying the percentage of FREE GPU memory
to be reserved for the k/v cache

prefill_interval (`int`) – Interval to perform prefill,
Default 16.

block_size (`int`) – paging cache block size, default 64.

num_cpu_blocks (`int`) – Num cpu blocks. If num is 0, cache
would be allocate according to current environment.

num_gpu_blocks (`int`) – Num gpu blocks. If num is 0, cache
would be allocate according to current environment.

adapters (`Optional`[`dict`[`str`, `str`]]) – The path configs to lora adapters.

max_prefill_token_num (`int`) – tokens per iteration.

thread_safe (`bool`) – thread safe engine instance.

enable_prefix_caching (`bool`) – Enable token match and sharing caches.

device_type (`str`) – The inference device type, options [‘cuda’]

eager_mode (`bool`) – Enable “eager” mode or not

custom_module_map (`Optional`[`dict`[`str`, `str`]]) – nn module map customized by users. Once
provided, the original nn modules of the model will be
substituted by the mapping ones

download_dir (`Optional`[`str`]) – Directory to download and load the weights,
default to the default cache directory of huggingface.

revision (`Optional`[`str`]) – The specific model version to use.
It can be a branch name, a tag name, or a commit id.
If unspecified, will use the default version.

quant_policy (`Literal`[`0`, `4`, `8`]) – default to 0. When k/v is quantized into 4 or 8
bit, set it to 4 or 8, respectively

distributed_executor_backend (`Optional`[`str`]) – backend of distributed backend,
options: [‘uni’, ‘mp’, ‘ray’]

empty_init (`bool`) – Whether to load the model weights, you should set
it to True if you want to update weights after create the pipeline

enable_microbatch (`bool`) – enable microbatch for specified model

enable_eplb (`bool`) – enable eplb for specified model

enable_metrics (`bool`) – enable metrics system

role (`EngineRole`) – role of engin, options: [‘Hybrid’, ‘Prefill’,
‘Decode’]. Default to EngineRole.Hybrid.

migration_backend (`MigrationBackend`) – migration backend. options: [‘DLSlime’].
Default to MigrationBackend.DLSlime.

enable_mp_engine (`bool`) – run engine in multi-process mode.

mp_engine_backend (`str`) – backend of mp engine, options:
[‘mp’, ‘ray’]. Default to mp.

model_format (`Optional`[`str`]) – weight quantization policy, options: [‘fp8’].

hf_overrides (`Optional`[`dict`[`str`, `Any`]]) – Huggingface overrides for the model.
It can be used to override the default config of the model,

disable_vision_encoder (`bool`) – Whether to disable loading vision
encoder. Default to False.

logprobs_mode (`Optional`[`str`]) – The mode of logprob, options: [‘raw_logits’, ‘raw_logprobs’]

dllm_block_length (`Optional`[`int`]) – Block size of block diffusion model.

dllm_unmasking_strategy (`str`) – Dllm unmasking strategy, options:
[‘low_confidence_dynamic’, ‘low_confidence_static’, ‘sequential’].

dllm_denoising_steps (`Optional`[`int`]) – Dllm denoising steps.

dllm_confidence_threshold (`float`) – dllm unmasking threshold for
dynamic unmasking.

classlmdeploy.TurbomindEngineConfig(*args, **kwargs)[source]#

TurboMind Engine config.

Parameters:

dtype – data type for model weights and activations. It can be
one of the following values, [‘auto’, ‘float16’, ‘bfloat16’]
The auto option will use FP16 precision for FP32 and FP16
models, and BF16 precision for BF16 models.

model_format – the layout of the deployed model. It can be one
of the following values [hf, awq, gptq, compressed-tensors,
fp8, mxfp4]. hf means a Hugging Face model (.bin,
.safetensors), awq and gptq mean grouped 4-bit
weight-only checkpoints, compressed-tensors means
pack-quantized grouped int4 checkpoints and is usually
auto-detected from the input model config, fp8 means
blocked fp8 checkpoints, and mxfp4 means MXFP4 expert
weights. If it is not specified, i.e. None, it will be
extracted from the input model

tp – the number of GPU cards used in tensor parallelism,
default to 1

session_len – the max session length of a sequence, default to
None

max_batch_size – the max batch size during inference. If it is
not specified, the engine will automatically set it according to
the device

cache_max_entry_count – the percentage of gpu memory occupied
by the k/v cache.
For versions of lmdeploy between v0.2.0 and v0.2.1, it
defaults to 0.5, depicting the percentage of TOTAL GPU memory to
be allocated to the k/v cache.
For lmdeploy versions greater than v0.2.1, it defaults to 0.8,
signifying the percentage of FREE GPU memory to be reserved for
the k/v cache.
When it’s an integer > 0, it represents the total number of k/v
blocks.

cache_chunk_size – The policy to apply for KV block from
the block manager, default to -1.

cache_block_seq_len – the length of the token sequence in
a k/v block, default to 64

enable_prefix_caching – enable cache prompts for block reuse,
default to False

quant_policy – default to 0. When k/v is quantized into 4 or 8
bit, set it to 4 or 8, respectively

rope_scaling_factor – scaling factor used for dynamic ntk,
default to 0. TurboMind follows the implementation of transformer
LlamaAttention

use_logn_attn – whether or not to use log attn: default to False

download_dir – Directory to download and load the weights,
default to the default cache directory of huggingface.

revision – The specific model version to use. It can be a branch
name, a tag name, or a commit id. If unspecified, will use the
default version.

max_prefill_token_num – the number of tokens each iteration during
prefill, default to 8192

num_tokens_per_iter – the number of tokens processed in each
forward pass. Working with max_prefill_iters enables the
“Dynamic SplitFuse”-like scheduling

max_prefill_iters – the max number of forward pass during prefill
stage

async – enable async execution, default to 1 (enabled)

devices – the used devices

empty_init – Whether to load the model weights, you should set
it to True if you want to update weights after create the pipeline

hf_overrides – Huggingface overrides for the model.
It can be used to override the default config of the model

enable_metrics – enable metrics system

classlmdeploy.GenerationConfig(n=1, max_new_tokens=512, do_sample=False, top_p=1.0, top_k=50, min_p=0.0, temperature=0.8, repetition_penalty=1.0, ignore_eos=False, random_seed=None, stop_words=None, bad_words=None, stop_token_ids=None, bad_token_ids=None, min_new_tokens=None, skip_special_tokens=True, spaces_between_special_tokens=True, logprobs=None, response_format=None, logits_processors=None, output_logits=None, output_last_hidden_state=None, include_stop_str_in_output=False, with_cache=False, preserve_cache=False, migration_request=None, return_routed_experts=False, repetition_ngram_size=0, repetition_ngram_threshold=0)[source]#

Generation parameters used by inference engines.

Parameters:

n (`int`) – Define how many chat completion choices to generate for each
input message. Only 1 is supported now.

max_new_tokens (`int`) – The maximum number of tokens that can be
generated in the chat completion

do_sample (`bool`) – Whether or not to use sampling, use greedy
decoding otherwise. Default to be False.

top_p (`float`) – An alternative to sampling with temperature, called
nucleus sampling, where the model considers the results of the
tokens with top_p probability mass

top_k (`int`) – An alternative to sampling with temperature, where
the model considers the top_k tokens with the highest probability

min_p (`float`) – Minimum token probability, which will be scaled by the
probability of the most likely token. It must be a value between
0 and 1. Typical values are in the 0.01-0.2 range, comparably
selective as setting top_p in the 0.99-0.8 range (use the
opposite of normal top_p values)

temperature (`float`) – Sampling temperature

repetition_penalty (`float`) – Penalty to prevent the model from
generating repeated words or phrases. A value larger than
1 discourages repetition

ignore_eos (`bool`) – Indicator to ignore the eos_token_id or not

random_seed (`Optional`[`int`]) – Seed used when sampling a token

stop_words (`Optional`[`list`[`str`]]) – Words that stop generating further tokens

bad_words (`Optional`[`list`[`str`]]) – Words that the engine will never generate

stop_token_ids (`Optional`[`list`[`int`]]) – list of tokens that stop the generation
when they are generated. The returned output will not contain
the stop tokens.

bad_token_ids (`Optional`[`list`[`int`]]) – list of tokens that the engine will never
generate.

min_new_tokens (`Optional`[`int`]) – The minimum numbers of tokens to generate,
ignoring the number of tokens in the prompt.

skip_special_tokens (`bool`) – Whether or not to remove special tokens
in the decoding. Default to be True.

spaces_between_special_tokens (`bool`) – Whether or not to add spaces
around special tokens. The behavior of Fast tokenizers is to have
this to False. This is setup to True in slow tokenizers.

logprobs (`Optional`[`int`]) – Number of log probabilities to return per output token.

response_format (`Optional`[`dict`]) –
Generate responses according to given formatting.
Examples:

```text
{
    "type": "json_schema",
    "json_schema": {
        "name": "test",
        "schema": {
        "properties": {
            "name": {
            "type": "string"
            }
        },
        "required": ["name"],
        "type": "object"
        }
    }
}
```

or,

```text
{
    "type": "regex_schema",
    "regex_schema": "call me [A-Za-z]{1,10}"
}
```

logits_processors (`Optional`[`list`[`Callable`[[`Tensor`, `Tensor`], `Tensor`]]]) – Custom logit processors.

repetition_ngram_size (`int`) – The size of n-grams to consider for repetition early stop.

repetition_ngram_threshold (`int`) – The number of times an n-gram must be repeated to trigger early stop.

classlmdeploy.ChatTemplateConfig(model_name, model_path=None, system=None, meta_instruction=None, eosys=None, user=None, eoh=None, assistant=None, eoa=None, tool=None, eotool=None, separator=None, capability=None, stop_words=None)[source]#

Parameters for chat template.

Parameters:

model_name (`str`) – the name of the deployed model. Determine which chat template will be applied.
All the chat template names: `lmdeploylist`

system (`Optional`[`str`]) – begin of the system prompt.

meta_instruction (`Optional`[`str`]) – system prompt.

eosys (`Optional`[`str`]) – end of the system prompt.

user (`Optional`[`str`]) – begin of the user prompt.

eoh (`Optional`[`str`]) – end of the user prompt.

assistant (`Optional`[`str`]) – begin of the assistant prompt.

eoa (`Optional`[`str`]) – end of the assistant prompt.

tool (`Optional`[`str`]) – begin of the tool prompt.

eotool (`Optional`[`str`]) – end of the tool prompt.

capability (`Optional`[`Literal`[`'completion'`, `'infilling'`, `'chat'`, `'python'`]]) – the capability of the model, one of
`'completion'`, `'infilling'`, `'chat'`, `'python'`.
Default to None.

stop_words (`Optional`[`list`[`str`]]) – list of stop words. Default to None.
