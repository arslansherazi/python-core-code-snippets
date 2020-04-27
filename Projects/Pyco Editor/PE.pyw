from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


def messageWindow():
    msgWin=Tk()


    #The following code place the window at the top of any screen when it is created.User then can move it if we allow him to do so.
    x=435
    y=208
    w = msgWin.winfo_screenwidth()  #gives the width of any screen
    h = msgWin.winfo_screenheight() #gives the height of any screen
    width=(w/2)-(x/2)
    height=(h/2)-(y/2)
    
    msgWin.geometry('%dx%d+%d+%d' % (x, y,width,height))

    msgWin.overrideredirect(True)      #This line removes the window border from window.(used for displaying initial messages etc)
    
    photo=PhotoImage(file='images/pycoeditor.png') 
    label=Label(msgWin,image=photo)
    label.pack()

    msgWin.after(2000,lambda:mainWindow(msgWin)) # Destroy the Window after 5 seconds.5000milli seconds=5 econds
    
    msgWin.mainloop()


    


def mainWindow(msgWin):
    
    msgWin.destroy()

    mWin=Tk()

    mWin.geometry("600x500")   #Original size of window(if user tries to resize or move window then it converts to this size.)

    mWin.title('Pyco Editor')
    mWin.wm_iconbitmap('images/icon.ico')

    mWin.state('zoomed')        #this line display the window with zoom mode(full possible size of window)

    menuBar(mWin)               #Calling the menuBar Function to create menu bar in Window
    optionBar(mWin)

    textBox(mWin)
  
    mWin.mainloop()




def newFile():
    
    mWin=Tk()

    mWin.geometry("600x500")   

    mWin.title('Pyco Editor')
    mWin.wm_iconbitmap('images/icon.ico')    

    menuBar(mWin)               
    optionBar(mWin)

    textBox(mWin)
    
    mWin.mainloop()






    


def menuBar(mWin):
    menuBar=Menu()
    
    FileList=Menu(tearoff=0)
    ViewList=Menu(tearoff=0)
    EditList=Menu(tearoff=0)
    FormatList=Menu(tearoff=0)
    HelpList=Menu(tearoff=0)
    
    menuBar.add_cascade(label="File",menu=FileList)
    menuBar.add_cascade(label="Edit",menu=EditList)
    menuBar.add_cascade(label="Format",menu=FormatList) 
    menuBar.add_cascade(label="View",menu=ViewList)
    menuBar.add_cascade(label="Help",menu=HelpList)


    #File Item

    FileList.add_command(label="New File              Ctrl+N",command=newFile)
    FileList.add_command(label="Open File             Ctrl+O",command=OpenFile)
    FileList.add_separator()
    FileList.add_command(label="Save File               Ctrl+S")
    FileList.add_command(label="Save As                 Ctrl+Shift+S",command=SaveAsFile)
    FileList.add_separator()
    FileList.add_command(label="Exit                        Ctrl+Q",command=lambda:Exit(mWin))


    #View Item

    ViewList.add_checkbutton(label="Option Bar")

    #Format Item

    FormatList.add_command(label="Text Formatting")

    #Help Item

    HelpList.add_command(label="FAQs")


     #Edit Item

    EditList.add_command(label="Undo                Ctrl+Z")
    EditList.add_command(label="Redo                 Ctrl+Shift+Z",command=Redo)
    EditList.add_separator()
    EditList.add_command(label="Cut                   Ctrl+X")
    EditList.add_command(label="Copy                Ctrl+C")
    EditList.add_command(label="Paste                Ctrl+V")
    EditList.add_separator()
    EditList.add_command(label="Select All          Ctrl+A")
    

    mWin.config(menu=menuBar)



    


    


def textBox(mWin):
    boxWidth=mWin.winfo_width()-20
    boxHeight=mWin.winfo_height()-130

    frame=Frame(mWin,bg="white")
    frame.place(x=10,y=110,width=boxWidth,height=boxHeight)
    

    global textBox
    
    textBox = Text(frame,bg="white",fg="black",insertbackground="black",font=("Calibri",12),bd=0,undo=True)
    textBox.place(x=20,y=20,width=boxWidth-50,height=boxHeight-20)
    
    
    scrollbar = Scrollbar(frame,width=10)
    scrollbar.pack(side=RIGHT,fill=Y)
    textBox['yscrollcommand']=scrollbar.set
    scrollbar.config(command=textBox.yview)










def optionBar(mWin):

    boxWidth=mWin.winfo_width()
    upperFrame=Frame(mWin)
    upperFrame.place(x=0,y=0,width=boxWidth,height=100)

    photo1=PhotoImage(file='images/newfile.png') 
    button1=Button(upperFrame,text="New File",compound="top",image=photo1,relief=FLAT,command=newFile)
    button1.image=photo1
    button1.place(x=10,y=10)

    #Hover Effect
    button1.bind("<Enter>", lambda event: button1.configure(bg="#e0e0e0")) 
    button1.bind("<Leave>", lambda event: button1.configure(bg="#F0F0F0")) 


    photo2=PhotoImage(file='images/openfile.png') 
    button2=Button(upperFrame,text="Open File",compound="top",image=photo2,relief=FLAT,command=OpenFile)
    button2.image=photo2
    button2.place(x=100,y=10)

     #Hover Effect
    button2.bind("<Enter>", lambda event: button2.configure(bg="#e0e0e0")) 
    button2.bind("<Leave>", lambda event: button2.configure(bg="#F0F0F0"))


    photo3=PhotoImage(file='images/save.png') 
    button3=Button(upperFrame,text="Save",compound="top",image=photo3,relief=FLAT)
    button3.image=photo3
    button3.place(x=190,y=10)

     #Hover Effect
    button3.bind("<Enter>", lambda event: button3.configure(bg="#e0e0e0")) 
    button3.bind("<Leave>", lambda event: button3.configure(bg="#F0F0F0"))

    photo_3=PhotoImage(file='images/saveAs.png') 
    button_3=Button(upperFrame,text="Save As",compound="top",image=photo_3,relief=FLAT,command=SaveAsFile)
    button_3.image=photo_3
    button_3.place(x=280,y=10)

     #Hover Effect
    button_3.bind("<Enter>", lambda event: button_3.configure(bg="#e0e0e0")) 
    button_3.bind("<Leave>", lambda event: button_3.configure(bg="#F0F0F0"))


    cutPhoto=PhotoImage(file='images/cut.png') 
    cut=Button(upperFrame,text="Cut",compound="top",image=cutPhoto,relief=FLAT)
    cut.image=cutPhoto
    cut.place(x=370,y=10)

     #Hover Effect
    cut.bind("<Enter>", lambda event: cut.configure(bg="#e0e0e0")) 
    cut.bind("<Leave>", lambda event:cut.configure(bg="#F0F0F0"))



    c=PhotoImage(file='images/copy.png') 
    c1=Button(upperFrame,text="Copy",compound="top",image=c,relief=FLAT)
    c1.image=c
    c1.place(x=460,y=10)

     #Hover Effect
    c1.bind("<Enter>", lambda event: c1.configure(bg="#e0e0e0")) 
    c1.bind("<Leave>", lambda event:c1.configure(bg="#F0F0F0"))


    p=PhotoImage(file='images/paste.png') 
    p1=Button(upperFrame,text="Paste",compound="top",image=p,relief=FLAT)
    p1.image=p
    p1.place(x=550,y=10)

     #Hover Effect
    p1.bind("<Enter>", lambda event: p1.configure(bg="#e0e0e0")) 
    p1.bind("<Leave>", lambda event:p1.configure(bg="#F0F0F0"))



    u=PhotoImage(file='images/undo.png') 
    u1=Button(upperFrame,text="Undo",compound="top",image=u,relief=FLAT)
    u1.image=u
    u1.place(x=640,y=10)

     #Hover Effect
    u1.bind("<Enter>", lambda event: u1.configure(bg="#e0e0e0")) 
    u1.bind("<Leave>", lambda event:u1.configure(bg="#F0F0F0"))



    r=PhotoImage(file='images/redo.png') 
    r1=Button(upperFrame,text="Redo",compound="top",image=r,relief=FLAT,command=Redo)
    r1.image=r
    r1.place(x=730,y=10)

     #Hover Effect
    r1.bind("<Enter>", lambda event: r1.configure(bg="#e0e0e0")) 
    r1.bind("<Leave>", lambda event:r1.configure(bg="#F0F0F0"))


    photo_33=PhotoImage(file='images/font.png') 
    button_33=Button(upperFrame,text="Formatting",compound="top",image=photo_33,relief=FLAT)
    button_33.image=photo_33
    button_33.place(x=820,y=10)

     #Hover Effect
    button_33.bind("<Enter>", lambda event: button_33.configure(bg="#e0e0e0")) 
    button_33.bind("<Leave>", lambda event: button_33.configure(bg="#F0F0F0"))


    photo4=PhotoImage(file='images/internet.png') 
    button4=Button(upperFrame,text="Save to Cloud",compound="top",image=photo4,relief=FLAT)
    button4.image=photo4
    button4.place(x=910,y=10)

     #Hover Effect
    button4.bind("<Enter>", lambda event: button4.configure(bg="#e0e0e0")) 
    button4.bind("<Leave>", lambda event: button4.configure(bg="#F0F0F0"))


    photo5=PhotoImage(file='images/exit.png') 
    button5=Button(upperFrame,text="Exit",compound="top",image=photo5,relief=FLAT,command=lambda:Exit(mWin))
    button5.image=photo5
    button5.place(x=1000,y=10)


     #Hover Effect
    button5.bind("<Enter>", lambda event: button5.configure(bg="#e0e0e0")) 
    button5.bind("<Leave>", lambda event: button5.configure(bg="#F0F0F0"))





   





                                #### Button and Menu Options Commands ####
def Exit(mWin):
    
    opt=messagebox.askyesno(title="Exit",message="Are you want to Exit?")
    if (opt==1):
        mWin.destroy()






def OpenFile():
    file1=filedialog.askopenfile(title="Open File",mode='r',filetypes=(('text files','.txt'),('all files', '.*')))

    file2=file1.name
    
    f=open(file2)

    text=f.read()
    
    textBox.insert("1.0",text)






def SaveAsFile():
    file=filedialog.asksaveasfile(title="Save File As",filetypes=(('text files','.txt'),('all files', '.*')),initialfile='myFile.txt',defaultextension='.txt')
    text=textBox.get("1.0",END)
    file.write(text)
    file.close



def Redo():
    textBox.edit_redo()










                                                        ####Main Function###

if__name__="__main__"

messageWindow()

    
    
    
