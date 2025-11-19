import tkinter as tk

def reverse_string():
    input_text = entry.get()
    reversed_text = input_text[::-1]
    result_label.config(text=f"Reversed: {reversed_text}")

# Create the main application window
window = tk.Tk()
window.title("String Reverser")
window.geometry("300x180")

# Set a font
custom_font = ("Times New Roman", 12)

# Input Label
label = tk.Label(window, text="Enter a string:", font=custom_font)
label.pack(pady=5)

# Entry box with default text "hello"
entry = tk.Entry(window, width=30, font=custom_font)
entry.insert(0, "hello")
entry.pack(pady=5)

# Button to reverse the string
reverse_button = tk.Button(window, text="Reverse", command=reverse_string, font=custom_font)
reverse_button.pack(pady=5)

# Label to show the result
result_label = tk.Label(window, text="Reversed:", font=custom_font)
result_label.pack(pady=5)

# Start the GUI loop
window.mainloop()
