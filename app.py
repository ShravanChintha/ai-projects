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
def ensure_history():
    if "history" not in st.session_state:
        st.session_state.history = []

ensure_history()

st.set_page_config(page_title="Ollama Streamlit Chat", layout="centered")
st.title("My RAG Chatbot")
st.write("A simple Streamlit interface to chat with an Ollama model.")

model = st.sidebar.text_input("Model", value="gpt-oss:120b-cloud")

with st.form(key="message_form", clear_on_submit=True):
    user_input = st.text_input("You:")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    st.session_state.history.append(("user", user_input))
    with st.spinner("Generating response..."):
        try:
            response: ChatResponse = chat(model=model, messages=[{"role": "user", "content": user_input}])
            bot_text = getattr(response, "message", None)
            if bot_text and hasattr(bot_text, "content"):
                bot_content = bot_text.content
            else:
                bot_content = str(response)
            st.session_state.history.append(("bot", bot_content))
        except Exception as e:
            st.session_state.history.append(("bot", f"Error: {e}"))

# Display chat history
for role, text in st.session_state.history:
    if role == "user":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**Ollama:** {text}")

