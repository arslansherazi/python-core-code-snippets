from tkinter import *
import sys
from _thread import *
import socket
import time

 

#Functions	


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
    left=LeftFrame(win1)
    upper=UpperFrame(win1)
    
    Center=Frame(win1,bg="white")
    Center.place(x=150,y=0,width=350,height=390)

     
    ConnectClient(p,n,win1)
    win1.mainloop()


def ConnectClient(p,n,win1):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = socket.gethostname()
    port = p
    client.connect((host,port))
    client.send(bytes(n,'utf-8'))
    
    def Threaded_Receive(client,i,win1):
        OnlineUser=[]
        while(1):
            tok=client.recv(1024)
            print(tok)
            if(tok==bytes("name",'utf-8')):
                i=i+30
                user=client.recv(1024)
                obj=Buttonn(user,win1,OnlineUser,i,client)
            elif(tok==bytes("message",'utf-8')):
                 
                
                 name=client.recv(1024)
                 msg=client.recv(1024)
                 
                 L=Label(win1,text="Received Message From",bg="white")
                 L.place(x=150,y=20)
                 L=Label(win1,text=name,font=("Berlin Sans FB",10,'bold'),bg="white",fg="#FFBE4A")
                 L.place(x=275,y=20)
                
                 
                 l=Label(win1,text=name,fg="#FFBE4A",font=("Berlin Sans FB",10,'bold'),bg="white")
                 l.place(x=150,y=inc[0])

                 inc[0]=inc[0]+20

                 l2=Label(win1,text=msg,bg="white",font=("Berlin Sans FB",10))
                 l2.place(x=180,y=inc[0])

                 
                 inc[0]=inc[0]+20
                 
                 
                 Bottom=Frame(win1,bg="#FFBE4A")
                 Bottom.place(x=150,y=450,width=300,height=50)
                 
                 Message= Text(Bottom,bg="#FFBE4A")
                 Message.place(x=5,y=5,width=290,height=40)
                 send=Button(win1,text="Send",bg="lightblue",fg="white",width=7,font=("Calibri",10,'bold'),height=3,command=lambda:CommunicationHandling1(Message,win1,client,name))
                 send.place(x=450,y=450)
                 
                
                
          
            
    i=20
    start_new_thread(Threaded_Receive,(client,i,win1))



def CommunicationHandling1(Message,win1,client,user):
    msg=Message.get("1.0",END)
    Message.delete("1.0",END)
        
    l=Label(win1,text="You to",bg="white",font=("Berlin Sans FB",10,'bold'))
    l.place(x=150,y=inc[0])

    l=Label(win1,text=user,bg="white",font=("Berlin Sans FB",10,'bold'),fg="#FFBE4A")
    l.place(x=195,y=inc[0])

    inc[0]=inc[0]+20
        
    l=Label(win1,text=msg,bg="white",font=("Berlin Sans FB",10))
    l.place(x=180,y=inc[0])
    inc[0]=inc[0]+20
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




#Classess

class LeftFrame:
    def __init__(self,root):
        Left=Frame(root,bg="lightblue")
        Left.place(x=0,y=0,width=150,height=500)
        OnlineLabel=Label(Left,text="Online Users",font=('Berlin Sans FB',20),bg="lightblue").pack()
        
class UpperFrame:
    def __init__(self,root1):
        upper1=Frame(root1,bg="lightblue")
        upper1.place(x=150,y=0,width=350,height=60)
        
        
        

class Buttonn:
    def __init__(self,user,win1,OnlineUser,i,client):
        OnlineUser.append(Button(win1,text=user,bg="lightblue",fg="white",font=("Calibri",10),width=20,command=lambda:self.SendReceive(user,client,win1)).place(x=0,y=i))



    def SendReceive(self,user,client,win1):
        
        L=Label(win1,text="You are Connect with",bg="white")
        L.place(x=150,y=0)
        L=Label(win1,text=user,font=("Berlin Sans FB",10,'bold'),bg="white",fg="#FFBE4A")
        L.place(x=270,y=0)
        Bottom=Frame(win1,bg="#FFBE4A")
        Bottom.place(x=150,y=450,width=300,height=50)
        Message= Text(Bottom,bg="#FFBE4A")
        Message.place(x=5,y=5,width=290,height=40)
        send=Button(win1,text="Send",bg="lightblue",fg="white",width=7,font=("Calibri",10,'bold'),height=3,command=lambda:CommunicationHandling1(Message,win1,client,user))
        send.place(x=450,y=450)


    def CommunicationHandling(self,Message,win1,client,user):
        msg=Message.get("1.0",END)
        Message.delete("1.0",END)

        
        l=Label(win1,text="You to",bg="white",font=("Berlin Sans FB",10,'bold'))
        l.place(x=150,y=inc[0])

        l=Label(win1,text=user,bg="white",font=("Berlin Sans FB",10,'bold'))
        l.place(x=195,y=inc[0])

        inc[0]=inc[0]+20
        
        l=Label(win1,text=msg,bg="white",font=("Berlin Sans FB",10))
        l.place(x=180,y=inc[0])

        inc[0]=inc[0]+20
        
        self.SendMessage(msg,user,client)

    def SendMessage(self,msg,user,client):
        print(msg)
        token="message"
        client.send(bytes(token,'utf-8'))
        time.sleep(1)
        client.send(user)
        time.sleep(1)
        client.send(bytes(msg,'utf-8'))
        time.sleep(1)
        


#Main function

global inc
inc=[60]

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

