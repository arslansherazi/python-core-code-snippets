from tkinter import *


if__name__="__main__"

win=Tk()

win.geometry("500x500")    #While using grid() Function first value(500) is no of columns in window and second value(500) is no of rows in window.
win.configure(background="lightblue")
win.title("Grid() Function")
win.resizable(0,0)

msg=Label(win,text='Welcome',bg='lightblue',fg='black',font=("Arial Black",20))
msg.grid(row=250,column=250,rowspan=100,columnspan=100,sticky=E)

#"row" specify the row where we put the Widget(Default is 0)
#"column" specify the column where we put the Widget(Default is 0)
#"rowspan" spcify no of rows the Widget can have
#"columnspan" spcify no of columns the Widget can have



 ### Other Options ###

#"sticky" specify the direction of widget (E=East,W=West,S=south,ES=East-South and so on)
#"ipadx" and "ipady" specify the no of rows and columns respectively that the Widget can have outside its Border(Margin)
#"padx" and "pady" specify the no of rows and columns respectively that the Widget can have inside its Border(Padding)


win.mainloop()
