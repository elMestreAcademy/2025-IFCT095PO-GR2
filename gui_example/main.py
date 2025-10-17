# Python tkinter hello world program

from tkinter import *

root = Tk()

a = Label(
    text="Hello, PATATA GUI",
    foreground="white",  # Set the text color to white
    background="black",  # Set the background color to black
    width=50,
    height=10
)

a.pack()

root.mainloop()
