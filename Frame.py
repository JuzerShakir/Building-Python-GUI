""" Exercise 3 """

from tkinter import *

# builds blank window, returns object
window = Tk()

# 1st Frame, creates invisible frame on window
topframe = Frame(window)
topframe.pack()
# 2nd Frame, will be positioned to the bottom of the window
bottomframe = Frame(window)
bottomframe.pack(side=BOTTOM)

# creates buttons within specified frames with colorful text on it
button_1 = Button(topframe, text='Button 1', fg="red")
button_2 = Button(topframe, text='Button 2', fg="green")
button_3 = Button(bottomframe, text='Button 3', fg="purple")
button_4 = Button(bottomframe, text='Button 4', fg="blue")

# makes the buttons visible
button_1.pack(side=LEFT)
button_2.pack()
button_3.pack(side=LEFT)
button_4.pack()

# do not terminate until user wants to
window.mainloop()

# THE END