# Streamlit - vLLM

Source: https://docs.vllm.ai/en/v0.15.0/deployment/frameworks/streamlit/

Streamlit¶

Streamlit lets you transform Python scripts into interactive web apps in minutes, instead of weeks. Build dashboards, generate reports, or create chat apps.

It can be quickly integrated with vLLM as a backend API server, enabling powerful LLM inference via API calls.

Prerequisites¶

Set up the vLLM environment by installing all required packages:

```text
pip install vllm streamlit openai
```

Deploy¶

Start the vLLM server with a supported chat completion model, e.g.

```text
vllm serve Qwen/Qwen1.5-0.5B-Chat
```

Use the script: examples/online_serving/streamlit_openai_chatbot_webserver.py

Start the streamlit web UI and start to chat:

```text
streamlit run streamlit_openai_chatbot_webserver.py

# or specify the VLLM_API_BASE or VLLM_API_KEY
VLLM_API_BASE="http://vllm-server-host:vllm-server-port/v1" \
    streamlit run streamlit_openai_chatbot_webserver.py

# start with debug mode to view more details
streamlit run streamlit_openai_chatbot_webserver.py --logger.level=debug
```
