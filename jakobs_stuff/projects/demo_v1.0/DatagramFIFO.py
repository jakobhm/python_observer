# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 08:18:10 2015

@author: Jakob Wittmann
"""

class DatagramFIFO():
    def __init__(self, bufSize):
        self.__fifo=[bytearray() for x in range(bufSize)]
        self.__ptrStart=0
        self.__ptrEnd=0
        self.__size=0
        self.__bufSize=bufSize
        
    def push(self, newDatagram):
        if self.isFull():
            self.__ptrStart=self.__incPtr(self.__ptrStart)
        else:
            self.__size = self.__size + 1
        
        self.__fifo[self.__ptrEnd]=newDatagram
        self.__ptrEnd=self.__incPtr(self.__ptrEnd)
        
    def pushEmpty(self):
        self.push(bytearray())
        
    def pull(self):
        if self.isEmpty():
            answer=None
        else:
            answer=self.__fifo[self.__ptrStart]
            self.__ptrStart=self.__incPtr(self.__ptrStart)
            self.__size=self.__size-1
        return answer
        
    def empty(self):
        self.__ptrStart=0
        self.__ptrEnd=0
        self.__size=0
        
    def getSize(self):
        return self.__size
        
    def isEmpty(self):
        return self.__size == 0
        
    def isFull(self):
        return self.__size == self.__bufSize
        
    def getBuffer(self):
        return self.__fifo
        
    def __incPtr(self, ptr):
        if ptr == self.__bufSize-1:
            ptr = 0
        else:
            ptr = ptr+1
        return ptr
        
    def __decPtr(self, ptr):
        if ptr == 0:
            ptr = self.__bufSize
        else:
            ptr = ptr-1
        return ptr