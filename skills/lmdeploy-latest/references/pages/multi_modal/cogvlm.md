# CogVLM — lmdeploy

Source: https://lmdeploy.readthedocs.io/en/latest/multi_modal/cogvlm.html

CogVLM

CogVLM#

Introduction#

CogVLM is a powerful open-source visual language model (VLM). LMDeploy supports CogVLM-17B models like THUDM/cogvlm-chat-hf and CogVLM2-19B models like THUDM/cogvlm2-llama3-chat-19B in PyTorch engine.

Quick Start#

Install LMDeploy by following the installation guide

Prepare#

When deploying the CogVLM model using LMDeploy, it is necessary to download the model first, as the CogVLM model repository does not include the tokenizer model.
However, this step is not required for CogVLM2.

Taking one CogVLM model `cogvlm-chat-hf` as an example, you can prepare it as follows:

```text
huggingface-cli download THUDM/cogvlm-chat-hf --local-dir ./cogvlm-chat-hf --local-dir-use-symlinks False
huggingface-cli download lmsys/vicuna-7b-v1.5 special_tokens_map.json tokenizer.model tokenizer_config.json --local-dir ./cogvlm-chat-hf --local-dir-use-symlinks False
```

Offline inference pipeline#

The following sample code shows the basic usage of VLM pipeline. For more examples, please refer to VLM Offline Inference Pipeline

```text
from lmdeploy import pipeline
from lmdeploy.vl import load_image


if __name__ == "__main__":
    pipe = pipeline('cogvlm-chat-hf')

    image = load_image('https://raw.githubusercontent.com/open-mmlab/mmdeploy/main/tests/data/tiger.jpeg')
    response = pipe(('describe this image', image))
    print(response)
```
