# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoMainGui.ui'
#
# Created: Mon Jun 08 18:01:05 2015
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
        MainWindow.resize(551, 284)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButtonStartServer = QtGui.QPushButton(self.centralwidget)
        self.pushButtonStartServer.setObjectName(_fromUtf8("pushButtonStartServer"))
        self.verticalLayout.addWidget(self.pushButtonStartServer)
        self.pushButtonStartContView = QtGui.QPushButton(self.centralwidget)
        self.pushButtonStartContView.setObjectName(_fromUtf8("pushButtonStartContView"))
        self.verticalLayout.addWidget(self.pushButtonStartContView)
        self.pushButtonStartTriggerView = QtGui.QPushButton(self.centralwidget)
        self.pushButtonStartTriggerView.setObjectName(_fromUtf8("pushButtonStartTriggerView"))
        self.verticalLayout.addWidget(self.pushButtonStartTriggerView)
        self.pushButtonConfigurations = QtGui.QPushButton(self.centralwidget)
        self.pushButtonConfigurations.setObjectName(_fromUtf8("pushButtonConfigurations"))
        self.verticalLayout.addWidget(self.pushButtonConfigurations)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButtonStartServer.setText(_translate("MainWindow", "Start Server", None))
        self.pushButtonStartContView.setText(_translate("MainWindow", "Open Conitnuous View", None))
        self.pushButtonStartTriggerView.setText(_translate("MainWindow", "Open Triggered View", None))
        self.pushButtonConfigurations.setText(_translate("MainWindow", "Configurations", None))