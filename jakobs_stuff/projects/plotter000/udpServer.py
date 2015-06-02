# -*- coding: utf-8 -*-
"""
Created on Tue Jun 02 17:33:21 2015

@author: Jakob Wittmann
"""

import socket

#UDP_IP = "192.168.178.30"
#UDP_IP = "169.254.207.255"
UDP_IP = "127.0.0.1"
UDP_PORT = 0xAAAA

sock = socket.socket(socket.AF_INET, # Internet
                 socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data