from ollama import chat
from ollama import ChatResponse

# accept user input and generate a response until 'exit' is typed
def main():
    print("Welcome to the Ollama Chat! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Exiting chat. Goodbye!")
            break

        response: ChatResponse = chat(model="gpt-oss:120b-cloud", messages=[{"role": "user", "content": user_input}])
        print(f"Ollama: {response.message.content}")

if __name__ == "__main__":
    main()  