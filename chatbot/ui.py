import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton, QLabel, QSizePolicy
from PyQt5.QtGui import QTextCursor, QFont
from PyQt5.QtCore import Qt

class ChatbotWindow(QWidget):
    def __init__(self):  # Fix: __init__ instead of _init_
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Ice Cream Shop Chatbot')

        self.chat_history = QTextEdit()
        self.chat_history.setReadOnly(True)
        self.chat_history.setStyleSheet(
            'background-color: #f0f0f0; color: #333; font-size: 14px; padding: 10px; border: 1px solid #ccc;')
        self.chat_history.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.user_input = QLineEdit()
        self.user_input.setStyleSheet(
            'background-color: #fff; color: #333; font-size: 14px; padding: 10px; border: 1px solid #ccc;')
        self.user_input.setPlaceholderText('Type your message here...')
        self.user_input.returnPressed.connect(self.send_message)

        self.send_button = QPushButton('Send')
        self.send_button.setStyleSheet(
            'background-color: #4CAF50; color: white; font-size: 14px; padding: 10px; border: none;')
        self.send_button.clicked.connect(self.send_message)

        vbox = QVBoxLayout()
        vbox.addWidget(self.chat_history)
        vbox.addWidget(self.user_input)
        vbox.addWidget(self.send_button)

        self.setLayout(vbox)

        self.start_chat()

    def start_chat(self):
        self.chat_history.append('<b>Chatbot:</b> Hello! Welcome to the Ice Cream Shop. Type "exit" to end the chat.')
        self.chat_history.append('')

    def send_message(self):
        user_input = self.user_input.text()
        self.user_input.clear()

        self.chat_history.append('<b>You:</b> '+user_input)

        response = self.get_response(user_input.lower())
        self.chat_history.append('<b>Chatbot:</b> '+response)
        self.chat_history.append('')

    def get_response(self, user_input):
        if 'hello' in user_input or 'hi' in user_input:
            return "Hello! Welcome to the Ice Cream Shop. How can I help you today?"
        elif 'flavors' in user_input:
            return "We have vanilla, chocolate, strawberry, and mint. Which one would you like?"
        elif 'vanilla' in user_input:
            return "Vanilla is a classic choice! How many scoops would you like?"
        elif 'chocolate' in user_input:
            return "Chocolate is a great choice! How many scoops would you like?"
        elif 'trawberry' in user_input:
            return "Strawberry is delicious! How many scoops would you like?"
        elif 'int' in user_input:
            return "Mint is refreshing! How many scoops would you like?"
        elif 'coops' in user_input or 'coop' in user_input:
            return "Got it! Your order will be ready soon. Anything else I can help you with?"
        elif 'bye' in user_input or 'exit' in user_input:
            return "Goodbye! Have a sweet day!"
        else:
            return "I'm sorry, I don't understand that. Could you please rephrase or ask about flavors?"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChatbotWindow()
    window.show()
    sys.exit(app.exec_())