from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI

load_dotenv()

openrouter_llm = ChatOpenAI(
    model="google/gemma-4-26b-a4b-it:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    temperature=0.3
)