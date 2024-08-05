from tkinter import *
keshav = Tk()

keshav.geometry("755x644")
photo = PhotoImage(file="python.png")
keshav_label = Label(image=photo)
keshav_label.pack()
keshav_label = Label(text="Its a Python logo")
keshav_label.pack()
keshav.mainloop()