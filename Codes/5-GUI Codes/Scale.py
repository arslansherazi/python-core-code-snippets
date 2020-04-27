from tkinter import *


def ShowValue():
    num=value.get()
    L=Label(win,text=num,bg="lightblue",font=('Arial Black',20))
    L.place(x=250,y=400)

if__name__="__main__"

win=Tk()

win.geometry("500x500")
win.configure(background="lightblue")
win.resizable(0,0)

value=IntVar()

s=Scale(win,activebackground="pink",bg="blue",cursor="circle",orient=HORIZONTAL,length="485",relief=RAISED,
        variable=value,label="PercentageScale",sliderlength="10",from_="0",to="1000",tickinterval="100",
        troughcolor="pink",showvalue="0",highlightbackground="yellow")
s.place(x=5,y=250)

button = Button(win, text="Get Scale Value", command=ShowValue,bg="blue",fg="lightblue")
button.place(x=250,y=350)

#activebackground=The background color when the mouse is over the scale.

#command=A procedure to be called every time the slider is moved.This procedure will be passed one argument,the new scale value.If the slider is moved rapidly,you may not get a callback forevery possible position, but you'll certainly get a callback when it settles.

#tickinterval=it shows intervals at the bottom for user help.
#Showvalue=It determines wheter the value show or not while sliding.
#highlight background=It set the border 

win.mainloop()
