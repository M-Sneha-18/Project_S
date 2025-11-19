import tkinter as tk
from tkinter import messagebox
import re

# Function to check for palindrome
def check_palindrome():
    text = entry.get()
    cleaned = re.sub(r'[^a-z0-9]', '', text.lower())
    if cleaned == cleaned[::-1]:
        messagebox.showinfo("Result", "✅ It's a palindrome!")
    else:
        messagebox.showerror("Result", "❌ It's not a palindrome.")

# Set up GUI window
root = tk.Tk()
root.title("Palindrome Checker")
root.geometry("400x200")
root.configure(bg="#fdf5e6")  # light cream background

font_style = ("Times New Roman", 14)

# Label
label = tk.Label(root, text="Enter a word or phrase:", font=font_style, bg="#fdf5e6")
label.pack(pady=10)

# Entry
entry = tk.Entry(root, font=font_style, width=30)
entry.pack(pady=5)

# Button
check_button = tk.Button(root, text="Check", command=check_palindrome, font=font_style, bg="white")
check_button.pack(pady=20)

# Run the GUI
root.mainloop()
