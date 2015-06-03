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
windowPeriod=periodSize/14.0

# create multinimensional list for channel-data
data=[[0 for x in range(periodSize)] for x in range(3)]

for i in range(periodSize):
    # write channel 1: Trigger
    if i%int(periodSize/14.0) == 0:
        data[0][i]=1
    # write channel 2: Ram
    data[1][i]=int(((i/windowPeriod)%1)*255.0)
    # wirte channel 3: FMCW-Signal
    data[2][i]=int((numpy.sin((numpy.pi/windowPeriod*i))+1.0)*255.0/2)

#create list of empty dataRaw-Buffer
dataRaw=[bytearray(3) for i in range(burstSize)]

#pick first burstSize rows of data and convert it to dataRaw
for i in range(burstSize):
    pack_into('!3B', dataRaw[i], 0, data[0][i], data[1][i], data[2][i])

# create socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
# dem Socket eine IP und Port zuweisen. Wird das nicht gemacht, vergibt das Betriebssystem einen Port, der bei jeder sich nach jeder Nachricht ändern kann
sock.bind((MY_UDP_IP, MY_UDP_PORT))

print ">>> send burst:"
print "    burstSize=", burstSize
print ""

for i in range(0, burstSize):
    # doku: https://docs.python.org/2/library/struct.html
    sock.sendto(dataRaw[i], (DST_UDP_IP, DST_UDP_PORT))
    print datetime.now(), ": ", unpack('!3B', dataRaw[i])
    time.sleep(sleepTime/1000.0)

print "done"








