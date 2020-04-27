from tkinter import *

win=Tk()
win.title("Tic Toc Toe Game")
win.geometry("500x500")

def WelcomeMessage():
    var=t.get() #Getting the value of t variable which is the value of text box
    label=Label(win,text=var,fg="red",font=20)   #Now label becomes the value of text box
    label.pack()


t=StringVar() #Declaring a variale T of string Type


button=Button(win,text="Press To start the Game",bg="Green",fg="White",font=500,command=WelcomeMessage)
button.pack()

#Creating Text Box

text=Entry(win,textvariable=t)   #text box value save in t variable
text.pack()




win.mainloop()     
