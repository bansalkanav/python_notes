# Entry(), Button(), CheckButton(), Listbox()

from tkinter import *

root = Tk()
root.title('My App')
root.configure(background='blue')

userL = Label(root, text='User Name: ')
passL = Label(root, text='Password: ')
userL.pack()
passL.pack()

userE = Entry(root)
passE = Entry(root, show='*')
userE.pack()
passE.pack()

countryLb = Listbox(root)
countryLb.insert(1, 'India')
countryLb.insert(2, 'Sri Lanka')
countryLb.insert(3, 'Bangladesh')
countryLb.insert(4, 'Nepal')
countryLb.insert(5, 'Bhutan')
countryLb.insert(6, 'Pakistan')
countryLb.insert(7, 'China')
countryLb.pack()

rememberCb = Checkbutton(root, text='Remember this login')
rememberCb.pack()

submitB = Button(root, text='Submit', bg='green',\
                 activebackground='yellow', \
                 activeforeground='white')
exitB = Button(root, text='exit', width=25, \
               command=root.destroy)
submitB.pack()
exitB.pack()

root.mainloop()
