import llama_index as ll
from langchain import OpenAI


class LLM:
    def __init__(self, index_path):
        self.llm_predictor = ll.LLMPredictor(llm=OpenAI(temperature=0, model_name='gpt-3.5-turbo'))
        self.index = ll.GPTSimpleVectorIndex.load_from_disk(index_path, llm_predictor=self.llm_predictor)

    def query(self, question):
        return self.index.query(question)
