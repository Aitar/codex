* GenAI-Perf...

# GenAI-Perf Process Export Files Subcommand[#](#genai-perf-process-export-files-subcommand "Link to this heading")

The `process-export-files` subcommand is used to process multiple profile export files from distributed runs
and generate outputs with aggregated metrics.

## Process Export Files CLI[#](#process-export-files-cli "Link to this heading")

The `process-export-files` uses the following CLI options:

`--input-directory/-d` - The path to the input directory containing directories of profile export files from distributed runs (default: `aggregated`). These directories must include perf analyzer profile export (e.g., profile\_export.json) and GenAI-Perf profile export JSON files (e.g., profile\_export\_genai\_perf.json).

Example input directory structure

```
input_dir/
    âââ run_1/
    â   âââ profile_export.json
    â   âââ profile_export_genai_perf.json
    âââ run_2/
    â   âââ profile_export.json
    â   âââ profile_export_genai_perf.json
    âââ run_3/
        âââ profile_export.json
        âââ profile_export_genai_perf.json
```

> [!Note]
> The file names can be anything as long as the files are of the correct type: one for perf analyzer profile data (\*.json) and
> one for GenAI-Perf profile data (\*\_genai\_perf.json).
> The names provided here (e.g., profile\_export.json and profile\_export\_genai\_perf.json) are just examples.

The `process-export-files` subcommand supports the following output options:

`--artifact-dir` - Specifies the directory where artifacts will be saved.

`--profile-export-file` - Custom name for the profile export files.

> [!Note]
> This subcommand does not support the `--generate-plots` option.

### CLI Examples[#](#cli-examples "Link to this heading")

```
genai-perf process-export-files --input-directory /path/to/input/directory
```

Example output:

```
                               NVIDIA GenAI-Perf | LLM Metrics
ââââââââââââââââââââââââââââââââââââââââ³âââââââââ³âââââââââ³âââââââââ³âââââââââ³âââââââââ³âââââââââ
â                            Statistic â    avg â    min â    max â    p99 â    p90 â    p75 â
â¡âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ©
â             Time To First Token (ms) â  11.59 â   6.38 â  43.23 â  41.11 â  17.29 â  15.22 â
â            Time To Second Token (ms) â   4.13 â   3.84 â   7.22 â   6.67 â   4.05 â   4.00 â
â                 Request Latency (ms) â  71.89 â  64.63 â 103.02 â 102.05 â  80.83 â  74.94 â
â             Inter Token Latency (ms) â   4.03 â   3.88 â   4.39 â   4.37 â   4.26 â   4.02 â
â     Output Token Throughput Per User â 248.14 â 227.77 â 257.95 â 257.66 â 256.09 â 252.30 â
â                    (tokens/sec/user) â        â        â        â        â        â        â
â      Output Sequence Length (tokens) â  15.95 â  15.00 â  16.00 â  16.00 â  16.00 â  16.00 â
â       Input Sequence Length (tokens) â 550.00 â 550.00 â 550.00 â 550.00 â 550.00 â 550.00 â
â Output Token Throughput (tokens/sec) â 443.39 â    N/A â    N/A â    N/A â    N/A â    N/A â
â         Request Throughput (per sec) â  27.80 â    N/A â    N/A â    N/A â    N/A â    N/A â
â                Request Count (count) â  20.00 â    N/A â    N/A â    N/A â    N/A â    N/A â
ââââââââââââââââââââââââââââââââââââââââ´âââââââââ´âââââââââ´âââââââââ´âââââââââ´âââââââââ´âââââââââ
```

This command processes profile export files from distributed runs located in subdirectories inside `/path/to/input/directory`.
It aggregates results across all runs and displays the aggregated metrics on the console.
The merged profile export file, along with GenAI-Perf JSON and CSV export files, are stored in the specified `artifacts` directory.

> [!Note]
> Users should ensure that the profile export files provided are comparable.
> For example, if profile results from different stimuli types (e.g., `concurrency`, `request rate`)
> are provided, they will be aggregated together, which may lead to unintended results.

