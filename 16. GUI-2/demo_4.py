from tkinter import *


def fun():
    if v.get() == 1:
        lblL.configure(text='You pressed radiobutton 1')
    else:
        lblL.configure(text='You pressed radiobutton 2')


root = Tk()

v = IntVar()
Radiobutton(root, text='DIT', variable=v, \
            value=1, command=fun).pack(anchor=W)
Radiobutton(root, text='UIT', variable=v, \
            value=2, command=fun).pack(anchor=W)

lblL = Label(root)
lblL.pack()

root.mainloop()
