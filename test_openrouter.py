from utils.openrouter_llm import openrouter_llm

response = openrouter_llm.invoke("Say Hello")

print(response.content)