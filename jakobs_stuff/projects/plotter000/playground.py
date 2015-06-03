# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 13:04:43 2015

@author: Sübinger
"""

import socket
import time
from struct import *
from datetime import datetime

size=5
data=[2,1,0]

print data

dataRaw=bytearray(3)
for i in range(0, 3):
    pack_into('!B', dataRaw, i, data[i])

print dataRaw
print unpack('!3B', dataRaw)


print "done"