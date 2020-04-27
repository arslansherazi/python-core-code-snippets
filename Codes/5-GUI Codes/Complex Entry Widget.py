from tkinter import *

def callback(self):
    user.delete(0,END)

def callback1(self):
    password.delete(0,END)

if__name__="__main__"

win=Tk()

win.geometry("500x500")
win.configure(background="lightblue")
win.resizable(0,0)

#l=Label(win,text="User Name",bg="lightblue")
#l.place(x=120,y=150)

user=Entry(win,cursor="arrow",bg="lightblue",fg="yellow",font=("Calibri",15),relief=FLAT,selectbackground="white"
           ,selectborderwidth=4,selectforeground="black",width=40)
user.insert(END,'username')
user.bind("<Button-1>",callback)
user.place(x=120,y=150)


u1=Label(win,text="________________________________________________________",fg="pink",bg="lightblue")
u1.place(x=120,y=175)

#l=Label(win,text="Password",bg="lightblue")
#l.place(x=120,y=190)

password=Entry(win,cursor="arrow",bg="lightblue",fg="yellow",font=("Calibri",15),relief=FLAT,selectbackground="white",selectborderwidth=4,selectforeground="black",width=40)
password.insert(END,'Password')
password.bind("<Button-1>",callback1)
password.show="*"
password.place(x=120,y=200)


u2=Label(win,text="________________________________________________________",fg="pink",bg="lightblue")
u2.place(x=120,y=225)

#"cursor" specify the mouse cursor when we moves the mose over the entry widget.
#"bg" specify the background of Entry widget.
#"fg" specify the color of text inside the Entry Widget.
#"font" specify the font of text inside the Entry Widget.
#"selectbackground" specify the background color when we select the text inside the Entry Widget.
#"selectborderwidth" specify the width of Entry Widget Border.
#"selectforeground" specify the color of text when we select it.
#"show" specify the password Entry.
#"width" specify the width of Entry Box.




win.mainloop()
