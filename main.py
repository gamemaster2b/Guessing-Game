import random
import sys

from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class GuessingGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # Create a label for displaying the instructions
        self.instructions_label = QLabel("Welcome to the guessing game! Enter your guess below:")

        # Create a line edit for getting the player's guess
        self.guess_edit = QLineEdit()

        # Create a button for submitting the guess
        self.guess_button = QPushButton("Guess")
        self.guess_button.clicked.connect(self.onGuessButtonClick)

        # Create a label for displaying the result of the guess
        self.result_label = QLabel()

        # Create a layout to hold the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.instructions_label)
        layout.addWidget(self.guess_edit)
        layout.addWidget(self.guess_button)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

    def onGuessButtonClick(self):
        # Get the player's guess
        guess = int(self.guess_edit.text())

        # Check if the guess is correct
        if guess == self.answer:
            self.result_label.setText(f"You got it in {self.guesses} guesses! The answer was {self.answer}.")
            self.guess_button.setEnabled(False)
        # Check if the guess is too high
        elif guess > self.answer:
            self.result_label.setText("Your guess is too high.")
        # The guess must be too low
        else:
            self.result_label.setText("Your guess is too low.")
        
        # Clear the line edit
        self.guess_edit.clear()

        # Increment the number of guesses
        self.guesses += 1

if __name__ == "__main__":
    # Create the application and the main window
    app = QApplication(sys.argv)
    window = GuessingGame()

    # Generate a random number between 1 and 100
    window.answer = random.randint(1, 100)

    # Keep track of the number of guesses the player has made
    window.guesses = 0

    # Show the main window
    window.show()

    # Run the application's event loop
    sys.exit(app.exec_())
