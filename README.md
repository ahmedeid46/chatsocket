# chatsocket
## Training Project
## Introduction and Important Definitions:
The project is a chat socket between devices connected to the same network. To achieve this connection, we must know the following
IP Address: An Internet Protocol address (IP address) is a numerical label such as 192.0.2.1 that is connected to a computer network that uses the Internet Protocol for communication.
TCP Protocol: TCP stands for Transmission Control Protocol. It is a transport layer protocol that facilitates the transmission of packets from source to destination.
Port Number: Specific port numbers are reserved to identify specific services so that an arriving packet can be easily forwarded to a running application.
We also used Threading for separate flow of execution. This means that program will have two things or more happening at once and user for parallel programming. But for most Python 3 implementations the different threads do not actually execute at the same time: they merely appear to.
One of the important things in the program is the socket, which is as follows the combination of the source and destination IP address and source and
destination Ethernet address. the combination of a source IP address and port number or a destination IP address and port number. the combination of the source and destination sequence and acknowledgment numbers .the combination of the source and destination sequence numbers and port numbers
Explanation: A socket is a combination of the source IP address and source port or the destination IP address and the destination port number
## Project Details:
The code was written using the Python language. We installed the necessary packages such as socket and threading. We called them via import. Then we created an object from the socket and then we used bind, a function inside the socket library. The task of opening the port needed to start the socket service is inserted into it. The IP of the device on which the code will run and the port to be opened, then the functions of sending and receiving are done as follows
The function of the send is at the beginning of an infinite loop at the beginning, a message will appear, “Enter message to send...” When the message is entered, it will be received in a variable named mess, and then this message is encrypted and sent to the other party as follows
 socket_obj .sendto(b_mess,([ip] ,[port] ))
Then the message sent is printed
As for the function of receiving, it will receive the message via
socket_obj .recvfrom()
 The two devices must be open to the same port, and then we start decoding the message and displaying it
For the two functions to work together in receiving and sending, we use parallel programming. We make 2 objects of threading, and the target is the name of the function, and then we make a start for both objects.
Note:For the program to work, it must be placed on two devices within the same network or on devices outside the network, specifying the public IP of both devices and modifying them in the code

