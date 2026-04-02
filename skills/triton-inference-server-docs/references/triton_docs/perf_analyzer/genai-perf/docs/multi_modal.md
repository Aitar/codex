* [GenAI Performance Analyzer](../../../perf_benchmark/genai_perf.md)
* Profile...

# Profile Multi-Modal Language Models with GenAI-Perf[#](#profile-multi-modal-language-models-with-genai-perf "Link to this heading")

GenAI-Perf allows you to profile Multi-Modal Language Models (MMLM) running on
[OpenAI Chat Completions API](https://platform.openai.com/docs/guides/chat-completions)-compatible server
by sending multi-modal contents to the server
(for instance, see OpenAI [vision](https://platform.openai.com/docs/guides/vision) and
[audio](https://platform.openai.com/docs/guides/audio?example=audio-in) inputs).

## Quickstart 1. Run GenAI-Perf on Vision Language Model (VLM)[#](#quickstart-1-run-genai-perf-on-vision-language-model-vlm "Link to this heading")

Start OpenAI API compatible server with a VLM model using following command:

```
docker run --runtime nvidia --gpus all \
    -p 8000:8000 --ipc=host \
    vllm/vllm-openai:latest \
    --model llava-hf/llava-v1.6-mistral-7b-hf --dtype float16
```

Use GenAI-Perf to generate/send text and image request data to the server

```
genai-perf profile \
    -m llava-hf/llava-v1.6-mistral-7b-hf \
    --endpoint-type multimodal \
    --image-width-mean 50 \
    --image-height-mean 50 \
    --synthetic-input-tokens-mean 10 \
    --output-tokens-mean 10 \
    --streaming
```

Console output will have the following result table

```
                           NVIDIA GenAI-Perf | Multi-Modal Metrics
âââââââââââââââââââââââââââââââââââââ³âââââââââ³âââââââââ³âââââââââââ³âââââââââ³âââââââââ³âââââââââ
â                         Statistic â    avg â    min â      max â    p99 â    p90 â    p75 â
â¡ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ©
â          Time To First Token (ms) â 205.38 â 172.31 â 1,020.58 â 246.02 â 207.33 â 204.96 â
â         Time To Second Token (ms) â  18.58 â  18.03 â    19.22 â  19.13 â  18.72 â  18.65 â
â              Request Latency (ms) â 369.06 â 336.56 â 1,183.65 â 408.84 â 370.97 â 368.50 â
â          Inter Token Latency (ms) â  16.41 â  16.27 â    18.32 â  18.16 â  16.47 â  16.41 â
â   Output Sequence Length (tokens) â  10.98 â  10.00 â    11.00 â  11.00 â  11.00 â  11.00 â
â    Input Sequence Length (tokens) â  10.06 â  10.00 â    11.00 â  11.00 â  10.00 â  10.00 â
â Output Token Throughput (per sec) â  29.74 â    N/A â      N/A â    N/A â    N/A â    N/A â
â      Request Throughput (per sec) â   2.71 â    N/A â      N/A â    N/A â    N/A â    N/A â
â             Request Count (count) â  97.00 â    N/A â      N/A â    N/A â    N/A â    N/A â
âââââââââââââââââââââââââââââââââââââ´âââââââââ´âââââââââ´âââââââââââ´âââââââââ´âââââââââ´âââââââââ
```

## Quickstart 2. Run GenAI-Perf on Multi-Modal Language Model (MMLM)[#](#quickstart-2-run-genai-perf-on-multi-modal-language-model-mmlm "Link to this heading")

In this example, we will measure performance of the recent Multi-Modal Language Model (MMLM)
`Phi-4-multimodal-instruct` from Microsoft hosted on NVIDIA API which is OpenAI API compatible.
First, visit https://build.nvidia.com/microsoft/phi-4-multimodal-instruct and create API key.

Run GenAI-Perf to generate/send all three modalities to the server

```
export NVIDIA_API_KEY=your_api_key

genai-perf profile \
    -m microsoft/phi-4-multimodal-instruct \
    -u https://integrate.api.nvidia.com \
    --endpoint-type multimodal \
    --synthetic-input-tokens-mean 10 \
    --output-tokens-mean 10 \
    --image-width-mean 50 \
    --image-height-mean 50 \
    --audio-length-mean 3 \
    --audio-depths 16 32 \
    --audio-sample-rates 16 44.1 48 \
    --audio-num-channels 2 \
    --audio-format wav \
    --streaming \
    --header "Authorization: Bearer '${NVIDIA_API_KEY}'"
```

Console output will have the following result table

```
                          NVIDIA GenAI-Perf | Multi-Modal Metrics
âââââââââââââââââââââââââââââââââââââ³âââââââââ³âââââââââ³âââââââââ³âââââââââ³âââââââââ³âââââââââ
â                         Statistic â    avg â    min â    max â    p99 â    p90 â    p75 â
â¡ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ©
â          Time To First Token (ms) â 284.94 â 228.38 â 562.57 â 371.15 â 325.76 â 295.26 â
â         Time To Second Token (ms) â  10.02 â   8.79 â  10.94 â  10.89 â  10.59 â  10.32 â
â              Request Latency (ms) â 346.80 â 251.96 â 662.96 â 463.03 â 404.79 â 382.18 â
â          Inter Token Latency (ms) â   9.56 â   0.00 â  15.76 â  14.22 â  11.05 â  10.81 â
â   Output Sequence Length (tokens) â   7.43 â   1.00 â  14.00 â  14.00 â  12.00 â  10.00 â
â    Input Sequence Length (tokens) â  10.11 â  10.00 â  11.00 â  11.00 â  11.00 â  10.00 â
â Output Token Throughput (per sec) â  20.96 â    N/A â    N/A â    N/A â    N/A â    N/A â
â      Request Throughput (per sec) â   2.82 â    N/A â    N/A â    N/A â    N/A â    N/A â
â             Request Count (count) â 101.00 â    N/A â    N/A â    N/A â    N/A â    N/A â
âââââââââââââââââââââââââââââââââââââ´âââââââââ´âââââââââ´âââââââââ´âââââââââ´âââââââââ´âââââââââ
```

## Generating Multi-Modal Requests with GenAI-Perf[#](#generating-multi-modal-requests-with-genai-perf "Link to this heading")

Currently, you can send multi-modal contents with GenAI-Perf using the following two approaches:

1. The synthetic data generation approach, where GenAI-Perf generates the multi-modal data for you.
2. The Bring Your Own Data (BYOD) approach, where you provide GenAI-Perf with the data to send.

### Approach 1: Synthetic Multi-Modal Data Generation[#](#approach-1-synthetic-multi-modal-data-generation "Link to this heading")

GenAI-Perf can generate synthetic data of three modalities (text, image, and audio)
using the modality-specific parameters provide by the user through CLI.
Checkout [CLI Input Options](../README.md#input-options) for a complete list of parameters
that you can tweak for different modalities.

```
genai-perf profile \
    -m <multimodal_model> \
    --endpoint-type multimodal \
    # audio parameters
    --audio-length-mean 10 \
    --audio-length-stddev 2 \
    --audio-depths 16 32 \
    --audio-sample-rates 16 44.1 48 \
    --audio-num-channels 1 \
    --audio-format wav \
    # image parameters
    --image-width-mean 512 \
    --image-width-stddev 30 \
    --image-height-mean 512 \
    --image-height-stddev 30 \
    --image-format png \
    # text parameters
    --synthetic-input-tokens-mean 100 \
    --synthetic-input-tokens-stddev 0 \
    --streaming
```

> [!Note]
> Under the hood, GenAI-Perf generates synthetic images using a few source images
> under the `inputs/source_images` directory.
> If you would like to add/remove/edit the source images,
> you can do so by directly editing the source images under the directory.
> GenAI-Perf will pickup the images under the directory automatically when
> generating the synthetic images.

### Approach 2: Bring Your Own Data (BYOD)[#](#approach-2-bring-your-own-data-byod "Link to this heading")

> [!Note]
> This approach only supports text and image inputs at the moment.

Instead of letting GenAI-Perf create the synthetic data,
you can also provide GenAI-Perf with your own data using
[`--input-file`](../README.md#input-file-path) CLI option.
The input file must be in JSONL format, where each line can define both `text` and `image` data.
The `image` field can be either a path to a local image file or a URL.
GenAI-Perf converts local image filepaths to base64-encoded strings and leaves URL paths as is,
consistent with the [OpenAI Vision Guide](https://platform.openai.com/docs/guides/images-vision?api-mode=chat&amp;format=url#giving-a-model-images-as-input).

A sample input file `input.jsonl` would look like

```
// texts and local image files
{"text": "What is in this image?", "image": "path/to/image1.png"}
{"text": "What is the color of the dog?", "image": "path/to/image2.jpeg"}

// Or, text and URL path
{"text": "What is in this image?", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"}
```

After you create the file, you can run GenAI-Perf using the following command:

```
genai-perf profile \
    -m <multimodal_model> \
    --endpoint-type multimodal \
    --input-file input.jsonl \
    --streaming
```

