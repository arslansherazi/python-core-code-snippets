import socket
import sys
from _thread import *
import time



def Threaded_Function(c,):
    
    name = c.recv(1024)
    names.append(name)
    clients.update({name:c})
    token="name"
    for i in range(len(names)-1):
        c.send(bytes(token,'utf-8'))
        time.sleep(1)
        c.send(names[i])
		
    for i in range(len(names)-1):
        clients[names[i]].send(bytes(token,'utf-8'))
        time.sleep(1)
        clients[names[i]].send(name)

    start_new_thread(Send,(c,name))

def Send(c,name):
    while(1):
        t=c.recv(1024)
        print(t)
        nam=c.recv(1024)
        print(nam)
        msg=c.recv(1024)
        print(msg)
        
        clients[nam].send(t)
        time.sleep(1)
        clients[nam].send(name)
        time.sleep(1)
        clients[nam].send(msg)
        time.sleep(1)
    




 

                                        #MAIN FUNCTION

if__name__="__main__"


global clients
clients={}
names=[]
num=0

HOST = ''
PORT = 6467

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

s.listen(50)

while 1:

    c, addr = s.accept()
    print ('Connected with ' + addr[0] + ':' + str(addr[1]))
    start_new_thread(Threaded_Function,(c,))

s.close()
