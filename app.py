import streamlit as st
from ollama import chat
from ollama import ChatResponse

st.title("My RAG Chatbot")
st.write("Welcome to the Ollama Chat! Type your message below and press Enter to chat.")
st.button("Send")
user_input = st.text_input("You:", "")
with st.spinner("Generating response..."):
    if user_input:
        response: ChatResponse = chat(model="gpt-oss:120b-cloud", messages=[{"role": "user", "content": user_input}])
        st.write(f"Ollama: {response.message.content}")

