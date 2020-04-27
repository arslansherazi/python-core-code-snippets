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

#Creating Menu Bar
#Menu() is a class of tkinter Module and menuBar is its object.

menuBar=Menu()

#Creating Menu(Drop Down List) for Menu Items(menu Bar)
FileList=Menu()

#Adding a label(item) to the Menu Bar

menuBar.add_cascade(label="File",menu=FileList)   #menu=FileList is include to specify the specific drop down menu for "File" Menu Item
menuBar.add_cascade(label="Edit")
menuBar.add_cascade(label="Format")
menuBar.add_cascade(label="Run")
menuBar.add_cascade(label="Options")
menuBar.add_cascade(label="Window")
menuBar.add_cascade(label="Help")

#Adding Drp Down Menus for Menu Items

#File Item

FileList.add_command(label="New",command=NewFile)  #Command is used to specify a functionaly if user clicks on New after clicking on File
FileList.add_command(label="Open",command=OpenFile)
FileList.add_command(label="Save",command=SaveFile)
FileList.add_command(label="Save As",command=SaveAsFile)


#By using same method we can Add drop down menus to the other Menu Items




#Now Config(specify that menu goes to which window)
#win1 is an object which creats the menu



win1.config(menu=menuBar) #menuBar is the object which creates the Menu Items in above lines of code





win1.mainloop()     
