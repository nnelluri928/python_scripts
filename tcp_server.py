#!/usr/binpython 

import socket

host = '127.0.0.123'
port = 12345
buffer_size = 1024

sock_tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock_tcp.bind((host,port))

sock_tcp.listen(5)

conn,addr = sock_tcp.accept()

print("conn address:",addr)

while True:

  data = sock_tcp.recv(buffer_size)
  if not data:
    break
  else:
    print("data received: {}".format(data.decode('utf-8')))


  conn.send(data)

  
