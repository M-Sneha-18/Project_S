import tkinter as tk
from tkinter import filedialog, messagebox
import os

def choose_dir():
    path = filedialog.askdirectory()
    if path:
        dir_entry.delete(0, tk.END)
        dir_entry.insert(0, path)

def rename_files():
    folder = dir_entry.get().strip()
    prefix = prefix_entry.get().strip()
    if not folder or not os.path.isdir(folder):
        messagebox.showerror("Error", "Choose a valid folder.")
        return
    try:
        files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        for idx, fname in enumerate(files, start=1):
            ext = os.path.splitext(fname)[1]
            new_name = f"{prefix}_{idx}{ext}"
            os.rename(os.path.join(folder, fname), os.path.join(folder, new_name))
        messagebox.showinfo("Done", f"Renamed {len(files)} files.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Automation: Batch Rename")
root.geometry("700x220")

tk.Label(root, text="Folder:", font=("Times New Roman", 14)).pack(pady=6)
dir_entry = tk.Entry(root, font=("Times New Roman", 14), width=60)
dir_entry.pack(pady=4)
tk.Button(root, text="Browse", command=choose_dir, font=("Times New Roman", 12)).pack(pady=6)

tk.Label(root, text="Prefix for files:", font=("Times New Roman", 14)).pack(pady=6)
prefix_entry = tk.Entry(root, font=("Times New Roman", 14), width=30)
prefix_entry.pack()

tk.Button(root, text="Rename Files", command=rename_files, font=("Times New Roman", 14), pady=6).pack(pady=12)

root.mainloop()
