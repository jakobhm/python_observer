# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 07:45:33 2015

@author: Jakob Wittmann
"""

import threading
import socket
from datetime import datetime
from DatagramFIFO import DatagramFIFO

class Event(object):
    def __init__(self):
        self.source=None

class UDPServerDeamon(threading.Thread):
    #lock = threading.Lock()
    
    def __init__(self, datagramFIFOSize):
        super(UDPServerDeamon, self).__init__()
        self.__MY_UDP_IP = "192.168.178.31"
        self.__MY_UDP_PORT = 60111
        self.__DATAGRAM_BUFFER_SIZE=65535
        self.__serverActive=True
        
        if datagramFIFOSize > 1:
            self.__datagramFIFOSize=datagramFIFOSize
        else:
            self.__datagramFIFOSize=2
        self.__datagramFIFOHighWater=self.__datagramFIFOSize-1
        self.__fifo=DatagramFIFO(self.__datagramFIFOSize)
         
        self.__callbacks=[]
        
         
        print "Server erstellt"
         
    def setMyUDPIP(self, myUDPIP):
        self.__MY_UDP_IP=myUDPIP
        
    def setMyUDPPort(self, myUDPPort):
        self.__MY_UDP_PORT=myUDPPort
        
    def setDatagramBufferSize(self, datagramBufferSize):
        self.__BUFFER_SIZE=datagramBufferSize
        
    def setFIFOHighWater(self, size):
        if size > 0:
            self.__datagramFIFOHighWater=size
        else:
            self.__datagramFIFOHighWater=1

    def run(self):
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        self.sock.bind((self.__MY_UDP_IP, self.__MY_UDP_PORT))         
        self.sock.settimeout(1)
        print "socket erstellt"
         
        while self.__serverActive:
            print "empfange..."
            addr = ""
            while self.__serverActive:
                try:
                    dataRaw, addr = self.sock.recvfrom(self.__DATAGRAM_BUFFER_SIZE)
                except socket.timeout:
                    pass
                else:
                    break
            
            if self.__serverActive:
                #UDPServerDeamon.lock.acquire()
                self.__fifo.push(dataRaw)
                
                if self.__fifo.getSize() >= self.__datagramFIFOHighWater:
                    flag_fire = True
                else:
                    flag_fire = False

                #UDPServerDeamon.lock.release()
                                
                if flag_fire:
                    self.__fire()
                    
                print ('at {} message from {}'.format(datetime.now(), addr))
             
    def stopServer(self):
        self.__serverActive=False
        self.sock.close()
        
    def subscribe(self, callback):
        self.__callbacks.append(callback)
        
    def __fire(self):
        e = Event()
        e.source=self
        for cb in self.__callbacks:
            cb(e)
            
    def getDatagram(self):
        #UDPServerDeamon.lock.acquire()
        if not self.__fifo.isEmpty():
            answer = self.__fifo.pull()
        #UDPServerDeamon.lock.release()
        return answer