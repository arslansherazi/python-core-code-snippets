from tkinter import *
from tkinter import ttk  #Progressbar is a Widget of ttk so it should be included to use Treeview Widget.
import time


if__name__="__main__"

win=Tk()

win.geometry("500x500")
win.configure(background="lightblue")
win.resizable(0,0)

pbar=ttk.Progressbar(win,orient=HORIZONTAL)#This Line creates the Progress bar."orient" specify the direction of Progress Bar.It can be VERTICAL.
pbar.place(x=0,y=0,width=500,height=25)

pbar.config(mode='indeterminate') #"config" function is used to specify properties of a Widget.
#"mode" specify the style of Progress bar."mode=indeterminate" specify that Progressbar has specific size of intervals.Its size cant be changed.

pbar.start() #This Line start the Progress Bar.
pbar.stop()  #This Line stop the Progress Bar.

pbar.config(mode='determinate',maximum=10.0,value=4.0)
#"mode=determinate" specify that Progressbar can have different size of intervals(we can specify the size)
#"maximum" specify the maximum size of Progress Bar.
#"value" specify the current size of Progress Bar. 

pbar.config(value=7.0)

pbar.step()
#"step" function without any parameter add one value in current value.After executing this value=7.0(previous value)+1.0=8.0

pbar.step(5) #This line add 5 in current value. After executing this value=8.0(previous value)+5.0=13.0
             #(Here value exceeds the maximum value so value=exceeds value-maximum value=13-11=2)




            ### Connecting the Scale with Progress Bar ###
value=DoubleVar()

pbar.config(variable=value)
#This Line link a variable "value" to the Progress Bar.when this variable is changed then Progress bar is also changed according to this variable.
#Here Variable "value" is changed by the Scale widget.When the value of Variable changed by the Scale then Progress Bar is also changed according to this Variable.


scale=Scale(win,orient=HORIZONTAL,variable=value,from_=0.0,to=11.0)
scale.place(x=0,y=50,width=500)


win.mainloop()
