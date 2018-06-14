from tkinter import *

root = Tk()

textT = Text(root)

textT.configure(height=10, width=20)

textT.pack()

textT.insert(END, 'hi\n')

textT.insert(END, 'how are you')

textT.insert(1.0, 'hello, ')

root.mainloop()
