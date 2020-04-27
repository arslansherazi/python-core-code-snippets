from tkinter import *

win=Tk()
win.title("Languages")
win.geometry("500x500")



def ShowMessage():
    #getting the values of var1,var2,var3,var4 and var5 to be used inside the function
    v1=var1.get()
    v2=var2.get()
    v3=var3.get()
    v4=var4.get()
    v5=var5.get()
    Label(win,text="\n\nYou have knowledge of following Languages:\n\n",font=("broadway",8)).pack()
    if(v1==1):
        Label(win,text="C",font=("bauhaus 93",20)).pack(anchor=W)
    if(v2==1):
        Label(win,text="C++",font=("bauhaus 93",20)).pack(anchor=W)
    if(v3==1):
        Label(win,text="Java",font=("bauhaus 93",20)).pack(anchor=W)
    if(v4==1):
        Label(win,text="Cobol",font=("bauhaus 93",20)).pack(anchor=W)
    if(v5==1):
        Label(win,text="Python",font=("bauhaus 93",20)).pack(anchor=W)
    
    
    
    

var1=IntVar()#it is received the value of first check box(var1=1 if checked otherwise var1=0)
var2=IntVar()#it is received the value of 2nd check box(var2=1 if checked otherwise var2=0)
var3=IntVar()#it is received the value of 3rd check box(var3=1 if checked otherwise var3=0)
var4=IntVar()#it is received the value of 4th check box(var4=1 if checked otherwise var4=0)
var5=IntVar()#it is received the value of 5th check box(var5=1 if checked otherwise var5=0)



Label(text="Select the Languages You have knowledge about it from the following:\n\n",font=("broadway",8)).pack()
Checkbutton(win,text="C",font=("bauhaus 93",20),variable=var1).pack(anchor=W)
Checkbutton(win,text="C++",font=("bauhaus 93",20),variable=var2).pack(anchor=W)
Checkbutton(win,text="Java",font=("bauhaus 93",20),variable=var3).pack(anchor=W)
Checkbutton(win,text="Cobol",font=("bauhaus 93",20),variable=var4).pack(anchor=W)
Checkbutton(win,text="Python",font=("bauhaus 93",20),variable=var5).pack(anchor=W)



Button(win,text="Submit",font=("Arial Black",24),command=ShowMessage).pack()



win.mainloop()     

