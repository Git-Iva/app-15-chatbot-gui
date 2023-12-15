from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, \
     QPushButton
import sys


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 500)

        # All widgets added to main window through self argument

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Add input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)

        # Add the button
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.setGeometry(500, 340, 100, 40)

        # Show is a method of QMainWindow
        # Needs to be used when not using setCentralWidget
        self.show()


class Chatbot:
    pass


chatbot_app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(chatbot_app.exec())
