# Understanding the layout

from tkinter import *

root = Tk()

root.title('My App')

root.configure(background='blue')

lbl_1L = Label(root, text='This is Label 1', bg='red', \
               font='none 30')

lbl_1L.pack(fill=Y, side=LEFT)

lbl_2L = Label(root, text='This is Label 2', bg='white', \
               font='none 30')

lbl_2L.pack(fill=X)

root.mainloop()

# try lbl_1 side=LEFT, lbl_2 side=BOTTOM
