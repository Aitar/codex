Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/examples/curl_chat_client_for_multimodal.md

* [Online Serving Examples](trtllm_serve_examples.md)
* Curl Chat Client For Multimodal

# Curl Chat Client For Multimodal[#](#curl-chat-client-for-multimodal "Link to this heading")

Refer to the [trtllm-serve documentation](https://nvidia.github.io/TensorRT-LLM/commands/trtllm-serve.md) for starting a server.

Source [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM/blob/48b7b5d8b7ed1e6bff57aecc6ff7d1533288bed8/examples/serve/curl_chat_client_for_multimodal.sh).

```
 1#! /usr/bin/env bash
 2
 3# SINGLE IMAGE INFERENCE
 4curl http://localhost:8000/v1/chat/completions \
 5    -H "Content-Type: application/json"  \
 6    -d '{
 7        "model": "Qwen2.5-VL-3B-Instruct",
 8        "messages":[{
 9            "role": "system",
10            "content": "You are a helpful assistant."
11        }, {
12            "role": "user",
13            "content": [
14                {
15                    "type": "text",
16                    "text": "Describe the natural environment in the image."
17                },
18                {
19                    "type":"image_url",
20                    "image_url": {
21                        "url": "https://huggingface.co/datasets/YiYiXu/testing-images/resolve/main/seashore.png"
22                    }
23                }
24            ]
25        }],
26        "max_tokens": 64,
27        "temperature": 0
28    }'
29
30# MULTI IMAGE INFERENCE
31curl http://localhost:8000/v1/chat/completions \
32    -H "Content-Type: application/json" \
33    -d '{
34        "model": "Qwen2.5-VL-3B-Instruct",
35        "messages":[{
36            "role": "system",
37            "content": "You are a helpful assistant."
38        }, {
39            "role": "user",
40            "content": [
41                {
42                    "type": "text",
43                    "text":"Tell me the difference between two images"
44                },
45                {
46                    "type":"image_url",
47                    "image_url": {
48                        "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/inpaint.png"
49                    }
50                },
51                {
52                    "type":"image_url",
53                    "image_url": {
54                        "url": "https://huggingface.co/datasets/YiYiXu/testing-images/resolve/main/seashore.png"
55                    }
56                }
57            ]
58        }],
59        "max_tokens": 64,
60        "temperature": 0
61    }'
62
63# SINGLE VIDEO INFERENCE
64curl http://localhost:8000/v1/chat/completions \
65    -H "Content-Type: application/json" \
66    -d '{
67        "model": "Qwen2.5-VL-3B-Instruct",
68        "messages":[{
69            "role": "system",
70            "content": "You are a helpful assistant."
71        }, {
72            "role": "user",
73            "content": [
74                {
75                    "type": "text",
76                    "text":"Tell me what you see in the video briefly."
77                },
78                {
79                    "type":"video_url",
80                    "video_url": {
81                        "url": "https://huggingface.co/datasets/Efficient-Large-Model/VILA-inference-demos/resolve/main/OAI-sora-tokyo-walk.mp4"
82                    }
83                }
84            ]
85        }],
86        "max_tokens": 64,
87        "temperature": 0
88    }'
```

[previous

Curl Chat Client](curl_chat_client.md "previous page")
[next

Curl Completion Client](curl_completion_client.md "next page")