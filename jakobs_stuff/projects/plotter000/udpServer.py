# -*- coding: utf-8 -*-
"""
Created on Tue Jun 02 17:33:21 2015

@author: Jakob Wittmann
"""

import socket
from struct import *
from datetime import datetime

#UDP_IP = "192.168.178.30"
#UDP_IP = "169.254.207.255"
MY_UDP_IP = "10.27.192.90"
MY_UDP_PORT = 60111

sock = socket.socket(socket.AF_INET, # Internet
                 socket.SOCK_DGRAM) # UDP
sock.bind((MY_UDP_IP, MY_UDP_PORT))

while True:
    dataRaw, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    data=unpack('!3B',dataRaw)
    print ('at {} message from {}: {}'.format(datetime.now(), addr, data))