#!/usr/bin/env python3

import socket

UDP_IP_ADDRESS = "127.0.0.123"
UDP_PORT = 12345
buffer=4096


address = (UDP_IP_ADDRESS ,UDP_PORT)

sock_udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:

  message = input("Enter your message:")
  if message == "exit":
    break
  sock_udp.sendto(message.encode(),address)
  response,addr = sock_udp.recvfrom(buffer)
  print("Server response => %s" % response)

sock_udp.close()



