from tkinter import *

win=Tk()
win.geometry("500x500+120+150")


def ColorPicker():
    color=colorchooser.askcolor() #colorchooser is the class of tkinter() and askcolor is the further functionality in it.They are used to create the color picker.
    #The color that the user picks has three values which are saved in color[0] color[1] and color[2].the actual value is in color[1]
    
    L=Label(text="You successfully choose the color",bg=color[1]).pack()  #here in label we used the color value which is choosen by the user 

button=Button(text="Click for Color Picker",font=("Arial Black",30,"bold"),command=ColorPicker).pack()




win.mainloop()     
