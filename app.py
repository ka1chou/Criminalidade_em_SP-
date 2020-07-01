import pandas as pd
import streamlit as st
import pydeck as pdk


dataframe = pd.read_csv('criminalidade_sp_2.csv')

st.title("Criminalidade em São Paulo")

st.markdown("""
    A **criminalidade** é um problema recorrente no Brasil.
    Buscamos sempre formas de diminuir esses índices e usando técnicas de 
    Ciências de Dados conseguimos entender melhor o que está acontecendo e 
    gerar insights que direcionem ações capazes de diminuir os 
    Índices de criminalidade.
""")

st.sidebar.info("Foram carregadas {} linhas.".format(dataframe.shape[0]))

if st.sidebar.checkbox("Mostrar tabela?"):
    st.header("Raw Data")
    st.write(dataframe)

df.time = pd.to_datetime(df.time)
ano_selecionado = st.sidebar.slider("Selecione um ano", 2010,2018,2015)
df_selected = df[df.time.dt.year == ano_selecionado]

## st.map(df_selected)
## mapa
st.subheader("Mapa da Criminalidade")
## st.map(df)
st.pydeck_chart(pdf.Deck(
    initial_view_state = pdf.ViewState(
        latitude=-23.567145,
        longitude=-46.648936,
        zoom=8,
        pitch=50
    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=df_selected[['latitude', 'longitude']],
            get_position='[longitude,latitude]',
            auto_highlight=True,
            elevation_scale=50,
            pickable=True,
            elevation_range=[0, 3000],
            extruded=True,
            coverage=1
        )
    ],
))

