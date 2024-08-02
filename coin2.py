import pandas as pd
import streamlit as st
import plotly.express as px
import requests

url = "https://api.coingecko.com/api/v3/coins/markets"
parametros = {
    "vs_currency": "brl",
    "order": "market_cap_desc",
    "per_page": 1000,
    "page": 1,
    "sparkline": "false"
}

response = requests.get(url, params=parametros)
data = response.json()

df = pd.DataFrame(data)
print(df.head())



st.set_page_config(layout='wide')

st.title('Dados das principais Criptomoedas')
st.write("API: coingecko.com")

# Criação das abas no Streamlit
tabs = st.tabs(['Dataframe'])
#Menu 

with tabs[0]:
    st.dataframe(df, height=1000)
    #st.plotly_chart(grafico_de_linha, use_container_width=True)
# Rodapé da aplicação
st.markdown(
    """
    <style>
        footer {
            position: relative;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
        }
    </style>
    <footer>
        <p>Aplicação desenvolvida por Anderson Bezerra Silva.</p>
        <p>© 2024 @oanderoficial</p>
    </footer>
    """,
    unsafe_allow_html=True
)