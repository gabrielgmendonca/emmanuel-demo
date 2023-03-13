import llama_index as ll
from langchain import OpenAI


if __name__ == '__main__':
    documents = ll.SimpleDirectoryReader('data/A caminho da Luz').load_data()
    llm_predictor = ll.LLMPredictor(llm=OpenAI(temperature=0, model_name='gpt-3.5-turbo'))
    index = ll.GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor)
    index.save_to_disk('index_a_caminho_da_luz.json')
