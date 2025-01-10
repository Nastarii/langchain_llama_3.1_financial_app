import streamlit as st

def sidebar():

    with open("LICENSE", "r") as file:
        license_content = file.read()
        license_content = license_content.split("Permission")[0]

    st.sidebar.title("Navigation")

    with st.sidebar:
        st.page_link("app.py", label="Home", icon=":material/home:")
        st.page_link("pages/chatbot.py", label="Chatbot", icon=":material/support_agent:")
        st.page_link("pages/dashboard.py", label="Dashboard", icon=":material/dashboard:")
        st.divider()
        st.title("License")
        st.text(license_content)
        st.divider()
        st.title("Contact Me")
        
        st.image("assets/qr-code-dynamic.png", width=120)
