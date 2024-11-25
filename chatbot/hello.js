function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    addMessage('You', userInput);
    
    const response = getResponse(userInput);
    addMessage('Chatbot', response);
    
    document.getElementById('user-input').value = '';
}

function addMessage(sender, message) {
    const chatContainer = document.getElementById('chat-container');
    const messageElement = document.createElement('div');
    messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatContainer.appendChild(messageElement);
}

function getResponse(userInput) {
    function getResponse(userInput) {
        userInput = userInput.toLowerCase();
    
        if (userInput.includes('hello') || userInput.includes('hi')) {
            return "Hello! Welcome to the Ice Cream Shop. How can I help you today?";
        } else if (userInput.includes('flavors')) {
            return "We have vanilla, chocolate, strawberry, and mint. Which one would you like?";
        } else if (userInput.includes('vanilla')) {
            return "Vanilla is a classic choice! How many scoops would you like?";
        } else if (userInput.includes('chocolate')) {
            return "Chocolate is a great choice! How many scoops would you like?";
        } else if (userInput.includes('strawberry')) {
            return "Strawberry is delicious! How many scoops would you like?";
        } else if (userInput.includes('mint')) {
            return "Mint is refreshing! How many scoops would you like?";
        } else if (userInput.includes('scoops') || userInput.includes('scoop')) {
            return "Got it! Your order will be ready soon. Anything else I can help you with?";
        } else if (userInput.includes('bye') || userInput.includes('exit')) {
            return "Goodbye! Have a sweet day!";
        } else {
            return "I'm sorry, I don't understand that. Could you please rephrase or ask about flavors?";
        }
    }
}

function chat() {
    addMessage('Chatbot', 'Hello! Welcome to the Ice Cream Shop. Type "exit" to end the chat.');
}

chat();