import os
import streamlit as st  
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI 

load_dotenv()


openrouter_api_key = st.secrets.get("OPENROUTER_API_KEY") or os.getenv("OPENROUTER_API_KEY")

openrouter_llm = ChatOpenAI(
    model_name="openai/gpt-3.5-turbo", 
    openai_api_key=openrouter_api_key,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.3
)