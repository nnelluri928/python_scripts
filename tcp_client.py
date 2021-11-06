#!/usr/bin/python 


import socket

host = '127.0.0.123'
port = 12345
buffer_size = 1024



MESSAGE = "Hellow world ,Thsi is my first message"
sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

sock_tcp.connect((host,port))

sock_tcp.send(MESSAGE.encode('utf-8'))

data = sock_tcp.recv(buffer_size)

