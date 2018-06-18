from tkinter import *
from backend import *

root = Tk()

root.title('Library Management System')

def get_data():
    title=e1.get()
    author=e2.get()
    year=e3.get()
    isbn=e4.get()
    return title, author, year, isbn


def get_id():
    row = lstbox.curselection()
    myString = lstbox.get(row)
    myString = myString.split()
    id = myString[0]
    return (id,)


def front_fill(event):
    row = lstbox.curselection()
    myString = lstbox.get(row)
    myString = myString.split('  |  ')
    title_text.set(myString[1])
    author_text.set(myString[2])
    year_text.set(myString[3])
    isbn_text.set(myString[4])


def front_view():
    lstbox.delete(0, END)
    front_data = view()
    for row in front_data:
        lstbox.insert(END, str(row[0])+'  |  '+row[1]+'  |  '+row[2]\
                      + '  |  '+str(row[3])+'  |  '+str(row[4]))


def front_search():
    lstbox.delete(0, END)
    title, author, year, isbn = get_data()
    front_data = search(title, author, year, isbn)
    for row in front_data:
        lstbox.insert(END, str(row[0]) + '  |  ' + row[1] + '  |  ' + row[2]\
                      + '  |  ' + str(row[3]) + '  |  ' + str(row[4]))


def front_add():
    title, author, year, isbn = get_data()
    insert(title, author, year, isbn)
    front_view()


def front_update():
    id = get_id()
    title, author, year, isbn = get_data()
    update(id, title, author, year, isbn)
    front_view()


def front_delete():
    id = get_id()
    delete(id)
    front_view()


# define Labels
l1 = Label(root, text='Title')
l1.grid(row=0, column=0)

l2 = Label(root, text='Author')
l2.grid(row=0, column=2)

l3 = Label(root, text='Year')
l3.grid(row=1, column=0)

l4 = Label(root, text='ISBN')
l4.grid(row=1, column=2)

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
lstbox.bind('<Double-Button-1>', front_fill)


# add scrollbar to listbox
sb = Scrollbar(root)
sb.grid(row=2, column=2, rowspan=6)

lstbox.configure(yscrollcommand=sb.set)
sb.configure(command=lstbox.yview)

# define Buttons
b1 = Button(root, text='View All', width=12, command=front_view)
b1.grid(row=2, column=3)

b1 = Button(root, text='Search Entry', width=12, command=front_search)
b1.grid(row=3, column=3)

b1 = Button(root, text='Add Entry', width=12, command=front_add)
b1.grid(row=4, column=3)

b1 = Button(root, text='Update Selected', width=12, command=front_update)
b1.grid(row=5, column=3)

b1 = Button(root, text='Delete Selected', width=12, command=front_delete)
b1.grid(row=6, column=3)

b1 = Button(root, text='Close', width=12, command=root.destroy)
b1.grid(row=7, column=3)

connectdb()
front_view()

root.resizable(False, False)

root.mainloop()
