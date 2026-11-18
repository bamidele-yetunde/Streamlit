import streamlit as st

st.header('New Chat')

st.subheader("Where should we start?")

with st.container():
    prompt = st.chat_input("Ask Gemini")