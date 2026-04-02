# Generate text with guided decoding — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/examples/llm_guided_decoding.html

Generate text with guided decoding#

Source NVIDIA/TensorRT-LLM.

```text
 1from tensorrt_llm import LLM, SamplingParams
 2from tensorrt_llm.llmapi import GuidedDecodingParams
 3
 4
 5def main():
 6
 7    # Specify the guided decoding backend; xgrammar and llguidance are supported currently.
 8    llm = LLM(model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
 9              guided_decoding_backend='xgrammar')
10
11    # An example from json-mode-eval
12    schema = '{"title": "WirelessAccessPoint", "type": "object", "properties": {"ssid": {"title": "SSID", "type": "string"}, "securityProtocol": {"title": "SecurityProtocol", "type": "string"}, "bandwidth": {"title": "Bandwidth", "type": "string"}}, "required": ["ssid", "securityProtocol", "bandwidth"]}'
13
14    prompt = [{
15        'role':
16        'system',
17        'content':
18        "You are a helpful assistant that answers in JSON. Here's the json schema you must adhere to:\n<schema>\n{'title': 'WirelessAccessPoint', 'type': 'object', 'properties': {'ssid': {'title': 'SSID', 'type': 'string'}, 'securityProtocol': {'title': 'SecurityProtocol', 'type': 'string'}, 'bandwidth': {'title': 'Bandwidth', 'type': 'string'}}, 'required': ['ssid', 'securityProtocol', 'bandwidth']}\n</schema>\n"
19    }, {
20        'role':
21        'user',
22        'content':
23        "I'm currently configuring a wireless access point for our office network and I need to generate a JSON object that accurately represents its settings. The access point's SSID should be 'OfficeNetSecure', it uses WPA2-Enterprise as its security protocol, and it's capable of a bandwidth of up to 1300 Mbps on the 5 GHz band. This JSON object will be used to document our network configurations and to automate the setup process for additional access points in the future. Please provide a JSON object that includes these details."
24    }]
25    prompt = llm.tokenizer.apply_chat_template(prompt, tokenize=False)
26    print(f"Prompt: {prompt!r}")
27
28    output = llm.generate(prompt, sampling_params=SamplingParams(max_tokens=50))
29    print(f"Generated text (unguided): {output.outputs[0].text!r}")
30
31    output = llm.generate(
32        prompt,
33        sampling_params=SamplingParams(
34            max_tokens=50, guided_decoding=GuidedDecodingParams(json=schema)))
35    print(f"Generated text (guided): {output.outputs[0].text!r}")
36
37    # Got output like
38    # Prompt: "<|system|>\nYou are a helpful assistant that answers in JSON. Here's the json schema you must adhere to:\n<schema>\n{'title': 'WirelessAccessPoint', 'type': 'object', 'properties': {'ssid': {'title': 'SSID', 'type': 'string'}, 'securityProtocol': {'title': 'SecurityProtocol', 'type': 'string'}, 'bandwidth': {'title': 'Bandwidth', 'type': 'string'}}, 'required': ['ssid', 'securityProtocol', 'bandwidth']}\n</schema>\n</s>\n<|user|>\nI'm currently configuring a wireless access point for our office network and I need to generate a JSON object that accurately represents its settings. The access point's SSID should be 'OfficeNetSecure', it uses WPA2-Enterprise as its security protocol, and it's capable of a bandwidth of up to 1300 Mbps on the 5 GHz band. This JSON object will be used to document our network configurations and to automate the setup process for additional access points in the future. Please provide a JSON object that includes these details.</s>\n"
39    # Generated text (unguided): '<|assistant|>\nHere\'s a JSON object that accurately represents the settings of a wireless access point for our office network:\n\n```json\n{\n  "title": "WirelessAccessPoint",\n  "'
40    # Generated text (guided): '{"ssid": "OfficeNetSecure", "securityProtocol": "WPA2-Enterprise", "bandwidth": "1300 Mbps"}'
41
42
43if __name__ == '__main__':
44    main()
```
