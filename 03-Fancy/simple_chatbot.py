# A very basic AI-like chatbot using rule-based responses

responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there!",
    "how are you": "I'm just a bunch of Python code, but I'm doing great!",
    "bye": "Goodbye! Have a great day!",
}

print("Chatbot: Hi! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower().strip()
    if user_input in responses:
        print("Chatbot:", responses[user_input])
        if user_input == "bye":
            break
    else:
        print("Chatbot: I don't understand that, but I'm learning!")
