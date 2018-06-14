from tkinter import *

root = Tk()

menuM = Menu(root)
root.configure(menu=menuM)

fileM = Menu(menuM)
menuM.add_cascade(label='File', menu=fileM)
fileM.add_command(label='New')
fileM.add_command(label='Open...')
fileM.add_separator()
fileM.add_command(label='Exit', command=root.destroy)

helpM = Menu(menuM)
menuM.add_cascade(label='Help', menu=helpM)
helpM.add_command(label='About')

root.mainloop()
