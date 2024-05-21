import tkinter as tk
from tkinter import messagebox
import string
import random


def generate_password():
    length = length_var.get()
    if not length.isdigit() or int(length) <= 0:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number for length.")
        return
    
    length = int(length)
    
    use_lowercase = lowercase_var.get()
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()
    
    
    character_pool = ''
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation
    
    
    if not character_pool:
        messagebox.showerror("Invalid Selection", "At least one character type must be selected.")
        return
    
    
    password = ''.join(random.choice(character_pool) for _ in range(length))
    password_var.set(password)


app = tk.Tk()
app.title("Password Generator")


length_var = tk.StringVar()
lowercase_var = tk.BooleanVar(value=True)
uppercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)
password_var = tk.StringVar()


tk.Label(app, text="Password Length:").grid(row=0, column=0, sticky="w")
tk.Entry(app, textvariable=length_var).grid(row=0, column=1)

tk.Checkbutton(app, text="Include lowercase letters", variable=lowercase_var).grid(row=1, column=0, columnspan=2, sticky="w")
tk.Checkbutton(app, text="Include uppercase letters", variable=uppercase_var).grid(row=2, column=0, columnspan=2, sticky="w")
tk.Checkbutton(app, text="Include digits", variable=digits_var).grid(row=3, column=0, columnspan=2, sticky="w")
tk.Checkbutton(app, text="Include special characters", variable=special_var).grid(row=4, column=0, columnspan=2, sticky="w")

tk.Button(app, text="Generate Password", command=generate_password).grid(row=5, column=0, columnspan=2)

tk.Label(app, text="Generated Password:").grid(row=6, column=0, sticky="w")
tk.Entry(app, textvariable=password_var, state="readonly").grid(row=6, column=1)


app.mainloop()
