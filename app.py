import streamlit as st
st.set_page_config(page_title = "About Me", page_icon = '🫡', layout= 'centered')
st.title("HEMARAJ DM")
st.caption("FOCUSE ON CARRIER ")
try:
  client = Groq(api_key = st.secrets["GROQ_API_KEY"])
except (KeyError, FileNorFound):
                st.error("API Key is missing . Add it in Advance setting")
                st.stop()
role = st.selectbox("JOB TITLE", ['software engineer','senior software engineer', 'data analyst','prompt engineer', 'Devops engineer', 'other'])
if role == "other":
  st.text_input("Enter your job title ","XXXXXXX")
role = st.selectbox("model", ['openai/gpt-oss-safeguard-20b', 'openai/gpt-oss-120b'])
role = st.selectbox("difficult level", ['bigginer','intermidiate','advance'])
mode = st.radio('Activity', ['generate questions', 'generate code questions', 'evaluate answer','improve answers'])
if mode == 'generate questions':
  count = st.slider(1,10,5)
elif mode == 'generate code questions':
  topic = st.selectbox('Topics', ['SQL','AIML','Python','DSA','c++/c','Java','cyber security','ML'])
  count = st.slider("Number od question",1,10,5)
else:
  question = st.text_area('Enter interview question here ')
  answer = st.text_area('enter your answer ', height = 160)
