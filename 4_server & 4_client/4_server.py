#!/usr/bin/env python
import socket, sys, os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #create a socket object
host = socket.gethostname()   #get local machine name
port = 8080;                  #reserve a port for your service
s.bind((host,port))           #bind to that port
s.listen(5)                   #now wait for client connection

c, addr = s.accept()          #establish connection with client
print 'New connection!!', addr

if os.fork():
	while True:
		receive = c.recv(1024)      #read the client's message/Receive no more than  1024 bytes
		sys.stdout.write(receive)   #print the client's message in monitor
		sys.stdout.flush()   #forces it to "flush" the buffer, meaning that it will write everything in the buffer to the terminal, even if normally it would wait before doing so.
else:
	while True:
		Line = sys.stdin.readline()  #reads from the keyboard
		c.send(Line);                #sends the message to the client

s.close()                     #close the connection
