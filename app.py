import streamlit as st
from components.sidebar import sidebar

sidebar()

st.markdown("""
# Documentation 📚

This Virtual Finance Assistant App is designed to simplify personal and business finance management through the power of an intelligent chatbot. This user-friendly app helps you track expenses, manage budgets, monitor savings goals, and gain valuable financial insights.
""")

st.image("assets/banner.png", width=600)

st.markdown(
"""
Key features include:

* Expense Tracking: Log daily transactions easily or connect your bank accounts for automated updates.
* Smart Budgeting: Set monthly limits, and the chatbot will provide real-time alerts and recommendations to keep you on track.
* Savings Guidance: Plan and achieve financial goals with personalized saving strategies.
* Investment Insights: Receive tailored advice on investments, market trends, and portfolio diversification.
* Bill Reminders: Never miss a payment with automated bill alerts and scheduling.
* Financial Education: Learn about finance through interactive sessions and personalized tips from the chatbot.
""")
