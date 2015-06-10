# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 09:37:29 2015

@author: Jakob Wittmann
"""

import demoContinuousViewGui
from UDPServerDeamon import UDPServerDeamon, Event

import numpy


class DemoContinuousView(object):
    def __init__(self):
        self.win_demoContinuousViewGui = demoContinuousViewGui.QtGui.QMainWindow()
        self.ui_demoContinuousViewGui = demoContinuousViewGui.Ui_MainWindow()
        
    def showGui(self):
        self.ui_demoContinuousViewGui.setupUi(self.win_demoContinuousViewGui)
        self.win_demoContinuousViewGui.show()
        
    def __call__(self, e):
        e.source.getDatagram()