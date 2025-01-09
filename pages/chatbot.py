from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from components.sidebar import sidebar
import streamlit as st

sidebar()


st.title("LangChain + LLama 3.1 Financial Assistant 🚀")

template = """Question: {question}

Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.1")

chain = prompt | model


question = st.chat_input("Ask me anything about finance, economics, or business!")

if question: 
    st.write(chain.invoke({"question": question}))