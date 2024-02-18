import tkinter as tk
from tkinter import ttk, messagebox
import random


def user_choice(choice):
    determine_winner(choice)

# Function to determine the winner
def determine_winner(user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    result_text = f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n\n"
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You win yayayyy!"
    else:
        result = "You lose 😹 😹 😹 😹 😹 😹 😹 😹 😹 😹 😹 😹 !"
    
    messagebox.showinfo("Result", result_text + result)


##the window where we actually play the game
def setup_window():
    window = tk.Tk()
    window.title("Rock,Paper,Scissors :) ")
    # Buttons for user to make their choice
    ttk.Button(window, text="Rock", command=lambda: user_choice("rock")).pack(side=tk.LEFT, padx=5, pady=5)
    ttk.Button(window, text="Paper", command=lambda: user_choice("paper")).pack(side=tk.LEFT, padx=5, pady=5)
    ttk.Button(window, text="Scissors", command=lambda: user_choice("scissors")).pack(side=tk.LEFT, padx=5, pady=5)
    return window



# Main
def run_game():
    window = setup_window()
    window.mainloop()

if __name__ == "__main__":
    run_game()