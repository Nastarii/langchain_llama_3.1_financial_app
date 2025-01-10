import streamlit as st
import pandas as pd
import plotly.express as px
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from components.sidebar import sidebar
import json
import os

sidebar()

if os.path.exists('assets/chat_history.csv'):
    df = pd.read_csv('assets/chat_history.csv')

    # Convert the DataFrame to a JSON-like string to pass to the LLM
    data_as_text = df.to_csv(index=False)  # Convert DataFrame to CSV string

    # LLM setup
    template = """
    You are a financial assistant and a Python expert. Based on the following dataset, create a financial dashboard.

    Dataset:
    {data}

    Instructions:
    1. Write Python code using libraries such as Pandas and Plotly to create meaningful financial charts.
    2. Provide up to three types of visualizations and explain their purpose.
    3. Return only the Python code for implementation in a Streamlit app.
    """
    prompt = ChatPromptTemplate.from_template(template)
    model = OllamaLLM(model="llama3.1")

    # Create the prompt with the data passed correctly
    formatted_prompt = template.format(data=data_as_text)

    # Pass the correctly formatted prompt to the model
    response = model.invoke(formatted_prompt)

    # Display the response
    st.subheader("Generated Dashboard Code")
    st.code(response, language="python")

    # Option to execute the generated code (use with caution)
    execute_code = st.checkbox("Run the generated code?")
    if execute_code:
        exec(response)
else:
    st.warning("No chat history available. Please chat with the bot to generate data for the dashboard.")
