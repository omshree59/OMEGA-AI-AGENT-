from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.1:8b",
    temperature=0
)

def ask(prompt: str):
    response = llm.invoke(prompt)
    return response.content