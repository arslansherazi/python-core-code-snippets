from tkinter import *


if__name__="__main__"

win=Tk()

#First window is at the top and so on for other windows.previous one is at the top of next.

win.geometry("500x500")
win.configure(background="lightblue")
win.resizable(0,0)

win1=Toplevel(bg="pink")
win1.geometry("500x500")
win1.resizable(0,0)



win.mainloop()

win1.mainloop()
