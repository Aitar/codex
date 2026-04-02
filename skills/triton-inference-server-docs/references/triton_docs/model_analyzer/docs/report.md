* [Model Analyzer](../../perf_benchmark/model_analyzer.md)
* Model...

# Model Analyzer Reports[#](#model-analyzer-reports "Link to this heading")

The Model analyzer can run inferences with models across multiple parameters. It
can also generate reports containing useful plots such as the throughput versus
latency curve obtained from these inference runs, as well as tables describing
the best performing model configurations for each model.

## Summary Reports[#](#summary-reports "Link to this heading")

The most basic type of report is the *Summary Report* which the Model Analyzerâs
`profile` subcommand generates by default for each model.

```
$ model-analyzer profile --profile-models <list of model names> --checkpoint-directory <path to checkpoints directory> -e <path to export directory> -f <path to optional config file>
```

The export directory will, by default, contain 3 subdirectories. The summary
report for a model will be located in `[export-path]/reports/summaries/<model name>`. The report will look like the one shown [*here*](https://github.com/triton-inference-server/model_analyzer/blob/main/examples/online_summary.pdf).

To disable summary report generation use `--skip-summary-reports` or set the
`skip_summary_reports` yaml option to `false`.

## Detailed Reports[#](#detailed-reports "Link to this heading")

The second type of report is the *Detailed Report* which can be generated using
the Model Analyzerâs `report` subcommand.

```
$ model-analyzer report --report-model-configs <list of model configs> --checkpoint-directory <path to checkpoints directory> -e <path to export directory> -f <path to optional config file>
```

You will be able to locate the detailed report for a model config under
`[export-path]/reports/detailed/<model config name>` The detailed reports
contain a detailed breakdown plot of the throughput vs latency for the
particular model config with which the measurements are obtained, as well as
extra configurable plots. The user can define the plots they would like to see
in the detailed report using the YAML config file (See [**Configuring Model
Analyzer**](config.md) section for more details) The detailed report will
look like the one shown [*here*](https://github.com/triton-inference-server/model_analyzer/blob/main/examples/online_detailed_report.pdf).

See the [**configuring model
analyzer**](config.md) section for more details on how to configure these
reports.

Detailed reports for the top-N (based on the value of `--num-configs-per-model`) configurations are also generated at the end of `profile`.
To disable detailed report generation after `profile` use `--skip-detailed-reports` or set the
`skip_detailed_reports` yaml option to `false`.

