Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/commands/trtllm-eval.md

* trtllm-eval

# trtllm-eval[#](#trtllm-eval "Link to this heading")

## About[#](#about "Link to this heading")

The `trtllm-eval` command provides developers with a unified entry point for accuracy evaluation. It shares the core evaluation logic with the [accuracy test suite](https://github.com/NVIDIA/TensorRT-LLM/tree/main/tests/integration/defs/accuracy) of TensorRT LLM.

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

## Usage and Examples[#](#usage-and-examples "Link to this heading")

Some evaluation tasks (e.g., GSM8K and GPQA) depend on the `lm_eval` package. To run these tasks, you need to install `lm_eval` with:

```
pip install -r requirements-dev.txt
```

Alternatively, you can install the `lm_eval` version specified in `requirements-dev.txt`.

Here are some examples:

```
# Evaluate Llama-3.1-8B-Instruct on MMLU
trtllm-eval --model meta-llama/Llama-3.1-8B-Instruct mmlu

# Evaluate Llama-3.1-8B-Instruct on GSM8K
trtllm-eval --model meta-llama/Llama-3.1-8B-Instruct gsm8k

# Evaluate Llama-3.3-70B-Instruct on GPQA Diamond
trtllm-eval --model meta-llama/Llama-3.3-70B-Instruct gpqa_diamond
```

The `--model` argument accepts either a Hugging Face model ID or a local checkpoint path. By default, `trtllm-eval` runs the model with the PyTorch backend; you can pass `--backend tensorrt` to switch to the TensorRT backend.

Alternatively, the `--model` argument also accepts a local path to pre-built TensorRT engines. In this case, you should pass the Hugging Face tokenizer path to the `--tokenizer` argument.

For more details, see `trtllm-eval --help` and `trtllm-eval <task> --help`.

## Syntax[#](#syntax "Link to this heading")

### trtllm-eval[#](#trtllm-eval "Link to this heading")

Usage

```
trtllm-eval [OPTIONS] COMMAND [ARGS]...
```

Options

--model <model>[#](#cmdoption-trtllm-eval-model "Link to this definition")
:   **Required** model name | HF checkpoint path | TensorRT engine path

--tokenizer <tokenizer>[#](#cmdoption-trtllm-eval-tokenizer "Link to this definition")
:   Path | Name of the tokenizer.Specify this value only if using TensorRT engine as model.

--backend <backend>[#](#cmdoption-trtllm-eval-backend "Link to this definition")
:   The backend to use for evaluation. Default is pytorch backend.

    Options:
    :   pytorch | tensorrt

--log\_level <log\_level>[#](#cmdoption-trtllm-eval-log_level "Link to this definition")
:   The logging level.

    Options:
    :   internal\_error | error | warning | info | verbose | debug | trace

--max\_beam\_width <max\_beam\_width>[#](#cmdoption-trtllm-eval-max_beam_width "Link to this definition")
:   Maximum number of beams for beam search decoding.

--max\_batch\_size <max\_batch\_size>[#](#cmdoption-trtllm-eval-max_batch_size "Link to this definition")
:   Maximum number of requests that the engine can schedule.

--max\_num\_tokens <max\_num\_tokens>[#](#cmdoption-trtllm-eval-max_num_tokens "Link to this definition")
:   Maximum number of batched input tokens after padding is removed in each batch.

--max\_seq\_len <max\_seq\_len>[#](#cmdoption-trtllm-eval-max_seq_len "Link to this definition")
:   Maximum total length of one request, including prompt and outputs. If unspecified, the value is deduced from the model config.

--tp\_size <tp\_size>[#](#cmdoption-trtllm-eval-tp_size "Link to this definition")
:   Tensor parallelism size.

--pp\_size <pp\_size>[#](#cmdoption-trtllm-eval-pp_size "Link to this definition")
:   Pipeline parallelism size.

--ep\_size <ep\_size>[#](#cmdoption-trtllm-eval-ep_size "Link to this definition")
:   expert parallelism size

--gpus\_per\_node <gpus\_per\_node>[#](#cmdoption-trtllm-eval-gpus_per_node "Link to this definition")
:   Number of GPUs per node. Default to None, and it will be detected automatically.

--kv\_cache\_free\_gpu\_memory\_fraction <kv\_cache\_free\_gpu\_memory\_fraction>[#](#cmdoption-trtllm-eval-kv_cache_free_gpu_memory_fraction "Link to this definition")
:   Free GPU memory fraction reserved for KV Cache, after allocating model weights and buffers.

--trust\_remote\_code[#](#cmdoption-trtllm-eval-trust_remote_code "Link to this definition")
:   Flag for HF transformers.

--extra\_llm\_api\_options <extra\_llm\_api\_options>[#](#cmdoption-trtllm-eval-extra_llm_api_options "Link to this definition")
:   Path to a YAML file that overwrites the parameters

--disable\_kv\_cache\_reuse[#](#cmdoption-trtllm-eval-disable_kv_cache_reuse "Link to this definition")
:   Flag for disabling KV cache reuse.

#### cnn\_dailymail[#](#trtllm-eval-cnn-dailymail "Link to this heading")

Usage

```
trtllm-eval cnn_dailymail [OPTIONS]
```

Options

--dataset\_path <dataset\_path>[#](#cmdoption-trtllm-eval-cnn_dailymail-dataset_path "Link to this definition")
:   The path to CNN Dailymail dataset. If unspecified, the dataset is downloaded from HF hub.

--num\_samples <num\_samples>[#](#cmdoption-trtllm-eval-cnn_dailymail-num_samples "Link to this definition")
:   Number of samples to run the evaluation; None means full dataset.

--random\_seed <random\_seed>[#](#cmdoption-trtllm-eval-cnn_dailymail-random_seed "Link to this definition")
:   Random seed for dataset processing.

--rouge\_path <rouge\_path>[#](#cmdoption-trtllm-eval-cnn_dailymail-rouge_path "Link to this definition")
:   The path to rouge repository.If unspecified, the repository is downloaded from HF hub.

--apply\_chat\_template[#](#cmdoption-trtllm-eval-cnn_dailymail-apply_chat_template "Link to this definition")
:   Whether to apply chat template.

--system\_prompt <system\_prompt>[#](#cmdoption-trtllm-eval-cnn_dailymail-system_prompt "Link to this definition")
:   System prompt.

--max\_input\_length <max\_input\_length>[#](#cmdoption-trtllm-eval-cnn_dailymail-max_input_length "Link to this definition")
:   Maximum prompt length.

--max\_output\_length <max\_output\_length>[#](#cmdoption-trtllm-eval-cnn_dailymail-max_output_length "Link to this definition")
:   Maximum generation length.

#### gpqa\_diamond[#](#trtllm-eval-gpqa-diamond "Link to this heading")

Usage

```
trtllm-eval gpqa_diamond [OPTIONS]
```

Options

--dataset\_path <dataset\_path>[#](#cmdoption-trtllm-eval-gpqa_diamond-dataset_path "Link to this definition")
:   The path to GPQA dataset. If unspecified, the dataset is downloaded from HF hub.

--num\_samples <num\_samples>[#](#cmdoption-trtllm-eval-gpqa_diamond-num_samples "Link to this definition")
:   Number of samples to run the evaluation; None means full dataset.

--random\_seed <random\_seed>[#](#cmdoption-trtllm-eval-gpqa_diamond-random_seed "Link to this definition")
:   Random seed for dataset processing.

--apply\_chat\_template[#](#cmdoption-trtllm-eval-gpqa_diamond-apply_chat_template "Link to this definition")
:   Whether to apply chat template.

--system\_prompt <system\_prompt>[#](#cmdoption-trtllm-eval-gpqa_diamond-system_prompt "Link to this definition")
:   System prompt.

--max\_input\_length <max\_input\_length>[#](#cmdoption-trtllm-eval-gpqa_diamond-max_input_length "Link to this definition")
:   Maximum prompt length.

--max\_output\_length <max\_output\_length>[#](#cmdoption-trtllm-eval-gpqa_diamond-max_output_length "Link to this definition")
:   Maximum generation length.

#### gpqa\_extended[#](#trtllm-eval-gpqa-extended "Link to this heading")

Usage

```
trtllm-eval gpqa_extended [OPTIONS]
```

Options

--dataset\_path <dataset\_path>[#](#cmdoption-trtllm-eval-gpqa_extended-dataset_path "Link to this definition")
:   The path to GPQA dataset. If unspecified, the dataset is downloaded from HF hub.

--num\_samples <num\_samples>[#](#cmdoption-trtllm-eval-gpqa_extended-num_samples "Link to this definition")
:   Number of samples to run the evaluation; None means full dataset.

--random\_seed <random\_seed>[#](#cmdoption-trtllm-eval-gpqa_extended-random_seed "Link to this definition")
:   Random seed for dataset processing.

--apply\_chat\_template[#](#cmdoption-trtllm-eval-gpqa_extended-apply_chat_template "Link to this definition")
:   Whether to apply chat template.

--system\_prompt <system\_prompt>[#](#cmdoption-trtllm-eval-gpqa_extended-system_prompt "Link to this definition")
:   System prompt.

--max\_input\_length <max\_input\_length>[#](#cmdoption-trtllm-eval-gpqa_extended-max_input_length "Link to this definition")
:   Maximum prompt length.

--max\_output\_length <max\_output\_length>[#](#cmdoption-trtllm-eval-gpqa_extended-max_output_length "Link to this definition")
:   Maximum generation length.

#### gpqa\_main[#](#trtllm-eval-gpqa-main "Link to this heading")

Usage

```
trtllm-eval gpqa_main [OPTIONS]
```

Options

--dataset\_path <dataset\_path>[#](#cmdoption-trtllm-eval-gpqa_main-dataset_path "Link to this definition")
:   The path to GPQA dataset. If unspecified, the dataset is downloaded from HF hub.

--num\_samples <num\_samples>[#](#cmdoption-trtllm-eval-gpqa_main-num_samples "Link to this definition")
:   Number of samples to run the evaluation; None means full dataset.

--random\_seed <random\_seed>[#](#cmdoption-trtllm-eval-gpqa_main-random_seed "Link to this definition")
:   Random seed for dataset processing.

--apply\_chat\_template[#](#cmdoption-trtllm-eval-gpqa_main-apply_chat_template "Link to this definition")
:   Whether to apply chat template.

--system\_prompt <system\_prompt>[#](#cmdoption-trtllm-eval-gpqa_main-system_prompt "Link to this definition")
:   System prompt.

--max\_input\_length <max\_input\_length>[#](#cmdoption-trtllm-eval-gpqa_main-max_input_length "Link to this definition")
:   Maximum prompt length.

--max\_output\_length <max\_output\_length>[#](#cmdoption-trtllm-eval-gpqa_main-max_output_length "Link to this definition")
:   Maximum generation length.

#### gsm8k[#](#trtllm-eval-gsm8k "Link to this heading")

Usage

```
trtllm-eval gsm8k [OPTIONS]
```

Options

--dataset\_path <dataset\_path>[#](#cmdoption-trtllm-eval-gsm8k-dataset_path "Link to this definition")
:   The path to GSM8K dataset. If unspecified, the dataset is downloaded from HF hub.

--num\_samples <num\_samples>[#](#cmdoption-trtllm-eval-gsm8k-num_samples "Link to this definition")
:   Number of samples to run the evaluation; None means full dataset.

--random\_seed <random\_seed>[#](#cmdoption-trtllm-eval-gsm8k-random_seed "Link to this definition")
:   Random seed for dataset processing.

--apply\_chat\_template[#](#cmdoption-trtllm-eval-gsm8k-apply_chat_template "Link to this definition")
:   Whether to apply chat template.

--fewshot\_as\_multiturn[#](#cmdoption-trtllm-eval-gsm8k-fewshot_as_multiturn "Link to this definition")
:   Apply fewshot as multiturn.

--system\_prompt <system\_prompt>[#](#cmdoption-trtllm-eval-gsm8k-system_prompt "Link to this definition")
:   System prompt.

--max\_input\_length <max\_input\_length>[#](#cmdoption-trtllm-eval-gsm8k-max_input_length "Link to this definition")
:   Maximum prompt length.

--max\_output\_length <max\_output\_length>[#](#cmdoption-trtllm-eval-gsm8k-max_output_length "Link to this definition")
:   Maximum generation length.

#### json\_mode\_eval[#](#trtllm-eval-json-mode-eval "Link to this heading")

Usage

```
trtllm-eval json_mode_eval [OPTIONS]
```

Options

--dataset\_path <dataset\_path>[#](#cmdoption-trtllm-eval-json_mode_eval-dataset_path "Link to this definition")
:   The path to JSON Mode Eval dataset. If unspecified, the dataset is downloaded from HF hub.

--num\_samples <num\_samples>[#](#cmdoption-trtllm-eval-json_mode_eval-num_samples "Link to this definition")
:   Number of samples to run the evaluation; None means full dataset.

--random\_seed <random\_seed>[#](#cmdoption-trtllm-eval-json_mode_eval-random_seed "Link to this definition")
:   Random seed for dataset processing.

--system\_prompt <system\_prompt>[#](#cmdoption-trtllm-eval-json_mode_eval-system_prompt "Link to this definition")
:   System prompt.

--max\_input\_length <max\_input\_length>[#](#cmdoption-trtllm-eval-json_mode_eval-max_input_length "Link to this definition")
:   Maximum prompt length.

--max\_output\_length <max\_output\_length>[#](#cmdoption-trtllm-eval-json_mode_eval-max_output_length "Link to this definition")
:   Maximum generation length.

#### mmlu[#](#trtllm-eval-mmlu "Link to this heading")

Usage

```
trtllm-eval mmlu [OPTIONS]
```

Options

--dataset\_path <dataset\_path>[#](#cmdoption-trtllm-eval-mmlu-dataset_path "Link to this definition")
:   The path to MMLU dataset. The commands to prepare the dataset: wget <https://people.eecs.berkeley.edu/~hendrycks/data.tar> && tar -xf data.tar. If unspecified, the dataset is downloaded automatically.

--num\_samples <num\_samples>[#](#cmdoption-trtllm-eval-mmlu-num_samples "Link to this definition")
:   Number of samples to run the evaluation; None means full dataset.

--num\_fewshot <num\_fewshot>[#](#cmdoption-trtllm-eval-mmlu-num_fewshot "Link to this definition")
:   Number of fewshot.

--random\_seed <random\_seed>[#](#cmdoption-trtllm-eval-mmlu-random_seed "Link to this definition")
:   Random seed for dataset processing.

--apply\_chat\_template[#](#cmdoption-trtllm-eval-mmlu-apply_chat_template "Link to this definition")
:   Whether to apply chat template.

--system\_prompt <system\_prompt>[#](#cmdoption-trtllm-eval-mmlu-system_prompt "Link to this definition")
:   System prompt.

--max\_input\_length <max\_input\_length>[#](#cmdoption-trtllm-eval-mmlu-max_input_length "Link to this definition")
:   Maximum prompt length.

--max\_output\_length <max\_output\_length>[#](#cmdoption-trtllm-eval-mmlu-max_output_length "Link to this definition")
:   Maximum generation length.

--check\_accuracy[#](#cmdoption-trtllm-eval-mmlu-check_accuracy "Link to this definition")

--accuracy\_threshold <accuracy\_threshold>[#](#cmdoption-trtllm-eval-mmlu-accuracy_threshold "Link to this definition")

#### mmmu[#](#trtllm-eval-mmmu "Link to this heading")

Usage

```
trtllm-eval mmmu [OPTIONS]
```

Options

--dataset\_path <dataset\_path>[#](#cmdoption-trtllm-eval-mmmu-dataset_path "Link to this definition")
:   The path to MMMU dataset. If unspecified, the dataset is downloaded from HF hub.

--num\_samples <num\_samples>[#](#cmdoption-trtllm-eval-mmmu-num_samples "Link to this definition")
:   Number of samples to run the evaluation; None means full dataset.

--random\_seed <random\_seed>[#](#cmdoption-trtllm-eval-mmmu-random_seed "Link to this definition")
:   Random seed for dataset processing.

--system\_prompt <system\_prompt>[#](#cmdoption-trtllm-eval-mmmu-system_prompt "Link to this definition")
:   The system prompt to be added on the prompt. If specified, it will add {‘role’: ‘system’, ‘content’: system\_prompt} to the prompt.

--max\_input\_length <max\_input\_length>[#](#cmdoption-trtllm-eval-mmmu-max_input_length "Link to this definition")
:   Maximum prompt length.

--max\_output\_length <max\_output\_length>[#](#cmdoption-trtllm-eval-mmmu-max_output_length "Link to this definition")
:   Maximum generation length.

[previous

trtllm-bench](trtllm-bench.md "previous page")
[next

trtllm-serve](trtllm-serve/index.md "next page")

On this page

* [About](#about)
* [Usage and Examples](#usage-and-examples)
* [Syntax](#syntax)
  + [trtllm-eval](#trtllm-eval)
    - [cnn\_dailymail](#trtllm-eval-cnn-dailymail)
    - [gpqa\_diamond](#trtllm-eval-gpqa-diamond)
    - [gpqa\_extended](#trtllm-eval-gpqa-extended)
    - [gpqa\_main](#trtllm-eval-gpqa-main)
    - [gsm8k](#trtllm-eval-gsm8k)
    - [json\_mode\_eval](#trtllm-eval-json-mode-eval)
    - [mmlu](#trtllm-eval-mmlu)
    - [mmmu](#trtllm-eval-mmmu)