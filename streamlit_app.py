import streamlit as st
from llm import LLM


llm = LLM('index_a_caminho_da_luz.json')

st.title('A Caminho da Luz')

"""
Nessa demo, o ChatGPT tentará responder às suas perguntas usando o livro
"A Caminho da Luz" de Emmanuel / Chico Xavier como base.
"""

st.markdown("""
Exemplos de perguntas:
- Qual o papel de Jesus na criação da Terra?
- O que você sabe sobre a criação da lua?
- O que você pode me contar sobre a família romana?
- Quem foram os mahatmas?
- Quem foi Fo-Hi?
""")

question = st.text_input('O que você gostaria de saber com base no livro "A Caminho da Luz"?')
if question:
    answer = llm.query(question)
    st.write(answer)
