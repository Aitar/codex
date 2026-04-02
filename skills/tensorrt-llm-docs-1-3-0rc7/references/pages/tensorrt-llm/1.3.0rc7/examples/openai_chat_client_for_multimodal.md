# OpenAI Chat Client for Multimodal — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/examples/openai_chat_client_for_multimodal.html

OpenAI Chat Client for Multimodal#

Refer to the trtllm-serve documentation for starting a server.

Source NVIDIA/TensorRT-LLM.

```text
  1
  2import os
  3from pathlib import Path
  4
  5from openai import OpenAI
  6from PIL import Image
  7
  8from tensorrt_llm.inputs import (encode_base64_content_from_url,
  9                                 encode_base64_image)
 10
 11client = OpenAI(
 12    base_url="http://localhost:8000/v1",
 13    api_key="tensorrt_llm",
 14)
 15
 16llm_models_root = Path(os.environ.get("LLM_MODELS_ROOT"))
 17
 18if llm_models_root is not None:
 19    multimodal_test_data_path = llm_models_root / "multimodals" / "test_data"
 20    image_url1 = str(multimodal_test_data_path / "seashore.png")
 21    image_url2 = str(multimodal_test_data_path / "inpaint.png")
 22    video_url = str(multimodal_test_data_path / "OAI-sora-tokyo-walk.mp4")
 23    image64 = encode_base64_image(
 24        Image.open(multimodal_test_data_path / "seashore.png"))
 25else:
 26    image_url1 = "https://huggingface.co/datasets/YiYiXu/testing-images/resolve/main/seashore.png"
 27    image_url2 = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/inpaint.png"
 28    video_url = "https://huggingface.co/datasets/Efficient-Large-Model/VILA-inference-demos/resolve/main/OAI-sora-tokyo-walk.mp4"
 29    image64 = encode_base64_content_from_url(
 30        "https://huggingface.co/datasets/YiYiXu/testing-images/resolve/main/seashore.png"
 31    )
 32
 33# SINGLE IMAGE INFERENCE
 34response = client.chat.completions.create(
 35    model="Qwen2.5-VL-3B-Instruct",
 36    messages=[{
 37        "role": "system",
 38        "content": "you are a helpful assistant"
 39    }, {
 40        "role":
 41        "user",
 42        "content": [{
 43            "type": "text",
 44            "text": "Describe the natural environment in the image."
 45        }, {
 46            "type": "image_url",
 47            "image_url": {
 48                "url": image_url1
 49            }
 50        }]
 51    }],
 52    max_tokens=64,
 53)
 54print(response)
 55
 56# MULTI IMAGE INFERENCE
 57response = client.chat.completions.create(
 58    model="Qwen2.5-VL-3B-Instruct",
 59    messages=[{
 60        "role": "system",
 61        "content": "you are a helpful assistant"
 62    }, {
 63        "role":
 64        "user",
 65        "content": [{
 66            "type": "text",
 67            "text": "Tell me the difference between two images"
 68        }, {
 69            "type": "image_url",
 70            "image_url": {
 71                "url": image_url2
 72            }
 73        }, {
 74            "type": "image_url",
 75            "image_url": {
 76                "url": image_url1
 77            }
 78        }]
 79    }],
 80    max_tokens=64,
 81)
 82print(response)
 83
 84# SINGLE VIDEO INFERENCE
 85response = client.chat.completions.create(
 86    model="Qwen2.5-VL-3B-Instruct",
 87    messages=[{
 88        "role": "system",
 89        "content": "you are a helpful assistant"
 90    }, {
 91        "role":
 92        "user",
 93        "content": [{
 94            "type": "text",
 95            "text": "Tell me what you see in the video briefly."
 96        }, {
 97            "type": "video_url",
 98            "video_url": {
 99                "url": video_url
100            }
101        }]
102    }],
103    max_tokens=64,
104)
105print(response)
106
107# IMAGE EMBED INFERENCE
108response = client.chat.completions.create(
109    model="Qwen2.5-VL-3B-Instruct",
110    messages=[{
111        "role": "system",
112        "content": "you are a helpful assistant"
113    }, {
114        "role":
115        "user",
116        "content": [{
117            "type": "text",
118            "text": "Describe the natural environment in the image."
119        }, {
120            "type": "image_url",
121            "image_url": {
122                "url": "data:image/png;base64," + image64
123            }
124        }]
125    }],
126    max_tokens=64,
127)
128print(response)
```
