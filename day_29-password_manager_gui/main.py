#!/usr/bin/env python3
'''Password GUI App'''


from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
web_label = Label(text="Website:").grid(row=1, column=0)
mail_label = Label(text="Email/Username:").grid(row=2, column=0)
pass_label = Label(text="Password:").grid(row=3, column=0)

#Entries
web_entry = Entry(width=35).grid(row=1, column=1, columnspan=2)
mail_entry = Entry(width=35).grid(row=2, column=1, columnspan=2)
pwd_entry = Entry(width=20).grid(row=3, column=1)

#Buttons
gen_btn = Button(text="Generate Password").grid(row=3, column=2)
add_btn = Button(text="Add", width=36).grid(row=4, column=1)

window.mainloop()