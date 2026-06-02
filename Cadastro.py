import streamlit as st
import pandas as pd
from datetime import date


def gravar_dados(nome, dt_nasc, tipo):
    if nome and dt_nasc <= date.today():
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome},{dt_nasc},{tipo}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False


st.set_page_config(
    page_title="Cadastro de Clientes",
    page_icon="📕"
)

st.title("Cadastro de Clientes")
st.divider()

nome = st.text_input("Digie o nome do cliente:",
                     key="nome_cliente")
dt_nasc = st.date_input("Data Nacimento:", 
                        format="DD/MM/YYYY", 
                        key="dt_nasc", 
                        min_value=date(1900, 1, 1), max_value=date.today())


tipo = st.selectbox("Tipo de cliente:",
                    ["Pessoa Física", "Pessoa Jurídica"],
                    key="tipo_cliente"
                    )

btn_cadastrar = st.button("Cadastrar", 
                          on_click=gravar_dados,
                          args=[nome, dt_nasc, tipo]
                          )

if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!", icon="✅")
    else:
        st.error("Erro ao cadastrar cliente. Verifique os dados e tente novamente.", icon="❌")
    