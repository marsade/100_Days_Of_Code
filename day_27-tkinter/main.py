#!/usr/bin/env python3
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label = tkinter.Label(text="I am a Label", font= ("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.grid(column=0, row=0)

#Buttons
def button_clicked():
    print("I got clicked")
    my_label["text"] = input.get()


button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = tkinter.Button(text="New Button")
button2.grid(column=2, row=0)

#Entry
input = tkinter.Entry()
input.grid(column=3, row=2)

window.mainloop()