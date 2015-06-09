# -*- coding: utf-8 -*-
"""
Created on Mon Jun 08 18:05:00 2015

@author: Jakob Wittmann
"""

import sys
import demoConfigurationsGui
import demoMainGui
from PyQt4 import QtCore, QtGui
import PyQt4.Qwt5 as Qwt
from UDPServerDeamon import UDPServerDeamon

class Something():
    def __call__(self, e):
        print "Event empfangen"


class controller:
    
    def __init__(self):
        self.__srcIP="192.168.178.21"
        
    def start(self):
        app = QtGui.QApplication(sys.argv)
        
        self.win_demoMainGui = demoMainGui.QtGui.QMainWindow()
        self.ui_demoMainGui = demoMainGui.Ui_MainWindow()
        
        self.win_demoConfigurationsGui = demoConfigurationsGui.QtGui.QDialog()
        self.ui_demoConfigurationsGui = demoConfigurationsGui.Ui_Dialog()

        # start demoMainGui
    
        #win_demoMainGui, ui_demoMainGui=self.startDemoMainGui()
        self.__startDemoMainGui()
        #win_demoConfigurationsGui, ui_demoConfigurationsGui=startDemoConfigurationsGui()

        #WAIT UNTIL QT RETURNS EXIT CODE
        sys.exit(app.exec_())
        
    def __startDemoMainGui(self):
        #win_demoMainGui = demoMainGui.QtGui.QMainWindow()
        #ui_demoMainGui = demoMainGui.Ui_MainWindow()
        self.ui_demoMainGui.setupUi(self.win_demoMainGui)
        #ui_demoMainGui.timer = QtCore.QTimer()

        self.ui_demoMainGui.pushButtonConfigurations.clicked.connect(lambda: self.__startDemoConfigurationsGui())
        self.ui_demoMainGui.pushButtonStartServer.clicked.connect(lambda: self.__startServer())
        self.ui_demoMainGui.pushButtonStopServer.clicked.connect(lambda: self.__stopServer())
    
        self.win_demoMainGui.show()
        #return win_demoMainGui, ui_demoMainGui

    def __startDemoConfigurationsGui(self):
        #win_demoConfigurationsGui = demoConfigurationsGui.QtGui.QDialog()
        #ui_demoConfigurationsGui = demoConfigurationsGui.Ui_Dialog()
        self.ui_demoConfigurationsGui.setupUi(self.win_demoConfigurationsGui)
        #ui_demoConfigurationGui.timer = QtCore.QTimer()
        self.ui_demoConfigurationsGui.buttonBox.clicked.connect(lambda: self.__setSrcIP(self.ui_demoConfigurationsGui.lineEditSrcIP.text()))
        self.win_demoConfigurationsGui.show()
        
    def __startServer(self):
        self.serverDeamon = UDPServerDeamon(5)
        self.serverDeamon.daemon=True
        self.serverDeamon.setDatagramBufferSize(65535)
        self.serverDeamon.setMyUDPIP("10.27.192.90")
        self.serverDeamon.setMyUDPPort(60111)
        
        self.asdf=Something()
        self.serverDeamon.subscribe(self.asdf)
        
        self.serverDeamon.start()
        
    def __stopServer(self):
        self.serverDeamon.stopServer()
        self.serverDeamon.join()
        
    def __setSrcIP(self, srcIP):
        print "srcIP=", self.__srcIP
        self.__srcIP = srcIP
        print "srcIP=", self.__srcIP
    
    def __del__(self):
        print "Destruktor gestartet"

if __name__ == "__main__":
    
    c = controller()
    c.start()