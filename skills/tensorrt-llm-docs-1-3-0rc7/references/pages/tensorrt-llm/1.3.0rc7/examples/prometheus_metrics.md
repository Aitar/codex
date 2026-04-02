# Prometheus Metrics — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/examples/prometheus_metrics.html

Prometheus Metrics#

Refer to the trtllm-serve documentation for starting a server.

Source NVIDIA/TensorRT-LLM.

```text
  1
  2# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
  3# SPDX-License-Identifier: Apache-2.0
  4#
  5# Licensed under the Apache License, Version 2.0 (the "License");
  6# you may not use this file except in compliance with the License.
  7# You may obtain a copy of the License at
  8#
  9# http://www.apache.org/licenses/LICENSE-2.0
 10#
 11# Unless required by applicable law or agreed to in writing, software
 12# distributed under the License is distributed on an "AS IS" BASIS,
 13# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 14# See the License for the specific language governing permissions and
 15# limitations under the License.
 16
 17from urllib.request import urlopen
 18
 19from openai import OpenAI
 20
 21# Initialize the OpenAI client
 22client = OpenAI(
 23    base_url="http://localhost:8000/v1",
 24    api_key="tensorrt_llm",
 25)
 26
 27# Prometheus metric prefix used by TensorRT-LLM
 28METRIC_PREFIX = "trtllm_"
 29
 30# Base URL for the metrics endpoint
 31METRICS_URL = "http://localhost:8000/prometheus/metrics"
 32
 33
 34def fetch_metrics() -> dict | None:
 35    """Fetch metrics from the Prometheus endpoint."""
 36    try:
 37        response = urlopen(METRICS_URL)
 38        if response.status == 200:
 39            return response.read().decode("utf-8")
 40        else:
 41            print(f"Error fetching metrics: HTTP {response.status}")
 42            return None
 43    except Exception as e:
 44        print(f"Error fetching metrics: {e}")
 45        return None
 46
 47
 48def parse_and_display_metrics(metrics_data: dict) -> None:
 49    """Parse and display relevant TensorRT-LLM metrics."""
 50    if not metrics_data:
 51        return
 52
 53    print("\n" + "=" * 80)
 54    print("TensorRT-LLM Prometheus Metrics")
 55    print("=" * 80)
 56
 57    # Define metrics to display with descriptions
 58    metrics_of_interest = {
 59        f"{METRIC_PREFIX}request_success_total": "Total successful requests",
 60        f"{METRIC_PREFIX}e2e_request_latency_seconds": "End-to-end request latency",
 61        f"{METRIC_PREFIX}time_to_first_token_seconds": "Time to first token",
 62        f"{METRIC_PREFIX}request_queue_time_seconds": "Request queue time",
 63        f"{METRIC_PREFIX}kv_cache_hit_rate": "KV cache hit rate",
 64        f"{METRIC_PREFIX}kv_cache_utilization": "KV cache utilization",
 65    }
 66
 67    found_metrics = []
 68    missing_metrics = []
 69
 70    for metric_name, description in metrics_of_interest.items():
 71        if metric_name in metrics_data:
 72            found_metrics.append((metric_name, description))
 73        else:
 74            missing_metrics.append((metric_name, description))
 75
 76    # Display found metrics
 77    if found_metrics:
 78        print("\n✓ Available Metrics:")
 79        print("-" * 80)
 80        for metric_name, description in found_metrics:
 81            # Extract the metric lines from the data
 82            lines = [
 83                line
 84                for line in metrics_data.split("\n")
 85                if line.startswith(metric_name) and not line.startswith("#")
 86            ]
 87            print(f"\n{description} ({metric_name}):")
 88            for line in lines:
 89                print(f"  {line}")
 90
 91    # Display missing metrics
 92    if missing_metrics:
 93        print("\n✗ Not Yet Available:")
 94        print("-" * 80)
 95        for metric_name, description in missing_metrics:
 96            print(f"  {description} ({metric_name})")
 97
 98    print("\n" + "=" * 80)
 99
100
101def main():
102    print("Prometheus Metrics Example")
103    print("=" * 80)
104    print("This script will:")
105    print("1. Send several completion requests to a running TensorRT-LLM server")
106    print(
107        "2. After each response, fetch and display Prometheus metrics from the /prometheus/metrics endpoint"
108    )
109    print()
110
111    # Make several completion requests to generate metrics
112    print("Sending completion requests...")
113    num_requests = 10
114    for i in range(num_requests):
115        try:
116            response = client.completions.create(
117                model="Server",
118                prompt=(
119                    f"Hello, this is request {i + 1}. "
120                    "Use your greatest imagination in this request. Tell me a lot about"
121                ),
122                max_tokens=1000,
123                stream=False,
124            )
125            print(
126                f"  Request {i + 1}/{num_requests} completed. Response: {response.choices[0].text[:50]}..."
127            )
128
129            # Fetch and display metrics after each response
130            print(f"\n  Fetching metrics after request {i + 1}...")
131            metrics_data = fetch_metrics()
132            if metrics_data:
133                parse_and_display_metrics(metrics_data)
134            else:
135                print("  ✗ Failed to fetch metrics")
136            print()
137        except Exception as e:
138            print(f"  Error on request {i + 1}: {e}")
139    print("All requests completed.")
140
141
142if __name__ == "__main__":
143    main()
```
