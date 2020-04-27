from tkinter import *
from tkinter import ttk


if__name__="__main__"

win=Tk()

win.geometry("500x500")
win.configure(background="lightblue")
win.title("ScrollBar")


l1=Label(win,text="Scroll Bars in Text Widget",font=('Arial Black',18),bg='light blue')
l1.pack()


frame=Frame(win)
frame.place(x=100,y=100,width=300,height=300)

text=Text(frame)
text.place(x=0,y=0,width=282,height=282)


#The Following lines add Vertical scrollBar into the text Widget.
yScroll=ttk.Scrollbar(frame,orient=VERTICAL,command=text.yview)#"command" specifies the direction of ScrollBar into Text Widget. yview=Vertical ,xview=Horizontal
yScroll.place(x=282,y=0,height=300)

#The Following lines add Horizontal scrollBar into the text Widget.
xScroll=ttk.Scrollbar(frame,orient=HORIZONTAL,command=text.xview)
xScroll.place(x=0,y=282,width=300)

#The Following Lines sets the specified ScrollBars into the Text Widget.
text.config(yscrollcommand=yScroll.set)
text.config(xscrollcommand=xScroll.set)




win.mainloop()
