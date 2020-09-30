from tkinter import * #import Tkinter for GUI( Graphical User Interface )
from tkinter.ttk import *
from time import strftime  #import time

root = Tk()
root.title("Digital Clock")

#def a time function
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text = string)
    label.after(1000,time)

label = Label(root, font = ("ds-digital", 50), background = "black", foreground = "cyan")
label.pack(anchor = 'center')
time()

mainloop()