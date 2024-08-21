import streamlit as st

import google.generativeai as genai

st.title=("Welcome to gemini")
genai.configure(api_key="AIzaSyAR-2Ub5LK1w5cC4qpntEHvtETRmxA8c58")
text = st.text_input("Enter your question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("Click me"):
        response = chat.send_message(text)
        st.write(response.text)
