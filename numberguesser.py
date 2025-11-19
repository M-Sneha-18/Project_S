import tkinter as tk
import random
from tkinter import messagebox

game = {"low":1, "high":100, "secret":random.randint(1,100), "attempts":0}

def start_game():
    try:
        low = int(low_entry.get())
        high = int(high_entry.get())
        if low >= high:
            raise ValueError
    except ValueError:
        messagebox.showerror("Range error", "Enter valid integers with low < high.")
        return
    game["low"] = low
    game["high"] = high
    game["secret"] = random.randint(low, high)
    game["attempts"] = 0
    status.config(text=f"Game started: guess number between {low} and {high}.")

def guess():
    try:
        n = int(guess_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter an integer to guess.")
        return
    game["attempts"] += 1
    if n == game["secret"]:
        status.config(text=f"Correct! {n} in {game['attempts']} attempts.")
    elif n < game["secret"]:
        status.config(text="Too low.")
    else:
        status.config(text="Too high.")

root = tk.Tk()
root.title("Number Guesser (Custom Range)")
root.geometry("520x300")

tk.Label(root, text="Low:", font=("Times New Roman", 12)).pack(pady=4)
low_entry = tk.Entry(root, font=("Times New Roman", 12), width=10)
low_entry.pack()

tk.Label(root, text="High:", font=("Times New Roman", 12)).pack(pady=4)
high_entry = tk.Entry(root, font=("Times New Roman", 12), width=10)
high_entry.pack()

tk.Button(root, text="Start Game", command=start_game, font=("Times New Roman", 12)).pack(pady=8)

tk.Label(root, text="Your Guess:", font=("Times New Roman", 12)).pack(pady=6)
guess_entry = tk.Entry(root, font=("Times New Roman", 12), width=12)
guess_entry.pack()

tk.Button(root, text="Guess", command=guess, font=("Times New Roman", 12)).pack(pady=8)
status = tk.Label(root, text="Set range and start the game.", font=("Times New Roman", 13))
status.pack(pady=10)

root.mainloop()
