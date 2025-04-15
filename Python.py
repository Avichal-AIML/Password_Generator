import tkinter as tk
from tkinter import messagebox, ttk
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Password Generator")
        self.root.geometry("500x450")
        self.root.configure(bg="#f0f4f7")
        self.root.resizable(False, False)

        # Variables
        self.length_var = tk.IntVar(value=12)
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_lowercase = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_symbols = tk.BooleanVar(value=True)
        self.exclude_chars = tk.StringVar(value="")

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="🔐 Advanced Password Generator", font=("Helvetica", 16, "bold"), bg="#f0f4f7")
        title.pack(pady=15)

        frame = tk.Frame(self.root, bg="#ffffff", bd=2, relief="groove", padx=15, pady=15)
        frame.pack(padx=20, pady=10, fill="x")

        ttk.Label(frame, text="Password Length:").grid(row=0, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.length_var, width=5).grid(row=0, column=1, sticky="w")

        ttk.Checkbutton(frame, text="Include Uppercase (A-Z)", variable=self.include_uppercase).grid(row=1, column=0, columnspan=2, sticky="w", pady=2)
        ttk.Checkbutton(frame, text="Include Lowercase (a-z)", variable=self.include_lowercase).grid(row=2, column=0, columnspan=2, sticky="w", pady=2)
        ttk.Checkbutton(frame, text="Include Digits (0-9)", variable=self.include_digits).grid(row=3, column=0, columnspan=2, sticky="w", pady=2)
        ttk.Checkbutton(frame, text="Include Symbols (!@#$...)", variable=self.include_symbols).grid(row=4, column=0, columnspan=2, sticky="w", pady=2)

        ttk.Label(frame, text="Exclude Characters:").grid(row=5, column=0, sticky="w", pady=5)
        ttk.Entry(frame, textvariable=self.exclude_chars, width=30).grid(row=5, column=1, sticky="w", pady=5)

        ttk.Button(self.root, text="Generate Password", command=self.generate_password).pack(pady=10)

        self.result_entry = tk.Entry(self.root, font=("Helvetica", 14), justify='center', bd=2, relief="solid", width=30)
        self.result_entry.pack(pady=10)

        ttk.Button(self.root, text="📋 Copy to Clipboard", command=self.copy_to_clipboard).pack()

    def generate_password(self):
        length = self.length_var.get()
        exclude = set(self.exclude_chars.get())
        char_pool = ""

        if self.include_uppercase.get():
            char_pool += string.ascii_uppercase
        if self.include_lowercase.get():
            char_pool += string.ascii_lowercase
        if self.include_digits.get():
            char_pool += string.digits
        if self.include_symbols.get():
            char_pool += string.punctuation

        char_pool = ''.join(c for c in char_pool if c not in exclude)

        if not char_pool:
            messagebox.showerror("Error", "No characters available for password.")
            return

        password = ''.join(random.choice(char_pool) for _ in range(length))
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, password)

    def copy_to_clipboard(self):
        password = self.result_entry.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
