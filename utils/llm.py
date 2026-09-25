import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# Streamlit Secrets හෝ Local .env එකෙන් API Key එක ගැනීම
groq_api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")

# API Key එක නැත්නම් App එක නවතා Error එකක් පෙන්වීම
if not groq_api_key:
    st.error("❌ GROQ_API_KEY සොයා ගැනීමට නොහැකි විය! Streamlit Cloud හි Secrets පරීක්ෂා කරන්න.")
    st.stop()

# Groq LLM Initialization
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=groq_api_key,
    temperature=0.3
)