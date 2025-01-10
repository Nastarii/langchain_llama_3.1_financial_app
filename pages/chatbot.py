from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from components.sidebar import sidebar
import streamlit as st
import pandas as pd

# Sidebar setup
sidebar()

# Page title
st.title("LangChain + LLama 3.1 Financial Assistant 🚀")

# Persistent state to check if the user has already provided information
if "user_info" not in st.session_state:
    st.session_state["user_info"] = None

# Initialize session state
if "chat_data" not in st.session_state:
    st.session_state["chat_data"] = []
    
# Popup for first-time users to gather input
if st.session_state["user_info"] is None:
    with st.form("user_info_form", clear_on_submit=True):
        st.subheader("Welcome to the Financial Assistant!")
        st.write("To better assist you, please share some details about your goals and financial situation.")
        
        # User input fields
        financial_goals = st.text_input("What are your financial goals?", placeholder="E.g., Save for retirement, pay off debt")
        objectives = st.text_input("What are your objectives in using this assistant?", placeholder="E.g., Learn to invest, budget better")
        current_condition = st.text_area("Describe your current financial condition", placeholder="E.g., Monthly income, expenses, debts")
        
        # Submit button
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state["user_info"] = {
                "goals": financial_goals,
                "objectives": objectives,
                "condition": current_condition,
            }
            st.success("Thank you! Your information has been saved.")

# Load user information into the prompt
user_info = st.session_state["user_info"]
if user_info:
    template = f"""
    You are a financial assistant tailored to the user's needs.
    The user has shared the following details:
    
    - Financial Goals: {user_info['goals']}
    - Objectives: {user_info['objectives']}
    - Current Financial Condition: {user_info['condition']}
    
    Respond only to questions related to finance, economics, or business. If a question is unrelated, reply: 'I only answer financial questions.'

    Question: {{question}}

    Answer: Let's think step by step.
    """
else:
    template = """
    You are a financial assistant specialized in finance. 
    Respond only to questions about finance, economics, or business. 
    If a question is unrelated, reply: 'I only answer financial questions.'

    Question: {question}

    Answer: Let's think step by step.
    """

# Create the prompt
prompt = ChatPromptTemplate.from_template(template)

# Initialize the Llama 3.1 model
model = OllamaLLM(model="llama3.1")

# Chain the prompt and model together
chain = prompt | model

# User chat input
question = st.chat_input("Ask me anything about finance, economics, or business!")

# Process and display the response
if question:
    response = chain.invoke({"question": question})

    # Save question and response
    st.session_state["chat_data"].append({"Question": question, "Response": response})

# Convert chat data to a dataframe
chat_df = pd.DataFrame(st.session_state["chat_data"])
chat_df.to_csv("assets/chat_history.csv", index=False)

st.subheader("Chat History")
if not chat_df.empty:
    for index, row in chat_df.iterrows():
        st.write(row['Question'])
        message = st.chat_message("assistant")
        message.write(row['Response'])
        st.divider()  # Optional, to add a visual separator between interactions