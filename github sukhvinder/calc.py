import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Calculator")
window.geometry("350x550")
window.configure(bg="#FFDAB9")

n1 = n2 = entry = 0

def operation():
    b1.pack_forget()
    global b3
    b3.place_forget()
    global n1, n2, entry
    
    l1 = tk.Label(window, text="Enter the 1st number :", font="normal 11 bold", fg="blue", bg="#FFDAB9")
    l1.pack(side=tk.TOP, pady=10)
    
    n1 = tk.Entry(window)
    n1.pack()
    
    l2 = tk.Label(window, text="Enter the 2nd number :", font="normal 11 bold", fg="blue", bg="#FFDAB9")
    l2.pack(side=tk.TOP, pady=10)
    
    n2 = tk.Entry(window)
    n2.pack()
    
    l3 = tk.Label(window, text="1 Addition", font="normal 11 bold", fg="black", bg="#FFDAB9")
    l3.pack(side=tk.TOP, pady=5)
    
    l4 = tk.Label(window, text="2 Subtraction", font="normal 11 bold", fg="black", bg="#FFDAB9")
    l4.pack(side=tk.TOP, pady=5)
    
    l5 = tk.Label(window, text="3 Multiplication", font="normal 11 bold", fg="black", bg="#FFDAB9")
    l5.pack(side=tk.TOP, pady=5)
    
    l6 = tk.Label(window, text="4 Division", font="normal 11 bold", fg="black", bg="#FFDAB9")
    l6.pack(side=tk.TOP, pady=5)

    l7 = tk.Label(window, text=": Enter the operation number :", font="normal 13 bold", fg="red", bg="#FFDAB9")
    l7.pack(side=tk.TOP, pady=5)
    
    entry = tk.Entry(window)
    entry.pack()
    
    b2 = tk.Button(window, text="Submit", font=5, width=8, command=check)
    b2.pack(side=tk.TOP, pady=5)
    
    b5 = tk.Button(window, text="Exit", font=5, width=5, command=window.destroy)
    b5.pack()

def check():
    entryy = float(entry.get())
    
    if entryy == 0 or entryy > 4:
        tk.messagebox.showwarning("Wrong choice", "Wrong choice. Incorrect choice!")
        window.destroy()
    elif entryy == 1:
         addition()
    elif entryy == 2:
         subtract()
    elif entryy == 3:
         multiply()
    elif entryy == 4:
         divide()

def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
        
def addition():
    a = float(n1.get())
    b = float(n2.get())
    
    if not (is_numeric(a) and is_numeric(b)):
        tk.messagebox.showwarning("Invalid Input", "Enter Numeric number only!")
        window.destroy()
    else:
        result_message.config(text="Result of Addition = " + str(a + b),font="normal 15 bold")

def subtract():
    a = float(n1.get())
    b = float(n2.get())
    
    if not (is_numeric(a) and is_numeric(b)):
        tk.messagebox.showwarning("Invalid Input", "Enter Numeric number only!")
        window.destroy()
    else:
        result_message.config(text="Result of Subtraction = " + str(a - b),font="normal 15 bold")

def multiply():
    a = float(n1.get())
    b = float(n2.get())
    
    if not (is_numeric(a) and is_numeric(b)):
        tk.messagebox.showwarning("Invalid Input", "Enter Numeric number only!")
        window.destroy()
    else:
        result_message.config(text="Result of Multiplication = " + str(a * b),font="normal 15 bold")

def divide():
    a = float(n1.get())
    b = float(n2.get())
    
    if not (is_numeric(a) and is_numeric(b)):
        tk.messagebox.showwarning("Invalid Input", "Enter Numeric number only!")
        window.destroy()
    else:
        if b == 0:
            result_message.config(text="Cannot divide by zero")
        else:
            result_message.config(text="Result of Division = " + str(a / b),font="normal 15 bold")

la = tk.Label(text="CALCULATOR", font="normal 20 bold", fg="blue", bg="#FFDAB9")
la.pack(side=tk.TOP, pady=20)

b1 = tk.Button(window, text="Start", font=8, width=10, bg="orange", command=operation)
b1.pack(side=tk.TOP, pady=150)

b3 = tk.Button(window, text="Exit", font=5, width=8, bg="orange", command=window.destroy)
b3.place(x=125, y=300)

result_message = tk.Label(window, text="", font=("normal", 9), bg="#FFDAB9")
result_message.pack()

laa = tk.Label(text="Made By Sukhvinder Singh", font="normal 15 bold", fg="BLACK", bg="#FFDAB9")
laa.pack(side=tk.TOP)

window.mainloop()
