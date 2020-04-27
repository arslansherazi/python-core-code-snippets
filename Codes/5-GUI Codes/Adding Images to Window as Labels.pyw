from tkinter import *

win=Tk()


win.title("Tic Toc Toe Game")
win.geometry("500x500")
win.resizable(0,0)

photo=PhotoImage(file='arslan.png') #Image Should be in the same directory where the Python file exist or give the full path of Image.
label=Label(win,image=photo) #Images should be displayed in the window through Labels
label.pack()



win.mainloop()      #It is used to control the window in console works same as input() function.

