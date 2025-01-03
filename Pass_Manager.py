import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store passwords
PASSWORD_FILE = "passwords.json"

# Load existing passwords
def load_passwords():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            return json.load(file)
    return {}

# Save passwords to file
def save_passwords(passwords):
    with open(PASSWORD_FILE, "w") as file:
        json.dump(passwords, file, indent=4)

# Add a password
def add_password():
    platform = platform_entry.get().strip()
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not platform or not username or not password:
        messagebox.showerror("Error", "All fields are required!")
        return

    passwords[platform] = {"username": username, "password": password}
    save_passwords(passwords)
    platform_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Password saved successfully!")

# Search for a password
def search_password():
    platform = platform_entry.get().strip()
    if platform in passwords:
        username = passwords[platform]["username"]
        password = passwords[platform]["password"]
        messagebox.showinfo(
            "Password Found",
            f"Platform: {platform}\nUsername: {username}\nPassword: {password}",
        )
    else:
        messagebox.showerror("Error", "No password found for this platform.")

# UI setup
passwords = load_passwords()

root = tk.Tk()
root.title("Password Manager")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="white")  # Set the background color

# Labels
tk.Label(root, text="Platform:", bg="white", font=("Arial", 10, "bold")).pack(pady=5)
platform_entry = tk.Entry(root, width=40, bg="white", fg="black")
platform_entry.pack()

tk.Label(root, text="Username:", bg="white", font=("Arial", 10, "bold")).pack(pady=5)
username_entry = tk.Entry(root, width=40, bg="white", fg="black")
username_entry.pack()

tk.Label(root, text="Password:", bg="white", font=("Arial", 10, "bold")).pack(pady=5)
password_entry = tk.Entry(root, width=40, bg="white", fg="black")
password_entry.pack()

# Buttons
tk.Button(root, text="Add Password", command=add_password, bg="#4CAF50", fg="white", width=20).pack(pady=10)
tk.Button(root, text="Search Password", command=search_password, bg="#2196F3", fg="white", width=20).pack(pady=10)

# Run the application
root.mainloop()
