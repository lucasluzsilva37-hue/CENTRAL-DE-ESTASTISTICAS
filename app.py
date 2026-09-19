

import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Football Stats & Probabilities", layout="wide")
st.title("⚽ Football Match Stats & Probabilities")

API_KEY = "7e94815863msh0e01b870a071291p148c51jsn131ab4402ec7"
URL_da_API = "https://sportapi7.p.rapidapi.com/api/v1/sport/football/events/live"

@st.cache_data(ttl=300)
def fetch_live_data():
    try:
        resposta = requests.get(URL_da_API, headers={"x-rapidapi-key": API_KEY, "x-rapidapi-host": "sportapi7.p.rapidapi.com"})
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return None
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

try:
    data = fetch_live_data()
    if data:
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.warning("No live data available. Please check the API connection.")
except Exception as e:
    st.info("App initialized. Connect a sports API or load match data to begin.")
