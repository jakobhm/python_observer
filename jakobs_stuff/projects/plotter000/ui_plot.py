# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_plot.ui'
#
# Created: Tue Jun 02 14:58:31 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_win_plot(object):
    def setupUi(self, win_plot):
        win_plot.setObjectName(_fromUtf8("win_plot"))
        win_plot.resize(940, 588)
        self.centralwidget = QtGui.QWidget(win_plot)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.qwtPlot = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot.setLineWidth(1)
        self.qwtPlot.setObjectName(_fromUtf8("qwtPlot"))
        self.verticalLayout.addWidget(self.qwtPlot)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnLeft = QtGui.QPushButton(self.centralwidget)
        self.btnLeft.setObjectName(_fromUtf8("btnLeft"))
        self.horizontalLayout.addWidget(self.btnLeft)
        self.btnRight = QtGui.QPushButton(self.centralwidget)
        self.btnRight.setObjectName(_fromUtf8("btnRight"))
        self.horizontalLayout.addWidget(self.btnRight)
        self.verticalLayout.addLayout(self.horizontalLayout)
        win_plot.setCentralWidget(self.centralwidget)

        self.retranslateUi(win_plot)
        QtCore.QMetaObject.connectSlotsByName(win_plot)

    def retranslateUi(self, win_plot):
        win_plot.setWindowTitle(_translate("win_plot", "MainWindow", None))
        self.btnLeft.setText(_translate("win_plot", "<<<", None))
        self.btnRight.setText(_translate("win_plot", ">>>", None))

from PyQt4 import Qwt5
