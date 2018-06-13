# Customizing root and Label + geometry

from tkinter import *

root = Tk()

root.title('My App')

root.geometry('300x300')

root.configure(background='blue')

hwL = Label(root)

hwL.configure(text='Hello World!!', bg='blue',\
              font='Times 25 bold underline')

hwL.pack()

root.mainloop()


# ***************************************************************
# geometry('widhtxheight') -> 'x' is lower case, dont put spaces in between

# ***************************************************************