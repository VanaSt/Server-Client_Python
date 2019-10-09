#!/usr/bin/env python
import socket, sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #create a socket object 
host = socket.gethostname()   #get local machine name
port = 8080                   #reserve a port for your service

s.connect((host,port))	      #connection with the server

while True:
	Line = sys.stdin.readline()  #reads from the keyboard
	s.send(Line);                #sends the message to the server

	receive = s.recv(1024)       #read the server's message/Receive no more than  1024 bytes
	sys.stdout.write(receive)    #print the server's message in monitor
	sys.stdout.flush()     #forces it to "flush" the buffer, meaning that it will write everything in the buffer to the terminal, even if normally it would wait before doing so.

s.close()                   #close the connection
