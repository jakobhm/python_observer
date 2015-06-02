import ui_plot
import sys
import numpy
from PyQt4 import QtCore, QtGui
import PyQt4.Qwt5 as Qwt

numPoints=1000
#erstellt array mit 'numPoints' Elementen, abstant: 1
xs=numpy.arange(numPoints)
#berechnet zu jedem Wert in ys den Sin
ys=numpy.sin(3.14159*xs*10/numPoints)

def plotSomething():
    # in der Funktion kann auf ys aus main zugegriffen werden
    global ys
    # sift left, linker Wert wird rechts wieder eingefügt
    ys=numpy.roll(ys,-1)
    #print "PLOTTING"
    c.setData(xs, ys)
    uiplot.qwtPlot.replot()   

if __name__ == "__main__":
    #GUI-Applikation wird erzeugt
    app = QtGui.QApplication(sys.argv)

    ### SET-UP WINDOWS
    
    # WINDOW plot
    #erzeugt ein Fenster
    win_plot = ui_plot.QtGui.QMainWindow()
    uiplot = ui_plot.Ui_win_plot()
    uiplot.setupUi(win_plot)
    uiplot.btnA.clicked.connect(plotSomething)
    uiplot.btnB.clicked.connect(lambda: uiplot.timer.setInterval(100.0))
    uiplot.btnC.clicked.connect(lambda: uiplot.timer.setInterval(1.0))
    uiplot.btnD.clicked.connect(lambda: uiplot.timer.setInterval(0.1))
    # erstellt ein "Werteobjekt" für Plot
    c=Qwt.QwtPlotCurve()
    # hängt das QwtPlot-Widget an "Werteobjekt" an
    c.attach(uiplot.qwtPlot)

    # erzeugt Timer
    uiplot.timer = QtCore.QTimer()
    #
    uiplot.timer.start(100.0)
    # win_plot soll plotSimething ausführen, sobald uiplot.timer 'timeout()' sendet
    # Doku: http://doc.qt.io/qt-4.8/qobject.html#connect-3
    win_plot.connect(uiplot.timer, QtCore.SIGNAL('timeout()'), plotSomething) 

    ### DISPLAY WINDOWS
    win_plot.show()

    #WAIT UNTIL QT RETURNS EXIT CODE
    # app.exec_() startet das Fenster
    sys.exit(app.exec_())