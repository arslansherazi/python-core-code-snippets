from tkinter import *

win=Tk()
win.title("Tic Toc Toe Game")
win.geometry("500x500")

def WelcomeMessage():
    label=Label(win,text="Welcome to the Game",fg="red")
    label.pack()

#Adding Functionality to the buttons

button=Button(win,text="Press To start the Game",bg="Green",fg="White",font=500,command=WelcomeMessage)
button.pack()




win.mainloop()     
