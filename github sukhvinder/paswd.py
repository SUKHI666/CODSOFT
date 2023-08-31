import tkinter as tk
import random
import string

root = tk.Tk()
root.geometry("800x400")
root.title("Password Generator")
root.configure(bg="#FFDAB9")

def generate_password():
    password_length = int(user_input.get())  
    if password_length <= 0:
        result_label.config(text="Invalid length")
        generated_password_text.delete("1.0", tk.END)
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(password_length))
        result_label.config(text="")
        generated_password_text.delete("1.0", tk.END)
        generated_password_text.insert(tk.END, password)

def exit_app():
    root.destroy()

password_label = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold italic"), bg="#FFDAB9")
password_label.pack()

user_label = tk.Label(root, text="Enter password length:", font=("Arial", 14), bg="#FFDAB9")
user_label.pack()

user_input = tk.Entry(root, font=("Arial", 14))
user_input.pack(pady=10)

generate_button = tk.Button(root, text="Generate Password", font=("Arial", 14), command=generate_password)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#FFDAB9")
result_label.pack()

generated_password_text = tk.Text(root, font=("Arial", 14), height=1, wrap=tk.WORD)
generated_password_text.pack(pady=10)

cancel_button = tk.Button(root, text="Cancel", font=("Arial", 14), command=exit_app)
cancel_button.pack()

lbl = tk.Label(root, text="Made By Sukhvinder Singh", font=("Arial", 15, "bold italic"), bg="#FFDAB9").pack(side="top")

root.mainloop()
