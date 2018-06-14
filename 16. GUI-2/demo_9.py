from tkinter import *

dict= {}
root = Tk()


def fun():
    k = e1.get()
    v = e2.get()
    dict[k]=v
    lbl3.configure(text=k)
    lbl4.configure(text=v)


lbl1 = Label(root, text='Key')
lbl1.grid(row=0, column=0)
lbl2 = Label(root, text='Value')
lbl2.grid(row=1, column=0)

e1 = Entry(root)
e1.grid(row=0, column=1)

e2 = Entry(root)
e2.grid(row=1, column=1)

add = Button(root, text='ADD IT', command=fun)
add.grid(row=2, column=1)

lbl3 = Label(root)
lbl3.grid(row=3, column=0)

lbl4 = Label(root)
lbl4.grid(row=3, column=1)
root.mainloop()