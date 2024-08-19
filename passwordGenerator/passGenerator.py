# package importing
import random, string
import tkinter as tk
from tkinter import messagebox
import re

# creating widgets
root =tk.Tk()
tk.Label(root, text="Password Generator", font=("Arial", 20, "bold"), bg="pink").pack()
root.geometry("500x500")
root.title("Password Generator")
tk.Label(text="Enter length of password", font=("Arial", 10, "bold")).pack(padx=25, pady=10)
ent = tk.Entry(root, width=50, borderwidth=5, bg="grey")
ent.pack(pady=5, padx=5)

# password generator function
def passGen():
    if ent.get() == "":
        messagebox.showerror("Error", "Please enter length of password")
    else:
        try:
            length = int(ent.get())
            char = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
            password = ''.join(random.sample(char, length))
            ent.delete(0, tk.END)
            ent.insert(0, password)
        except ValueError:
            messagebox.showerror("Error", "Password length must be a number")

gen_btn = tk.Button(root, text="Generate Password", command=passGen, bg="green")
gen_btn.pack(pady=10, padx=10)

# password checking function
#also generate color meter according to password strenght
def checkPass():
    messagebox.askyesno("Check Password", "Do you want to check your password")
    chk = ent.get()
    if len(chk) < 6:
        canvas.config(bg="red")
        messagebox.showerror("Error", "Password too short")
        strength_lbl.config(text="Password Strength: poor")
    elif len(chk) > 8:
        canvas.config(bg="green")
        messagebox.showinfo("Success", "Password is valid")
        strength_lbl.config(text="Password Strength: very strong")
    else:
        canvas.config(bg="yellow")
        messagebox.showinfo("Success", "Password is valid")
        strength_lbl.config(text="Password Strength: good")


# buttons
chk_btn = tk.Button(root, text="Check Password", command=checkPass, bg="yellow")
chk_btn.pack(pady=10, padx=10)
destroy_btn = tk.Button(root, text="Exit screen", command=root.destroy, bg="red")
destroy_btn.pack(pady=10, padx=10)


strength_lbl = tk.Label(root, text="Password Strength: None",font=("Arial", 10, "bold"))
strength_lbl.pack()
canvas = tk.Canvas(root, width=50)
canvas.pack()

tk.mainloop()

