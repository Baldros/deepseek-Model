import ollama
from time import time

def chat_with_model(model_name="deepseek-r1:8b"):
    print("Chat iniciado. Digite 'exit' para sair.")
    
    # Initialize conversation history
    messages = []
    
    while True:
        try:
            # User input
            prompt = input("\nVocê: ")
            if prompt.lower() == 'exit':
                print("Encerrando chat...")
                break
            
            # Add user message to history
            messages.append({
                'role': 'user',
                'content': prompt
            })
            
            # Send message and measure response time
            start = time()
            response = ollama.chat(
                model=model_name,
                messages=messages  # Pass full conversation history
            )
            
            # Add assistant's response to history
            messages.append({
                'role': 'assistant',
                'content': response['message']['content']
            })
            
            # Show formatted response
            print("\nModelo:", response['message']['content'])
            print(f"Tempo de resposta: {time() - start:.2f}s")
            
        except KeyboardInterrupt:
            print("\nChat interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    chat_with_model()