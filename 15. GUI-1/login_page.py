from tkinter import *


def CheckLogin():
    with open('creds.txt') as f:
        data = f.readlines()
        uname = data[0].rstrip()
        pword = data[1].rstrip()

    if userE.get() == uname and passE.get() == pword:
        r = Tk()
        r.title(':D')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[+] Logged In')
        rlbl.pack()
        r.mainloop()
    else:
        r = Tk()
        r.title('D:')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()


root = Tk()
root.title('Login Page')
root.configure(background='#EEEEEE')

userL = Label(root, text='User Name: ')
passL = Label(root, text='Password: ')
userL.grid(row=0, column=0)
passL.grid(row=1, column=0)

userE = Entry(root)
passE = Entry(root, show='*')
userE.grid(row=0, column=1)
passE.grid(row=1, column=1)

loginB = Button(root, text='Login', command=CheckLogin)
loginB.grid(row=2, column=0)

root.mainloop()




