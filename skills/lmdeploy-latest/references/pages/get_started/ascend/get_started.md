# Get Started with Huawei Ascend — lmdeploy

Source: https://lmdeploy.readthedocs.io/en/latest/get_started/ascend/get_started.html

Get Started with Huawei Ascend

Get Started with Huawei Ascend#

We currently support running lmdeploy on Atlas 800T A3, Atlas 800T A2 and Atlas 300I Duo.
The usage of lmdeploy on a Huawei Ascend device is almost the same as its usage on CUDA with PytorchEngine in lmdeploy.
Please read the original Get Started guide before reading this tutorial.

Here is the supported model list.

[!IMPORTANT]
We have uploaded a docker image with KUNPENG CPU to aliyun.
Please try to pull the image by following command:

Atlas 800T A3:

`dockerpullcrpi-4crprmm5baj1v8iv.cn-hangzhou.personal.cr.aliyuncs.com/lmdeploy_dlinfer/ascend:a3-latest`

(Atlas 800T A3 currently supports only the Qwen-series with eager mode.)

Atlas 800T A2:

`dockerpullcrpi-4crprmm5baj1v8iv.cn-hangzhou.personal.cr.aliyuncs.com/lmdeploy_dlinfer/ascend:a2-latest`

300I Duo:

`dockerpullcrpi-4crprmm5baj1v8iv.cn-hangzhou.personal.cr.aliyuncs.com/lmdeploy_dlinfer/ascend:300i-duo-latest`

(Atlas 300I Duo currently works only with graph mode.)

To build the environment yourself, refer to the Dockerfiles here.

Offline batch inference#

LLM inference#

Set `device_type="ascend"` in the `PytorchEngineConfig`:

```text
from lmdeploy import pipeline
from lmdeploy import PytorchEngineConfig
pipe = pipeline("internlm/internlm2_5-7b-chat",
        backend_config=PytorchEngineConfig(tp=1, device_type="ascend"))
question = ["Shanghai is", "Please introduce China", "How are you?"]
response = pipe(question)
print(response)
```

VLM inference#

Set `device_type="ascend"` in the `PytorchEngineConfig`:

```text
from lmdeploy import pipeline, PytorchEngineConfig
from lmdeploy.vl import load_image
pipe = pipeline('OpenGVLab/InternVL2-2B',
        backend_config=PytorchEngineConfig(tp=1, device_type='ascend'))
image = load_image('https://raw.githubusercontent.com/open-mmlab/mmdeploy/main/tests/data/tiger.jpeg')
response = pipe(('describe this image', image))
print(response)
```

Online serving#

Serve a LLM model#

Add `--deviceascend` in the serve command.

```text
lmdeploy serve api_server --backend pytorch --device ascend internlm/internlm2_5-7b-chat
```

Run the following commands to launch docker container for lmdeploy LLM serving:

```text
docker run -it --net=host crpi-4crprmm5baj1v8iv.cn-hangzhou.personal.cr.aliyuncs.com/lmdeploy_dlinfer/ascend:a2-latest \
    bash -i -c "lmdeploy serve api_server --backend pytorch --device ascend internlm/internlm2_5-7b-chat"
```

Serve a VLM model#

Add `--deviceascend` in the serve command

```text
lmdeploy serve api_server --backend pytorch --device ascend OpenGVLab/InternVL2-2B
```

Run the following commands to launch docker container for lmdeploy VLM serving:

```text
docker run -it --net=host crpi-4crprmm5baj1v8iv.cn-hangzhou.personal.cr.aliyuncs.com/lmdeploy_dlinfer/ascend:a2-latest \
    bash -i -c "lmdeploy serve api_server --backend pytorch --device ascend OpenGVLab/InternVL2-2B"
```

Inference with Command line Interface#

Add `--deviceascend` in the serve command.

```text
lmdeploy chat internlm/internlm2_5-7b-chat --backend pytorch --device ascend
```

Run the following commands to launch lmdeploy chatting after starting container:

```text
docker run -it crpi-4crprmm5baj1v8iv.cn-hangzhou.personal.cr.aliyuncs.com/lmdeploy_dlinfer/ascend:a2-latest \
    bash -i -c "lmdeploy chat --backend pytorch --device ascend internlm/internlm2_5-7b-chat"
```

Quantization#

w4a16 AWQ#

Run the following commands to quantize weights on Atlas 800T A2.

```text
lmdeploy lite auto_awq $HF_MODEL --work-dir $WORK_DIR --device npu
```

Please check supported_models before use this feature.

w8a8 SMOOTH_QUANT#

Run the following commands to quantize weights on Atlas 800T A2.

```text
lmdeploy lite smooth_quant $HF_MODEL --work-dir $WORK_DIR --device npu
```

Please check supported_models before use this feature.

int8 KV-cache Quantization#

Ascend backend has supported offline int8 KV-cache Quantization on eager mode.

Please refer this doc for details.

Limitations on 300I Duo#

only support dtype=float16.

only support graph mode, please do not add –eager-mode.
