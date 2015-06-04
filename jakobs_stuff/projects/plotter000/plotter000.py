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


numPoints=200000
numShifts=1
speed=2 #seconds for one complete roll of ys, xs
numPointsInWindow=1366/2
shiftFreq=120 #Hz

shiftWidth=int(numPoints/float(shiftFreq*speed))

incWidth=int(numPoints/numPointsInWindow)

xs=numpy.arange(numPoints)
ys=numpy.sin(3.14159*xs*10/numPoints)
xsTmp=numpy.arange(numPointsInWindow)
ysTmp=numpy.arange(numPointsInWindow, dtype=float)


def plotSomething():
    global ys, xs, xsTmp, ysTmp
    ys=numpy.roll(ys,-shiftWidth)
    #print "PLOTTING"
    for i in range(numPointsInWindow):
        xsTmp[i]=xs[i*incWidth]
        ysTmp[i]=ys[i*incWidth]
    c.setData(xsTmp, ysTmp)
    uiplot.qwtPlot.replot()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    ### SET-UP WINDOWS
    
    # WINDOW plot
    win_plot = ui_plot.QtGui.QMainWindow()
    uiplot = ui_plot.Ui_win_plot()
    uiplot.setupUi(win_plot)
    c=Qwt.QwtPlotCurve()  
    c.attach(uiplot.qwtPlot)

    uiplot.timer = QtCore.QTimer()
    uiplot.timer.start(1.0/shiftFreq)
    
    win_plot.connect(uiplot.timer, QtCore.SIGNAL('timeout()'), plotSomething) 
    

    ### DISPLAY WINDOWS
    win_plot.show()

    #WAIT UNTIL QT RETURNS EXIT CODE
    sys.exit(app.exec_())