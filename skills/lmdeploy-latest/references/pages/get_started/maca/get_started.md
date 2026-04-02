# MetaX-tech — lmdeploy

Source: https://lmdeploy.readthedocs.io/en/latest/get_started/maca/get_started.html

MetaX-tech

MetaX-tech#

The usage of lmdeploy on a MetaX-tech device is almost the same as its usage on CUDA with PytorchEngine in lmdeploy.
Please read the original Get Started guide before reading this tutorial.

Here is the supported model list.

[!IMPORTANT]
We have uploaded a docker image to aliyun.
Please try to pull the image by following command:

`dockerpullcrpi-4crprmm5baj1v8iv.cn-hangzhou.personal.cr.aliyuncs.com/lmdeploy_dlinfer/maca:latest`

Offline batch inference#

LLM inference#

Set `device_type="maca"` in the `PytorchEngineConfig`:

```text
from lmdeploy import pipeline
from lmdeploy import PytorchEngineConfig
pipe = pipeline("internlm/internlm2_5-7b-chat",
        backend_config=PytorchEngineConfig(tp=1, device_type="maca"))
question = ["Shanghai is", "Please introduce China", "How are you?"]
response = pipe(question)
print(response)
```

VLM inference#

Set `device_type="maca"` in the `PytorchEngineConfig`:

```text
from lmdeploy import pipeline, PytorchEngineConfig
from lmdeploy.vl import load_image
pipe = pipeline('OpenGVLab/InternVL2-2B',
        backend_config=PytorchEngineConfig(tp=1, device_type='maca'))
image = load_image('https://raw.githubusercontent.com/open-mmlab/mmdeploy/main/tests/data/tiger.jpeg')
response = pipe(('describe this image', image))
print(response)
```

Online serving#

Serve a LLM model#

Add `--devicemaca` in the serve command.

```text
lmdeploy serve api_server --backend pytorch --device maca internlm/internlm2_5-7b-chat
```

Run the following commands to launch docker container for lmdeploy LLM serving:

```text
docker run -it --net=host crpi-4crprmm5baj1v8iv.cn-hangzhou.personal.cr.aliyuncs.com/lmdeploy_dlinfer/maca:latest \
    bash -i -c "lmdeploy serve api_server --backend pytorch --device maca internlm/internlm2_5-7b-chat"
```

Serve a VLM model#

Add `--devicemaca` in the serve command

```text
lmdeploy serve api_server --backend pytorch --device maca OpenGVLab/InternVL2-2B
```

Run the following commands to launch docker container for lmdeploy VLM serving:

```text
docker run -it --net=host crpi-4crprmm5baj1v8iv.cn-hangzhou.personal.cr.aliyuncs.com/lmdeploy_dlinfer/maca:latest \
    bash -i -c "lmdeploy serve api_server --backend pytorch --device maca OpenGVLab/InternVL2-2B"
```

Inference with Command line Interface#

Add `--devicemaca` in the serve command.

```text
lmdeploy chat internlm/internlm2_5-7b-chat --backend pytorch --device maca
```

Run the following commands to launch lmdeploy chatting after starting container:

```text
docker run -it crpi-4crprmm5baj1v8iv.cn-hangzhou.personal.cr.aliyuncs.com/lmdeploy_dlinfer/maca:latest \
    bash -i -c "lmdeploy chat --backend pytorch --device maca internlm/internlm2_5-7b-chat"
```
