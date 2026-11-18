import streamlit as st
from groq import Groq
from streamlit.errors import StreamlitSecretNotFoundError

st.set_page_config(page_title="Placement Practice", layout="centered")

st.title("AI Placement Assistant")
st.caption("Practice and prepare for your interviews")

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])

except (KeyError, StreamlitSecretNotFoundError):
    st.error("API key is missing")
    st.stop()
