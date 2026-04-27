#!/usr/bin/env python3
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="I am a Label", font= ("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"

#Buttons
def button_clicked():
    print("I got clicked")
    my_label["text"] = input.get()


button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

#Entry

input = tkinter.Entry()
input.pack()

window.mainloop()