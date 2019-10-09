#!/usr/bin/env python
import socket, sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #create a socket object 
host = socket.gethostname()   #get local machine name
port = 8080                   #reserve a port for your service

s.connect((host,port))        #connection with the server

Line = sys.stdin.readline()   #reads from the keyboard
s.send(Line);                 #sends the message to the server

s.close()                     #close the connection
