import streamlit as st
from llm import LLM


def check_password():
    def password_entered():
        if st.session_state['password'] == st.secrets['password']:
            st.session_state['password_correct'] = True
            del st.session_state['password']  # don't store password
        else:
            st.session_state['password_correct'] = False

    if 'password_correct' not in st.session_state:
        st.text_input(
            'Password', type='password', on_change=password_entered, key='password'
        )
        return False
    elif not st.session_state['password_correct']:
        st.text_input(
            'Password', type='password', on_change=password_entered, key='password'
        )
        st.error('😕 Password incorrect')
        return False
    else:
        return True


st.title('A Caminho da Luz')

"""
Nessa demo, o ChatGPT tentará responder às suas perguntas usando o livro
"A Caminho da Luz" de Emmanuel / Chico Xavier como base.
"""

if check_password():
    st.markdown("""
    Exemplos de perguntas:
    - Qual o papel de Jesus na criação da Terra?
    - O que você sabe sobre a criação da lua?
    - O que você pode me contar sobre a família romana?
    - Quem foram os mahatmas?
    - Quem foi Fo-Hi?
    """)

    llm = LLM('index_a_caminho_da_luz.json')

    question = st.text_input('O que você gostaria de saber com base no livro "A Caminho da Luz"?')
    if question:
        answer = llm.query(question)
        st.write(answer)
