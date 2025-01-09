import streamlit as st

def sidebar():

    with open("LICENSE", "r") as file:
        license_content = file.read()
        license_content = license_content.split("Permission")[0]

    st.sidebar.title("Navigation")

    with st.sidebar:
        st.page_link("app.py", label="Home", icon=":material/home:")
        st.page_link("pages/Chatbot.py", label="Chatbot", icon=":material/support_agent:")
        st.divider()
        st.title("License")
        st.text(license_content)
    st.markdown("# Documentation 📚")