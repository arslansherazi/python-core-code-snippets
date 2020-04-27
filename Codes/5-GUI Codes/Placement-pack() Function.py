from tkinter import *


if__name__="__main__"

win=Tk()

win.geometry("1000x500")
win.configure(background="lightblue")
win.title("Grid() Function")
win.resizable(0,0)

msg=Label(text='Welcome',bg='lightblue',fg='black',font=('Arial Black',20))
msg.pack()
#pack() Method without any option is used to place the Widget at the center of the line where the widget is specified.




                                            ###fill Option###


msg1=Label(text='fill=Y',bg='green',fg='black',font=('Arial Black',20))
msg1.pack(fill=X)
#pack() Method with fill=X is used to place the Widget at the center of the line where the widget is specified.but the background color of the widget is applied on
#the whole line horizontally.

msg2=Label(text='fill=Y',bg='pink',fg='black',font=('Arial Black',20))
msg2.pack(fill=Y)
#pack() Method with fill=X is used to place the Widget at the center of the line where the widget is specified.but the background color of the widget is applied on
#the whole line Vertically.


msg3=Label(text='fill=BOTH',bg='yellow',fg='black',font=('Arial Black',20))
msg3.pack(fill=BOTH)
#pack() Method with fill=X is used to place the Widget at the center of the line where the widget is specified.but the background color of the widget is applied on
#the whole line Both Horizontally & Vertically.





                                            ### expand Option ###


msg4=Label(text='expand=TRUE',bg='yellow',fg='black',font=('Arial Black',20))
msg4.pack(expand=TRUE)
#pack() Method with expand=TRUE is used to fill the empty space which is not used by Widget's Parent.








                                            ### side Option ###


msg5=Label(text='side=LEFT',bg='yellow',fg='black',font=('Arial Black',20))
msg5.pack(side=LEFT)
#pack() Method with side=LEFT is used to place the Widget at the LEFT of the line where the widget is specified.


msg6=Label(text='side=RIGHT',bg='yellow',fg='black',font=('Arial Black',20))
msg6.pack(side=RIGHT)
#pack() Method with side=RIGHT is used to place the Widget at the RIGHT of the line where the widget is specified.


msg7=Label(text='side=BOTTOM',bg='yellow',fg='black',font=('Arial Black',20))
msg7.pack(side=BOTTOM)
#pack() Method with side=BOTTOM is used to place the Widget at the BOTTOM of its Parent(in this example main window is its Parent).







win.mainloop()
