# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:45:56 2015

@author: Jakob Wittmann
"""

import socket
import time
from struct import *
from datetime import datetime
import numpy

DST_UDP_IP = "10.27.192.90"
DST_UDP_PORT = 60111
MY_UDP_IP = "10.27.192.152"
MY_UDP_PORT = 60000

sleepTime = 3 #in milliseconds
burstSize=1000
periodSize=7700

data=[[0 for x in range(periodSize)] for x in range(3)]

data[0][0]=1

for i in range(periodSize):
    data[1][i]=255/burstSize*i
    data[2][i]=int(numpy.sin(numpy.pi/(periodSize/14.0)*i*255))

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
# dem Socket eine IP und Port zuweisen. Wird das nicht gemacht, vergibt das Betriebssystem einen Port, der bei jeder sich nach jeder Nachricht ändern kann
sock.bind((MY_UDP_IP, MY_UDP_PORT))

print ">>> send burst:"
print "    burstSize=", burstSize
print ""

for i in range(0, burstSize):
    # doku: https://docs.python.org/2/library/struct.html
    sock.sendto(pack('!iii', data[0], data[1], data[2]), (DST_UDP_IP, DST_UDP_PORT))    
    print datetime.now(), ": ", data
    data= [j+1 for j in data]
    time.sleep(sleepTime/1000.0)

print "done"