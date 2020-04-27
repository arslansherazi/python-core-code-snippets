from tkinter import *


if__name__="__main__"

win=Tk()

win.geometry("500x500")
#While using place() Function first value(500) is no of pixels(x-axis) Horizontally in window and second value(500) is no of Pixels(y-axis) Vertically in window.
win.configure(background="lightblue")
win.title("Place() Function")
win.resizable(0,0)

msg=Label(win,text='W',bg='lightblue',fg='black',font=("Arial Black",20))

#msg.place(anchor=e,height=200,width=300)
#msg.place(relx=0.5,rely=0.7,relheight=0.4,relwidth=0.5)


#"x" specify the x-axis in pixels (x-axis is from left-right starting from top)
#"y" specify the y-axis in pixels (y-axis is from top-bottom starting from top)


            ### Other Options ###

#"anchor" specify the direction of widget (e=East,w=West,s=south,ES=East-South and so on)
#"width" specify the width of Widget in pixels
#"height" specify the height of the Widget in pixels
#"relheight" and "relwidth" specify height and width of Widget in range 0.0-1.0 which is used as percentage(0=0% ,0.1=10% ans so on)
#"relx" and "rely" specify x-axis and y-axis of Widget in range 0.0-1.0 which is used as percentage(0=0% ,0.1=10% ans so on)


win.mainloop()
