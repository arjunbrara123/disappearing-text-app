from tkinter import *
from time import time

window = Tk()
window.title("Typing Speed Checker")
window.config(padx=100, pady=50, bg='#ffffff')

lblTitle = Label(text="Type your text below", )
lblTitle.grid(column=0, row=0)

textExample = Text(window, height=10)
textExample.grid(column=0, row=1)

timer = None

start_time = time()


def set_invisible():
    textExample.config(fg="white")


def set_visible():
    textExample.config(fg="black")


def key_pressed(event):
    global timer
    print(event.char)
    set_visible()
    timer = window.after(2000, set_invisible)

window.bind("<Key>",key_pressed)

window.mainloop()
