#!/usr/bin/env python3
import socket, sys, os, select
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #create a socket object
host = socket.gethostname()   #get local machine name
port = 8080;                  #reserve a port for your service
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))           #bind to that port
s.listen(5)                   #now wait for client connection
clients = [s]

while True:
	(evnt_enter, evnt_sort, evnt_exception) = select.select(clients, [], [])
	for new_client in evnt_enter:
		if (new_client == s):
			connection, addr = s.accept()  #establish a connection with the  client
			print "New connection!!", addr
			clients.append(connection)    #adds its argument as a single element to the end of a list     
			continue

		line = new_client.recv(1024)    #read the client's message
		if not line:
			clients.remove(new_client)  #client disconnected
		else:
			for client in clients:
				if client not in [s, new_client]:
					client.send(line)

	
