from tkinter import *


if__name__="__main__"

win=Tk()

win.geometry("500x500")
win.configure(background="lightblue")
win.resizable(0,0)

label=LabelFrame(win,text="Left Frame",bg="yellow",fg="light blue",font=("Arial Black",15),cursor="heart",highlightthickness=5,labelanchor="n")  
label.place(x=5,y=5,width=150,height=490)

#"fg" sets the color of Frame label while bg sets the color of Frame.
#"font" sets the font of Frame label.
#"cursor" change the cursor when user moves his mouse to the specified frame.
#"highlightthickness" sets the size of Frame border.
#"labelanchor" specifies where to place the label of Frame.  n=north(direction)


win.mainloop()
