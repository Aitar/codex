# Open WebUI - vLLM

Source: https://docs.vllm.ai/en/v0.15.0/deployment/frameworks/open-webui/

Open WebUI¶

Open WebUI is an extensible, feature-rich, and user-friendly self-hosted AI platform designed to operate entirely offline. It supports various LLM runners like Ollama and OpenAI-compatible APIs, with built-in RAG capabilities, making it a powerful AI deployment solution.

To get started with Open WebUI using vLLM, follow these steps:

Install the Docker.

Start the vLLM server with a supported chat completion model:

```text
vllm serve Qwen/Qwen3-0.6B-Chat
```

Note

When starting the vLLM server, be sure to specify the host and port using the `--host` and `--port` flags. For example:

```text
vllm serve <model> --host 0.0.0.0 --port 8000
```

Start the Open WebUI Docker container:

```text
docker run -d \
    --name open-webui \
    -p 3000:8080 \
    -v open-webui:/app/backend/data \
    -e OPENAI_API_BASE_URL=http://0.0.0.0:8000/v1 \
    --restart always \
    ghcr.io/open-webui/open-webui:main
```

Open it in the browser: http://open-webui-host:3000/

At the top of the page, you should see the model `Qwen/Qwen3-0.6B-Chat`.
