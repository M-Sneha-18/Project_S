import tkinter as tk
import random
from tkinter import messagebox

secret = random.randint(1, 100)
attempts = 0

def guess():
    global attempts, secret
    try:
        num = int(entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter an integer between 1 and 100.")
        return
    attempts += 1
    if num == secret:
        result.config(text=f"Correct! The number was {secret}. Attempts: {attempts}")
        secret = random.randint(1, 100)
        attempts = 0
    elif num < secret:
        result.config(text="Too low. Try again.")
    else:
        result.config(text="Too high. Try again.")

def new_game():
    global secret, attempts
    secret = random.randint(1, 100)
    attempts = 0
    result.config(text="New game started. Guess the number (1-100).")

root = tk.Tk()
root.title("Guessing Game")
root.geometry("480x220")

tk.Label(root, text="Guess a number (1-100):", font=("Times New Roman", 14)).pack(pady=10)
entry = tk.Entry(root, font=("Times New Roman", 14), width=12)
entry.pack()

tk.Button(root, text="Guess", command=guess, font=("Times New Roman", 14)).pack(pady=8)
tk.Button(root, text="New Game", command=new_game, font=("Times New Roman", 12)).pack()

result = tk.Label(root, text="Good luck!", font=("Times New Roman", 14))
result.pack(pady=12)

root.mainloop()
