import ollama
import streamlit as st
from time import time


# Função para interagir com o modelo
def chat_with_model(messages, model_name="deepseek-r1:8b"):
    """
    Envia uma mensagem ao modelo e mantém o histórico da conversa.
    """
   
    # Send the full conversation history and measure response time
    start = time()
    response = ollama.chat(
        model=model_name,
        messages=messages  # Pass full conversation history
    )

    # Return formatted response and response time
    formatted_response = "\nModelo:", response['message']['content']
    timer = f"{time() - start:.2f}s"

    return formatted_response, timer
