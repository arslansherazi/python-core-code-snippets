from tkinter import *

win1=Tk()
win1.title("Text Editor")
win1.geometry("500x500")

def Save():
    #Creating a prompt for user 
    messagebox.showinfo(title="Save",message="Successfully Saved")

def Quit():
    #The following code ask user user to Quit.If he/she press yes then the specified window is vanished.
    opt=messagebox.askyesno(title="Quit",message="Are you want to Quit?")    #opt is returned 1 if user press yes otherwise 0.
    if (opt==1):
        win1.destroy()   #if opt is 1(user press yes) then this function vanish(destroy) the Specified Window(win1)


button=Button(win1,text="Press To Save",bg="Green",fg="White",font=('algerian',24,'bold'),command=Save).pack()
button=Button(win1,text="Press To Quit the Screen",bg="Green",fg="White",font=('bauhaus 93',24,'bold'),command=Quit).pack()

win1.mainloop()     
