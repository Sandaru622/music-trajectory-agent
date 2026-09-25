import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# Streamlit Secrets හෝ Environment Variable එකෙන් ගන්න
groq_api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")

# Key එක ලැබෙනවාදැයි පරීක්ෂා කිරීම (Key එකේ මුල් අකුරු කිහිපයක් පමණක් පෙන්වයි)
if not groq_api_key:
    st.error("❌ GROQ_API_KEY සොයාගත නොහැක! Streamlit Secrets පරීක්ෂා කරන්න.")
    st.stop()
else:
    print(f"Loaded Groq Key starting with: {groq_api_key[:6]}...")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=groq_api_key,
    temperature=0.3
)