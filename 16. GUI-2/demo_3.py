from tkinter import *

root = Tk()

messageM = Message(root)
messageM.configure(text='I am writing this message', \
                   bg='lightgreen')
messageM.pack()
root.mainloop()
