from tkinter import *
from tkinter import ttk   #this module should be include to use Notebook Widget.

def text(tab,photo1):
    tab.add(page1,image=photo1, text='Note',padding=10,compound="top")



if __name__ == "__main__":


    win = Tk()
    win.title("Tabs")
    win.geometry("700x600")
    win.resizable(0,0)
   

    tab = ttk.Notebook(win,width=100)    #This Line Make Nootbook (tabs) in Window

    #The Following lines make pages(tabs) in Nootbook Widget.We can add any widget in the pake like Text,Frame,Label,Button etc)
    page1 = Text(tab,bg="black",fg="white",insertbackground="white")
    page2 = Frame(tab)

    photo=PhotoImage(file='msg.png')
    photo1=PhotoImage(file='text.png')

    #The following line add the defined pages into the Notebook
    tab.add(page2,image=photo, text='Message',padding=10,compound="top")
    #"padding" is used to add space between Tab button and Tab Page.
    #"image" specify the image as tab header.
    #"compund" specify the tab text,where to place according to the Tab Image.
    
    #The Following line add label into Message Tab of Nootbook.
    msg=Button(page2,text="Create Note Tab",bg="green",fg="white",font=('Arial Black',20),command=lambda:text(tab,photo1))
    msg.place(x=80,y=200)

    tab.place(x=0,y=0,width=700,height=600) #"width" and "height" should be defined for the Notebook.

    win.mainloop() 
