import tkinter as tk

def convert_temperature():
    try:
        temp = float(entry.get())
        unit = unit_var.get()
        if unit == "Celsius":
            converted = (temp * 9/5) + 32
            result_label.config(text=f"{converted:.2f} °F")
        else:
            converted = (temp - 32) * 5/9
            result_label.config(text=f"{converted:.2f} °C")
    except ValueError:
        result_label.config(text="Invalid input. Enter a number.")

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")
window.geometry("320x230")
window.configure(bg="white")  # White background

# Define font and colors
custom_font = ("Times New Roman", 12)
bg_color = "white"
fg_color = "black"
entry_bg = "white"
button_bg = "black"
button_fg = "white"
active_bg = "#333333"

# Label: Enter Temperature
label = tk.Label(window, text="Enter Temperature:", font=custom_font, bg=bg_color, fg=fg_color)
label.pack(pady=5)

# Entry field
entry = tk.Entry(window, font=custom_font, bg=entry_bg, fg=fg_color, insertbackground=fg_color)
entry.pack(pady=5)

# Dropdown menu for unit selection
unit_var = tk.StringVar(window)
unit_var.set("Celsius")  # Default selection
unit_menu = tk.OptionMenu(window, unit_var, "Celsius", "Fahrenheit")
unit_menu.config(font=custom_font, bg=button_bg, fg=button_fg, highlightbackground=bg_color)
unit_menu["menu"].config(bg=button_bg, fg=button_fg)
unit_menu.pack(pady=5)

# Convert Button
convert_button = tk.Button(window, text="Convert", command=convert_temperature,
                           font=custom_font, bg=button_bg, fg=button_fg,
                           activebackground=active_bg, activeforeground=button_fg)
convert_button.pack(pady=10)

# Label to show result
result_label = tk.Label(window, text="", font=custom_font, bg=bg_color, fg=fg_color)
result_label.pack(pady=10)

# Run the GUI loop
window.mainloop()
