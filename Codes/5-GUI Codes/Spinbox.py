from tkinter import *

def GetValue():
    value=var.get()
    l=Label(win,text=value,bg="lightblue",font=('Arial Black',20))
    l.place(x=170,y=150)

if__name__="__main__"

win=Tk()

win.geometry("500x500")
win.configure(background="lightblue")
win.resizable(0,0)

var=IntVar()

s=Spinbox(win,from_=0,to=100,font=('Arial Black',20),justify=RIGHT,bg="yellow",fg="pink",
          relief=RAISED,textvariable=var,width=3,state=NORMAL,disabledbackground="pink",disabledforeground="yellow")
s.pack()

#relief=it determines that whether the spinbox is at the top of backgroung
#or inside the background.
#width=it determines the Spinbox width.
#If state is DISABLED then we cant do any operation on Spinbox.State should be NORMAL to use Spinbox.
#disabledbackground=The background color to use when the widget is disabled.
#disabledforeground=The text color to use when the widget is disabled.

but=Button(win,text="Get Value",bg="black",fg="white",command=GetValue,font=('Arial Black',20))
but.place(x=170,y=70)


win.mainloop()
