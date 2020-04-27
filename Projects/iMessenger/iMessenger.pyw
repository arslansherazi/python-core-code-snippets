from tkinter import *
import sys
from _thread import *
import socket
import time
#from pygame import *

 

                                            #########----------Functions---------##############	


def Clear():
    text.delete(0,END)    
    text1.delete(0,END)
    
def NewWindow():
    p=port.get()
    n=name.get()
    win.destroy()
    win1=Tk()
    win1.configure(background="white")
    win1.geometry("500x500")
    win1.title(n)
    win1.wm_iconbitmap('icon.ico')
    win1.resizable( width = False , height = False )

    upperM=Frame(win1,bg="lightblue")
    upperM.place(x=0,y=0,width=150,height=30)
    OnlineLabel=Label(upperM,text="Online Users",font=('Berlin Sans FB',15),bg="lightblue").pack()
    
    Left=Frame(win1,bg="lightblue")
    Left.place(x=0,y=31,width=150,height=470)
    

    MessageWin1= Text(Left,bg="lightblue")
    MessageWin1.place(x=0,y=0,width=150,height=500)
    MessageWin1.configure(state="disabled")

    scrollbar1 = Scrollbar(Left)
    scrollbar1.pack(side=RIGHT,fill=Y)
    MessageWin1['yscrollcommand']=scrollbar1.set
    scrollbar1.config(command=MessageWin1.yview)
    
    
    
    upper=Frame(win1,bg="white")
    upper.place(x=150,y=0,width=350,height=60)


    Center=Frame(win1,bg="white")
    Center.place(x=150,y=60,width=350,height=390)
    
    MessageWin= Text(Center,bg="white")
    MessageWin.place(x=0,y=0,width=350,height=390)
    MessageWin.configure(state="disabled")

    scrollbar = Scrollbar(Center)
    scrollbar.pack(side=RIGHT,fill=Y)
    MessageWin['yscrollcommand']=scrollbar.set
    scrollbar.config(command=MessageWin.yview)

    ConnectClient(p,n,win1,MessageWin,MessageWin1)
    
    win1.mainloop()

    


def ConnectClient(p,n,win1,MessageWin,MessageWin1):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = socket.gethostname()
    port = p
    client.connect((host,port))
    client.send(bytes(n,'utf-8'))
    
    def Threaded_Receive(client,i,win1,MessageWin,MessageWin1):
        OnlineUser=[]
        while(1):
            tok=client.recv(1024)
            print(tok)
            if(tok==bytes("name",'utf-8')):
                i=i+30
                user=client.recv(1024)
                
                obj=Buttonn(user,win1,OnlineUser,i,client,MessageWin,MessageWin1)
            elif(tok==bytes("message",'utf-8')):
                
                

                
                
                BorderLine=Label(win1,text="____________________________",font=('Berlin Sans FB',20),fg="lightblue",bg="white")
                BorderLine.place(x=150,y=25)
                
                name=client.recv(1024)
                msg=client.recv(1024)
                 
                L=Label(win1,text="Received Message From",bg="white")
                L.place(x=150,y=20)
                L=Label(win1,text=name,font=("Berlin Sans FB",10,'bold'),bg="white",fg="#FFBE4A")
                L.place(x=280,y=20)

                #LineNumber=float(MessageWin.index('end'))-1.0
                
                MessageWin.configure(state="normal")
                MessageWin.insert(END,name)
                
                #MessageWin.tag_add("A1",LineNumber,LineNumer+len(name))
                #MessageWin.tag_config("A1",foregroung="#FFBE4A")

                MessageWin.insert(END,':')
                #MessageWin.tag_add("A2",':')
                #MessageWin.tag_config("A2",foregroung="#FFBE4A")
                
                MessageWin.insert(END,'\n')
                MessageWin.insert(END,'    ')
                MessageWin.insert(END,msg)    
                MessageWin.insert(END,'\n')
                MessageWin.insert(END,'\n')

                MessageWin.configure(state="disabled")
                 
                Bottom=Frame(win1,bg="#FFBE4A")
                Bottom.place(x=150,y=450,width=300,height=50)
                 
                Message= Text(Bottom,bg="#FFBE4A")
                Message.place(x=5,y=5,width=290,height=40)
                send=Button(win1,text="Send",bg="lightblue",fg="white",width=7,font=("Calibri",10,'bold'),height=3,command=lambda:CommunicationHandling1(Message,win1,client,name,MessageWin))
                send.place(x=450,y=450)
                 
                
                
          
            
    i=20
    start_new_thread(Threaded_Receive,(client,i,win1,MessageWin,MessageWin1))



    





def CommunicationHandling1(Message,win1,client,user,MessageWin):
    msg=Message.get("0.0","end-1c")
    Message.delete("0.0","end-1c")

    MessageWin.configure(state="normal")
    
    MessageWin.insert(END,"You to ")
    MessageWin.insert(END,user)
    #MessageWin.tag_add("A3",user)
    #MessageWin.tag_config("A3",foregroung="#FFBE4A")
   # MessageWin.tag_config(user,foreground="#FFBE4A")
    MessageWin.insert(END,':')
    #MessageWin.tag_add("A4",':')
    #MessageWin.tag_config("A4",foregroung="#FFBE4A")

    MessageWin.insert(END,'\n')
    MessageWin.insert(END,'    ')
    MessageWin.insert(END,msg)
    MessageWin.insert(END,'\n')
    MessageWin.insert(END,'\n')

    MessageWin.configure(state="disabled")
    
    SendMessage1(msg,user,client)

def SendMessage1(msg,user,client):
    print(msg)
    token="message"
    client.send(bytes(token,'utf-8'))
    time.sleep(1)
    client.send(user)
    time.sleep(1)
    client.send(bytes(msg,'utf-8'))
    time.sleep(1)






                                               #######-------Classess--------#######



    
        

class Buttonn:
    def __init__(self,user,win1,OnlineUser,i,client,MessageWin,MessageWin1):
        OnlineUser.append(Button(win1,text=user,bg="lightblue",fg="white",font=("Calibri",10),width=17,command=lambda:self.SendReceive(user,client,win1,MessageWin)).place(x=2,y=i))



    def SendReceive(self,user,client,win1,MessageWin):

        L=Label(win1,text="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",bg="white",fg="white")
        L.place(x=150,y=0)

        BorderLine1=Label(win1,text="____________________________",font=('Berlin Sans FB',20),fg="lightblue",bg="white")
        BorderLine1.place(x=150,y=25)
        
        L=Label(win1,text="You are Connect with",bg="white")
        L.place(x=150,y=0)
        L=Label(win1,text=user,font=("Berlin Sans FB",10,'bold'),bg="white",fg="#FFBE4A")
        L.place(x=270,y=0)
        Bottom=Frame(win1,bg="#FFBE4A")
        Bottom.place(x=150,y=450,width=300,height=50)
        Message= Text(Bottom,bg="#FFBE4A")
        Message.place(x=5,y=5,width=290,height=40)
        send=Button(win1,text="Send",bg="lightblue",fg="white",width=7,font=("Calibri",10,'bold'),height=3,command=lambda:CommunicationHandling1(Message,win1,client,user,MessageWin))
        send.place(x=450,y=450)

        


                                                                #######---------Main function------#######



win=Tk()
win.configure(background="#00AFF0")
win.title("iMessenger")
win.geometry("500x500")
win.wm_iconbitmap('icon.ico')
win.resizable( width = False , height = False )




l1=Label(text="Welcome to",bg="#00AFF0",fg="white",font=('Calibri',20))
l1.pack()
l2=Label(text="iMessenger",bg="#00AFF0",fg="white",font=('Calibri',40))
l2.pack()

port=IntVar()
name=StringVar()

l3=Label(text="Enter Your Name",bg="#00AFF0",fg="white",font=('Calibri',15))
l3.place(x=80,y=250)
text=Entry(win,textvariable=name)
text.place(x=260,y=255)


l4=Label(text="Port No",bg="#00AFF0",fg="white",font=('Calibri',15))
l4.place(x=80,y=200)
text1=Entry(win,textvariable=port)
text1.place(x=260,y=202)

Clear()

Enter=Button(win,text="Enter",bg="lightblue",fg="black",font=('Calibri',20),width=10,command=NewWindow)
Enter.place(x=90,y=350)

reset=Button(win,text="Reset",bg="lightblue",fg="black",font=('Calibri',20),width=10,command=Clear)
reset.place(x=250,y=350)

win.mainloop()    

