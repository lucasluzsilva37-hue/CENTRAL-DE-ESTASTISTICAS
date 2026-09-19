import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Football Stats & Probabilities", layout="wide")
st.title("⚽ Estatísticas e Probabilidades de Partidas de Futebol")

API_KEY = "7e94815863mshe0b18b870a071291p148c51jsn131ab4402ec7"
URL_DA_API = "https://sportap17.p.rapidapi.com/v1/sport/football/events/live"

@st.cache_data(ttl=300)
def fetch_live_data():
   try:
    resposta = requests.get(
        URL_DA_API,
        headers={
            "X-RapidAPI-Key": API_KEY,
            "X-RapidAPI-Host": "sportap17.p.rapidapi.com",
        },
    )
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return None
   except Exception as e:
    st.error(f"Error fetching data: {e}")
    return None

try:
    dados = fetch_live_data()
    print(dados)  # Adicionado para ver os dados no console
    if dados:
        df = pd.DataFrame(dados)
        st.dataframe(df)
    else:
        st.warning(
            "No live data available. Please check the API connection."
        )
except Exception as e:
    st.error(f"Error: {e}")
 st.info("App initialized. Connect a sports API or load match data to begin.")
