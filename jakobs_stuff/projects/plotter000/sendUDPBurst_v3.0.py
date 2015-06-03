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

#DST_UDP_IP = "10.27.192.90"
DST_UDP_IP = "192.168.178.21"
DST_UDP_PORT = 60111
#MY_UDP_IP = "10.27.192.152"
MY_UDP_IP = "192.168.178.31"
MY_UDP_PORT = 60000

sleepTime = 3 #in milliseconds
datagramSizePref=2000 # bytes in UDP-Datagram
burstSize=1000
triggerSize=7700
sinPeriod=triggerSize/14.0

samplesPerDatagram=int(datagramSizePref)/3
datagramSize=samplesPerDatagram*3

# create multinimensional list for channel-data for one triggerSize
data=[[0 for x in range(triggerSize)] for x in range(3)]

# write channel 1: Trigger
data[0][0]=1

for i in range(triggerSize):
    # write channel 2: Ram
    data[1][i]=int((float(i)/triggerSize)*255.0)
    # wirte channel 3: FMCW-Signal
    data[2][i]=int((numpy.sin((numpy.pi/sinPeriod*i))+1.0)*255.0/2)

#create list of empty dataRaw-Buffer
dataRaw=[bytearray(datagramSize) for i in range(burstSize)]

#pick first burstSize rows of data and convert it to dataRaw
x=0
for i in range(burstSize):
    for j in range(samplesPerDatagram):
        pack_into('!3B', dataRaw[i], j*3, data[0][x], data[1][x], data[2][x])
        if x==triggerSize-1:
            x=0
        else:
            x=x+1

# create socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
# dem Socket eine IP und Port zuweisen. Wird das nicht gemacht, vergibt das Betriebssystem einen Port, der bei jeder sich nach jeder Nachricht ändern kann
sock.bind((MY_UDP_IP, MY_UDP_PORT))

print ">>> send burst:"
print "    samplesPerDatagram =", samplesPerDatagram
print "    datagramSize =      ", datagramSize
print "    burstSize =         ", burstSize
print ""

unpackString='!{}B'.format(datagramSize)
for i in range(0, burstSize):
    # doku: https://docs.python.org/2/library/struct.html
    sock.sendto(dataRaw[i], (DST_UDP_IP, DST_UDP_PORT))
    #print datetime.now(), ": ", unpack(unpackString, dataRaw[i]) # Ausgabe funktioniert!
    print datetime.now(), ": send Datagram!"   
    time.sleep(sleepTime/1000.0)

print "done"








