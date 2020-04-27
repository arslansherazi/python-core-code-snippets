import tkinter as tk #now we can access the functionality of tkinter () module by using "tk" instead of whole "tkinter" we can change name of "tk" 

win=tk.Tk()
win.title("Tic Toc Toe Game")
win.geometry("500x500")

counter=0
def CounterLabel(label):
    counter=0
    
    def count():
        global counter    #globaal variable can accessed everywhere
        counter += 1
        label.config(text=str(counter))   #converting counter into string because label should be in string
        label.after(1,count)    #this function change the value of counter after 100 milli seconds we can change it.
    
    count()

    
L=tk.Label(win,fg="Green")# Creating Empty label for Counter
L.pack()

CounterLabel(L)   #Calling the counter function by passing L (label) as a parameter because counter shows on the place of label

button=tk.Button(win,text="Stop",comman=win.destroy,bg="Green",fg="black",width=40,height=5) #destroy is a function of Tk() class which can access by its object(win) and used to terminate the window.
button.pack()

win.mainloop()     

