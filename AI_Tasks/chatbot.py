import random

def simple_chatbot():
    responses = {
        "hello": "Hi there! How can I help you today?",
        "how are you": "I'm just a bot, but I'm doing fine! How about you?",
        "bye": "Goodbye! Have a great day!",
        "help": "I can respond to simple greetings and questions. Try saying 'hello' or 'bye'."
    }
    
    print("Chatbot: Hello! Type something to start chatting. Type 'exit' to end.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = responses.get(user_input, "I'm not sure I understand that.")
        print(f"Chatbot: {response}")

# simple_chatbot()
