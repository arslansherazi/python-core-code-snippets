from tkinter import *


def key_press(event):
    print('Type:',format(event.type))        #This Line prints the type of pressed key.
    print('Widget:',format(event.widget))    #This Line prints the Widget name on which key is pressed. "." represents the top level window which is our application.
    print('Char:',format(event.char))        #This Line prints the character for the pressed key if available.
    print('KeySym:',format(event.keysym))    #This Line prints the name of pressed key.
    print('KeyCode:',format(event.keycode))  #This Line prints the code of pressed key e.g. ASCII Code.

def Copy(para):
    print(para)

def Paste(event):#"event" should be the argument of those functions which are called as Keyboard Events.
    print('Paste')

if__name__="__main__"

win=Tk()

win.geometry("500x500")
win.configure(background="lightblue")
win.title("KeyBoard Events")
win.resizable(0,0)

win.bind("<KeyPress>",key_press) #This line calls "key_press" function if user press any keyboard key but only when "win" Window lies on the top of other windows.

win.bind("<Control-c>",lambda e: Copy('Copy'))
#This line calls the "Copy" function if Control+c key is pressed.
#Syntax:-  windowObject.bind("<KeyName>",Function_Name)

win.bind("<Control-v>",Paste)

win.mainloop()
