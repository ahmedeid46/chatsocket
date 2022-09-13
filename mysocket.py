import socket
import threading
s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
s.bind(("192.168.56.1",2435)) #my ip

def send():
    while(True):
        mess = input("Enter message to send..")
        b_mess = mess.encode()
        s.sendto(b_mess,("192.168.56.102",2435)) #anthor ip
        print("sent: ",mess)

def recive():
    while(True):
        b_mess = s.recvfrom(1024)
        mess = b_mess[0].decode()
        print('\nReceived: ',mess)

t1 = threading.Thread(target = recive)
t2 = threading.Thread(target = send)

t1.start()
t2.start()
