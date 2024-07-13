import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        # Label and instructions
        self.label = tk.Label(root, text="Choose your move:")
        self.label.pack(pady=10)

        # Buttons for rock, paper, and scissors
        self.rock_button = tk.Button(root, text="Rock", width=10, command=lambda: self.handle_click("rock"))
        self.rock_button.pack(pady=5)

        self.paper_button = tk.Button(root, text="Paper", width=10, command=lambda: self.handle_click("paper"))
        self.paper_button.pack(pady=5)

        self.scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: self.handle_click("scissors"))
        self.scissors_button.pack(pady=5)

        # Labels for displaying scores and result
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(root, text=f"Your Score: {self.user_score}   Computer Score: {self.computer_score}")
        self.score_label.pack()

        # Button to play again
        self.play_again_button = tk.Button(root, text="Play Again", command=self.play_again)
        self.play_again_button.pack(pady=10)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "You lose!"

    def play_game(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        result = self.determine_winner(user_choice, computer_choice)

        # Update result label
        self.result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n\n{result}")

        # Update score label
        self.score_label.config(text=f"Your Score: {self.user_score}   Computer Score: {self.computer_score}")

    def handle_click(self, choice):
        self.play_game(choice)

    def play_again(self):
        # Reset scores
        self.user_score = 0
        self.computer_score = 0

        # Reset labels
        self.result_label.config(text="")
        self.score_label.config(text=f"Your Score: {self.user_score}   Computer Score: {self.computer_score}")

# Create the main window
root = tk.Tk()

# Create an instance of the game
game = RockPaperScissorsGame(root)

# Run the main event loop
root.mainloop()
