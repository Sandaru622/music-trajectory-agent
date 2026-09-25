from turtle import st

from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI

load_dotenv()

openrouter_api_key = st.secrets.get("OPENROUTER_API_KEY") or os.getenv("OPENROUTER_API_KEY")

openrouter_llm = ChatOpenAI(
    model="google/gemma-4-26b-a4b-it:free",
    api_key=openrouter_api_key,
    base_url="https://openrouter.ai/api/v1",
    temperature=0.3
)