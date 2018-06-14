from tkinter import *

root = Tk()

sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)
mylist = Listbox(root, yscrollcommand=sb.set)
for line in range(100):
    mylist.insert(END, 'Hi '+str(line))
mylist.pack(side=LEFT, fill=Y)
sb.configure(command=mylist.yview)

root.mainloop()
