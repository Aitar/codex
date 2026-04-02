* vLLM Health...

# vLLM Health Check (BETA)[#](#vllm-health-check-beta "Link to this heading")

> [!NOTE]
> The vLLM Health Check support is currently in BETA. Its features and
> functionality are subject to change as we collect feedback. We are excited to
> hear any thoughts you have!

The vLLM backend supports checking for
[vLLM Engine Health](https://github.com/vllm-project/vllm/blob/v0.6.3.post1/vllm/engine/async_llm_engine.py#L1177-L1185)
upon receiving each inference request. If the health check fails, the model
state will becomes NOT Ready at the server, which can be queried by the
[Repository Index](../../protocol/extension_model_repository.md#index)
or
[Model Ready](https://github.com/triton-inference-server/client/blob/main/src/c%2B%2B/library/http_client.h#L178-L192)
APIs.

The Health Check is disabled by default. To enable it, set the following
parameter on the model config to true

```
parameters: {
  key: "ENABLE_VLLM_HEALTH_CHECK"
  value: { string_value: "true" }
}
```

and select
[Model Control Mode EXPLICIT](../../user_guide/model_management.md#model-control-mode-explicit)
when the server is started.