* [Model Analyzer](../../perf_benchmark/model_analyzer.md)
* Checkpointin...

# Checkpointing in Model Analyzer[#](#checkpointing-in-model-analyzer "Link to this heading")

The Model Analyzer writes the collected measurements to checkpoint files when profiling. These are
located within the specified checkpoint directory (See [Config
Defaults](config.md#config-defaults) section for default location). Checkpoint files are used to create data table, summaries and detailed reports.

## When is Checkpointing Done?[#](#when-is-checkpointing-done "Link to this heading")

Model Analyzer saves a checkpoint in multiple circumstances:

1. Model Analyzer will save a checkpoint after all the perf
   analyzer runs for a given model are complete.
2. The user can initiate an early exit from profiling using `CTRL-C (SIGINT)`. This will wait for the current perf analyzer run to finish and
   then save a checkpoint before exiting.
3. If the user needs to exit immediately, they send the `SIGINT` 3 times. In
   this case, Model Analyzer will save a checkpoint and exit immediately.

## Checkpoint Naming Scheme[#](#checkpoint-naming-scheme "Link to this heading")

When a profiling run completes:

```
$ model-analyzer profile -m example_model_repo --profile-models example_model_1,example_model_2
2021-05-13 19:57:05.87 INFO[entrypoint.py:98] Starting a local Triton Server...
2021-05-13 19:57:05.92 INFO[server_local.py:64] Triton Server started.
2021-05-13 19:57:09.234 INFO[server_local.py:81] Triton Server stopped.
2021-05-13 19:57:09.235 INFO[analyzer_state_manager.py:118] No checkpoint file found, starting a fresh run.
.
.
.
2021-05-13 19:58:01.625 INFO[analyzer.py:110] Finished profiling. Obtained measurements for models: ['example_model_1', 'example_model_2']
```

In the checkpoint directory, there will be 2 checkpoints.

```
$ ls -l checkpoints
-rw-r--r-- 1 root root 11356 May 11 20:00 0.ckpt
-rw-r--r-- 1 root root 11356 May 13 19:58 1.ckpt
```

Checkpoints are named using consecutive non-negative integers. On startup, Model
Analyzer identifies the latest checkpoint (highest integer) and loads it. If
there are any changes to the data in the checkpoint, the checkpoint index is
incremented before it is saved again, thus creating a new latest checkpoint.

**Note**: Model analyzer does not clean up old checkpoints. It merely guarantees
that the checkpoint with the highest integer index is the one with the most
up-to-date measurements. The checkpoint directory should be removed between
consecutive runs of the `model-analyzer profile` command if you want to start
a fresh run.

