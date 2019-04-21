from tkinter import *

# builds blank window, returns object
window = Tk()

# prints text in blank window, returns object
label = Label(window, text = 'Hello Python Geeks')

# positioning text
label.pack()

# displays window continously until you close it
window.mainloop()