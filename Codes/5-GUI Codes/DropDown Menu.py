from tkinter import *


if__name__="__main__"

win=Tk()

win.geometry("500x500")
win.configure(background="lightblue")
win.resizable(0,0)

color=StringVar()

choices = ['red', 'green', 'blue', 'yellow','white', 'magenta']
option = OptionMenu(win,color,*choices)

#choices(array) should be used as *choices otherwise menu does not create.
#a string type variable should be used for displaying item name at the menu
#after choosing.

option.pack()

win.mainloop()
