import pandas as pd
import streamlit as st


dataframe = pd.read_csv('criminalidade_sp_2.csv')

st.title("Criminalidade em São Paulo")

st.markdown("""
    A **criminalidade** é um problema recorrente no Brasil.
    Buscamos sempre formas de diminuir esses índices e usando técnicas de 
    Ciências de Dados conseguimos entender melhor o que está acontecendo e 
    gerar insights que direcionem ações capazes de diminuir os 
    Índices de criminalidade.
""")

if st.sidebar.checkbox("Mostrar tabela?"):
    st.header("Raw Data")
    st.write(dataframe)

st.sidebar.info("Foram carregadas {} linhas.".format(dataframe.shape[0]))
