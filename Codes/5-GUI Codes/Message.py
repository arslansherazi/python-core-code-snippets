from tkinter import *


if__name__="__main__"

win=Tk()

win.geometry("500x500")
win.configure(background="lightblue")
win.resizable(0,0)

strr=StringVar()

#here win is parent window in which we want to create the Message widget.(we can change it to a frame or another window according to our need).
msg=Message(win,bg="blue",text="Hello!!!!!Welcome to the Game",relief=RAISED,width="500",cursor="heart",textvariable=strr)
msg.pack()

strr.set("Tic toc toe")     #Now the text of Message is set to Tic toc toe.

win.mainloop()
