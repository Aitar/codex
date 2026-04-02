# Continuous Integration Overview — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/developer-guide/ci-overview.html

Continuous Integration Overview#

This page explains how TensorRT‑LLM’s CI is organized and how individual tests map to Jenkins stages. Most stages execute integration tests defined in YAML files, while unit tests run as part of a merge‑request pipeline. The sections below describe how to locate a test and trigger the stage that runs it.

Table of Contents#

CI pipelines

Test definitions

Unit tests

Jenkins stage names

Finding the stage for a test

Waiving tests

Triggering CI Best Practices

CI pipelines#

Pull requests do not start testing by themselves. Developers trigger the CI by commenting `/botrun` (optionally with arguments) on the pull request (see Pull Request Template for more details). That kicks off the merge-request pipeline (defined in `jenkins/L0_MergeRequest.groovy`), which runs unit tests and integration tests whose YAML entries specify `stage:pre_merge`. Once a pull request is merged, a separate post-merge pipeline (defined in `jenkins/L0_Test.groovy`) runs every test marked `post_merge` across all supported GPU configurations.

`stage` tags live in the YAML files under `tests/integration/test_lists/test-db/`. Searching those files for `stage:pre_merge` shows exactly which tests the merge-request pipeline covers.

Test definitions#

Integration tests are listed under `tests/integration/test_lists/test-db/`. Most YAML files are named after the GPU or configuration they run on (for example `l0_a100.yml`). Some files, like `l0_sanity_check.yml`, use wildcards and can run on multiple hardware types. Entries contain conditions and a list of tests. Two important terms in each entry are:

`stage`: either `pre_merge` or `post_merge`.

`backend`: `pytorch`, `tensorrt` or `triton`.

Example from `l0_a100.yml`:

```text
      terms:
        stage: post_merge
        backend: triton
  tests:
  - triton_server/test_triton.py::test_gpt_ib_ptuning[gpt-ib-ptuning]
```

Unit tests#

Unit tests live under `tests/unittest/` and run during the merge-request pipeline. They are invoked from `jenkins/L0_MergeRequest.groovy` and do not require mapping to specific hardware stages.

Jenkins stage names#

`jenkins/L0_Test.groovy` maps stage names to these YAML files. For A100 the mapping includes:

```text
    "A100X-Triton-[Post-Merge]-1": ["a100x", "l0_a100", 1, 2],
    "A100X-Triton-[Post-Merge]-2": ["a100x", "l0_a100", 2, 2],
```

The array elements are: GPU type, YAML file (without extension), shard index, and total number of shards. Only tests with `stage:post_merge` from that YAML file are selected when a `Post-Merge` stage runs.

Finding the stage for a test#

Locate the test in the appropriate YAML file under `tests/integration/test_lists/test-db/` and note its `stage` and `backend` values.

Search `jenkins/L0_Test.groovy` for a stage whose YAML file matches (for example `l0_a100`) and whose name contains `[Post-Merge]` if the YAML entry uses `stage:post_merge`.

The resulting stage name(s) are what you pass to Jenkins via the `stage_list` parameter when triggering a job.

Using `test_to_stage_mapping.py`#

Manually searching YAML and Groovy files can be tedious. The helper script
`scripts/test_to_stage_mapping.py` automates the lookup:

```text
python scripts/test_to_stage_mapping.py --tests "triton_server/test_triton.py::test_gpt_ib_ptuning[gpt-ib-ptuning]"
python scripts/test_to_stage_mapping.py --tests gpt_ib_ptuning
python scripts/test_to_stage_mapping.py --stages A100X-Triton-Post-Merge-1
python scripts/test_to_stage_mapping.py --test-list my_tests.txt
python scripts/test_to_stage_mapping.py --test-list my_tests.yml
```

The first two commands print the Jenkins stages that run the specified tests or
patterns. Patterns are matched by substring, so partial test names are
supported out of the box. The third lists every test executed in the given stage. When
providing tests on the command line, quote each test string so the shell does
not interpret the `[` and `]` characters as globs. Alternatively, store the
tests in a newline‑separated text file or a YAML list and supply it with
`--test-list`.

To run the same tests on your pull request, comment:

```text
/bot run --stage-list "A100X-Triton-[Post-Merge]-1,A100X-Triton-[Post-Merge]-2"
```

This executes the same tests that run post-merge for this hardware/backend.

Waiving tests#

Sometimes a test is known to fail due to a bug or unsupported feature. Instead
of removing it from the YAML test lists, add the test name to
`tests/integration/test_lists/waives.txt`. Every CI run passes this file to
pytest via `--waives-file`, so the listed tests are skipped automatically.

Each line contains the fully qualified test name followed by an optional
`SKIP(reason)` marker. A `full:GPU_TYPE/` prefix restricts the waive to a
specific hardware family. Example:

```text
examples/test_openai.py::test_llm_openai_triton_1gpu SKIP (https://nvbugspro.nvidia.com/bug/4963654)
full:GH200/examples/test_qwen2audio.py::test_llm_qwen2audio_single_gpu[qwen2_audio_7b_instruct] SKIP (arm is not supported)
```

Changes to `waives.txt` should include a bug link or brief explanation so other
developers understand why the test is disabled.

Triggering CI Best Practices#

Triggering Post-merge tests#

When you only need to verify a handful of post-merge tests, avoid the heavy
`/botrun--post-merge` command. Instead, specify exactly which stages to run:

```text
/bot run --stage-list "stage-A,stage-B"
```

This runs only the stages listed. You can also add stages on top of the
default pre-merge set:

```text
/bot run --extra-stage "stage-A,stage-B"
```

Both options accept any stage name defined in `jenkins/L0_Test.groovy`. Being
selective keeps CI turnaround fast and conserves hardware resources.

Avoiding unnecessary `--disable-fail-fast` usage#

Avoid habitually using `--disable-fail-fast` as it wastes scarce hardware resources. The CI system automatically reuses successful test stages when commits remain unchanged, and subsequent `/botrun` commands only retry failed stages. Overusing `--disable-fail-fast` keeps failed pipelines consuming resources (like DGX-H100s), increasing queue backlogs and reducing team efficiency.
