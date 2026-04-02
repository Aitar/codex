* [Model Analyzer](../../perf_benchmark/model_analyzer.md)
* Table of Contents

# Table of Contents[#](#table-of-contents "Link to this heading")

* [Search Modes](#search-modes)
* [Default Search Mode](#default-search-mode)
* [Brute Search Mode](#brute-search-mode)

  + [Automatic Brute Search](#automatic-brute-search)
  + [Manual Brute Search](#manual-brute-search)
* [Quick Search Mode](#quick-search-mode)
* [Optuna Search Mode](#optuna-search-mode)

# Model Config Search[#](#model-config-search "Link to this heading")

## Support Matrix[#](#support-matrix "Link to this heading")

The table below illustrates shows which search modes are available based on the model type:

|  | Single Model | Multi-Model | BLS | Ensemble | LLM |
| --- | --- | --- | --- | --- | --- |
| **Brute** | o | o | - | - | - |
| **Quick** | o | o | o | o | o |
| **Optuna** | o | o | o | o | o |

## Search Modes[#](#search-modes "Link to this heading")

Model Analyzerâs `profile` subcommand supports multiple modes when searching to find the best model configuration:

* [Brute Force Search](#brute-search-mode)

  + **Search type:** Brute-force sweep of the cross product of all possible configurations
  + **Default for:**

    - Single models, which are not ensemble or BLS
    - Multiple models being profiled sequentially
  + **Command:** `--run-config-search-mode brute`
* [Quick Search](#quick-search-mode)

  + **Search type:** Heuristic sweep using a hill-climbing algorithm to find an optimal configuration
  + **Default for:**

    - Single ensemble models
    - Single BLS models
    - Multiple models being profiled concurrently
  + **Command:** `--run-config-search-mode quick`
* [Optuna Search](#optuna-search-mode) **-ALPHA RELEASE-**

  + **Search type:** Heuristic sweep using a hyperparameter optimization framework to find an optimal configuration
  + **Command:** `--run-config-search-mode optuna`

---

## Default Search Mode[#](#default-search-mode "Link to this heading")

Model Analyzerâs default search mode depends on the type of model and if you are profiling models concurrently (in the case of multiple models):

* [Sequential (single or multi-model) Search](#brute-search-mode)

  + **Default Search type:** [Brute Force Search](#brute-search-mode)
* [Concurrent / Multi-model Search](#multi-model-search-mode)

  + **Default Search type:** [Quick Search](#quick-search-mode)
  + **Command:** `--run-config-profile-models-concurrently-enable`
* [Ensemble Model Search](#ensemble-model-search):

  + **Default Search type:** [Quick Search](#quick-search-mode)
* [BLS Model Search](#bls-model-search):

  + **Default Search type:** [Quick Search](#quick-search-mode)

---

## Brute Search Mode[#](#brute-search-mode "Link to this heading")

**Default search mode when profiling non-ensemble/BLS models sequentially**

Model Analyzerâs brute search mode will do a brute-force sweep of the cross product of all possible configurations.   
It has two modes:

* [Automatic](#automatic-brute-search)

  + **No** model config parameters are specified
* [Manual](#manual-brute-search)

  + **Any** model config parameters are specified
  + `--run-config-search-disable` option is specified

---

## Automatic Brute Search[#](#automatic-brute-search "Link to this heading")

**Default brute search mode when no model config parameters are specified**

The parameters that are automatically searched are
[model maximum batch size](https://github.com/triton-inference-server/server/blob/master/docs/user_guide/model_configuration.md#maximum-batch-size),
[model instance groups](https://github.com/triton-inference-server/server/blob/master/docs/user_guide/model_configuration.md#instance-groups), and [request concurrencies](../../perf_analyzer/docs/cli.md#measurement-options).
Additionally, [dynamic\_batching](https://github.com/triton-inference-server/server/blob/master/docs/user_guide/model_configuration.md#dynamic-batcher) will be enabled if it is legal to do so.

*An example model analyzer YAML config that performs an Automatic Brute Search:*

```
model_repository: /path/to/model/repository/

profile_models:
  - model_A
```

You can also modify the minimum/maximum values that the automatic search space will iterate through:

### [Instance Group Search Space](https://github.com/triton-inference-server/server/blob/master/docs/user_guide/model_configuration.md#instance-groups)[#](#instance-group-search-space "Link to this heading")

* `Default:` 1 to 5 instance group counts
* `--run-config-search-min-instance-count: <val>`: Changes the instance group countâs minimum automatic search space value
* `--run-config-search-max-instance-count: <val>`: Changes the instance group countâs maximum automatic search space value

---

### [Model Batch Size Search Space](https://github.com/triton-inference-server/server/blob/master/docs/user_guide/model_configuration.md#maximum-batch-size)[#](#model-batch-size-search-space "Link to this heading")

* `Default:` 1 to 128 max batch sizes, sweeping over powers of 2 (i.e. 1, 2, 4, 8, â¦)
* `--run-config-search-min-model-batch-size: <val>`: Changes the modelâs batch size minimum automatic search space value
* `--run-config-search-max-model-batch-size: <val>`: Changes the modelâs batch size maximum automatic search space value

---

### [Request Concurrency Search Space](../../perf_analyzer/docs/inference_load_modes.md#concurrency-mode)[#](#request-concurrency-search-space "Link to this heading")

* `Default:` 1 to 1024 concurrencies, sweeping over powers of 2 (i.e. 1, 2, 4, 8, â¦)
* `--run-config-search-min-concurrency: <val>`: Changes the request concurrency minimum automatic search space value
* `--run-config-search-max-concurrency: <val>`: Changes the request concurrency maximum automatic search space value

### [Request Rate Search Space](../../perf_analyzer/docs/inference_load_modes.md#request-rate-mode)[#](#request-rate-search-space "Link to this heading")

* `Default:` 1 to 1024 concurrencies, sweeping over powers of 2 (i.e. 1, 2, 4, 8, â¦)
* `--run-config-search-min-request-rate: <val>`: Changes the request rate minimum automatic search space value
* `--run-config-search-max-request-rate: <val>`: Changes the request rate maximum automatic search space value

---

*An example YAML config that limits the search space:*

```
model_repository: /path/to/model/repository/

run_config_search_max_instance_count: 3
run_config_search_min_model_batch_size: 16
run_config_search_min_concurrency: 8
run_config_search_max_concurrency: 256
profile_models:
  - model_A
```

*This will perform an Automatic Brute Search with instance group counts: 3-5, batch sizes: 16-128, and concurrencies: 8-256*

---

## Manual Brute Search[#](#manual-brute-search "Link to this heading")

**Default brute search mode when any model config parameters or parameters are specified**

Using Manual Brute Search, you can create custom sweeps for any parameter that can be specified in the model configuration. There are two ways this mode is enabled when doing a brute search:

* Any [`model config parameters`](config.md#model-config-parameters) are specified:

  + You must manually specify the batch sizes and instance group counts you want Model Analyzer to sweep
  + Request concurrencies will still be automatically swept (as they are not a model config parameter)
* Any [`parameters`](config.md#test-configuration-parameter) are specified:

  + You must manually specify the batch sizes, instance group counts, and request concurrencies you want Model Analyzer to sweep
* `--run-config-search-disable` is specified:

  + You must manually specify the batch sizes, instance group counts, and request concurrencies you want Model Analyzer to sweep

***Note**: Model Analyzer only checks the syntax of the `model config parameters` and cannot guarantee that the configuration that is generated is loadable by Triton. For a complete list of parameters allowed under model\_config\_parameters, refer to the [Triton Model
Configuration](https://github.com/triton-inference-server/server/blob/master/docs/user_guide/model_configuration.md).   
**It is your responsibility to ensure the sweep configuration specified works with your model.***

---

*In this example, Model Analyzer will only sweep through different values of `request concurrencies`:*

```
model_repository: /path/to/model/repository/

profile_models:
  model_1:
    model_config_parameters:
      instance_group:
        - kind: KIND_GPU
          count: [1, 2]
```

*In this example, Model Analyzer will not sweep through any values, and will only try the concurrencies listed below:*

```
model_repository: /path/to/model/repository/

profile_models:
  model_1:
    parameters:
      concurrency: 1,2,3,128
```

*This example shows how a value other than instance, batch size or concurrency can be swept, and will sweep through eight configs:*

* [2 \* `max_batch_size`] \* [2 \* `max_queue_delay_microseconds`] \* [2 \* `instance_group`].

```
model_repository: /path/to/model/repository/

run_config_search_disable: True
profile_models:
  model_1:
    model_config_parameters:
      max_batch_size: [6, 8]
      dynamic_batching:
        max_queue_delay_microseconds: [200, 300]
      instance_group:
        - kind: KIND_GPU
          count: [1, 2]
```

---

### **Examples of Additional Model Config Parameters**[#](#examples-of-additional-model-config-parameters "Link to this heading")

In this section, we describe some of the parameters that might be of interest for
manual sweep:

* [Rate limiter](../../user_guide/model_configuration.md#rate-limiter-config) setting
* If the model is using [ONNX](https://github.com/triton-inference-server/onnxruntime_backend) or [Tensorflow backend](https://github.com/triton-inference-server/tensorflow_backend), the âexecution\_acceleratorsâ parameters. More information about this parameter is
  available in the [Triton Optimization Guide](../../user_guide/optimization.md#framework-specific-optimization)

---

## Quick Search Mode[#](#quick-search-mode "Link to this heading")

**Default search mode when profiling ensemble models, BLS models, or multiple models concurrently**

*This mode has the following limitations:*

* If model config parameters are specified, they can contain only one possible combination of parameters

This mode uses a hill climbing algorithm to search the configuration space, looking for
the maximal objective value within the specified constraints. In the majority of cases
this will find greater than 95% of the maximum objective value (that could be found using a brute force search), while needing to search less than 10% of the configuration space.

After quick search has found the best config(s), it will then sweep the top-N configurations found (specified by `--num-configs-per-model`) over the default concurrency range before generation of the summary reports.

---

*An example model analyzer YAML config that performs a Quick Search:*

```
model_repository: /path/to/model/repository/

run_config_search_mode: quick
profile_models:
  - model_A
```

---

### **Limiting Batch Size, Instance Group, and Client Concurrency**[#](#limiting-batch-size-instance-group-and-client-concurrency "Link to this heading")

Using the `--run-config-search-<min/max>...` config options you have the ability to clamp the algorithmâs upper or lower bounds for the modelâs batch size and instance group count, as well as the clientâs request concurrency.

*Note: By default, quick search runs unbounded and ignores any default values for these settings*

---

*An example model analyzer YAML config that performs a Quick Search and constrains the search parameters:*

```
model_repository: /path/to/model/repository/

run_config_search_mode: quick
run_config_search_max_instance_count: 4
run_config_search_max_concurrency: 16
run_config_search_min_model_batch_size: 8

profile_models:
  - model_A
```

---

## Optuna Search Mode[#](#optuna-search-mode "Link to this heading")

**-ALPHA RELEASE-**

*This mode has the following limitations:*

* **Ensemble, BLS or concurrent multi-model profiling is not supported**
* **Profiling with request rate is not supported**

This mode uses a hyperparameter optimization framework to search the configuration
space, looking for the maximal objective value within the specified constraints.
Please see the [Optuna](https://optuna.org/) website if you are interested in specific details on how the algorithm functions.

Optuna allows you to search for every parameter that can be specified in the model configuration. Parameters can be specified
with a min/max range (using the run-config-search options) or a list of parameters to test against can be set in the
parameters/model\_config\_parameters field.

After optuna search has found the best config(s), it will then sweep the top-N configurations found (specified by `--num-configs-per-model`) over the default concurrency range before generation of the summary reports.

---

*An example model analyzer YAML config that performs an Optuna Search:*

```
model_repository: /path/to/model/repository/

run_config_search_mode: optuna
profile_models:
  - model_A
```

---

A number of new configuration options were added to support tailoring the Optuna search to your needs:

* `--min/max_percentage_of_search_space`: sets the percentage of the space you want Optuna to search
* `--optuna-min/max-trials`: sets the number of trials Optuna will attempt
* `--optuna-early-exit-threshold`: sets the number of trials without improvement before triggering early exit
* `--use-concurrency-formula`: uses a formula (2 \* batch size \* instance group count), rather than sweeping concurrency

---

*An example that performs an Optuna Search using these new configuration options:*

```
model_repository: /path/to/model/repository/

run_config_search_mode: optuna
run_config_search_max_instance_count: 8
run_config_search_min_concurrency: 32
run_config_search_max_concurrency: 256

use_concurrency_formula: True
min_percentage_of_search_space: 10
optuna_max_trials: 200
optuna_early_exit_threshold: 15

profile_models:
  model_A:
    model_config_parameters:
      max_batch_size: [1, 4, 8, 32, 64, 128]
      dynamic_batching:
        max_queue_delay_microseconds: [100, 200, 300]
    parameters:
      batch_sizes: 1, 2, 4, 8, 16
```

*The debug output showing how the space will be searched:*

```
Number of configs in search space: 720
   batch_sizes: [1, 2, 4, 8, 16] (https://github.com/triton-inference-server/model_analyzer/blob/main/docs/5)
   max_batch_size: [1, 4, 8, 32, 64, 128] (https://github.com/triton-inference-server/model_analyzer/blob/main/docs/6)
   instance_group: 1 to 8 (8)
   max_queue_delay_microseconds: [100, 200, 300] (https://github.com/triton-inference-server/model_analyzer/blob/main/docs/3)

Minimum number of trials: 72 (10% of search space)
Maximum number of trials: 200 (set by max trials)
```

---

### Optuna Search in Detail[#](#optuna-search-in-detail "Link to this heading")

When performing an Optuna Search, Model Analyzerâs goal is to maximize the configurationâs `objective score`. First,
MA profiles the default configuration and assigns it an `objective score` of zero. All future configurations
are also assigned an `objective score`; with positive values indicating this configuration is better than the default
configuration and negative values indicating it performs worse.

*Here is an example debug output:*

```
Trial 7 of 200:
  Creating model config: model_A_config_6
  Setting dynamic_batching to {'max_queue_delay_microseconds': 200}
  Setting instance_group to [{'count': 4, 'kind': 'KIND_GPU'}]
  Setting max_batch_size to 64

  Profiling model_A_config_6: client batch size=4, concurrency=256
  Objective score for model_A_config_6: 57 --- Best: model_A_config_4 (83)
```

## Ensemble Model Search[#](#ensemble-model-search "Link to this heading")

*This mode has the following limitations:*

* Can only be run in `quick` search mode
* Only supports up to four composing models
* Composing models cannot be ensemble or BLS models

Ensemble models can be optimized using the Quick Search modeâs hill climbing algorithm to search the composing modelsâ configuration spaces in parallel, looking for the maximal objective value within the specified constraints. Model Analyzer has observed positive outcomes towards finding the maximum objective value; with runtimes under one hour (compared to the days it would take a brute force run to complete) for ensembles that contain up to four composing models.

After Model Analyzer has found the best config(s), it will then sweep the top-N configurations found (specified by `--num-configs-per-model`) over the concurrency range before generation of the summary reports.

---

## BLS Model Search[#](#bls-model-search "Link to this heading")

*This mode has the following limitations:*

* Can only be run in `quick` search mode
* Only supports up to four composing models
* Composing models cannot be ensemble or BLS models

BLS models can be optimized using the Quick Search modeâs hill climbing algorithm to search the BLS composing modelsâ configuration spaces, as well as the BLS modelâs instance count, in parallel, looking for the maximal objective value within the specified constraints. Model Analyzer has observed positive outcomes towards finding the maximum objective value; with runtimes under one hour (compared to the days it would take a brute force run to complete) for BLS models that contain up to four composing models.

After Model Analyzer has found the best config(s), it will then sweep the top-N configurations found (specified by `--num-configs-per-model`) over the concurrency range before generation of the summary reports.

---

## LLM Search[#](#llm-search "Link to this heading")

*This mode has the following limitations:*

* Summary/Detailed reports do not include the new metrics

In order to profile LLMs you must tell MA that the model type is LLM by setting `--model-type LLM` in the CLI/config file. You can specify CLI options to the GenAI-Perf tool using `genai_perf_flags`. See the [GenAI-Perf CLI](../../perf_analyzer/genai-perf/README.md#command-line-options) documentation for a list of the flags that can be specified.

LLMs can be optimized using either Quick or Brute search mode.

*An example model analyzer YAML config for a LLM:*

```
model_repository: /path/to/model/repository/

model_type: LLM
client_prototcol: grpc

genai_perf_flags:
  backend: vllm
  streaming: true
```

For LLMs there are three new metrics being reported: **Inter-token Latency**, **Time to First Token Latency** and **Output Token Throughput**.

These new metrics can be specified as either objectives or constraints.

***NOTE: In order to enable these new metrics you must enable `streaming` in `genai_perf_flags` and the `client protocol` must be set to `gRPC`***

---

## Multi-Model Search Mode[#](#multi-model-search-mode "Link to this heading")

*This mode has the following limitations:*

* Can only be run in `quick` search mode
* Does not support detailed reporting, only summary reports

Multi-model concurrent search mode can be enabled by adding the parameter `--run-config-profile-models-concurrently-enable` to the CLI.

It uses Quick Search modeâs hill climbing algorithm to search all models configurations spaces in parallel, looking for the maximal objective value within the specified constraints. Model Analyzer has observed positive outcomes towards finding the maximum objective value; with typical runtimes of around 20-30 minutes (compared to the days it would take a brute force run to complete) for a two to three model run.

After it has found the best config(s), it will then sweep the top-N configurations found (specified by `--num-configs-per-model`) over the default concurrency range before generation of the summary reports.

*Note:* The algorithm attempts to find the most fair and optimal result for all models, by evaluating each model objectiveâs gain/loss. In many cases this will result in the algorithm ranking higher a configuration that has a lower total combined throughput (if that was the objective), if this better balances the throughputs of all the models.

---

*An example model analyzer YAML config that performs a Multi-model search:*

```
model_repository: /path/to/model/repository/

run_config_profile_models_concurrently_enable: true

profile_models:
  - model_A
  - model_B
```

---

### **Model Weighting**[#](#model-weighting "Link to this heading")

In addition to setting a modelâs objectives or constraints, in multi-model search mode, you have the ability to set a modelâs weighting. By default each model is set for equal weighting (value of 1), but in the YAML you can specify `weighting: <int>` which will bias that modelâs objectives when evaluating for an optimal result.

---

*An example where model Aâs objective gains (towards minimizing latency) will have 3 times the importance versus maximizing model Bâs throughput gains:*

```
model_repository: /path/to/model/repository/

run_config_profile_models_concurrently_enable: true

profile_models:
  model_A:
    weighting: 3
    objectives:
      perf_latency_p99: 1
  model_B:
    weighting: 1
    objectives:
      perf_throughput: 1
```

