# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:45:56 2015

@author: Jakob Wittmann
"""

import socket
import time

UDP_IP = "10.27.192.90"
UDP_PORT = 60111
MESSAGE = "Hello, World!"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

val=0

while True:
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
    sock.sendto(str(val), (UDP_IP, UDP_PORT))
    if val==20:
        val=1
    else:
        ++val
    time.sleep(1)
    