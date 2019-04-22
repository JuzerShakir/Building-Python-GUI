""" Exercise 1 """

from tkinter import *

# builds blank window, returns object
window = Tk()

# to show text in window, returns object
label = Label(window, text = 'Hello Python Geeks')

# makes text visible
label.pack()

# displays window continously until you close it
window.mainloop()

# THE END