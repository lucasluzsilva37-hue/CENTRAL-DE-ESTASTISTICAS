import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Football Stats & Probabilities", layout="wide")
st.title("⚽ Football Match Stats & Probabilities")

API_KEY = "SUA_API_KEY_AQUI"
API_URL = "https://api.example.com/matches"

@st.cache_data(ttl=300)
def fetch_live_data():
    try:
        response = requests.get(API_URL, headers={"x-api-key": API_KEY})
        if response.status_code == 200:
            return response.json()
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
