# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 08:58:28 2015

@author: Jakob Wittmann
"""

from DatagramFIFO import DatagramFIFO


def printStatus():
    global fifo
    print "Leer: ", fifo.isEmpty()
    print "Voll: ", fifo.isFull()
    print "Size: ", fifo.getSize()
    print "Inhalt:"
    for i in range(5):
        print "   ",i," : ", (fifo.getBuffer())[i]
        
    print ""


d0=bytearray("ba 0")
d1=bytearray("ba 1")
d2=bytearray("ba 2")
d3=bytearray("ba 3")
d4=bytearray("ba 4")
d5=bytearray("ba 5")
d6=bytearray("ba 6")
d7=bytearray("ba 7")




fifo=DatagramFIFO(5)

#printStatus()

fifo.push(d0)
printStatus()
fifo.push(d1)
printStatus()
fifo.push(d2)
printStatus()
fifo.push(d3)
printStatus()
fifo.push(d4)
printStatus()
fifo.push(d5)
printStatus()
fifo.push(d6)
printStatus()
fifo.push(d7)
printStatus()

print "pull: ", fifo.pull()
print "pull: ", fifo.pull()
print "pull: ", fifo.pull()
print "pull: ", fifo.pull()
print "pull: ", fifo.pull()
print "pull: ", fifo.pull()
print ""
printStatus()