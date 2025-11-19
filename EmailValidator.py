import tkinter as tk
from tkinter import messagebox
from email_validator import validate_email, EmailNotValidError

# Function to validate the email
def check_email():
    email = entry.get()
    try:
        validate_email(email)
        messagebox.showinfo("Result", "✅ Valid Email Address")
    except EmailNotValidError as e:
        messagebox.showerror("Invalid", f"❌ Invalid Email Address\n\n{str(e)}")

# Set up the main window
root = tk.Tk()
root.title("Email Validator")
root.geometry("400x200")
root.resizable(False, False)

# Font settings
font_style = ("Times New Roman", 14)

# Label
label = tk.Label(root, text="Enter Email Address:", font=font_style)
label.pack(pady=10)

# Entry box
entry = tk.Entry(root, font=font_style, width=30)
entry.pack(pady=5)

# Validate button
validate_btn = tk.Button(root, text="Validate", command=check_email, font=font_style)
validate_btn.pack(pady=20)

# Run the application
root.mainloop()
