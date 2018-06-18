from tkinter import *

root = Tk()

# define Labels
l1 = Label(root, text='Title')
l1.grid(row=0, column=0)

l1 = Label(root, text='Author')
l1.grid(row=0, column=2)

l1 = Label(root, text='Year')
l1.grid(row=1, column=0)

l1 = Label(root, text='ISBN')
l1.grid(row=1, column=2)

# define Entries
title_text=StringVar()
e1=Entry(root,textvariable=title_text)
e1.grid(row=0, column=1)

author_text=StringVar()
e2=Entry(root,textvariable=author_text)
e2.grid(row=0, column=3)

year_text=StringVar()
e3=Entry(root,textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text=StringVar()
e4=Entry(root,textvariable=isbn_text)
e4.grid(row=1, column=3)

# define Listbox
lstbox = Listbox(root, height=6, width=35)
lstbox.grid(row=2, column=0, rowspan=6, columnspan=2)

# add scrollbar to listbox
sb = Scrollbar(root)
sb.grid(row=2, column=2, rowspan=6)

lstbox.configure(yscrollcommand=sb.set)
sb.configure(command=lstbox.yview)

# define Buttons
b1 = Button(root, text='View All', width=12)
b1.grid(row=2, column=3)

b1 = Button(root, text='Search Entry', width=12)
b1.grid(row=3, column=3)

b1 = Button(root, text='Add Entry', width=12)
b1.grid(row=4, column=3)

b1 = Button(root, text='Update Selected', width=12)
b1.grid(row=5, column=3)

b1 = Button(root, text='Delete Selected', width=12)
b1.grid(row=6, column=3)

b1 = Button(root, text='Close', width=12)
b1.grid(row=7, column=3)

root.mainloop()
