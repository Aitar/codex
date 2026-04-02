* Single-Model...

# Single-Model Quick Start[#](#single-model-quick-start "Link to this heading")

The steps below will guide you through using Model Analyzer in Docker mode to profile and analyze a simple PyTorch model: add\_sub.

## `Step 1:` Download the add\_sub model[#](#step-1-download-the-add-sub-model "Link to this heading")

---

**1. Create a new directory and enter it**

```
mkdir <new_dir> && cd <new_dir>
```

**2. Start a git repository**

```
git init && git remote add -f origin https://github.com/triton-inference-server/model_analyzer.git
```

**3. Enable sparse checkout, and download the examples directory, which contains the add\_sub model**

```
git config core.sparseCheckout true && \
echo 'examples' >> .git/info/sparse-checkout && \
git pull origin main
```

## `Step 2:` Pull and Run the SDK Container[#](#step-2-pull-and-run-the-sdk-container "Link to this heading")

---

**1. Pull the SDK container:**

```
docker pull nvcr.io/nvidia/tritonserver:25.12-py3-sdk
```

**2. Run the SDK container**

```
docker run -it --gpus all \
      -v /var/run/docker.sock:/var/run/docker.sock \
      -v $(pwd)/examples/quick-start:$(pwd)/examples/quick-start \
      --net=host nvcr.io/nvidia/tritonserver:25.12-py3-sdk
```

## `Step 3:` Profile the `add_sub` model[#](#step-3-profile-the-add-sub-model "Link to this heading")

---

The [examples/quick-start](https://github.com/triton-inference-server/model_analyzer/blob/main/examples/quick-start) directory is an example
[Triton Model Repository](https://github.com/triton-inference-server/server/blob/r25.12/docs/user_guide/model_repository.md) that contains a simple libtorch model which calculates
the sum and difference of two inputs.

Run the Model Analyzer `profile` subcommand inside the container with:

```
model-analyzer profile \
    --model-repository <path-to-examples-quick-start> \
    --profile-models add_sub --triton-launch-mode=docker \
    --output-model-repository-path <path-to-output-model-repo>/<output_dir> \
    --export-path profile_results
```

**Important:** You must specify an `<output_dir>` subdirectory. You cannot have `--output-model-repository-path` point directly to `<path-to-output-model-repo>`

**Important:** If you already ran this earlier in the container, you can use the `--override-output-model-repository` option to overwrite the earlier results.

**Important:** The checkpoint directory should be removed between consecutive runs of
the `model-analyzer profile` command.

This will perform a search across limited configurable model parameters on the
`add_sub` model. This can take up to 60 minutes to finish. If you want a shorter
run (1-2 minutes) for example purposes, you can run with the below additional
options. Note that these options are not intended to find the best
configuration:

```
--run-config-search-max-concurrency 2 \
--run-config-search-max-model-batch-size 2 \
--run-config-search-max-instance-count 2
```

* `--run-config-search-max-concurrency` sets the max concurrency value that run
  config search will not go beyond.
* `--run-config-search-max-model-batch-size` sets the highest max\_batch\_size that run config search will not go beyond.
* `--run-config-search-max-instance-count`
  sets the max instance group count value that run config search will not go beyond.

With these options, model analyzer will test 5 configs (4 new configs as well as the unmodified default add\_sub config), and each config will have 2 experiments run on Perf Analyzer (concurrency=1 and concurrency=2). This significantly reduces the search space, and therefore, model analyzerâs runtime.

The measured data and summary report will be placed inside the
`./profile_results` directory. The directory will be structured as follows.

```
$HOME
  |--- model_analyzer
              |--- profile_results
              .       |--- plots
              .       |      |--- simple
              .       |      |      |--- add_sub
                      |      |              |--- gpu_mem_v_latency.png
                      |      |              |--- throughput_v_latency.png
                      |      |
                      |      |--- detailed
                      |             |--- add_sub
                      |                     |--- gpu_mem_v_latency.png
                      |                     |--- throughput_v_latency.png
                      |
                      |--- results
                      |       |--- metrics-model-inference.csv
                      |       |--- metrics-model-gpu.csv
                      |       |--- metrics-server-only.csv
                      |
                      |--- reports
                              |--- summaries
                              .        |--- add_sub
                              .                |--- result_summary.pdf
```

## `Step 4:` Generate a Detailed Report[#](#step-4-generate-a-detailed-report "Link to this heading")

---

Model analyzerâs report subcommand allows you to examine the performance of a
model config variant in detail. For example, it can show you the latency
breakdown of your model to help you identify potential bottlenecks in your model
performance.  
  
The detailed reports also contain other configurable plots and a
table of measurements taken of that particular config. You can generate a
detailed report for the two `add_sub` model configs `add_sub_config_default` and
`add_sub_config_0` using:

```
$ model-analyzer report --report-model-configs add_sub_config_default,add_sub_config_0 -e profile_results
```

This will create directories named after each of the model configs under
`./profile_results/reports/detailed` containing the detailed report PDF files as
shown below.

```
$HOME
  |--- model_analyzer
              |--- profile_results
              .       .
              .       .
                      .
                      |--- reports
                              .
                              .
                              .
                              |--- detailed
                                       |--- add_sub_config_default
                                       |        |--- detailed_report.pdf
                                       |
                                       |--- add_sub_config_0
                                                |--- detailed_report.pdf
```

