from transformers import AutoTokenizer, AutoModelWithLMHead, SummarizationPipeline

from Tokenizer import Tokenizer

class Model():
    def __init__(self):
        self.pipeline = SummarizationPipeline(
                model=AutoModelWithLMHead.from_pretrained("SEBIS/code_trans_t5_large_code_documentation_generation_python_multitask"),
                tokenizer=AutoTokenizer.from_pretrained("SEBIS/code_trans_t5_large_code_documentation_generation_python_multitask", skip_special_tokens=True),
                device=-1
            )
        self.tokenizer = Tokenizer()

    def tokenize(self, code):
        return self.tokenizer.tokenize(code)
        
    def process(self, text):
        if not text:
            print("Input text is empty.")
            return
        tokenized_text = self.tokenize(text)
        # print("Tokenized text: " + tokenized_text)
        return self.pipeline(tokenized_text, max_new_tokens=200)[0]['summary_text']