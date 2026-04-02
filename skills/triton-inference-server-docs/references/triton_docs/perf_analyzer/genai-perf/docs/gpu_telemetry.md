* Collecting...

# Collecting GPU Telemetry[#](#collecting-gpu-telemetry "Link to this heading")

This guide explains how to enable GPU metric collection during benchmarking with GenAI-Perf.
It also covers setting up the NVIDIA DCGM Exporter on the same machine as the inference server.

## Run the DCGM Exporter container[#](#run-the-dcgm-exporter-container "Link to this heading")

Create a custom GPU metrics file using the following command:

```
cat > custom_gpu_metrics.csv << 'EOF'
# Format
# If line starts with a '#' it is considered a comment
# DCGM FIELD, Prometheus metric type, help message

# Clocks
DCGM_FI_DEV_SM_CLOCK, gauge, SM clock frequency (in MHz)
DCGM_FI_DEV_MEM_CLOCK, gauge, Memory clock frequency (in MHz)

# Temperature
DCGM_FI_DEV_MEMORY_TEMP, gauge, Memory temperature (in Â°C)
DCGM_FI_DEV_GPU_TEMP, gauge, GPU temperature (in Â°C)

# Power
DCGM_FI_DEV_POWER_USAGE, gauge, Power draw (in W)
DCGM_FI_DEV_POWER_MGMT_LIMIT, gauge, Power management limit (in W)
DCGM_FI_DEV_TOTAL_ENERGY_CONSUMPTION, counter, Total energy consumption since boot (in mJ)

# Memory usage
DCGM_FI_DEV_FB_FREE, gauge, Framebuffer memory free (in MiB)
DCGM_FI_DEV_FB_TOTAL, gauge, Total framebuffer memory (in MiB)
DCGM_FI_DEV_FB_USED, gauge, Framebuffer memory used (in MiB)

# Utilization
DCGM_FI_DEV_GPU_UTIL, gauge, GPU utilization (in %)
DCGM_FI_DEV_MEM_COPY_UTIL, gauge, Memory copy utilization (in %)
DCGM_FI_DEV_ENC_UTIL, gauge, Encoder utilization (in %)
DCGM_FI_DEV_DEC_UTIL, gauge, Decoder utilization (in %)
DCGM_FI_PROF_SM_ACTIVE, gauge, Ratio of cycles at least one warp is active per SM

# ECC
DCGM_FI_DEV_ECC_SBE_VOL_TOTAL, counter, Total number of single-bit volatile ECC errors.
DCGM_FI_DEV_ECC_DBE_VOL_TOTAL, counter, Total number of double-bit volatile ECC errors.
DCGM_FI_DEV_ECC_SBE_AGG_TOTAL, counter, Total number of single-bit persistent ECC errors.
DCGM_FI_DEV_ECC_DBE_AGG_TOTAL, counter, Total number of double-bit persistent ECC errors.

# Errors and violations
DCGM_FI_DEV_XID_ERRORS,              gauge,   Value of the last XID error encountered.
DCGM_FI_DEV_POWER_VIOLATION,       counter, Throttling duration due to power constraints (in us).
DCGM_FI_DEV_THERMAL_VIOLATION,     counter, Throttling duration due to thermal constraints (in us).

# Retired pages
DCGM_FI_DEV_RETIRED_SBE,     counter, Total number of retired pages due to single-bit errors.
DCGM_FI_DEV_RETIRED_DBE,     counter, Total number of retired pages due to double-bit errors.

# NVLink
DCGM_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT_TOTAL, counter, Total number of NVLink flow-control CRC errors.
DCGM_FI_DEV_NVLINK_CRC_DATA_ERROR_COUNT_TOTAL, counter, Total number of NVLink data CRC errors.

# PCIE
DCGM_FI_PROF_PCIE_TX_BYTES,      gauge, The rate of data transmitted over the PCIe bus - including both protocol headers and data payloads - in bytes per second.
DCGM_FI_PROF_PCIE_RX_BYTES,      gauge, The rate of data received over the PCIe bus - including both protocol headers and data payloads - in bytes per second.
DCGM_FI_DEV_PCIE_REPLAY_COUNTER, counter, Total number of PCIe retries.
EOF
```

This will generate a `custom_gpu_metrics.csv` file that can be mounted into the DCGM Exporter container and
used directly for GPU telemetry collection with GenAI-Perf.

> [!Note]
> You can also view the complete metrics file at [custom\_gpu\_metrics.csv](https://github.com/triton-inference-server/perf_analyzer/blob/main/genai-perf/docs/assets/custom_gpu_metrics.csv) for reference or direct use.

Start the DCGM Exporter using Docker on the same machine as your inference server:

```
docker run -d --gpus all --cap-add SYS_ADMIN \
  -p 9400:9400 \
  -v "$PWD/custom_gpu_metrics.csv:/etc/dcgm-exporter/custom.csv" \
  -e DCGM_EXPORTER_INTERVAL=33 \
  nvcr.io/nvidia/k8s/dcgm-exporter:4.2.0-4.1.0-ubuntu22.04 \
  -f /etc/dcgm-exporter/custom.csv
```

### Configuration Details[#](#configuration-details "Link to this heading")

#### Custom Collection Interval[#](#custom-collection-interval "Link to this heading")

By default, DCGM Exporter collects telemetry metrics every 30 seconds, which is too infrequent for detailed performance benchmarking.
GenAI-Perf expects metrics to be collected every 33 milliseconds for fine-grained profiling.
This is configured via the following environment variable:

```
-e DCGM_EXPORTER_INTERVAL=33
```

### Custom GPU Metrics[#](#custom-gpu-metrics "Link to this heading")

DCGM Exporter comes with a default set of metrics, but GenAI-Perf supports additional metrics that are not collected by default.

To collect all supported metrics,
you can either use the file you generated using the steps above, or refer to the provided [custom\_gpu\_metrics.csv](https://github.com/triton-inference-server/perf_analyzer/blob/main/genai-perf/docs/assets/custom_gpu_metrics.csv) file.
Mount it into the container using:

```
-v "$PWD/custom_gpu_metrics.csv:/etc/dcgm-exporter/custom.csv"
```

> [!Note]
> You may comment out any metrics you do not want to collect in the CSV file.
> Lines starting with # are ignored by the exporter.

## Verifying DCGM Exporter is running[#](#verifying-dcgm-exporter-is-running "Link to this heading")

Once the container is running, confirm that metrics are being collected by running:

```
curl "localhost:9400/metrics"
```

You should see an output like this:

```
# HELP DCGM_FI_DEV_SM_CLOCK SM clock frequency (in MHz).
# TYPE DCGM_FI_DEV_SM_CLOCK gauge
# HELP DCGM_FI_DEV_MEM_CLOCK Memory clock frequency (in MHz).
# TYPE DCGM_FI_DEV_MEM_CLOCK gauge
# HELP DCGM_FI_DEV_MEMORY_TEMP Memory temperature (in C).
# TYPE DCGM_FI_DEV_MEMORY_TEMP gauge
...
DCGM_FI_DEV_SM_CLOCK{gpu="0", UUID="GPU-604ac76c-d9cf-fef3-62e9-d92044ab6e52"} 139
DCGM_FI_DEV_MEM_CLOCK{gpu="0", UUID="GPU-604ac76c-d9cf-fef3-62e9-d92044ab6e52"} 405
DCGM_FI_DEV_MEMORY_TEMP{gpu="0", UUID="GPU-604ac76c-d9cf-fef3-62e9-d92044ab6e52"} 9223372036854775794
...
```

> [!Note]
> For more details, see the [official DCGM Exporter documentation](https://github.com/NVIDIA/dcgm-exporter).

## Run GenAI-Perf[#](#run-genai-perf "Link to this heading")

Once the DCGM Exporter is up and running, start benchmarking using GenAI-Perf.

Use the `--server-metrics-urls <list>` flag to specify one or more DCGM Exporter /metrics endpoints
from which GPU telemetry will be collected during benchmarking.

Example:

```
--server-metrics-urls http://localhost:9400/metrics http://remote-node:9400/metrics
```

By default, GenAI-Perf collects metrics from `http://localhost:9400/metrics`.

> [!Note]
> To enable printing GPU telemetry metrics on console, pass the `--verbose` or `-v` flag.

Example command:

```
genai-perf profile \
    -m gpt2 \
    --endpoint-type chat \
    --server-metrics-urls http://localhost:9400/metrics \
    --verbose
```

Example console output in `verbose` mode:

```
                 NVIDIA GenAI-Perf | Power Metrics
ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
â                                                                  â
â¡âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ©
â                       GPU Power Usage (W)                        â
â âââââââââââââ³ââââââââ³ââââââââ³âââââââââ³âââââââââ³âââââââââ³ââââââââ â
â â GPU Index â   avg â   min â    max â    p99 â    p90 â   p75 â â
â â¡âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ© â
â â         0 â 63.55 â 21.00 â 111.39 â 110.84 â 105.91 â 95.16 â â
â âââââââââââââ´ââââââââ´ââââââââ´âââââââââ´âââââââââ´âââââââââ´ââââââââ â
â                 GPU Power Limit (W)                              â
â âââââââââââââ³âââââââââ³ââââââ³ââââââ³ââââââ³ââââââ³ââââââ             â
â â GPU Index â    avg â min â max â p99 â p90 â p75 â             â
â â¡âââââââââââââââââââââââââââââââââââââââââââââââââââ©             â
â â         0 â 300.00 â N/A â N/A â N/A â N/A â N/A â             â
â âââââââââââââ´âââââââââ´ââââââ´ââââââ´ââââââ´ââââââ´ââââââ             â
â                    Energy Consumption (MJ)                       â
â âââââââââââââ³ââââââââ³ââââââââ³ââââââââ³ââââââââ³ââââââââ³ââââââââ    â
â â GPU Index â   avg â   min â   max â   p99 â   p90 â   p75 â    â
â â¡ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ©    â
â â         0 â 67.33 â 67.33 â 67.33 â 67.33 â 67.33 â 67.33 â    â
â âââââââââââââ´ââââââââ´ââââââââ´ââââââââ´ââââââââ´ââââââââ´ââââââââ    â
ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
               NVIDIA GenAI-Perf | Memory Metrics
âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
â                                                               â
â¡ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ©
â                     GPU Memory Used (GB)                      â
â âââââââââââââ³ââââââââ³ââââââââ³ââââââââ³ââââââââ³ââââââââ³ââââââââ â
â â GPU Index â   avg â   min â   max â   p99 â   p90 â   p75 â â
â â¡ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ© â
â â         0 â 45.99 â 45.99 â 45.99 â 45.99 â 45.99 â 45.99 â â
â âââââââââââââ´ââââââââ´ââââââââ´ââââââââ´ââââââââ´ââââââââ´ââââââââ â
â                Total GPU Memory (GB)                          â
â âââââââââââââ³ââââââââ³ââââââ³ââââââ³ââââââ³ââââââ³ââââââ           â
â â GPU Index â   avg â min â max â p99 â p90 â p75 â           â
â â¡ââââââââââââââââââââââââââââââââââââââââââââââââââ©           â
â â         0 â 51.53 â N/A â N/A â N/A â N/A â N/A â           â
â âââââââââââââ´ââââââââ´ââââââ´ââââââ´ââââââ´ââââââ´ââââââ           â
âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
       NVIDIA GenAI-Perf | Utilization Metrics
âââââââââââââââââââââââââââââââââââââââââââââââââââââ
â                                                   â
â¡ââââââââââââââââââââââââââââââââââââââââââââââââââââ©
â                GPU Utilization (%)                â
â âââââââââââââ³ââââââ³ââââââ³ââââââ³ââââââ³ââââââ³ââââââ â
â â GPU Index â avg â min â max â p99 â p90 â p75 â â
â â¡ââââââââââââââââââââââââââââââââââââââââââââââââ© â
â â         0 â  28 â   0 â  50 â  50 â  50 â  49 â â
â âââââââââââââ´ââââââ´ââââââ´ââââââ´ââââââ´ââââââ´ââââââ â
âââââââââââââââââââââââââââââââââââââââââââââââââââââ
```

Example output on a machine with multiple GPUs:

```
                NVIDIA GenAI-Perf | Power Metrics
âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
â                                                               â
â¡ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ©
â                      GPU Power Usage (W)                      â
â âââââââââââââ³ââââââââ³ââââââââ³ââââââââ³ââââââââ³ââââââââ³ââââââââ â
â â GPU Index â   avg â   min â   max â   p99 â   p90 â   p75 â â
â â¡ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ© â
â â         0 â 79.60 â 59.40 â 98.85 â 98.37 â 94.03 â 88.96 â â
â â         1 â 42.09 â 42.08 â 42.10 â 42.10 â 42.10 â 42.10 â â
â â         2 â 43.99 â 43.98 â 44.00 â 44.00 â 44.00 â 44.00 â â
â â         3 â 42.56 â 42.56 â 42.56 â 42.56 â 42.56 â 42.56 â â
â âââââââââââââ´ââââââââ´ââââââââ´ââââââââ´ââââââââ´ââââââââ´ââââââââ â
â                 GPU Power Limit (W)                           â
â âââââââââââââ³âââââââââ³ââââââ³ââââââ³ââââââ³ââââââ³ââââââ          â
â â GPU Index â    avg â min â max â p99 â p90 â p75 â          â
â â¡âââââââââââââââââââââââââââââââââââââââââââââââââââ©          â
â â         0 â 300.00 â N/A â N/A â N/A â N/A â N/A â          â
â â         1 â 300.00 â N/A â N/A â N/A â N/A â N/A â          â
â â         2 â 300.00 â N/A â N/A â N/A â N/A â N/A â          â
â â         3 â 300.00 â N/A â N/A â N/A â N/A â N/A â          â
â âââââââââââââ´âââââââââ´ââââââ´ââââââ´ââââââ´ââââââ´ââââââ          â
â                 Energy Consumption (MJ)                       â
â âââââââââââââ³âââââââ³âââââââ³âââââââ³âââââââ³âââââââ³âââââââ       â
â â GPU Index â  avg â  min â  max â  p99 â  p90 â  p75 â       â
â â¡ââââââââââââââââââââââââââââââââââââââââââââââââââââââ©       â
â â         0 â 0.28 â 0.28 â 0.28 â 0.28 â 0.28 â 0.28 â       â
â â         1 â 0.23 â 0.23 â 0.23 â 0.23 â 0.23 â 0.23 â       â
â â         2 â 0.25 â 0.25 â 0.25 â 0.25 â 0.25 â 0.25 â       â
â â         3 â 0.24 â 0.24 â 0.24 â 0.24 â 0.24 â 0.24 â       â
â âââââââââââââ´âââââââ´âââââââ´âââââââ´âââââââ´âââââââ´âââââââ       â
âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
               NVIDIA GenAI-Perf | Memory Metrics
âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
â                                                               â
â¡ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ©
â                     GPU Memory Used (GB)                      â
â âââââââââââââ³ââââââââ³ââââââââ³ââââââââ³ââââââââ³ââââââââ³ââââââââ â
â â GPU Index â   avg â   min â   max â   p99 â   p90 â   p75 â â
â â¡ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ© â
â â         0 â 15.26 â 15.26 â 15.26 â 15.26 â 15.26 â 15.26 â â
â â         1 â  0.00 â  0.00 â  0.00 â  0.00 â  0.00 â  0.00 â â
â â         2 â  0.00 â  0.00 â  0.00 â  0.00 â  0.00 â  0.00 â â
â â         3 â  0.00 â  0.00 â  0.00 â  0.00 â  0.00 â  0.00 â â
â âââââââââââââ´ââââââââ´ââââââââ´ââââââââ´ââââââââ´ââââââââ´ââââââââ â
â                Total GPU Memory (GB)                          â
â âââââââââââââ³ââââââââ³ââââââ³ââââââ³ââââââ³ââââââ³ââââââ           â
â â GPU Index â   avg â min â max â p99 â p90 â p75 â           â
â â¡ââââââââââââââââââââââââââââââââââââââââââââââââââ©           â
â â         0 â 17.18 â N/A â N/A â N/A â N/A â N/A â           â
â â         1 â 17.18 â N/A â N/A â N/A â N/A â N/A â           â
â â         2 â 17.18 â N/A â N/A â N/A â N/A â N/A â           â
â â         3 â 17.18 â N/A â N/A â N/A â N/A â N/A â           â
â âââââââââââââ´ââââââââ´ââââââ´ââââââ´ââââââ´ââââââ´ââââââ           â
âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
       NVIDIA GenAI-Perf | Utilization Metrics
âââââââââââââââââââââââââââââââââââââââââââââââââââââ
â                                                   â
â¡ââââââââââââââââââââââââââââââââââââââââââââââââââââ©
â                GPU Utilization (%)                â
â âââââââââââââ³ââââââ³ââââââ³ââââââ³ââââââ³ââââââ³ââââââ â
â â GPU Index â avg â min â max â p99 â p90 â p75 â â
â â¡ââââââââââââââââââââââââââââââââââââââââââââââââ© â
â â         0 â  34 â   0 â  51 â  51 â  51 â  51 â â
â â         1 â   0 â   0 â   0 â   0 â   0 â   0 â â
â â         2 â   0 â   0 â   0 â   0 â   0 â   0 â â
â â         3 â   0 â   0 â   0 â   0 â   0 â   0 â â
â âââââââââââââ´ââââââ´ââââââ´ââââââ´ââââââ´ââââââ´ââââââ â
âââââââââââââââââââââââââââââââââââââââââââââââââââââ
```

> [!Note]
> GenAI-Perf prints a limited set of GPU metrics (as shown in the example output above) to the console
> when the âverbose (-v) flag is set. If GPU telemetry collection is configured correctly,
> all supported metrics enabled in the custom DCGM metrics file are always exported to CSV and JSON output files.

