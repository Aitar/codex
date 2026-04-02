Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/examples/openai_chat_client_for_multimodal.md

* [Online Serving Examples](trtllm_serve_examples.md)
* OpenAI Chat Client for Multimodal

# OpenAI Chat Client for Multimodal[#](#openai-chat-client-for-multimodal "Link to this heading")

Refer to the [trtllm-serve documentation](https://nvidia.github.io/TensorRT-LLM/commands/trtllm-serve.md) for starting a server.

Source [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM/blob/48b7b5d8b7ed1e6bff57aecc6ff7d1533288bed8/examples/serve/openai_chat_client_for_multimodal.py).

```
  1
  2from openai import OpenAI
  3
  4from tensorrt_llm.inputs import encode_base64_content_from_url
  5
  6client = OpenAI(
  7    base_url="http://localhost:8000/v1",
  8    api_key="tensorrt_llm",
  9)
 10
 11# SINGLE IMAGE INFERENCE
 12response = client.chat.completions.create(
 13    model="Qwen2.5-VL-3B-Instruct",
 14    messages=[{
 15        "role": "system",
 16        "content": "you are a helpful assistant"
 17    }, {
 18        "role":
 19        "user",
 20        "content": [{
 21            "type": "text",
 22            "text": "Describe the natural environment in the image."
 23        }, {
 24            "type": "image_url",
 25            "image_url": {
 26                "url":
 27                "https://huggingface.co/datasets/YiYiXu/testing-images/resolve/main/seashore.png"
 28            }
 29        }]
 30    }],
 31    max_tokens=64,
 32)
 33print(response)
 34
 35# MULTI IMAGE INFERENCE
 36response = client.chat.completions.create(
 37    model="Qwen2.5-VL-3B-Instruct",
 38    messages=[{
 39        "role": "system",
 40        "content": "you are a helpful assistant"
 41    }, {
 42        "role":
 43        "user",
 44        "content": [{
 45            "type": "text",
 46            "text": "Tell me the difference between two images"
 47        }, {
 48            "type": "image_url",
 49            "image_url": {
 50                "url":
 51                "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/inpaint.png"
 52            }
 53        }, {
 54            "type": "image_url",
 55            "image_url": {
 56                "url":
 57                "https://huggingface.co/datasets/YiYiXu/testing-images/resolve/main/seashore.png"
 58            }
 59        }]
 60    }],
 61    max_tokens=64,
 62)
 63print(response)
 64
 65# SINGLE VIDEO INFERENCE
 66response = client.chat.completions.create(
 67    model="Qwen2.5-VL-3B-Instruct",
 68    messages=[{
 69        "role": "system",
 70        "content": "you are a helpful assistant"
 71    }, {
 72        "role":
 73        "user",
 74        "content": [{
 75            "type": "text",
 76            "text": "Tell me what you see in the video briefly."
 77        }, {
 78            "type": "video_url",
 79            "video_url": {
 80                "url":
 81                "https://huggingface.co/datasets/Efficient-Large-Model/VILA-inference-demos/resolve/main/OAI-sora-tokyo-walk.mp4"
 82            }
 83        }]
 84    }],
 85    max_tokens=64,
 86)
 87print(response)
 88
 89# IMAGE EMBED INFERENCE
 90image64 = encode_base64_content_from_url(
 91    "https://huggingface.co/datasets/YiYiXu/testing-images/resolve/main/seashore.png"
 92)
 93response = client.chat.completions.create(
 94    model="Qwen2.5-VL-3B-Instruct",
 95    messages=[{
 96        "role": "system",
 97        "content": "you are a helpful assistant"
 98    }, {
 99        "role":
100        "user",
101        "content": [{
102            "type": "text",
103            "text": "Describe the natural environment in the image."
104        }, {
105            "type": "image_url",
106            "image_url": {
107                "url": "data:image/png;base64," + image64
108            }
109        }]
110    }],
111    max_tokens=64,
112)
113print(response)
```

[previous

OpenAI Chat Client](openai_chat_client.md "previous page")
[next

OpenAI Completion Client](openai_completion_client.md "next page")