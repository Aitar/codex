Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/examples/llm_sampling.md

* [LLM Examples](llm_api_examples.md)
* Sampling Techniques Showcase

# Sampling Techniques Showcase[#](#sampling-techniques-showcase "Link to this heading")

Source [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM/blob/48b7b5d8b7ed1e6bff57aecc6ff7d1533288bed8/examples/llm-api/llm_sampling.py).

```
  1"""
  2This example demonstrates various sampling techniques available in TensorRT-LLM.
  3It showcases different sampling parameters and their effects on text generation.
  4"""
  5
  6from typing import Optional
  7
  8import click
  9
 10from tensorrt_llm import LLM, SamplingParams
 11
 12# Example prompts to demonstrate different sampling techniques
 13prompts = [
 14    "What is the future of artificial intelligence?",
 15    "Describe a beautiful sunset over the ocean.",
 16    "Write a short story about a robot discovering emotions.",
 17]
 18
 19
 20def demonstrate_greedy_decoding(prompt: str):
 21    """Demonstrates greedy decoding with temperature=0."""
 22    print("\n🎯 === GREEDY DECODING ===")
 23    print("Using temperature=0 for deterministic, focused output")
 24
 25    llm = LLM(model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
 26
 27    sampling_params = SamplingParams(
 28        max_tokens=50,
 29        temperature=0.0,  # Greedy decoding
 30    )
 31
 32    response = llm.generate(prompt, sampling_params)
 33    print(f"Prompt: {prompt}")
 34    print(f"Response: {response.outputs[0].text}")
 35
 36
 37def demonstrate_temperature_sampling(prompt: str):
 38    """Demonstrates temperature sampling with different temperature values."""
 39    print("\n🌡️ === TEMPERATURE SAMPLING ===")
 40    print(
 41        "Higher temperature = more creative/random, Lower temperature = more focused"
 42    )
 43
 44    llm = LLM(model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
 45
 46    temperatures = [0.3, 0.7, 1.0, 1.5]
 47    for temp in temperatures:
 48
 49        sampling_params = SamplingParams(
 50            max_tokens=50,
 51            temperature=temp,
 52        )
 53
 54        response = llm.generate(prompt, sampling_params)
 55        print(f"Temperature {temp}: {response.outputs[0].text}")
 56
 57
 58def demonstrate_top_k_sampling(prompt: str):
 59    """Demonstrates top-k sampling with different k values."""
 60    print("\n🔝 === TOP-K SAMPLING ===")
 61    print("Only consider the top-k most likely tokens at each step")
 62
 63    llm = LLM(model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
 64
 65    top_k_values = [1, 5, 20, 50]
 66
 67    for k in top_k_values:
 68        sampling_params = SamplingParams(
 69            max_tokens=50,
 70            temperature=0.8,  # Use moderate temperature
 71            top_k=k,
 72        )
 73
 74        response = llm.generate(prompt, sampling_params)
 75        print(f"Top-k {k}: {response.outputs[0].text}")
 76
 77
 78def demonstrate_top_p_sampling(prompt: str):
 79    """Demonstrates top-p (nucleus) sampling with different p values."""
 80    print("\n🎯 === TOP-P (NUCLEUS) SAMPLING ===")
 81    print("Only consider tokens whose cumulative probability is within top-p")
 82
 83    llm = LLM(model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
 84
 85    top_p_values = [0.1, 0.5, 0.9, 0.95]
 86
 87    for p in top_p_values:
 88        sampling_params = SamplingParams(
 89            max_tokens=50,
 90            temperature=0.8,  # Use moderate temperature
 91            top_p=p,
 92        )
 93
 94        response = llm.generate(prompt, sampling_params)
 95        print(f"Top-p {p}: {response.outputs[0].text}")
 96
 97
 98def demonstrate_combined_sampling(prompt: str):
 99    """Demonstrates combined top-k and top-p sampling."""
100    print("\n🔄 === COMBINED TOP-K + TOP-P SAMPLING ===")
101    print("Using both top-k and top-p together for balanced control")
102
103    llm = LLM(model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
104
105    sampling_params = SamplingParams(
106        max_tokens=50,
107        temperature=0.8,
108        top_k=40,  # Consider top 40 tokens
109        top_p=0.9,  # Within 90% cumulative probability
110    )
111
112    response = llm.generate(prompt, sampling_params)
113    print(f"Combined (k=40, p=0.9): {response.outputs[0].text}")
114
115
116def demonstrate_multiple_sequences(prompt: str):
117    """Demonstrates generating multiple sequences with different sampling."""
118    print("\n📚 === MULTIPLE SEQUENCES ===")
119    print("Generate multiple different responses for the same prompt")
120
121    llm = LLM(model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
122
123    sampling_params = SamplingParams(
124        max_tokens=40,
125        temperature=0.8,
126        top_k=50,
127        top_p=0.95,
128        n=3,  # Generate 3 different sequences
129    )
130
131    response = llm.generate(prompt, sampling_params)
132    print(f"Prompt: {prompt}")
133    for i, output in enumerate(response.outputs):
134        print(f"Sequence {i+1}: {output.text}")
135
136
137def demonstrate_beam_search(prompt: str):
138    """Demonstrates beam search."""
139    print("\n🎯 === BEAM SEARCH ===")
140    beam_width = 2
141    llm = LLM(model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
142              max_beam_width=beam_width)
143
144    sampling_params = SamplingParams(
145        max_tokens=50,
146        use_beam_search=True,
147        n=beam_width,
148    )
149
150    response = llm.generate(prompt, sampling_params)
151    print(f"Prompt: {prompt}")
152    print(f"Response: {response.outputs[0].text}")
153
154
155def demonstrate_with_logprobs(prompt: str):
156    """Demonstrates generation with log probabilities."""
157    print("\n📊 === GENERATION WITH LOG PROBABILITIES ===")
158    print("Get probability information for generated tokens")
159
160    llm = LLM(model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
161
162    sampling_params = SamplingParams(
163        max_tokens=20,
164        temperature=0.7,
165        top_k=50,
166        logprobs=True,  # Return log probabilities
167    )
168
169    response = llm.generate(prompt, sampling_params)
170    output = response.outputs[0]
171
172    print(f"Prompt: {prompt}")
173    print(f"Generated: {output.text}")
174    print(f"Logprobs: {output.logprobs}")
175
176
177def run_all_demonstrations(model_path: Optional[str] = None):
178    """Run all sampling demonstrations."""
179    print("🚀 TensorRT LLM Sampling Techniques Showcase")
180    print("=" * 50)
181
182    # Use the first prompt for most demonstrations
183    demo_prompt = prompts[0]
184
185    # Run all demonstrations
186    demonstrate_greedy_decoding(demo_prompt)
187    demonstrate_temperature_sampling(demo_prompt)
188    demonstrate_top_k_sampling(demo_prompt)
189    demonstrate_top_p_sampling(demo_prompt)
190    demonstrate_combined_sampling(demo_prompt)
191    demonstrate_multiple_sequences(demo_prompt)
192    demonstrate_beam_search(demo_prompt)
193    demonstrate_with_logprobs(demo_prompt)
194
195    print("\n🎉 All sampling demonstrations completed!")
196
197
198@click.command()
199@click.option("--model",
200              type=str,
201              default=None,
202              help="Path to the model or model name")
203@click.option("--demo",
204              type=click.Choice([
205                  "greedy", "temperature", "top_k", "top_p", "combined",
206                  "multiple", "beam", "logprobs", "creative", "all"
207              ]),
208              default="all",
209              help="Which demonstration to run")
210@click.option("--prompt", type=str, default=None, help="Custom prompt to use")
211def main(model: Optional[str], demo: str, prompt: Optional[str]):
212    """
213    Showcase various sampling techniques in TensorRT-LLM.
214
215    Examples:
216        python llm_sampling.py --demo all
217        python llm_sampling.py --demo temperature --prompt "Tell me a joke"
218        python llm_sampling.py --demo beam --model path/to/your/model
219    """
220
221    demo_prompt = prompt or prompts[0]
222
223    # Run specific demonstration
224    if demo == "greedy":
225        demonstrate_greedy_decoding(demo_prompt)
226    elif demo == "temperature":
227        demonstrate_temperature_sampling(demo_prompt)
228    elif demo == "top_k":
229        demonstrate_top_k_sampling(demo_prompt)
230    elif demo == "top_p":
231        demonstrate_top_p_sampling(demo_prompt)
232    elif demo == "combined":
233        demonstrate_combined_sampling(demo_prompt)
234    elif demo == "multiple":
235        demonstrate_multiple_sequences(demo_prompt)
236    elif demo == "beam":
237        demonstrate_beam_search(demo_prompt)
238    elif demo == "logprobs":
239        demonstrate_with_logprobs(demo_prompt)
240    elif demo == "all":
241        run_all_demonstrations(model)
242
243
244if __name__ == "__main__":
245    main()
```

[previous

Runtime Configuration Examples](llm_runtime.md "previous page")
[next

Run LLM-API with pytorch backend on Slurm](llm_mgmn_llm_distributed.md "next page")