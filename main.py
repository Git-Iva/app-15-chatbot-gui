import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, \
     QPushButton
from backend import Chatbot
import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot = Chatbot()

        self.setMinimumSize(700, 500)

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Add input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)
        self.input_field.returnPressed.connect(self.send_message)

        # Add the button
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.setGeometry(500, 340, 100, 40)
        self.submit_button.clicked.connect(self.send_message)

        # Show is a method of QMainWindow
        # Needs to be used when not using setCentralWidget
        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#333333'>Me: {user_input}</p>")
        self.input_field.clear()

        # Get the bot response in a separate thread
        thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(
            f"<p style='color:#333333; background-color:#E9E9E9'>Bot:{response}</p>")


chatbot_app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(chatbot_app.exec())
