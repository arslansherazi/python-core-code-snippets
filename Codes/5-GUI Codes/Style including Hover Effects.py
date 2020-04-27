from tkinter import *
from tkinter import ttk



if__name__="__main__"

win=Tk()

win.geometry("500x500")
win.configure(background="lightblue")
win.title("Style including Hover Effect")
win.resizable(0,0)


b1=ttk.Button(win,text='Button1') #This Line creates a ttk Button(This Button is a bit different from tkinter Button)
b1.place(x=200,y=100)
b2=ttk.Button(win,text='Button2')
b2.place(x=200,y=250)

style=ttk.Style()   #This line creates a ttk Style widget.This widget is used to style the ttk Widgets.
                    #Unlike tkinter,in ttk most of the options of styling the widgets are not working directly into the widget creating Object itself.
                    
print(style.theme_names()) #This line prints all the available themes for the ttk widgets.
print(style.theme_use())   #This line prints the currently used theme by ttk.

style.theme_use('clam') #This line change the current theme by any of the available themes by specifying its name within ()

print(b2.winfo_class())    #This line prints the class name used by widget(b2 is the object of Button Widget,so this line prints the class used by Button Widget of object b2)



style.configure('TButton',foreground='pink',font=('Arial Black',14),relief=FLAT)
#This Line specify the styling for all widgets which have class "TButton"
#First Parameter is the class name of Widgets.
#The specified styling is applied on those Widgets which have class name same as this Parameter.



style.configure('Alarm.TButton',foreground='yellow',font=('Arial Black',14),background='lightblue')
#This line creates new styling class for Widgets which have class name "TButton"
#Syntax for creating new style class is as follows
        #newStyleName.ClassName
        #Example:: myStyle.TButton


b2.config(style='Alarm.TButton')
#This line apply the new created style on a specified Widget which should have class "TButton"

b1.config(style='Alarm.TButton')

style.map('Alarm.TButton',foreground=[('pressed','pink'),('hover','white')],background=[('pressed','light blue'),('hover','light blue')])
#This Line map the states of a widget(background/foreground color when it is pressed or mouse is moves over it ) into a specified Style(e.g Alarm.TButton)
#The First Parameter is the class name OR our created style name in which we want to apply the mapping.
#Mapping is also applied on those widgets for which we apply the mapped style.(e.g b2 object also mapped because we apply Alarm.TButton style on it) 


print(style.layout('TButton'))  #This line prints the layout schemes of a class.

print(style.element_options('Button.label')) #This Line prints the available properties for a specified layout.

print(style.lookup('TButton','foreground'))  #This line prints the value of a specified property of a specified class.



style.layout('TButton',[('Button.border', {'sticky': 'nswe', 'border': '1', 'children':
                       [('Button.padding', {'sticky': 'nswe', 'children':
                       [('Button.label', {'sticky': 'nswe'})]})]})])

#This line remove dotted lines from all widgets having class "TButton" which are appear arround the Widgets.
#We remove just focus layout from the layouts to remove dotted lines from widgets having class "TButton".
#The first parameter is the class name of widgets for which we want to remove dotted line focus.It can be our created style OR any other class.

win.mainloop()
