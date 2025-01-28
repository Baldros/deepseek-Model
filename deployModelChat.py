# Librarys
import streamlit as st
from deepseek import chat_with_model
from time import time

# Model name
model_name = "deepseek-r1:8b"  # They have better models, but this is light

# Streamlit App
def main():
    # App title
    st.title("Chatbot Deepseek")
    st.subheader("Converse com o modelo de forma interativa 🚀")

    # Initialize session state for messages and model's memory
    if "messages" not in st.session_state:
        st.session_state.messages = []  # User + assistant conversation history

    # Input box for user message
    with st.container():
        user_input = st.text_input("Digite sua mensagem:", key="user_input")
        if st.button("Enviar"):
            if user_input:
                # Add user message to session state
                st.session_state.messages.append({"role": "user", "content": user_input})

                # Get response from model
                response, timer = chat_with_model(st.session_state.messages, model_name)
                st.session_state.messages.append({"role": "assistant", "content": response[1]})

    # Display chat history
    st.divider()
    st.subheader("Histórico da conversa:")
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"**Você:** {message['content']}")
        else:
            st.markdown(f"**Modelo:** {message['content']}")
            st.write(f"Tempo de resposta: {timer}")

    st.divider()

if __name__ == "__main__":
    main()
