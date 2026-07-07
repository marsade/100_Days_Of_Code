#!/usr/bin/env python3 
from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, bg=THEME_COLOR)
        self.score = Label(text="Score: 0", bg=THEME_COLOR, pady=30)
        self.score.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas_q = self.canvas.create_text(
            150, 125, text="New Question",
            fill="black",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2)

        #Buttons
        self.image_t = PhotoImage(file="./images/true.png")
        self.image_f = PhotoImage(file="./images/false.png")
        self.true_btn = Button(image=self.image_t, highlightthickness=0, bd=0)
        self.false_btn = Button(image=self.image_f, highlightthickness=0, bd=0)
        self.true_btn.grid(row=2, column=0, pady=30)
        self.false_btn.grid(row=2, column=1, pady=30)
        self.window.mainloop()