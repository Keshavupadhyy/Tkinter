from tkinter import *
import ImageTK
import PIL

var = Image, ImageTK

keshav = Tk()

image = Image.open("python.png")
photo = ImageTK.PhotoImage(image)

keshav.mainloop()