import llama_index as ll


if __name__ == '__main__':
    documents = ll.SimpleDirectoryReader('data/A caminho da Luz').load_data()
    index = ll.GPTSimpleVectorIndex(documents)
    index.save_to_disk('index_a_caminho_da_luz.json')
