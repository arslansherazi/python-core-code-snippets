from tkinter import *
from tkinter import ttk


if__name__="__main__"

win=Tk()

win.geometry("500x500")
win.configure(background="lightblue")
win.title("Separator")
win.resizable(0,0)

#The following lines created a separator(Separator used to separate different Widgets)
sp=ttk.Separator(win,orient=HORIZONTAL)
sp.place(x=0,y=250,width=500)

#The Following Lines set the color of Separator
style=ttk.Style()
style.configure('Alarm.TSeparator',background='black')
sp.config(style='Alarm.TSeparator')

win.mainloop()
