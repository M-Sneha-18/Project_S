import tkinter as tk
import re

def check_strength():
    pwd = entry.get()
    length = len(pwd) >= 8
    upper = re.search(r"[A-Z]", pwd) is not None
    lower = re.search(r"[a-z]", pwd) is not None
    digit = re.search(r"\d", pwd) is not None
    special = re.search(r"[^\w\s]", pwd) is not None

    score = sum([length, upper, lower, digit, special])
    if score == 5:
        status = "Very Strong"
        color = "green"
    elif score >= 3:
        status = "Moderate"
        color = "orange"
    else:
        status = "Weak"
        color = "red"
    result_label.config(text=f"Strength: {status} ({score}/5)", fg=color)
    details = f"Length>=8: {length}, Upper: {upper}, Lower: {lower}, Digit: {digit}, Special: {special}"
    details_label.config(text=details)

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("600x240")

tk.Label(root, text="Enter password:", font=("Times New Roman", 14)).pack(pady=10)
entry = tk.Entry(root, font=("Times New Roman", 14), width=36, show="*")
entry.pack()

tk.Button(root, text="Check", command=check_strength, font=("Times New Roman", 14)).pack(pady=12)
result_label = tk.Label(root, text="", font=("Times New Roman", 14))
result_label.pack()
details_label = tk.Label(root, text="", font=("Times New Roman", 12))
details_label.pack(pady=6)

root.mainloop()
