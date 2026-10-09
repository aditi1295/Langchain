from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
import streamlit as st

model=ChatOpenAI(models="gpt-4")
load_dotenv()

st.header('Research Tool')

user_input=st.text_input("Enter your Prompt")

if st.button("Summarize"):
    result=model.invoke(user_input)
    st.write(result.content)
    