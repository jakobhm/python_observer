# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_plot.ui'
#
# Created: Thu Jun 04 19:27:47 2015
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(684, 445)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(525, 344))
        self.centralwidget.setMaximumSize(QtCore.QSize(10000, 10000))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.qwtPlot = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot.setObjectName(_fromUtf8("qwtPlot"))
        self.horizontalLayout.addWidget(self.qwtPlot)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelNumPoints = QtGui.QLabel(self.centralwidget)
        self.labelNumPoints.setObjectName(_fromUtf8("labelNumPoints"))
        self.verticalLayout.addWidget(self.labelNumPoints)
        self.spinBoxNumPoints = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxNumPoints.setMinimum(1)
        self.spinBoxNumPoints.setMaximum(1000000000)
        self.spinBoxNumPoints.setObjectName(_fromUtf8("spinBoxNumPoints"))
        self.verticalLayout.addWidget(self.spinBoxNumPoints)
        self.labelNumPointsInWindow = QtGui.QLabel(self.centralwidget)
        self.labelNumPointsInWindow.setObjectName(_fromUtf8("labelNumPointsInWindow"))
        self.verticalLayout.addWidget(self.labelNumPointsInWindow)
        self.spinBoxNumPointsInWindow = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxNumPointsInWindow.setMinimum(1)
        self.spinBoxNumPointsInWindow.setMaximum(1000000000)
        self.spinBoxNumPointsInWindow.setObjectName(_fromUtf8("spinBoxNumPointsInWindow"))
        self.verticalLayout.addWidget(self.spinBoxNumPointsInWindow)
        self.labelShiftFreq = QtGui.QLabel(self.centralwidget)
        self.labelShiftFreq.setObjectName(_fromUtf8("labelShiftFreq"))
        self.verticalLayout.addWidget(self.labelShiftFreq)
        self.spinBoxShiftFreq = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxShiftFreq.setMinimum(1)
        self.spinBoxShiftFreq.setMaximum(1000000)
        self.spinBoxShiftFreq.setObjectName(_fromUtf8("spinBoxShiftFreq"))
        self.verticalLayout.addWidget(self.spinBoxShiftFreq)
        self.labelSpeed = QtGui.QLabel(self.centralwidget)
        self.labelSpeed.setObjectName(_fromUtf8("labelSpeed"))
        self.verticalLayout.addWidget(self.labelSpeed)
        self.doubleSpinBoxSpeed = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxSpeed.setDecimals(4)
        self.doubleSpinBoxSpeed.setMinimum(0.0001)
        self.doubleSpinBoxSpeed.setMaximum(999999999.99)
        self.doubleSpinBoxSpeed.setObjectName(_fromUtf8("doubleSpinBoxSpeed"))
        self.verticalLayout.addWidget(self.doubleSpinBoxSpeed)
        self.pushButtonAnwenden = QtGui.QPushButton(self.centralwidget)
        self.pushButtonAnwenden.setObjectName(_fromUtf8("pushButtonAnwenden"))
        self.verticalLayout.addWidget(self.pushButtonAnwenden)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.labelShiftWidth = QtGui.QLabel(self.centralwidget)
        self.labelShiftWidth.setObjectName(_fromUtf8("labelShiftWidth"))
        self.verticalLayout.addWidget(self.labelShiftWidth)
        self.labelIncWidth = QtGui.QLabel(self.centralwidget)
        self.labelIncWidth.setObjectName(_fromUtf8("labelIncWidth"))
        self.verticalLayout.addWidget(self.labelIncWidth)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.labelNumPoints.setText(_translate("MainWindow", "Punkte Speicher", None))
        self.labelNumPointsInWindow.setText(_translate("MainWindow", "Punkte im Fenster", None))
        self.labelShiftFreq.setText(_translate("MainWindow", "Draw Frequency", None))
        self.labelSpeed.setText(_translate("MainWindow", "Speed", None))
        self.pushButtonAnwenden.setText(_translate("MainWindow", "Anwenden", None))
        self.labelShiftWidth.setText(_translate("MainWindow", "TextLabel", None))
        self.labelIncWidth.setText(_translate("MainWindow", "TextLabel", None))

from PyQt4 import Qwt5



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    win_plot = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(win_plot)
    win_plot.show()
    sys.exit(app.exec_())