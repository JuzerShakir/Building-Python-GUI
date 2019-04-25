""" Exercise 2 """

from tkinter import *

window = Tk()

text_1 = Label(window, text = 'Demo 1', fg = 'white', bg = 'red')
text_2 = Label(window, text = 'Demo 2', fg = 'white', bg = 'blue')
text_3 = Label(window, text = 'Demo 3', fg = 'white', bg = 'green')

text_1.pack(fill = X)
text_2.pack(fill = Y, expand = True)
text_3.pack(fill = BOTH, expand = True)

window.mainloop()