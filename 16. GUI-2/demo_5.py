# It is used to provide a graphical slider that allows to select any value from that scale.

from tkinter import *

root = Tk()

scale1 = Scale(root, from_=0, to=50)
scale1.pack()

scale2 = Scale(root, from_=0, to=50, \
               orient=HORIZONTAL)
scale2.pack()


root.mainloop()
