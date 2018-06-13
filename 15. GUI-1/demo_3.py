# Playing with geometry(), pack() and grid()

from tkinter import *

root = Tk()

root.title('My App')

root.configure(background='blue')

hwL = Label(root, text='Hello World!!', bg='yellow', \
            font='Times 25 bold underline')

randomL = Label(root)

randomL.configure(text='We are learning tkinter')

nextL = Label(root, text='Where?', bg='red')

# hwL.pack(side=LEFT, fill=Y)
#
# randomL.pack(fill=X)
#
# nextL.pack(side=BOTTOM)

hwL.grid(row=0, column=0)
randomL.grid(row=0, column=1)
nextL.grid(row=1, column=1, sticky=W)

root.mainloop()


# ***************************************************************
# pack()

# hwL.pack(side=LEFT)
#
# randomL.pack(side=LEFT)
# side->TOP(default), BOTTOM, LEFT, RIGHT
#
# hwL.pack(fill=X) -> 'X' is upper case

# ***************************************************************
# grid()

# hwL.grid(row=0, column=0, sticky=E)
# sticky->E,W,N,S
#
# randomL.grid(row=1, column=1)


