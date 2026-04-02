# DeepSeek-VL2 — lmdeploy

Source: https://lmdeploy.readthedocs.io/en/latest/multi_modal/deepseek_vl2.html

DeepSeek-VL2

DeepSeek-VL2#

Introduction#

DeepSeek-VL2, an advanced series of large Mixture-of-Experts (MoE) Vision-Language Models that significantly improves upon its predecessor, DeepSeek-VL.
DeepSeek-VL2 demonstrates superior capabilities across various tasks, including but not limited to visual question answering, optical character recognition, document/table/chart understanding, and visual grounding.

LMDeploy supports deepseek-vl2-tiny, deepseek-vl2-small and deepseek-vl2 in PyTorch engine.

Quick Start#

Install LMDeploy by following the installation guide.

Prepare#

When deploying the DeepSeek-VL2 model using LMDeploy, you must install the official GitHub repository and related 3-rd party libs. This is because LMDeploy reuses the image processing functions provided in the official repository.

```text
pip install git+https://github.com/deepseek-ai/DeepSeek-VL2.git --no-deps
pip install attrdict timm 'transformers<4.48.0'
```

Worth noticing that it may fail with `transformers>=4.48.0`, as known in this issue.

Offline inference pipeline#

The following sample code shows the basic usage of VLM pipeline. For more examples, please refer to VLM Offline Inference Pipeline.

To construct valid DeepSeek-VL2 prompts with image inputs, users should insert `<IMAGE_TOKEN>` manually.

```text
from lmdeploy import pipeline
from lmdeploy.vl import load_image


if __name__ == "__main__":
    pipe = pipeline('deepseek-ai/deepseek-vl2-tiny')

    image = load_image('https://raw.githubusercontent.com/open-mmlab/mmdeploy/main/tests/data/tiger.jpeg')
    response = pipe(('<IMAGE_TOKEN>describe this image', image))
    print(response)
```
