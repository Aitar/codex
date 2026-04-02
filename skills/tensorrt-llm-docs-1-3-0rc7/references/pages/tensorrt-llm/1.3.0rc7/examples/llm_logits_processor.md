# Control generated text using logits processor — TensorRT LLM

Source: https://nvidia.github.io/TensorRT-LLM/1.3.0rc7/examples/llm_logits_processor.html

Control generated text using logits processor#

Source NVIDIA/TensorRT-LLM.

```text
  1from typing import List, Optional
  2
  3import torch
  4from transformers import PreTrainedTokenizer
  5
  6from tensorrt_llm import LLM
  7from tensorrt_llm.sampling_params import LogitsProcessor, SamplingParams
  8
  9
 10def text_to_token(tokenizer: PreTrainedTokenizer, text: str, last: bool):
 11    tokens = tokenizer.encode(text, add_special_tokens=False)
 12
 13    max_token_count = 1
 14    bos_token_added = getattr(tokenizer, 'bos_token', None) and getattr(
 15        tokenizer, 'bos_token_id', None) in tokens
 16    prefix_token_added = getattr(tokenizer, 'add_prefix_space',
 17                                 None) is not False
 18    if bos_token_added or prefix_token_added:
 19        max_token_count = 2
 20
 21    if not last and len(tokens) > max_token_count:
 22        raise Exception(
 23            f"Can't convert {text} to token. It has {len(tokens)} tokens.")
 24
 25    return tokens[-1]
 26
 27
 28# The recommended way to create a customized logits processor:
 29#     * Subclass LogitsProcessor and implement the processing logics in the __call__ method.
 30#     * Create an instance and pass to SamplingParams.
 31# More LogitsProcessors references can be found at https://github.com/NVIDIA/logits-processor-zoo.
 32class GenLengthLogitsProcessor(LogitsProcessor):
 33    """
 34    A logits processor that adjusts the likelihood of the end-of-sequence (EOS) token
 35    based on the length of the generated sequence, encouraging or discouraging shorter answers.
 36    WARNING: Create a new object before every model.generate call since token_count is accumulated.
 37
 38    Parameters
 39    ----------
 40    tokenizer: The tokenizer used by the LLM.
 41    boost_factor (float): A factor to boost the likelihood of the EOS token as the sequence length increases.
 42                        Suggested value range is [-1.0, 1.0]. Negative values are used for the opposite effect.
 43    p (int, optional): The power to which the token count is raised when computing the boost value. Default is 2.
 44    complete_sentences (bool, optional): If True, boosts EOS token likelihood only when the last token is a full stop
 45                                        or a new line. Default is False.
 46
 47    """
 48
 49    def __init__(self,
 50                 tokenizer,
 51                 boost_factor: float,
 52                 p: int = 2,
 53                 complete_sentences: bool = False):
 54        self.eos_token = tokenizer.eos_token_id
 55        self.boost_factor = boost_factor
 56        self.p = p
 57        self.token_count = 0
 58        self.full_stop_token = text_to_token(tokenizer,
 59                                             "It is a sentence.",
 60                                             last=True)
 61        self.new_line_token = text_to_token(tokenizer,
 62                                            "It is a new line\n",
 63                                            last=True)
 64        self.complete_sentences = complete_sentences
 65
 66    def __call__(self, req_ids: int, logits: torch.Tensor, ids: List[List[int]],
 67                 stream_ptr, client_id: Optional[int]):
 68        boost_val = self.boost_factor * (self.token_count**self.p) / (10**
 69                                                                      self.p)
 70
 71        stream = None if stream_ptr is None else torch.cuda.ExternalStream(
 72            stream_ptr)
 73
 74        with torch.cuda.stream(stream):
 75            ids = torch.LongTensor(ids).to(logits.device, non_blocking=True)
 76
 77            if self.complete_sentences:
 78                enabled = (ids[:, -1] == self.full_stop_token) | (
 79                    ids[:, -1] == self.new_line_token)
 80                logits[:, :, self.eos_token] += enabled * boost_val
 81            else:
 82                logits[:, :, self.eos_token] += boost_val
 83
 84        self.token_count += 1
 85
 86
 87def main():
 88
 89    llm = LLM(model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
 90
 91    # Sample prompts
 92    prompts = [
 93        "The future of AI is",
 94        "The future of AI is",
 95    ]
 96
 97    # Generate text
 98    for prompt_id, prompt in enumerate(prompts):
 99        if prompt_id % 2 == 0:
100            # Without logit processor
101            sampling_params = SamplingParams(top_p=1, max_tokens=200)
102        else:
103            # Each prompt can be specified with a logits processor at runtime
104            sampling_params = SamplingParams(
105                temperature=0.8,
106                top_p=0.95,
107                logits_processor=GenLengthLogitsProcessor(
108                    llm.tokenizer, boost_factor=1, complete_sentences=True))
109
110        output = llm.generate(prompt, sampling_params)
111        print(
112            f"Prompt: {output.prompt!r}, Generated text: {output.outputs[0].text!r}"
113        )
114
115    # Got output like:
116    # Prompt (original): "bright, and it's not just for big companies. Small businesses can also benefit from AI technology. Here are some ways:\n\n1. Improved customer service: AI can help businesses provide better customer service by analyzing customer data and providing personalized recommendations.
117    #                    This can help businesses improve their customer experience and increase customer loyalty.\n\n2. Increased productivity: AI can help businesses automate repetitive tasks, freeing up employees to focus on more complex tasks. This can
118    #                    help businesses increase productivity and reduce costs.\n\n3. Enhanced marketing: AI can help businesses create more personalized marketing campaigns by analyzing customer data and targeting specific audiences. This can help businesses
119    #                    increase their marketing ROI and drive more sales.\n\n4. Improved supply chain management: AI can help businesses optimize their supply chain by analyzing data on demand,"'
120    #
121    # Prompt (with GenLenthLogitsProcesor): "bright, and it's not just for big companies. Small businesses can also benefit from AI technology."
122
123
124if __name__ == '__main__':
125    main()
```
