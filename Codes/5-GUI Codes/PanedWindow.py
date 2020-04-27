from tkinter import *


if__name__="__main__"

win=Tk()

win.geometry("500x500")
win.configure(background="lightblue")
win.resizable(0,0)


m1 = PanedWindow(win,relief=RAISED,sashwidth="10")
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text="left pane")
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL,relief=RAISED)
m1.add(m2)

top = Label(m2, text="top pane")
m2.add(top)

m3 = PanedWindow(m2, orient=VERTICAL,relief=RAISED)
m2.add(m3)

bottom = Label(m3, text="bottom pane")
m3.add(bottom)


win.mainloop()
