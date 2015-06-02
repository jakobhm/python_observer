# -*- coding: utf-8 -*-
"""
Created on Tue Jun 02 14:58:40 2015

@author: Jakob Wittmann
"""

import ui_plot
import sys
import numpy
from PyQt4 import QtCore, QtGui
import PyQt4.Qwt5 as Qwt


numPoints=1000000
numShifts=10000
xs=numpy.arange(numPoints)
ys=numpy.sin(3.14159*xs*10/numPoints)


if __name__ == "__main__":
    
    for x in range(0, numShifts):
        #print x
        ys=numpy.roll(ys, 1)
        
    print "THE END"