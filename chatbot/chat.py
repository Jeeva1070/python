def get_response(user_input):
    user_input = user_input.lower()
    
    if 'hello' in user_input or 'hi' in user_input:
        return "Hello! Welcome to the Ice Cream Shop. How can I help you today?"
    elif 'flavors' in user_input:
        return "We have vanilla, chocolate, strawberry, and mint. Which one would you like?"
    elif 'vanilla' in user_input:
        return "Vanilla is a classic choice! How many scoops would you like?"
    elif 'chocolate' in user_input:
        return "Chocolate is a great choice! How many scoops would you like?"
    elif 'strawberry' in user_input:
        return "Strawberry is delicious! How many scoops would you like?"
    elif 'mint' in user_input:
        return "Mint is refreshing! How many scoops would you like?"
    elif 'scoops' in user_input or 'scoop' in user_input:
        return "Got it! Your order will be ready soon. Anything else I can help you with?"
    elif 'bye' in user_input or 'exit' in user_input:
        return "Goodbye! Have a sweet day!"
    else:
        return "I'm sorry, I don't understand that. Could you please rephrase or ask about flavors?"

def chat():
    print("Chatbot: Hello! Welcome to the Ice Cream Shop. Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a sweet day!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")
_name_ = "_main_"
if _name_ == "_main_":
    chat()