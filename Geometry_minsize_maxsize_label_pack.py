from tkinter import *

keshav = Tk()

# widthXheight
keshav.geometry("888x234")

# width, height
keshav.minsize(745,500)

# Width , heigth
keshav.maxsize(745,500)

#show text on the GUI window
keshav = Label(text="Keshav is a good developer this is GUI")
keshav.pack()
keshav = Label(text=("Welcome to PyCharm"))
keshav.pack()
keshav.mainloop()

