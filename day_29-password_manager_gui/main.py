#!/usr/bin/env python3
'''Password GUI App'''


from tkinter import *
from tkinter import messagebox
import pyperclip
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    pwd_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_inp = web_entry.get()
    mail_inp = mail_entry.get()
    pass_inp = pwd_entry.get()

    if web_inp == "" or pass_inp == "":
        messagebox.showwarning(title="Oops", message="Please do not leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=web_inp, message=f"These are the details entered: \nEmail: {mail_inp} \nPassword: {pass_inp} \nIs it okay to save?")

        if is_ok:    
            line = f"{web_inp} | {mail_inp} | {pass_inp}\n"

            with open("data.txt", "a") as f:
                f.write(line)

            web_entry.delete(0, END)
            # mail_entry.delete(0, END)
            pwd_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)
mail_label = Label(text="Email/Username:")
mail_label.grid(row=2, column=0)
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

#Entries
web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()
mail_entry = Entry(width=35)
mail_entry.grid(row=2, column=1, columnspan=2)
mail_entry.insert(0, "adenijifara@gmail.com")
pwd_entry = Entry(width=35)
pwd_entry.grid(row=3, column=1)

#Buttons
gen_btn = Button(text="Generate Password", command=generate_password)
gen_btn.grid(row=3, column=2)
add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1)

window.mainloop()