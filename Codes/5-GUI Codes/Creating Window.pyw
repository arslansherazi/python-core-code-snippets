from tkinter import *





#Creating Window
#Tk() is the class in tkinter module which creates window.
win=Tk()
win.configure(background="Khaki")#this function is used to change background of Window


#Creating title.title is a function in Tk() class
win.title("Tic Toc Toe Game")
#Resize the window.geometry is also a function in Tk() class
win.geometry("500x500")



win.mainloop()      #It is used to control the window in console works same as input() function.

