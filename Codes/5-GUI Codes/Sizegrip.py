from tkinter import *
from tkinter import ttk


if__name__="__main__"

win=Tk()

win.geometry("500x500")
win.configure(background="lightblue")
win.title("Sizegrip")


#The following lines created a Sizegrip(Separator used to resize the Specified Widget)
sg=ttk.Sizegrip(win)
sg.place(x=480,y=480)

#The Following Lines set the color of Sizegrip
style=ttk.Style()
style.configure('Alarm.TSizegrip',background='light blue')
sg.config(style='Alarm.TSizegrip')

win.mainloop()
