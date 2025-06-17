# Simple Rule-Based Chatbot using Python

def chatbot():
    print("Hi! I'm ChatBot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()

        if user_input == 'bye':
            print("ChatBot: Goodbye! Have a great day!")
            break
        elif 'hello' in user_input or 'hi' in user_input:
            print("ChatBot: Hello! How can I help you?")
        elif 'how are you' in user_input:
            print("ChatBot: I'm a bot, but I'm doing great! Thanks for asking.")
        elif 'your name' in user_input:
            print("ChatBot: I'm a simple chatbot created with Python.")
        elif 'help' in user_input:
            print("ChatBot: Sure! I can help you with general questions.")
        else:
            print("ChatBot: Sorry, I didn't understand that.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
