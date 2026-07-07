#!/usr/bin/env python3 
from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, pady=30)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas_text = self.canvas.create_text(
            150, 125, 
            width=280,
            text="New Question",
            fill="black",
            font=("Arial", 16, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2)

        #Buttons
        self.image_t = PhotoImage(file="./images/true.png")
        self.image_f = PhotoImage(file="./images/false.png")

        self.true_btn = Button(image=self.image_t, highlightthickness=0, bd=0, command=self.true_click)
        self.false_btn = Button(image=self.image_f, highlightthickness=0, bd=0, command=self.false_click)

        self.true_btn.grid(row=2, column=0, pady=30)
        self.false_btn.grid(row=2, column=1, pady=30)

        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            quiz_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=quiz_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You've reached the end of the quiz")
            self.true_click.config(state="disabled")
            self.false_click.config(state="disabled")

    def false_click(self):
        self.canvas.config(bg="white")
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def true_click(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question) 