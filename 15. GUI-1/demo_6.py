from tkinter import *

root = Tk()

C = Canvas(root, bg='yellow')

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=300, fill="red")

C.pack()
root.mainloop()

# create_arc
# create_image
# create_line
# create_oval
# create_polygon
