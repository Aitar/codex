* [Speculative Decoding](../../../../llm_features/speculative_decoding_by_backend_type.md)
* Speculative...

# Speculative Decoding with vLLM[#](#speculative-decoding-with-vllm "Link to this heading")

* [About Speculative Decoding](#about-speculative-decoding)
* [EAGLE](#eagle)
* [Draft Model-Based Speculative Decoding](#draft-model-based-speculative-decoding)

## About Speculative Decoding[#](#about-speculative-decoding "Link to this heading")

This tutorial shows how to build and serve speculative decoding models in Triton Inference Server with [vLLM Backend](https://github.com/triton-inference-server/vllm_backend) on a single node with one GPU. Please go to [Speculative Decoding](../README.md) main page to learn more about other supported backends.

According to [Spec-Bench](https://sites.google.com/view/spec-bench), EAGLE is currently the top-performing approach for speeding up LLM inference across different tasks. In this tutorial, weâll focus on [EAGLE](#eagle) and demonstrate how to make it work with Triton Inference Server. Weâll also cover [Draft Model-Based Speculative Decoding](#draft-model-based-speculative-decoding) for those interested in exploring alternative methods. If you are interested in how vLLM supports speculative decoding, more details [here](https://blog.vllm.ai/2024/10/17/spec-decode.md). By finishing this tutorial, you will be able to try other speculative decoding techniques provided by vLLM [here](https://docs.vllm.ai/en/latest/features/spec_decode.md#speculative-decoding) with Triton Inference Server easily on your own.

## EAGLE[#](#eagle "Link to this heading")

EAGLE ([paper](https://arxiv.org/pdf/2401.15077) | [github](https://github.com/SafeAILab/EAGLE) | [blog](https://sites.google.com/view/eagle-llm)) is a speculative decoding technique that accelerates Large Language Model (LLM) inference by predicting future tokens based on contextual features extracted from the LLMâs second-top layer. It employs a lightweight Auto-regression Head to predict the next feature vector, which is then used to generate tokens through the LLMâs frozen classification head, achieving significant speedups (2x-3x faster than vanilla decoding) while maintaining output quality and distribution consistency.

### Acquiring EAGLE Model and its Base Model[#](#acquiring-eagle-model-and-its-base-model "Link to this heading")

In this example, we will be using the [EAGLE-LLaMA3-Instruct-8B](https://huggingface.co/yuhuili/EAGLE-LLaMA3-Instruct-8B) model.
More types of EAGLE models can be found [here](https://huggingface.co/yuhuili). The base model [Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) is also needed for EAGLE to work.

To download both models, run the following command:

```
# Install git-lfs if needed
apt-get update && apt-get install git-lfs -y --no-install-recommends
git lfs install
git clone https://huggingface.co/yuhuili/EAGLE-LLaMA3-Instruct-8B
git clone https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct
```

*NOTE: you need to request access in Hugging Face and login to download and use Llama3 models.*

### Convert EAGLE Model[#](#convert-eagle-model "Link to this heading")

According to vLLM official [doc](https://docs.vllm.ai/en/latest/features/spec_decode.md#speculating-using-eagle-based-draft-models):

> â¦ EAGLE models should be able to be loaded and used directly by vLLM after [PR 12304](https://github.com/vllm-project/vllm/pull/12304). If you are using vllm version before [PR 12304](https://github.com/vllm-project/vllm/pull/12304), please use the [script](https://gist.github.com/abhigoyal1997/1e7a4109ccb7704fbc67f625e86b2d6d) to convert the speculative model, and specify speculative\_model=âpath/to/modified/eagle/modelâ â¦

For Triton, if you are using Triton Server container version <= 25.02, you need to convert the EAGLE model by running above [script](https://gist.github.com/abhigoyal1997/1e7a4109ccb7704fbc67f625e86b2d6d), inside the folder than contains both EAGLE and base models. Triton Server container version >= 25.03 would use vLLM versions (>= 0.7.3) that contains PR 12304.

### Create Model Repository[#](#create-model-repository "Link to this heading")

A model repository is Tritonâs way of reading your models and any associated metadata with each model (configurations, version files, etc.). See [here](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Conceptual_Guide/Part_1-model_deployment/README.md#setting-up-the-model-repository) for model details.

We have prepared a template of a model repository for EAGLE model and base model in [model\_repository](https://github.com/triton-inference-server/tutorials/blob/main/Feature_Guide/Speculative_Decoding/vLLM/model_repository). Please make a copy and modify the model.json to suit your needs. For example, we are setting `num_speculative_tokens` to 5 for eagle\_model, according to the vLLM [example](https://docs.vllm.ai/en/latest/features/spec_decode.md#speculating-with-a-draft-model). You can change it to other values and it might affect the performance.

### Serving with Triton[#](#serving-with-triton "Link to this heading")

Letâs serve the model by launching Triton docker container with vLLM backend.
Note that weâre mounting the downloaded (and maybe converted) EAGLE and base models to `/hf-models` and the model repository acquired in the previous section to `/model_repository` in the docker container. Please, make sure to replace <xx.yy> with the version of Triton that you want
to use. The latest Triton Server container is recommended and could be found [here](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/tritonserver/tags).

```
docker run --gpus all -it --net=host --rm -p 8001:8001 --shm-size=1G \
    --ulimit memlock=-1 --ulimit stack=67108864 \
    -v </path/to/model_repository>:/model_repository \
    -v </path/to/eagle/and/base/model>:/hf-models \
    nvcr.io/nvidia/tritonserver:<xx.yy>-vllm-python-py3 \
    tritonserver --model-repository /model_repository \
    --model-control-mode explicit --load-model eagle_model
```

### Send Inference Requests[#](#send-inference-requests "Link to this heading")

Letâs send an inference request to the [generate endpoint](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/protocol/extension_generate.md).

```
curl -X POST localhost:8000/v2/models/eagle_model/generate -d '{"text_input": "What is Triton Inference Server?", "parameters": {"stream": false, "temperature": 0}}' | jq
```

> You should expect the following response:
>
> ```
> {
>  "model_name": "eagle_model",
>  "model_version": "1",
>  "text_output": "What is Triton Inference Server?Â¶\n\nTriton Inference Server is an open-source, high-performance,"
> }
> ```

### Evaluating Performance with Gen-AI Perf[#](#evaluating-performance-with-gen-ai-perf "Link to this heading")

Gen-AI Perf is a command line tool for measuring the throughput and latency of generative AI models as served through an inference server.
You can read more about Gen-AI Perf [here](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.md). We will use Gen-AI Perf to evaluate the performance gain of EAGLE model over the base model.

1. Prepare Dataset

We will be using the HumanEval dataset for our evaluation, which is used in the original EAGLE paper. The HumanEval dataset has been converted to the format required by EAGLE and is available [here](https://github.com/SafeAILab/EAGLE/blob/main/eagle/data/humaneval/question.jsonl). To make it compatible for Gen-AI Perf, we need to do another conversion. You may use other datasets besides HumanEval as well, as long as it could be converted to the
format required by Gen-AI Perf. Note that MT-bench could not be used since Gen-AI Perf does not support multiturn dataset as input yet. Follow the steps below to download and convert the dataset.

```
wget https://raw.githubusercontent.com/SafeAILab/EAGLE/main/eagle/data/humaneval/question.jsonl

# dataset-converter.py file can be found in the parent folder as this README.
python3 dataset-converter.py --input_file question.jsonl --output_file converted_humaneval.jsonl
```

2. Install GenAI-Perf (Ubuntu 24.04, Python 3.10+)

```
pip install genai-perf
```

*NOTE: you must already have CUDA 12 installed.*

3. Run Gen-AI Perf

Run the following command in the SDK container:

```
genai-perf \
  profile \
  -m ensemble \
  --service-kind triton \
  --backend tensorrtllm \
  --input-file /path/to/converted/dataset/converted_humaneval.jsonl \
  --tokenizer /path/to/hf-models/Meta-Llama-3-8B-Instruct/ \
  --profile-export-file my_profile_export.json \
  --url localhost:8001 \
  --concurrency 1
```

*NOTE: When benchmarking the speedup of speculative decoding versus the base model, use `--concurrency 1`. This setting is crucial because speculative decoding is designed to trade extra computation for reduced token generation latency. By limiting concurrency, we avoid saturating hardware resources with multiple requests, allowing for a more accurate assessment of the techniqueâs latency benefits. This approach ensures that the benchmark reflects the true performance gains of speculative decoding in real-world, low-concurrency scenarios.*

A sample output that looks like this:

```
                                    NVIDIA GenAI-Perf | LLM Metrics
âââââââââââââââââââââââââââââââââââââ³âââââââââââ³âââââââââââ³âââââââââââ³âââââââââââ³âââââââââââ³âââââââââââ
â                         Statistic â      avg â      min â      max â      p99 â      p90 â      p75 â
â¡ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ©
â              Request Latency (ms) â 7,510.69 â 6,534.94 â 8,433.33 â 8,409.31 â 8,193.07 â 7,832.68 â
â   Output Sequence Length (tokens) â   325.00 â   324.00 â   326.00 â   325.97 â   325.70 â   325.25 â
â    Input Sequence Length (tokens) â   112.50 â    79.00 â   137.00 â   136.55 â   132.50 â   125.75 â
â Output Token Throughput (per sec) â    43.27 â      N/A â      N/A â      N/A â      N/A â      N/A â
â      Request Throughput (per sec) â     0.13 â      N/A â      N/A â      N/A â      N/A â      N/A â
â             Request Count (count) â     4.00 â      N/A â      N/A â      N/A â      N/A â      N/A â
âââââââââââââââââââââââââââââââââââââ´âââââââââââ´âââââââââââ´âââââââââââ´âââââââââââ´âââââââââââ´âââââââââââ
```

*NOTE: above sample output is done on a single node with one GPU - RTX 5880 (48GB GPU memory). The number below is only for reference. The actual number may vary due to the different hardware and environment.*

4. Run Gen-AI Perf on Base Model

To compare performance between EAGLE and base model (i.e. vanilla LLM w/o speculative decoding), we need to run Gen-AI Perf Tool on the base model as well. To serve base model, we only need to change the [Serving with Triton](#Serving-with-Triton) by switching the `--load-model` argument from `eagle_model` to `base_model`:

```
docker run --gpus all -it --net=host --rm -p 8001:8001 --shm-size=1G \
    --ulimit memlock=-1 --ulimit stack=67108864 \
    -v </path/to/model_repository>:/model_repository \
    -v </path/to/eagle/and/base/model>:/hf-models \
    nvcr.io/nvidia/tritonserver:<xx.yy>-vllm-python-py3 \
    tritonserver --model-repository /model_repository \
    --model-control-mode explicit --load-model base_model
```

Please use EAGLE with care, since according to vLLM [doc](https://docs.vllm.ai/en/latest/features/spec_decode.md#speculating-using-eagle-based-draft-models):

> When using EAGLE-based speculators with vLLM, the observed speedup is lower than what is reported in the reference implementation [here](https://github.com/SafeAILab/EAGLE). This issue is under investigation and tracked here: [vllm-project/vllm#9565](https://github.com/vllm-project/vllm/issues/9565).

## Draft Model-Based Speculative Decoding[#](#draft-model-based-speculative-decoding "Link to this heading")

Draft Model-Based Speculative Decoding ([paper](https://arxiv.org/pdf/2302.01318)) is another (and earlier) approach to accelerate LLM inference, distinct from EAGLE. Here are the key differences:

* Draft Generation: it uses a smaller, faster LLM as a draft model to predict multiple tokens ahead. This contrasts with EAGLEâs feature-level extrapolation.
* Verification Process: it employs a chain-like structure for draft generation and verification, unlike EAGLE which uses tree-based attention mechanisms.
* Efficiency: While effective, it is generally slower than EAGLE.
* Implementation: it requires a separate draft model, which can be challenging to implement effectively for smaller target models. EAGLE, in contrast, modifies the existing model architecture.
* Accuracy: its draft accuracy can vary depending on the draft model used, while EAGLE achieves a higher draft accuracy (about 0.8).

To run Draft Model-Based Speculative Decoding with Triton Inference Server, it is very similar to the steps above for EAGLE. The only difference is that you need to use a different model repository. A template of model repository for Draft Model-Based Speculative Decoding is available in [model\_repository/opt\_model](https://github.com/triton-inference-server/tutorials/blob/main/Feature_Guide/Speculative_Decoding/vLLM/model_repository/opt_model), following the example from vLLM [doc](https://docs.vllm.ai/en/latest/features/spec_decode.md#speculating-with-a-draft-model). Please make a copy and modify the model.json to suit your needs. Then, you can start Triton server with the following command:

```
docker run --gpus all -it --net=host --rm -p 8001:8001 --shm-size=1G \
    --ulimit memlock=-1 --ulimit stack=67108864 \
    -v </path/to/model_repository>:/model_repository \
    nvcr.io/nvidia/tritonserver:25.02-vllm-python-py3 \
    tritonserver --model-repository /model_repository \
    --model-control-mode explicit --load-model opt_model
```

