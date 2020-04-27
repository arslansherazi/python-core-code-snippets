from tkinter import *


def key_press(event):
    global prev
    prev=event
    print('Type:',format(event.type))       #This Line prints the type of pressed mouse button.
    print('Widget:',format(event.widget))   #This Line prints the Widget name on which mouse button is pressed.
                                            #"." represents the top level window which is our application.
    print('Num:',format(event.num))         #This line prints the mouse button no which is pressed.
    print('x:',format(event.x))             #This line prints the x-coordinate of Window where the mouse button is pressed 
    print('y:',format(event.y))             #This line prints the y-coordinate of Window where the mouse button is pressed
    print('x_root:',format(event.x_root))   #This line prints the x-root of Window where the mouse button is pressed 
    print('y-root:',format(event.y_root))   #This line prints the y-root of Window where the mouse button is pressed

    '''Note That
    Number      Mouse Button
    1           Left Click    
    2           Right Click
    3           Mouse Wheel
    '''
    

def draw(event):
    global prev
    can.create_line(prev.x,prev.y,event.x,event.y,width=5)
    prev=event

if__name__="__main__"

win=Tk()

win.geometry("500x500")
win.configure(background="lightblue")
win.title("KeyBoard Events")
win.resizable(0,0)

can=Canvas(win,width=500,height=500,bg='white')
can.pack()

can.bind("<ButtonPress>",key_press)#This line calls "key_press" function if user press any mouse key but only when "win" Window lies on the top of other windows.


can.bind("<B1-Motion>",draw)
#This line calls the "draw" function if user press the Button no 1 of mouse which is Left Click and dont release it.
#Syntax:-  windowObject.bind("<KeyName>",Function_Name)

win.mainloop()
