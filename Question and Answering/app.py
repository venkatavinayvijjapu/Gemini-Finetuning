import streamlit as st 
from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as ai
os.getenv("GOOGLE_API_KEY")
ai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=ai.GenerativeModel("gemini-pro")
def res(que):
    res=model.generate_content(que)
    return res.text

st.set_page_config(page_title="QA")
st.header("GEMINI")
input=st.text_input("Input:",key="input")
submit=st.button("Ask")
if submit:
    res=res(input)
    st.write(res)