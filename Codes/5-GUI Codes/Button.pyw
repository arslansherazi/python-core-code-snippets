from tkinter import *

win=Tk()
win.title("Tic Toc Toe Game")
win.geometry("500x500")

     

#Creating Button

#Direction should also be specified for button otherwise it is not shown..Direction can be specified by any method(pack(),grid(),place() etc )

button=Button(win,text="Press To start the Game",bg="Green",fg="White",font=500).pack() #pack() function can also b used like this





win.mainloop()     
