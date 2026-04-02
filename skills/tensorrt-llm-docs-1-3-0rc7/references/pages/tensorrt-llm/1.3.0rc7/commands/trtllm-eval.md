# trtllm-eval — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/commands/trtllm-eval.html

trtllm-eval#

About#

The `trtllm-eval` command provides developers with a unified entry point for accuracy evaluation. It shares the core evaluation logic with the accuracy test suite of TensorRT LLM.

`trtllm-eval` is built on the offline API – LLM API. Compared to the online `trtllm-serve`, the offline API provides clearer error messages and simplifies the debugging workflow.

The following tasks are currently supported:

| Dataset | Task | Metric | Default ISL | Default OSL |
| --- | --- | --- | --- | --- |
| CNN Dailymail | summarization | rouge | 924 | 100 |
| MMLU | QA; multiple choice | accuracy | 4,094 | 2 |
| GSM8K | QA; regex matching | accuracy | 4,096 | 256 |
| GPQA | QA; multiple choice | accuracy | 32,768 | 4,096 |
| JSON mode eval | structured generation | accuracy | 1,024 | 512 |

Note

`trtllm-eval` originates from the TensorRT LLM accuracy test suite and serves as a lightweight utility for verifying and debugging accuracy. At this time, `trtllm-eval` is intended solely for development and is not recommended for production use.

Usage and Examples#

Some evaluation tasks (e.g., GSM8K and GPQA) depend on the `lm_eval` package. To run these tasks, you need to install `lm_eval` with:

```text
pip install -r requirements-dev.txt
```

Alternatively, you can install the `lm_eval` version specified in `requirements-dev.txt`.

Here are some examples:

```text
# Evaluate Llama-3.1-8B-Instruct on MMLU
trtllm-eval --model meta-llama/Llama-3.1-8B-Instruct mmlu

# Evaluate Llama-3.1-8B-Instruct on GSM8K
trtllm-eval --model meta-llama/Llama-3.1-8B-Instruct gsm8k

# Evaluate Llama-3.3-70B-Instruct on GPQA Diamond
trtllm-eval --model meta-llama/Llama-3.3-70B-Instruct gpqa_diamond
```

The `--model` argument accepts either a Hugging Face model ID or a local checkpoint path. By default, `trtllm-eval` runs the model with the PyTorch backend; you can pass `--backendtensorrt` to switch to the TensorRT backend.

Alternatively, the `--model` argument also accepts a local path to pre-built TensorRT engines. In this case, you should pass the Hugging Face tokenizer path to the `--tokenizer` argument.

For more details, see `trtllm-eval--help` and `trtllm-eval<task>--help`.

Note

Non-breaking: `--config<file.yaml>` is the preferred flag for passing a YAML configuration file.
Existing workflows using `--extra_llm_api_options<file.yaml>` continue to work; it is an equivalent alias.

Syntax#

trtllm-eval#

Usage

```text
trtllm-eval [OPTIONS] COMMAND [ARGS]...
```

Options

--model<model>#

Required model name | HF checkpoint path | TensorRT engine path

--tokenizer<tokenizer>#

Path | Name of the tokenizer.Specify this value only if using TensorRT engine as model.

--custom_tokenizer<custom_tokenizer>#

Custom tokenizer type: alias (e.g., ‘deepseek_v32’) or Python import path (e.g., ‘tensorrt_llm.tokenizer.deepseek_v32.DeepseekV32Tokenizer’). [Experimental]

--backend<backend>#

The backend to use for evaluation. Default is pytorch backend.

Options:

pytorch | tensorrt

--log_level<log_level>#

The logging level.

Options:

internal_error | error | warning | info | verbose | debug | trace

--max_beam_width<max_beam_width>#

Maximum number of beams for beam search decoding.

--max_batch_size<max_batch_size>#

Maximum number of requests that the engine can schedule.

--max_num_tokens<max_num_tokens>#

Maximum number of batched input tokens after padding is removed in each batch.

--max_seq_len<max_seq_len>#

Maximum total length of one request, including prompt and outputs. If unspecified, the value is deduced from the model config.

--tp_size<tp_size>#

Tensor parallelism size.

--pp_size<pp_size>#

Pipeline parallelism size.

--ep_size<ep_size>#

expert parallelism size

--gpus_per_node<gpus_per_node>#

Number of GPUs per node. Default to None, and it will be detected automatically.

--kv_cache_free_gpu_memory_fraction<kv_cache_free_gpu_memory_fraction>#

Free GPU memory fraction reserved for KV Cache, after allocating model weights and buffers.

--trust_remote_code#

Flag for HF transformers.

--revision<revision>#

The revision to use for the HuggingFace model (branch name, tag name, or commit id).

--config,--extra_llm_api_options<extra_llm_api_options>#

Path to a YAML file that overwrites the parameters. Can be specified as either –config or –extra_llm_api_options.

--disable_kv_cache_reuse#

Flag for disabling KV cache reuse.

cnn_dailymail#

Usage

```text
trtllm-eval cnn_dailymail [OPTIONS]
```

Options

--dataset_path<dataset_path>#

The path to CNN Dailymail dataset. If unspecified, the dataset is downloaded from HF hub.

--num_samples<num_samples>#

Number of samples to run the evaluation; None means full dataset.

--random_seed<random_seed>#

Random seed for dataset processing.

--rouge_path<rouge_path>#

The path to rouge repository.If unspecified, the repository is downloaded from HF hub.

--apply_chat_template#

Whether to apply chat template.

--system_prompt<system_prompt>#

System prompt.

--max_input_length<max_input_length>#

Maximum prompt length.

--max_output_length<max_output_length>#

Maximum generation length.

--output_dir<output_dir>#

Directory to save the task infos.

gpqa_diamond#

Usage

```text
trtllm-eval gpqa_diamond [OPTIONS]
```

Options

--dataset_path<dataset_path>#

The path to GPQA dataset. If unspecified, the dataset is downloaded from HF hub.

--num_samples<num_samples>#

Number of samples to run the evaluation; None means full dataset.

--random_seed<random_seed>#

Random seed for dataset processing.

--apply_chat_template#

Whether to apply chat template.

--chat_template_kwargs<chat_template_kwargs>#

Chat template kwargs as JSON string, e.g., ‘{“thinking_budget”: 0}’

--system_prompt<system_prompt>#

System prompt.

--max_input_length<max_input_length>#

Maximum prompt length.

--max_output_length<max_output_length>#

Maximum generation length.

--log_samples#

Log sample outputs for debugging.

--output_path<output_path>#

Path to save evaluation results.

--output_dir<output_dir>#

Directory to save the task infos.

gpqa_extended#

Usage

```text
trtllm-eval gpqa_extended [OPTIONS]
```

Options

--dataset_path<dataset_path>#

The path to GPQA dataset. If unspecified, the dataset is downloaded from HF hub.

--num_samples<num_samples>#

Number of samples to run the evaluation; None means full dataset.

--random_seed<random_seed>#

Random seed for dataset processing.

--apply_chat_template#

Whether to apply chat template.

--chat_template_kwargs<chat_template_kwargs>#

Chat template kwargs as JSON string, e.g., ‘{“thinking_budget”: 0}’

--system_prompt<system_prompt>#

System prompt.

--max_input_length<max_input_length>#

Maximum prompt length.

--max_output_length<max_output_length>#

Maximum generation length.

--log_samples#

Log sample outputs for debugging.

--output_path<output_path>#

Path to save evaluation results.

--output_dir<output_dir>#

Directory to save the task infos.

gpqa_main#

Usage

```text
trtllm-eval gpqa_main [OPTIONS]
```

Options

--dataset_path<dataset_path>#

The path to GPQA dataset. If unspecified, the dataset is downloaded from HF hub.

--num_samples<num_samples>#

Number of samples to run the evaluation; None means full dataset.

--random_seed<random_seed>#

Random seed for dataset processing.

--apply_chat_template#

Whether to apply chat template.

--chat_template_kwargs<chat_template_kwargs>#

Chat template kwargs as JSON string, e.g., ‘{“thinking_budget”: 0}’

--system_prompt<system_prompt>#

System prompt.

--max_input_length<max_input_length>#

Maximum prompt length.

--max_output_length<max_output_length>#

Maximum generation length.

--log_samples#

Log sample outputs for debugging.

--output_path<output_path>#

Path to save evaluation results.

--output_dir<output_dir>#

Directory to save the task infos.

gsm8k#

Usage

```text
trtllm-eval gsm8k [OPTIONS]
```

Options

--dataset_path<dataset_path>#

The path to GSM8K dataset. If unspecified, the dataset is downloaded from HF hub.

--num_samples<num_samples>#

Number of samples to run the evaluation; None means full dataset.

--random_seed<random_seed>#

Random seed for dataset processing.

--apply_chat_template#

Whether to apply chat template.

--chat_template_kwargs<chat_template_kwargs>#

Chat template kwargs as JSON string, e.g., ‘{“thinking_budget”: 0}’

--fewshot_as_multiturn#

Apply fewshot as multiturn.

--system_prompt<system_prompt>#

System prompt.

--max_input_length<max_input_length>#

Maximum prompt length.

--max_output_length<max_output_length>#

Maximum generation length.

--log_samples#

Log sample outputs for debugging.

--output_path<output_path>#

Path to save evaluation results.

--output_dir<output_dir>#

Directory to save the task infos.

json_mode_eval#

Usage

```text
trtllm-eval json_mode_eval [OPTIONS]
```

Options

--dataset_path<dataset_path>#

The path to JSON Mode Eval dataset. If unspecified, the dataset is downloaded from HF hub.

--num_samples<num_samples>#

Number of samples to run the evaluation; None means full dataset.

--random_seed<random_seed>#

Random seed for dataset processing.

--system_prompt<system_prompt>#

System prompt.

--max_input_length<max_input_length>#

Maximum prompt length.

--max_output_length<max_output_length>#

Maximum generation length.

--output_dir<output_dir>#

Directory to save the task infos.

longbench_v1#

Usage

```text
trtllm-eval longbench_v1 [OPTIONS]
```

Options

--dataset_path<dataset_path>#

The path to LongBench dataset. If unspecified, the dataset is downloaded from HF hub.

--num_samples<num_samples>#

Number of samples to run the evaluation; None means full dataset.

--random_seed<random_seed>#

Random seed for dataset processing.

--apply_chat_template<apply_chat_template>#

Whether to apply chat template.

Default:

`True`

--chat_template_kwargs<chat_template_kwargs>#

Chat template kwargs as JSON string, e.g., ‘{“thinking_budget”: 0}’

--system_prompt<system_prompt>#

System prompt.

--log_samples#

Log sample outputs for debugging.

--output_path<output_path>#

Path to save evaluation results.

--output_dir<output_dir>#

Directory to save the task infos.

longbench_v2#

Usage

```text
trtllm-eval longbench_v2 [OPTIONS]
```

Options

--dataset_path<dataset_path>#

Path to LongBench v2 dataset (HF dataset name or local path).

--prompts_dir<prompts_dir>#

Path to directory containing prompt templates.

--num_samples<num_samples>#

Number of samples to evaluate (None for all).

--start_idx<start_idx>#

Start index for evaluation.

--difficulty<difficulty>#

Filter by difficulty level.

Options:

easy | hard

--length<length>#

Filter by length category.

Options:

short | medium | long

--domain<domain>#

Filter by domain.

--cot#

Enable Chain-of-Thought reasoning using prompt engineering. Note: Modern models with thinking capability (e.g., DeepSeek-R1 and Qwen3) typically should not use this.

--no_context#

Test without long context.

--rag<rag>#

Use top-N retrieved contexts (0 to disable).

--output_dir<output_dir>#

Directory to save the task infos.

--random_seed<random_seed>#

Random seed for dataset processing.

--apply_chat_template#

Whether to apply chat template.

--system_prompt<system_prompt>#

System prompt.

--max_len<max_len>#

Maximum length (input + output) in tokens which can be supported by the model.

--max_input_length<max_input_length>#

Maximum context length in tokens. If exceeds, the prompt will be truncated in the middle.

--max_output_length<max_output_length>#

Maximum generation length in sampling parameters.

--chat_template_kwargs<chat_template_kwargs>#

A JSON string specifying chat template arguments, used to enable features like thinking mode. Examples: ‘{“enable_thinking”: true}’ for Qwen3, or ‘{“thinking”: true}’ for DeepSeek-V3.2.

--temperature<temperature>#

Temperature for sampling.

--top_p<top_p>#

Top p for sampling.

mmlu#

Usage

```text
trtllm-eval mmlu [OPTIONS]
```

Options

--dataset_path<dataset_path>#

The path to MMLU dataset. The commands to prepare the dataset: wget https://people.eecs.berkeley.edu/~hendrycks/data.tar && tar -xf data.tar. If unspecified, the dataset is downloaded automatically.

--num_samples<num_samples>#

Number of samples to run the evaluation; None means full dataset.

--num_fewshot<num_fewshot>#

Number of fewshot.

--random_seed<random_seed>#

Random seed for dataset processing.

--apply_chat_template#

Whether to apply chat template.

--chat_template_kwargs<chat_template_kwargs>#

Chat template kwargs as JSON string, e.g., ‘{“thinking_budget”: 0}’

--system_prompt<system_prompt>#

System prompt.

--max_input_length<max_input_length>#

Maximum prompt length.

--max_output_length<max_output_length>#

Maximum generation length.

--check_accuracy#

--accuracy_threshold<accuracy_threshold>#

--output_dir<output_dir>#

Directory to save the task infos.

mmmu#

Usage

```text
trtllm-eval mmmu [OPTIONS]
```

Options

--dataset_path<dataset_path>#

The path to MMMU dataset. If unspecified, the dataset is downloaded from HF hub.

--num_samples<num_samples>#

Number of samples to run the evaluation; None means full dataset.

--random_seed<random_seed>#

Random seed for dataset processing.

--chat_template_kwargs<chat_template_kwargs>#

Chat template kwargs as JSON string, e.g., ‘{“thinking_budget”: 0}’

--system_prompt<system_prompt>#

The system prompt to be added on the prompt. If specified, it will add {‘role’: ‘system’, ‘content’: system_prompt} to the prompt.

--max_input_length<max_input_length>#

Maximum prompt length.

--max_output_length<max_output_length>#

Maximum generation length.

--log_samples#

Log sample outputs for debugging.

--output_path<output_path>#

Path to save evaluation results.

--output_dir<output_dir>#

Directory to save the task infos.
