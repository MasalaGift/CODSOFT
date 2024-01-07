#Developed by: Ratshili Masala Gift
#Task Name: Rock Paper & Scissors APP
#Company: CodSoft Internship
#Status: Completed

import tkinter as tk
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")
        self.root.geometry("300x400")

        # User and computer choices
        self.user_choice = ""
        self.computer_choice = ""

        # Score tracking
        self.user_score = 0
        self.computer_score = 0

        # Labels
        self.label_instruction = tk.Label(root, text="Choose rock, paper, or scissors:", font=("Helvetica", 12))
        self.label_result = tk.Label(root, text="", font=("Helvetica", 12))
        self.label_score = tk.Label(root, text="Score: You - 0, Computer - 0", font=("Helvetica", 12))

        # Computer's choice label
        self.label_computer_choice = tk.Label(root, text="Computer's Choice: ", font=("Helvetica", 12))

        # Buttons
        self.button_rock = tk.Button(root, text="Rock", command=lambda: self.make_choice("rock"), font=("Helvetica", 12))
        self.button_paper = tk.Button(root, text="Paper", command=lambda: self.make_choice("paper"), font=("Helvetica", 12))
        self.button_scissors = tk.Button(root, text="Scissors", command=lambda: self.make_choice("scissors"), font=("Helvetica", 12))
        self.button_play_again = tk.Button(root, text="Play Again", command=self.reset_game, font=("Helvetica", 12))

        # Center all widgets
        self.label_instruction.pack(pady=(10, 5))

        # Center user choices horizontally
        self.button_rock.pack(side=tk.TOP)
        self.button_paper.pack(side=tk.TOP)
        self.button_scissors.pack(side=tk.TOP)

        self.label_computer_choice.pack(pady=10)
        self.label_result.pack(pady=10)
        self.label_score.pack(pady=10)
        self.button_play_again.pack(pady=10)

    def make_choice(self, choice):
        self.user_choice = choice
        self.computer_choice = random.choice(['rock', 'paper', 'scissors'])

        # Display the computer's choice
        self.label_computer_choice.config(text=f"Computer's Choice: {self.computer_choice.capitalize()}")

        result = self.determine_winner(self.user_choice, self.computer_choice)

        self.label_result.config(text=result)
        self.update_score()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'scissors' and computer_choice == 'paper') or
            (user_choice == 'paper' and computer_choice == 'rock')
        ):
            return "You win!"
        else:
            return "You lose!"

    def update_score(self):
        if "win" in self.label_result.cget("text"):
            self.user_score += 1
        elif "lose" in self.label_result.cget("text"):
            self.computer_score += 1

        self.label_score.config(text=f"Score: You - {self.user_score}, Computer - {self.computer_score}")

    def reset_game(self):
        self.label_computer_choice.config(text="Computer's Choice: ")
        self.label_result.config(text="")
        self.button_rock.config(state=tk.NORMAL)
        self.button_paper.config(state=tk.NORMAL)
        self.button_scissors.config(state=tk.NORMAL)

def main():
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
