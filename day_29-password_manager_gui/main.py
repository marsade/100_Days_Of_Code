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
pwd_entry = Entry(width=35)
pwd_entry.grid(row=3, column=1)

#Buttons
gen_btn = Button(text="Generate Password")
gen_btn.grid(row=3, column=2)
add_btn = Button(text="Add", width=36)
add_btn.grid(row=4, column=1)

window.mainloop()