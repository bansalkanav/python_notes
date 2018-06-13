# login layout

from tkinter import *

root = Tk()
root.title('My App')
root.configure(background='#EEEEEE')

userL = Label(root, text='User Name: ')
passL = Label(root, text='Password: ')
userL.grid(row=1, column=0, sticky=E)
passL.grid(row=2, column=0, sticky=E)

userE = Entry(root)
passE = Entry(root, show='*')
userE.grid(row=1, column=1)
passE.grid(row=2, column=1)

rememberCb = Checkbutton(root, text='Remember this login')
rememberCb.grid(row=3, columnspan=2)

submitB = Button(root, text='Submit', bg='green',\
                 activebackground='yellow', \
                 activeforeground='white')
exitB = Button(root, text='Log Out', \
               command=root.destroy)
submitB.grid(row=4, column=1, sticky=W)
exitB.grid(row=4, column=1, sticky=E)

root.mainloop()
