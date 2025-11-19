import tkinter as tk
from tkinter import messagebox

# Function to update expression in the entry box
def press(key):
    expression.set(expression.get() + str(key))

# Function to clear the entry box
def clear():
    expression.set("")

# Function to evaluate the final expression
def equal():
    try:
        result = str(eval(expression.get()))
        expression.set(result)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero.")
        expression.set("")
    except Exception:
        messagebox.showerror("Error", "Invalid input.")
        expression.set("")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x450")
root.configure(bg="#ffe4e1")  # Pale pink background

# Global expression variable
expression = tk.StringVar()

# Entry widget to show current expression
entry = tk.Entry(root, textvariable=expression, font=("Times New Roman", 20), bg="white", bd=5, relief="flat", justify="right")
entry.pack(pady=20, padx=10, ipady=10, fill="x")

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '%', '=', '+']
]

# Function to create button widgets
button_frame = tk.Frame(root, bg="#ffe4e1")
button_frame.pack()

for row in buttons:
    row_frame = tk.Frame(button_frame, bg="#ffe4e1")
    row_frame.pack(pady=5)
    for char in row:
        if char == '=':
            btn = tk.Button(row_frame, text=char, font=("Times New Roman", 16), width=5, height=2, bg="white",
                            command=equal)
        else:
            btn = tk.Button(row_frame, text=char, font=("Times New Roman", 16), width=5, height=2, bg="white",
                            command=lambda ch=char: press(ch))
        btn.pack(side="left", padx=5)

# Clear button at the bottom
clear_btn = tk.Button(root, text="Clear", font=("Times New Roman", 14), bg="white", width=20, height=2, command=clear)
clear_btn.pack(pady=15)

# Run the app
root.mainloop()
