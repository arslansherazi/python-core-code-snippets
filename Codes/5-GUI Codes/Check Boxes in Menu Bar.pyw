from tkinter import *

win1=Tk()
win1.title("Text Editor")
win1.geometry("500x500")


#Functions for File Drop Down Menu

def NewFile():
    L=Label(text="NEW FILE",font=20).pack()

def OpenFile():
    L=Label(text="OPEN FILE",font=20).pack()

def SaveFile():
    L=Label(text="SAVE FILE",font=20).pack()

def SaveAsFile():
    L=Label(text="SAVE AS FILE",font=20).pack()
def SelectAll():
    L=Label(text="SELECT ALL",font=20).pack()

menuBar=Menu()


FileList=Menu()



menuBar.add_cascade(label="File",menu=FileList)   
menuBar.add_cascade(label="Edit")
menuBar.add_cascade(label="Format")
menuBar.add_cascade(label="Run")
menuBar.add_cascade(label="Options")
menuBar.add_cascade(label="Window")
menuBar.add_cascade(label="Help")



FileList.add_command(label="New",command=NewFile)  
FileList.add_command(label="Open",command=OpenFile)
FileList.add_command(label="Save",command=SaveFile)
FileList.add_command(label="Save As",command=SaveAsFile)
FileList.add_checkbutton(label="Select All",command=SelectAll)     #add_checkbutton is used to add a check box as a drop down menu item of a menu bar item



win1.config(menu=menuBar) 





win1.mainloop()     
