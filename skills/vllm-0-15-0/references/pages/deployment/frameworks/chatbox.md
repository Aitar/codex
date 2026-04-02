# Chatbox - vLLM

Source: https://docs.vllm.ai/en/v0.15.0/deployment/frameworks/chatbox/

Chatbox¶

Chatbox is a desktop client for LLMs, available on Windows, Mac, Linux.

It allows you to deploy a large language model (LLM) server with vLLM as the backend, which exposes OpenAI-compatible endpoints.

Prerequisites¶

Set up the vLLM environment:

```text
pip install vllm
```

Deploy¶

Start the vLLM server with the supported chat completion model, e.g.

```text
vllm serve qwen/Qwen1.5-0.5B-Chat
```

Download and install Chatbox desktop.

On the bottom left of settings, Add Custom Provider

API Mode: `OpenAI API Compatible`

Name: vllm

API Host: `http://{vllm server host}:{vllm server port}/v1`

API Path: `/chat/completions`

Model: `qwen/Qwen1.5-0.5B-Chat`

Go to `Just chat`, and start to chat:
