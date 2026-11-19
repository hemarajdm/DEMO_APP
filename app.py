import streamlit as st
# Page configuration
st.set_page_config(
    page_title="LLM",
    layout="centered"
)
# Application title
st.title("AI Interview")
st.caption("Practice and Prepare for your placement")
# Import Groq safely
try:
    from groq import Groq
except ImportError:
    st.error("Groq package is not installed.")
    st.info("Add groq to your requirements.txt file and redeploy.")
    st.stop()
# API configuration
try:
    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )
except (KeyError, FileNotFoundError):
    st.error("API key is missing. Add it in Streamlit Secrets.")
    st.stop()
# Success message
st.success("Groq API connected successfully!")

st.write("Welcome to your AI Interview Assistant.")
role =st.selectbox("Job Title", ["Machine Learning Engineer", "Senior Software Engineering","data analysis","cyber security","software develovper","Others"])

if role =="Others":
    st.text_input("Enter your Job Title","XXXXXX")
model = st.selectbox(
    "choose your model",
[
"openai/gpt-oss-120b"
"openai/gpt-oss-20b"
]
)
level = st.selectbox(
    "choose your level",
    [
        "begginer","intermideate","advanced"
    ]
)
mode= st.radio("Activity",["Generate Questions","Generate Code Questions","Evaluate Answers","Improve answers"])
if mode =="Generate Question" :
    count = st.slider("Number Of Questions",1,10,5)
elif mode =="Generate code Questions" :
    topic = st.selectbox( "Select Topic",
                         [ "Python", "C++", "C", "DSA", "Aptitude","Java"])
    count= st.slider("Number of Questions",1,10,5)
else:
    question = st.text_area("Enter Interview Question Here")
    answer = st.text_area("Enter Your Answer", height=160)
    
    if st.button("Generate AI Response",type = "primary"):
        if mode == ["Evaluate Answer","Improve Answer"] and (not question.strip()):
       st.warning("please enter a valid Question and Answer")
        st.stop()
