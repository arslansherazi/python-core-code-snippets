from tkinter import *

win1=Tk()
win1.title("Tic Toc Toe Game")
win1.geometry("500x500")


win2=Tk()
win2.title("Tic Toc Toe Game")
win2.geometry("500x500")

#in which classes we pass win1 as a object shown in Window1 and in which we pass win2 shown in Window2 and so on

def WelcomeMessage():
    var=t.get()
    label=Label(win2,text=var,fg="red",font=20)
    label.pack()
    
    
   
    
    



t=StringVar() #Declaring a variale T of string Type


text=Entry(win1,textvariable=t)
text.pack()
button=Button(win1,text="Enter",bg="Green",fg="White",font=500,command=WelcomeMessage)
button.pack()

#Creating Text Box






win.mainloop()     
