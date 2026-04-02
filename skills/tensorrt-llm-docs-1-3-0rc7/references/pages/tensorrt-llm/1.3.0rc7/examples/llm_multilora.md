# Generate text with multiple LoRA adapters — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/examples/llm_multilora.html

Generate text with multiple LoRA adapters#

Source NVIDIA/TensorRT-LLM.

```text
 1
 2import argparse
 3from typing import Optional
 4
 5from huggingface_hub import snapshot_download
 6
 7from tensorrt_llm import LLM
 8from tensorrt_llm.executor import LoRARequest
 9from tensorrt_llm.lora_helper import LoraConfig
10
11
12def main(chatbot_lora_dir: Optional[str], mental_health_lora_dir: Optional[str],
13         tarot_lora_dir: Optional[str]):
14
15    # Download the LoRA adapters from huggingface hub, if not provided via command line args.
16    if chatbot_lora_dir is None:
17        chatbot_lora_dir = snapshot_download(
18            repo_id="snshrivas10/sft-tiny-chatbot")
19    if mental_health_lora_dir is None:
20        mental_health_lora_dir = snapshot_download(
21            repo_id=
22            "givyboy/TinyLlama-1.1B-Chat-v1.0-mental-health-conversational")
23    if tarot_lora_dir is None:
24        tarot_lora_dir = snapshot_download(
25            repo_id="barissglc/tinyllama-tarot-v1")
26
27    # Currently, we need to pass at least one lora_dir to LLM constructor via build_config.lora_config.
28    # This is necessary because it requires some configuration in the lora_dir to build the engine with LoRA support.
29    lora_config = LoraConfig(lora_dir=[chatbot_lora_dir],
30                             max_lora_rank=64,
31                             max_loras=3,
32                             max_cpu_loras=3)
33    llm = LLM(model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
34              lora_config=lora_config)
35
36    # Sample prompts
37    prompts = [
38        "Hello, tell me a story: ",
39        "Hello, tell me a story: ",
40        "I've noticed you seem a bit down lately. Is there anything you'd like to talk about?",
41        "I've noticed you seem a bit down lately. Is there anything you'd like to talk about?",
42        "In this reading, the Justice card represents a situation where",
43        "In this reading, the Justice card represents a situation where",
44    ]
45
46    # At runtime, multiple LoRA adapters can be specified via lora_request; None means no LoRA used.
47    for output in llm.generate(prompts,
48                               lora_request=[
49                                   None,
50                                   LoRARequest("chatbot", 1, chatbot_lora_dir),
51                                   None,
52                                   LoRARequest("mental-health", 2,
53                                               mental_health_lora_dir), None,
54                                   LoRARequest("tarot", 3, tarot_lora_dir)
55                               ]):
56        prompt = output.prompt
57        generated_text = output.outputs[0].text
58        print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
59
60    # Got output like
61    # Prompt: 'Hello, tell me a story: ', Generated text: '1. Start with a question: "What\'s your favorite color?" 2. Ask a question that leads to a story: "What\'s your'
62    # Prompt: 'Hello, tell me a story: ', Generated text: '1. A person is walking down the street. 2. A person is sitting on a bench. 3. A person is reading a book.'
63    # Prompt: "I've noticed you seem a bit down lately. Is there anything you'd like to talk about?", Generated text: "\n\nJASON: (smiling) No, I'm just feeling a bit overwhelmed lately. I've been trying to"
64    # Prompt: "I've noticed you seem a bit down lately. Is there anything you'd like to talk about?", Generated text: "\n\nJASON: (sighs) Yeah, I've been struggling with some personal issues. I've been feeling like I'm"
65    # Prompt: 'In this reading, the Justice card represents a situation where', Generated text: 'you are being asked to make a decision that will have a significant impact on your life. The card suggests that you should take the time to consider all the options'
66    # Prompt: 'In this reading, the Justice card represents a situation where', Generated text: 'you are being asked to make a decision that will have a significant impact on your life. It is important to take the time to consider all the options and make'
67
68
69if __name__ == '__main__':
70    parser = argparse.ArgumentParser(
71        description="Generate text with multiple LoRA adapters")
72    parser.add_argument('--chatbot_lora_dir',
73                        type=str,
74                        default=None,
75                        help='Path to the chatbot LoRA directory')
76    parser.add_argument('--mental_health_lora_dir',
77                        type=str,
78                        default=None,
79                        help='Path to the mental health LoRA directory')
80    parser.add_argument('--tarot_lora_dir',
81                        type=str,
82                        default=None,
83                        help='Path to the tarot LoRA directory')
84    args = parser.parse_args()
85    main(args.chatbot_lora_dir, args.mental_health_lora_dir,
86         args.tarot_lora_dir)
```
