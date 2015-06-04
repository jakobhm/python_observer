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
import time


SAMPLE_RATE=100000 #Hz

numPoints=200000
speed=float(2) #seconds for one complete roll of ys, xs
numPointsInWindow=1366/2
shiftFreq=120 #Hz

#params
shiftWidth=0
incWidth=0
xs=numpy.arange(0)
ys=numpy.arange(0, dtype=float)
xsTmp=numpy.arange(0)
ysTmp=numpy.arange(0, dtype=float)



def calcParams():
    global shiftWidth, incWidth, xs, ys, xsTmp, ysTmp
    shiftWidth=int(numPoints/float(shiftFreq*speed))

    incWidth=int(numPoints/numPointsInWindow)

    xs=numpy.arange(numPoints)
    ys=numpy.sin(3.14159*xs*10/numPoints)
    xsTmp=numpy.arange(numPointsInWindow)
    ysTmp=numpy.arange(numPointsInWindow, dtype=float)
    
def updateDisplay():
    global uiplot
    uiplot.spinBoxNumPoints.setValue(numPoints)
    uiplot.spinBoxNumPointsInWindow.setValue(numPointsInWindow)
    uiplot.spinBoxShiftFreq.setValue(shiftFreq)
    uiplot.doubleSpinBoxSpeed.setValue(float(speed))
    
    uiplot.labelIncWidth.setText('incWidth:   {}'.format(incWidth))
    uiplot.labelShiftWidth.setText('shiftWidth: {}'.format(shiftWidth))
    
def updateParams():
    global numPoints, speed, numPointsInWindow, shiftFreq, uiplot
    numPoints=uiplot.spinBoxNumPoints.value()
    speed=uiplot.doubleSpinBoxSpeed.value()
    if uiplot.spinBoxNumPointsInWindow.value() <= numPoints:
        numPointsInWindow=uiplot.spinBoxNumPointsInWindow.value()
    else:
        numPointsInWindow=numPoints
        
    shiftFreq=uiplot.spinBoxShiftFreq.value()
    calcParams()
    updateDisplay()
    uiplot.timer.setInterval(1000.0/shiftFreq)   
    print ">>> changed Parameter:"
    print "    numPoints:         ", numPoints
    print "    speed:             ", speed
    print "    numPointsInWindow: ", numPointsInWindow
    print "    shiftFreq:         ", shiftFreq    
    

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
    
    calcParams()
    
    app = QtGui.QApplication(sys.argv)

    ### SET-UP WINDOWS
    
    # WINDOW plot
    win_plot = ui_plot.QtGui.QMainWindow()
    uiplot = ui_plot.Ui_MainWindow()
    uiplot.setupUi(win_plot)
    updateDisplay()
    uiplot.pushButtonAnwenden.clicked.connect(lambda: updateParams())
    #uiplot.pushButtonAnwenden.clicked.connect(lambda: changeFreq())    
    c=Qwt.QwtPlotCurve()
    c.attach(uiplot.qwtPlot)

    uiplot.timer = QtCore.QTimer()
    
    win_plot.connect(uiplot.timer, QtCore.SIGNAL('timeout()'), plotSomething) 

    ### DISPLAY WINDOWS
    win_plot.show()
    
    uiplot.timer.start(1000.0/shiftFreq)
    
    #while True:
    #    plotSomething()
    #    time.sleep(1.0/shiftFreq)

    #WAIT UNTIL QT RETURNS EXIT CODE
    sys.exit(app.exec_())