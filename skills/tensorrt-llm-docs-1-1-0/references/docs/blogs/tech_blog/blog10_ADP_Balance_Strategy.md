Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/blogs/tech_blog/blog10_ADP_Balance_Strategy.md

* ADP Balance Strategy

# ADP Balance Strategy[#](#adp-balance-strategy "Link to this heading")

By NVIDIA TensorRT LLM team

## Table of Contents[#](#table-of-contents "Link to this heading")

* [ADP Balance Strategy](#adp-balance-strategy)

  + [Table of Contents](#table-of-contents)
  + [Motivation and Background](#motivation-and-background)
  + [Theoretical Analysis and Modeling](#theoretical-analysis-and-modeling)

    - [Mathematical Modeling](#mathematical-modeling)
    - [Scheduling Strategies for Load Balancing](#scheduling-strategies-for-load-balancing)

      * [Baseline: Round-Robin Token Distribution](#baseline-round-robin-token-distribution)
      * [ADP Balance Strategy: Coordinated Waiting Mechanism](#adp-balance-strategy-coordinated-waiting-mechanism)
    - [Performance Analysis: Baseline vs. ADP Balance](#performance-analysis-baseline-vs-adp-balance)
  + [Experiments](#experiments)

    - [Setting](#setting)

      * [Dataset Configuration](#dataset-configuration)
      * [Hardware and Model Configuration](#hardware-and-model-configuration)
    - [Performance Results](#performance-results)

      * [Performance Summary](#performance-summary)
      * [Baseline Performance](#baseline-performance)
      * [ADP Balance with Context Wait Implementation](#adp-balance-with-context-wait-implementation)
      * [ADP Balance with Full Strategy Implementation](#adp-balance-with-full-strategy-implementation)
    - [Pareto Analysis: Throughput-Latency Trade-off Optimization](#pareto-analysis-throughput-latency-trade-off-optimization)
  + [Conclusion](#conclusion)
  + [Acknowledgement](#acknowledgement)

## Motivation and Background[#](#motivation-and-background "Link to this heading")

In DeepSeek MLA + MoE architectures under maximum-throughput scenarios, an Attention Data Parallel (ADP) + MoE Expert Parallel (EP) strategy is commonly employed to eliminate redundant KV cache storage, and utilize disaggregated serving to prevent ADP imbalances. However, certain deployment scenarios still favor In-Flight Batching (IFB) inference, including:

* **System complexity reduction**: Avoiding the operational overhead and maintenance costs associated with disaggregated architectures
* **Specific workload patterns**: Scenarios with short input sequence lengths (ISL) and long output sequence lengths (OSL)
* **Offline inference**: Batch processing environments where Time-To-First-Token (TTFT) and Time-To-Output-Token (TPOT) requirements are more relaxed

However, IFB introduces significant load imbalance challenges within the Attention module that severely impact system performance. The core issue arises when different ranks simultaneously handle heterogeneous workloads within the same iteration. For instance, some ranks may be processing computationally intensive context phases while others execute generation phases, creating substantial disparities in token processing loads. This bottlenecks the overall system throughput, as the iteration time is dominated by the slowest rank.

To address this critical performance limitation, we introduce the **ADP (Attention Data Parallel) Balance Strategy**—a novel scheduling optimization designed to achieve optimal load distribution across DP ranks and maximize system utilization.

## Theoretical Analysis and Modeling[#](#theoretical-analysis-and-modeling "Link to this heading")

**Optimization Objective**: Minimize load imbalance across different GPU ranks to maximize overall system throughput.

### Mathematical Modeling[#](#mathematical-modeling "Link to this heading")

We model and quantify the performance impact of load imbalance in Attention DP. Since workloads across ranks can be heterogeneous, the execution time for the Attention module in any given iteration is bounded by the rank with the highest workload:

\[
time\_i = \max\_{0 \leq m < N} time\_{i,m}
\]

where \(time\_{i,m}\) represents the execution time of rank \(m\) in iteration \(i\), and \(N\) is the data parallel size.

To quantify load balance and theoretical performance bounds, we define two key metrics:

#### 1. Balance Ratio[#](#balance-ratio "Link to this heading")

The balance ratio measures the load distribution across ranks within the Attention module for each iteration:

\[
balance = \frac{tokens\_{avg}}{tokens\_{max}}
\]

where:

* \(tokens\_{avg}\) represents the average number of tokens across all ranks
* \(tokens\_{max}\) represents the maximum number of tokens across all ranks
* \(tokens\_i\) represents the number of tokens processed by rank \(i\)

Note: MoE module load balancing is handled separately by the Expert Parallel Load Balancer (EPLB) module and is not considered during the early scheduling phase.

#### 2. Speed-of-Light Throughput (SOL TPS)[#](#speed-of-light-throughput-sol-tps "Link to this heading")

The Speed-of-Light throughput represents the theoretical upper-bound throughput achievable with perfect load balancing:

\[
time\_{sol} = \sum\_{i=0}^{\infty} time\_i \times balance
\]

\[
tps\_{sol} = \frac{time\_{elapsed}}{time\_{sol}} \times tps\_{actual}
\]

where:

* \(time\_i\): Measured execution time of iteration \(i\)
* \(time\_{elapsed}\): Total empirically measured end-to-end execution time
* \(tps\_{actual}\): Observed throughput in tokens per second
* \(tps\_{sol}\): Theoretical maximum throughput under perfect load balance

This theoretical framework enables us to quantify the performance gap between current and optimal system utilization, providing clear targets for optimization.

### Scheduling Strategies for Load Balancing[#](#scheduling-strategies-for-load-balancing "Link to this heading")

The fundamental challenge in Attention DP is that ranks can process vastly different token loads within the same iteration, causing the overall execution time to be bottlenecked by the most heavily loaded rank.

#### Baseline: Round-Robin Token Distribution[#](#baseline-round-robin-token-distribution "Link to this heading")

The conventional approach employs a global load balancing strategy that sorts incoming requests by `num_tokens` and distributes them across ranks using round-robin scheduling, as illustrated in Figure 1. This method achieves reasonable token distribution from a cumulative perspective and effectively reduces token count disparities when all ranks are simultaneously processing context requests.

![](https://github.com/NVIDIA/TensorRT-LLM/raw/main/docs/source/blogs/media/tech_blog10_baseline_round_robin_strategy.png)

*Figure 1: Baseline round-robin strategy balances context request tokens across ranks through sorting and cyclic distribution*

**Limitations**: While effective globally, this approach fails to guarantee per-iteration load balance. A critical scenario arises when some ranks process context phases, while others handle generation (decode), creating severe load imbalances that dominate overall execution time.

#### ADP Balance Strategy: Coordinated Waiting Mechanism[#](#adp-balance-strategy-coordinated-waiting-mechanism "Link to this heading")

To address the per-iteration load imbalance problem, we propose the **ADP Balance Strategy**, which employs a sophisticated waiting mechanism to synchronize context processing across ranks. The core principle is strategic delay: instead of immediately scheduling context requests to available ranks, the system waits strategically to ensure multiple ranks have similar workloads before proceeding.

**Algorithm Design**: The strategy introduces two complementary control parameters:

**1. Context Synchronization (`timeout_iters`)**

* **Purpose**: Ensures temporal alignment of context processing across ranks
* **Mechanism**: When a rank becomes available for context processing while others remain in generation phases, it waits up to `timeout_iters` iterations until all other ranks have context tasks
* **Benefit**: Prevents the scenario where one rank processes context tasks while others handle generation tasks

**2. Batch Equilibration (`batching_wait_iters`)**

* **Purpose**: Balances the number of accumulated context batches across ranks
* **Mechanism**: After initial synchronization, ranks with fewer accumulated context batches wait up to `batching_wait_iters` additional iterations to accumulate more batches
* **Benefit**: Prevents load imbalances caused by uneven context batch accumulation, where some ranks may have multiple batches while others have only one

### Performance Analysis: Baseline vs. ADP Balance[#](#performance-analysis-baseline-vs-adp-balance "Link to this heading")

To illustrate the effectiveness of our approach, consider a simplified scenario where:

* All ranks have equal-length contexts and M ongoing requests
* N new requests arrive sequentially over N iterations.
* Context processing time: `time(ctx)` >> Generation processing time: `time(gen)`

**Baseline Behavior:**
In the traditional approach, contexts are processed sequentially across ranks, resulting in severe load imbalances:

```
iter_i:     [*C0*, g01, ..., g0M], [g10, g11, ..., g1M], ..., [gN0, gN1, ..., gNM]
iter_i+1:   [g00, g01, ..., g0M], [*C1*, g11, ..., g1M], ..., [gN0, gN1, ..., gNM]
...
iter_i+N-1: [g00, g01, ..., g0M], [g10, g11, ..., g1M], ..., [*CN*, gN1, ..., gNM]
```

*Legend: `*Ci*` = context request i, `gij` = generation request j on rank i*

* **Per-iteration time**: `time(ctx)` (dominated by context processing)
* **Total execution time**: `time(ctx) × N`
* **Balance ratio**: `(ctx_len + (M-1) + M × (N-1)) / (N × ctx_len)` (poor balance)

**ADP Balance Strategy:**
Our method synchronizes context processing by strategic waiting:

```
iter_i:     [g00, g01, ..., g0M], [g10, g11, ..., g1M], ..., [gN0, gN1, ..., gNM]
iter_i+1:   [g00, g01, ..., g0M], [g10, g11, ..., g1M], ..., [gN0, gN1, ..., gNM]
...
iter_i+N-1: [*C0*, g01, ..., g0M], [*C1*, g11, ..., g1M], ..., [*CN*, gN1, ..., gNM]
```

* **Per-iteration time**: `time(gen)` for first N-1 iterations, `time(ctx)` for final iteration
* **Total execution time**: `time(gen) × (N-1) + time(ctx)`
* **Balance ratio**: 1.0 (perfect balance)
* **Time savings**: `(time(ctx) - time(gen)) × (N-1)`

**Trade-offs:**

* ✅ **Throughput improvement** due to optimal load balancing
* ✅ **Maximized GPU utilization** across all ranks
* ⚠️ **Increased TTFT** due to strategic waiting mechanism
* 📋 **Best suited for** throughput-oriented scenarios where TTFT is not critical

## Experiments[#](#experiments "Link to this heading")

### Setting[#](#setting "Link to this heading")

#### Dataset Configuration[#](#dataset-configuration "Link to this heading")

We evaluate our approach using a comprehensive dataset comprising 16,000 inference requests with the following characteristics:

* **Request volume**: 16,000 total requests
* **Average input length**: 803 tokens
* **Average output length**: 3,653 tokens
* **Token distribution**: Figure 2 illustrates the distribution patterns for both input and output sequences

![](https://github.com/NVIDIA/TensorRT-LLM/raw/main/docs/source/blogs/media/tech_blog10_dataset_token_distribution.png)

*Figure 2: Distribution of input and output token lengths*

**Dataset Characteristics**: The dataset exhibits significant diversity in sequence lengths, with output tokens following a pronounced long-tail distribution. This heterogeneity presents substantial challenges for load balancing, as it becomes difficult to co-schedule multiple context requests within the same iteration while minimizing computational bubbles—making it an ideal testbed for evaluating our scheduling strategy.

#### Hardware and Model Configuration[#](#hardware-and-model-configuration "Link to this heading")

**Infrastructure**:

* **Platform**: NVIDIA Blackwell GB200 system
* **GPU Count**: 8 × GB200 GPUs
* **Model**: DeepSeek V3
* **Parallelization Strategy**:

  + Attention module: Data Parallel (DP) size = 8
  + MoE module: Expert Parallel (EP) size = 8

### Performance Results[#](#performance-results "Link to this heading")

We evaluate three distinct configurations to demonstrate the progressive benefits of our ADP Balance strategy:

1. **Baseline**: Round-robin scheduling
2. **ADP Balance (Context Wait)**: Implementing `timeout_iters` parameter only
3. **ADP Balance (Full Strategy)**: Complete implementation with both `timeout_iters` and `batching_wait_iters`

#### Performance Summary[#](#performance-summary "Link to this heading")

| Configuration | Actual TPS | Avg Balance Ratio | SOL TPS | Speedup |
| --- | --- | --- | --- | --- |
| Baseline | 25,664 | 54.11% | 39,552 | 1.00× |
| ADP Balance (Context Wait) | 33,499 | 84.33% | 38,312 | 1.31× |
| ADP Balance (Full Strategy) | 34,140 | 87.70% | 37,912 | 1.33× |

**Key Observations**:

* Context Wait alone delivers a substantial **31% throughput improvement**
* Full strategy achieves **33% total speedup** with near-optimal balance (87.70%)
* Balance ratio improvement: **54% → 87%** represents a dramatic reduction in load imbalance

*Note: The decrease in SOL TPS with waiting mechanisms occurs because the strategic delays in context scheduling increase the total number of iterations required to complete all requests. Since SOL TPS calculation only accounts for load imbalance effects within each iteration, it doesn’t reflect the iteration count increase caused by delayed context entry, leading to an apparent reduction despite overall system efficiency improvements.*

#### Baseline Performance[#](#baseline-performance "Link to this heading")

Figure 3 provides comprehensive insight into baseline system behavior, displaying both average tokens across ranks (top) and the corresponding balance ratio (bottom) by iteration. The balance ratio serves as a key indicator: values approaching 1.0 represent optimal balance, while values near 0.0 indicate severe imbalances.

![](https://github.com/NVIDIA/TensorRT-LLM/raw/main/docs/source/blogs/media/tech_blog10_baseline_performance_overview.png)

*Figure 3: Baseline performance overview showing token distribution and balance ratios across all iterations*

**Critical Insights**:

* **Imbalance window**: Most severe imbalances occur within the first 12,000 iterations, as evidenced by the average token distribution showing that all context processing phases occur within this critical interval
* **Performance gap**: SOL TPS of 39,552 vs. actual TPS of 25,664 reveals a **35% efficiency loss**
* **System behavior**: After iteration 12,000, all requests transition to generation phase, naturally reducing imbalances

Figure 4 zooms into the critical imbalance period [100-12,000], revealing the dramatic instability in load distribution:

![](https://github.com/NVIDIA/TensorRT-LLM/raw/main/docs/source/blogs/media/tech_blog10_baseline_performance_detail.png)

*Figure 4: Detailed baseline analysis for iterations 100-12,000 showing severe balance fluctuations*

**Performance Bottlenecks**:

* Balance ratio frequently drops to **0.4 or lower**, indicating 60%+ load imbalance
* Theoretical improvement potential of **70.23%** within the critical window
* Extreme volatility in load distribution creates unpredictable performance characteristics

#### ADP Balance with Context Wait Implementation[#](#adp-balance-with-context-wait-implementation "Link to this heading")

The Context Wait mechanism (`timeout_iters=50`) demonstrates the effectiveness of our first optimization component, achieving substantial performance improvements through context synchronization.

**Performance Achievements**:

* **Throughput**: 33,499 TPS (1.31× speedup)
* **Balance improvement**: 84.33% average (vs. 54.11% baseline)
* **Efficiency**: Actual TPS significantly closer to theoretical SOL TPS (38,312)

![](https://github.com/NVIDIA/TensorRT-LLM/raw/main/docs/source/blogs/media/tech_blog10_context_wait_performance.png)

*Figure 5: Context Wait performance showing improved balance stability for iterations 100-12,000*

**Remaining Challenges**:
Despite significant improvements, residual imbalances persist due to:

1. **Timeout scenarios**: Some ranks exceed the waiting threshold when context requests don’t arrive uniformly
2. **Batch accumulation disparity**: Longer-waiting ranks accumulate multiple context batches while recently-freed ranks process single batches
3. **Partial synchronization**: While initial synchronization succeeds, subsequent load variations still occur

This analysis motivated the development of our second optimization component: batch equilibration.

#### ADP Balance with Full Strategy Implementation[#](#adp-balance-with-full-strategy-implementation "Link to this heading")

The complete ADP Balance strategy combines both context synchronization and batch equilibration mechanisms, delivering optimal load balancing performance.

**Configuration**: `timeout_iters=50` + `batching_wait_iters=10`

**Performance Optimization Results**:

* **Peak throughput**: 34,140 TPS (1.33× speedup)
* **Optimal balance**: 87.70% average balance ratio
* **Near-theoretical efficiency**: Actual TPS (34,140) approaches SOL TPS (37,912)
* **System stability**: Dramatically reduced load variance across iterations

**Production Configuration**:
Users can enable the full ADP Balance strategy by adding the following configuration:

```
attention_dp_config:
    enable_balance: true
    batching_wait_iters: 10
    timeout_iters: 50
```

The effectiveness of our complete ADP Balance implementation is clearly demonstrated in Figure 6. The visualization reveals how the combination of context synchronization and batch equilibration mechanisms achieves near-optimal load balancing throughout the critical execution window.

![](https://github.com/NVIDIA/TensorRT-LLM/raw/main/docs/source/blogs/media/tech_blog10_full_strategy_performance.png)

*Figure 6: Full ADP Balance strategy demonstrating superior balance stability for iterations 100-12,000*

**Key Improvements Over Context Wait**:

* **Enhanced stability**: Balance ratio maintains consistently higher values with reduced volatility
* **Residual imbalance mitigation**: Batch equilibration addresses the remaining load disparities
* **System predictability**: More uniform performance characteristics across iterations

**Implementation Trade-offs**:

* ✅ **Maximum throughput improvement**: 33% gain over baseline
* ✅ **Near-optimal load balancing**: 87.70% average balance ratio
* ⚠️ **Iteration overhead**: Waiting mechanisms increase total iteration count
* ⚠️ **TTFT impact**: Strategic delays affect time-to-first-token metrics

### Pareto Analysis: Throughput-Latency Trade-off Optimization[#](#pareto-analysis-throughput-latency-trade-off-optimization "Link to this heading")

Understanding the performance trade-offs inherent in our ADP Balance strategy is crucial for production deployment decisions. Figure 7 presents a comprehensive Pareto frontier analysis that maps the relationship between system throughput (TPS per GPU) and Time-To-First-Token (TTFT) across varying workload intensities and parameter configurations.

**Experimental Design**: The analysis evaluates multiple configurations of `timeout_iters` (TO) and `batching_wait_iters` (BW) parameters under different system load conditions, revealing how parameter tuning affects the fundamental throughput-latency trade-off.

![](https://github.com/NVIDIA/TensorRT-LLM/raw/main/docs/source/blogs/media/tech_blog10_tps_ttft_pareto_curve.png)

*Figure 7: Pareto frontier analysis showing throughput-latency trade-offs across different ADP Balance configurations*

**Key Findings**:

1. **Universal Throughput Gains**: ADP Balance consistently delivers superior TPS/GPU performance across the entire operational spectrum, from latency-sensitive to throughput-maximized deployments
2. **Scalability Benefits**: Performance improvements become increasingly pronounced under higher system loads, where load imbalance penalties are most severe
3. **TTFT Trade-off**: Throughput gains necessitate increased first-token latency due to the strategic waiting mechanisms, with higher parameter values yielding greater throughput at the cost of longer response initiation
4. **Configuration Guidance**:

   * **Low-load scenarios**: `batching_wait_iters` provides minimal benefit while adding latency overhead
   * **High-throughput scenarios**: Both parameters contribute significantly to performance optimization
   * **Balanced deployments**: Moderate parameter values offer optimal throughput-latency balance

**Production Implications**: This analysis empowers system operators to make data-driven configuration decisions based on specific deployment requirements—whether optimizing for minimum response latency or maximum system throughput.

## Conclusion[#](#conclusion "Link to this heading")

Load imbalance in Attention Data Parallel processing represents a fundamental bottleneck in large language model inference systems, particularly under In-Flight Batching scenarios where heterogeneous workloads create severe performance penalties. This work introduces the **ADP Balance Strategy**—a sophisticated scheduling optimization that addresses this critical challenge through coordinated waiting mechanisms.

**Technical Contributions**:
Our approach employs two complementary optimization components: context synchronization (`timeout_iters`) and batch equilibration (`batching_wait_iters`). These mechanisms work in concert to achieve temporal alignment of computationally intensive context processing across data parallel ranks, effectively eliminating the performance bottlenecks caused by rank-level load imbalances.

**Experimental Validation**:
Comprehensive evaluation on the DeepSeek V3 architecture demonstrates compelling performance improvements:

* **33% throughput increase**: From 25,664 to 34,140 TPS
* **87% load balance achievement**: Dramatic improvement from 54% baseline
* **Near-theoretical efficiency**: Actual performance approaching speed-of-light throughput bounds

**Production Readiness**:
The Pareto frontier analysis provides critical insights for real-world deployment, revealing that while the strategy introduces TTFT trade-offs, it consistently delivers superior throughput across diverse operational scenarios. The configurable parameter framework enables operators to optimize for their specific performance requirements, whether prioritizing response latency or system throughput.

## Acknowledgement[#](#acknowledgement "Link to this heading")

The ADP Balance strategy was a great team effort, covering system performance analysis and optimization. While we cannot thank every contributor individually, we are proud to acknowledge the dedicated team of engineers whose collective expertise has propelled TensorRT LLM to new heights of performance. Through this collaborative effort, we have gained valuable insights into improving GPU utilization for large language model inference. We hope the techniques and experiences shared in this blog post will empower the developer community to better leverage the performance of NVIDIA GPUs in their mission-critical LLM inference applications.

[previous

LLM API Change Guide](../../developer-guide/api-change.md "previous page")
[next

Running GPT-OSS-120B with Eagle3 Speculative Decoding on GB200/B200 (TensorRT LLM)](blog11_GPT_OSS_Eagle3.md "next page")

On this page

* [Table of Contents](#table-of-contents)
* [Motivation and Background](#motivation-and-background)
* [Theoretical Analysis and Modeling](#theoretical-analysis-and-modeling)
  + [Mathematical Modeling](#mathematical-modeling)
    - [1. Balance Ratio](#balance-ratio)
    - [2. Speed-of-Light Throughput (SOL TPS)](#speed-of-light-throughput-sol-tps)
  + [Scheduling Strategies for Load Balancing](#scheduling-strategies-for-load-balancing)
    - [Baseline: Round-Robin Token Distribution](#baseline-round-robin-token-distribution)
    - [ADP Balance Strategy: Coordinated Waiting Mechanism](#adp-balance-strategy-coordinated-waiting-mechanism)
  + [Performance Analysis: Baseline vs. ADP Balance](#performance-analysis-baseline-vs-adp-balance)
* [Experiments](#experiments)
  + [Setting](#setting)
    - [Dataset Configuration](#dataset-configuration)
    - [Hardware and Model Configuration](#hardware-and-model-configuration)
  + [Performance Results](#performance-results)
    - [Performance Summary](#performance-summary)
    - [Baseline Performance](#baseline-performance)
    - [ADP Balance with Context Wait Implementation](#adp-balance-with-context-wait-implementation)
    - [ADP Balance with Full Strategy Implementation](#adp-balance-with-full-strategy-implementation)
  + [Pareto Analysis: Throughput-Latency Trade-off Optimization](#pareto-analysis-throughput-latency-trade-off-optimization)
* [Conclusion](#conclusion)
* [Acknowledgement](#acknowledgement)