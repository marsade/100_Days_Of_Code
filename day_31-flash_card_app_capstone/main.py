#!/usr/bin/env python3
from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

flip_timer = None
data = pandas.read_csv("data/french_words.csv")
lang_titles = list(data.columns)
ulang_title = lang_titles[0]
klang_title = lang_titles[1]
data_dict = data.to_dict("records")
current_card = {}


# ---Word Generation--- #
def generate_card():
    global flip_timer, current_card
    flip_timer = window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(canvas_title, text=ulang_title, fill="black")

    current_card = random.choice(data_dict)
    canvas.itemconfig(canvas_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_title, text=klang_title ,fill="white")
    canvas.itemconfig(canvas_word, fill="white")
    canvas.itemconfig(canvas_image, image=back_img)

    canvas.itemconfig(canvas_word, text=current_card["English"], fill="white")


# ---UI Setup--- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)
# Card Image
canvas = Canvas(width=800, height=526, highlightthickness=0,
                bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
canvas_title = canvas.create_text(
                                400, 120, text=ulang_title,
                                fill="black",
                                font=("Arial", 20, "italic")
                                )
canvas_word = canvas.create_text(
                                400, 263, text=ulang_title,
                                fill="black",
                                font=("Arial", 60, "bold")
                                )
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
image1 = PhotoImage(file="./images/wrong.png")
image2 = PhotoImage(file="./images/right.png")
right_btn = Button(image=image1, highlightthickness=0,
                   bd=0, command=generate_card)
wrng_btn = Button(image=image2, highlightthickness=0,
                  bd=0, command=generate_card)
right_btn.grid(row=1, column=0)
wrng_btn.grid(row=1, column=1)
generate_card()
window.mainloop()
