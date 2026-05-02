#!/usr/bin/env python3
from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=30, pady=20)

def calculate():
    entry = float(input.get())
    out = entry * 1.60934
    ans_label["text"] = str(out)


text1 = Label(text="is equal to")
text1.grid(column=0, row=1)

input = Entry(width=7)
input.grid(column=1, row=1)

ans_label = Label(text="0")
ans_label.grid(column=1, row=0)

ml_label = Label(text="Miles")
ml_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

cal_btn = Button(text="Calculate", command=calculate)
cal_btn.grid(column=1, row=2)

window.mainloop()