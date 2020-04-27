from tkinter import *


if__name__="__main__"

win=Tk()
win.geometry("500x500")
win.configure(background="lightblue")  #Window background color also shows to list elements if we select them.if it is not set
win.resizable(0,0)

scrollbar = Scrollbar(win)
scrollbar.pack( side = RIGHT, fill=Y )


List=Listbox(win,bg="blue",bd=10,highlightcolor="orange",fg="pink",selectbackground="Chartreuse",cursor="heart",width="100",yscrollcommand = scrollbar.set)  #bd=border size
#selectbackground property sets the color when we select an element from the list.
#cursor property sets the cursor when we move our mouse to List box or selects any element from ListBox.



List.insert(1,"C")

List.insert(2,"C++")

List.insert(3,"Java")

List.insert(4,"Cobol")

List.insert(5,"C")

List.insert(6,"C++")

List.insert(7,"Java")

List.insert(8,"Cobol")

List.insert(9,"C")

List.insert(10,"C++")

List.insert(11,"Java")

List.insert(12,"Cobol")


List.pack()    #List should be packed or placed or grid after done inserting elements in it.


scrollbar.config( command = List.yview )

win.mainloop()
