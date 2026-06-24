#!/usr/bin/env python3
BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50)

#Card Image
canvas = Canvas(width=800, height=526, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)

#Labels
lang = Label(text="Title", font=("Arial", 20, "italic"), bg="white")
word = Label(text="Word" , font=("Arial", 60, "bold"), bg="white")
lang.place(in_=canvas, x=400, y=150, anchor=CENTER)
word.place(x=400, y=263, anchor=CENTER)

#Buttons
image1 = PhotoImage(file="./images/wrong.png")
image2 = PhotoImage(file="./images/right.png")
right_btn = Button(image=image1, highlightthickness=0, bd=0)
wrng_btn = Button(image=image2, highlightthickness=0, bd=0)
right_btn.grid(row=1, column=0)
wrng_btn.grid(row=1, column=1)
window.mainloop()