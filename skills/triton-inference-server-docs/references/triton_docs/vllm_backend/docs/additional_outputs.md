* Additional...

# Additional Outputs from vLLM[#](#additional-outputs-from-vllm "Link to this heading")

The vLLM backend supports sending additional outputs from vLLM on top of the
usual `text_output` when requested.

All additional outputs are disabled by default and they need to be enabled on a
per-request basis. If enabled, the corresponding output tensor will be set for
all responses from the request.

## Supported Additional Outputs[#](#supported-additional-outputs "Link to this heading")

### Finish Reason[#](#finish-reason "Link to this heading")

The reason why the sequence is finished. See
[here](https://github.com/vllm-project/vllm/blob/v0.6.3.post1/vllm/outputs.py#L26)
for more details.

To enable, set `return_finish_reason` input tensor to `True`. The reason will be
sent as a string on the `finish_reason` output tensor.

### Cumulative Log Probabilities[#](#cumulative-log-probabilities "Link to this heading")

The cumulative log probability of the generated output text. See
[here](https://github.com/vllm-project/vllm/blob/v0.6.3.post1/vllm/outputs.py#L22)
for more details.

To enable, set `return_cumulative_logprob` input tensor to `True`. The floating
point value will be sent on the `cumulative_logprob` output tensor.

### Log Probabilities[#](#log-probabilities "Link to this heading")

The log probabilities of the top probability tokens at each position of the
[logprobs](https://github.com/vllm-project/vllm/blob/v0.6.3.post1/vllm/sampling_params.py#L146-L152)
are requested. Only the log probabilities of the new tokens generated since the
last response are returned on each new response. See
[here](https://github.com/vllm-project/vllm/blob/v0.6.3.post1/vllm/outputs.py#L24-L25)
for more details on the log probabilities.

To enable, set `return_logprobs` input tensor to `True`. The log probabilities
will be sent on the `logprobs` output tensor as a serialized JSON string.

### Number of Input Tokens[#](#number-of-input-tokens "Link to this heading")

The number of token IDs of the prompt. See
[here](https://github.com/vllm-project/vllm/blob/v0.6.3.post1/vllm/outputs.py#L79-L81)
for more details.

To enable, set `return_num_input_tokens` input tensor to `True`. The unsigned
integer value will be sent on the `num_input_tokens` output tensor.

### Number of Output Tokens[#](#number-of-output-tokens "Link to this heading")

The number of token IDs of the generated output text sent on this response. It
is the difference in length of the token IDs generated from the last response to
this response. If this is the first response, the last response length is
presumed to be zero. See
[here](https://github.com/vllm-project/vllm/blob/v0.6.3.post1/vllm/outputs.py#L21)
for more details on the token IDs of the generated output text.

To enable, set `return_num_output_tokens` input tensor to `True`. The unsigned
integer value will be sent on the `num_output_tokens` output tensor.

## Examples[#](#examples "Link to this heading")

### Add Finish Reason to Outputs[#](#add-finish-reason-to-outputs "Link to this heading")

```
import numpy as np
import tritonclient.grpc as grpcclient

inputs = []

inputs.append(grpcclient.InferInput("text_input", [1], "BYTES"))
inputs[-1].set_data_from_numpy(
    np.array(["example prompt".encode("utf-8")], dtype=np.object_)
)

inputs.append(grpcclient.InferInput("return_finish_reason", [1], "BOOL"))
inputs[-1].set_data_from_numpy(np.array([True], dtype=bool))

def callback(result, error):
    ...
    print(result.as_numpy(name="finish_reason"))

with grpcclient.InferenceServerClient("localhost:8001") as client:
    client.start_stream(callback)
    client.async_stream_infer("vLLM_model_name", inputs=inputs, ...)
    client.stop_stream()
```

## Notes[#](#notes "Link to this heading")

* Enabling additional outputs may impact performance, only add additional
  outputs when necessary.

