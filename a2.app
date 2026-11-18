import streamlit as st
from groq import groq
st.set_page_config(page_title="Placement pactice", layout = "centered")
st.title("AI Placement Assistant")
st.caption("Practice and prepare for your Interviews")
try:
client = Groq(api_key = st.secrets["GROQ_API_kEY"])
except (KeyError, FilrNotFound):
st.error("API key is missing")
st.stop()
