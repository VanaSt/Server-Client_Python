#!/usr/bin/env python3
import socket, sys, os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #create a socket object
host = socket.gethostname()   #get local machine name
port = 8080;                  #reserve a port for your service
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))           #bind to that port
s.listen(5)                   #now wait for client connection
clients = 3
client_3 = []

while len(client_3) < clients:  #for more than 3 clients, messages will not be read
	c, addr = s.accept()  #establish a connection with the  client
	print 'New connection!!', addr
	client_3.append(c)    #adds its argument as a single element to the end of a list     

pids = []                    #pid: process id
for client in client_3:

	if not os.fork():
		while True:
			receive = client.recv(1024)     #read the client's message/Receive no more than 1024 bytes
			for c in client_3:
				if c != client:
					c.send(receive)
	else:
		pids.append(os.fork())

for pid in pids:
	os.waitpid(pid, 0)      #wait for any child process whose process group ID is equal to that of the calling process
	
