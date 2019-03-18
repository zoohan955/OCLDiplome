# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import mainNEW as mn
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StatsApp(object):
    def setupUi(self, StatsApp):
        StatsApp.setObjectName("StatsApp")
        StatsApp.resize(882, 606)
        self.centralwidget = QtWidgets.QWidget(StatsApp)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(190, 10, 20, 551))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.SPIRMEN = QtWidgets.QPushButton(self.centralwidget)
        self.SPIRMEN.setGeometry(QtCore.QRect(10, 80, 181, 23))
        self.SPIRMEN.setObjectName("SPIRMEN")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.PIRSON = QtWidgets.QPushButton(self.centralwidget)
        self.PIRSON.setGeometry(QtCore.QRect(10, 120, 181, 23))
        self.PIRSON.setObjectName("PIRSON")
        self.ONEWAY = QtWidgets.QPushButton(self.centralwidget)
        self.ONEWAY.setGeometry(QtCore.QRect(10, 160, 181, 23))
        self.ONEWAY.setObjectName("ONEWAY")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 300, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.PLOT = QtWidgets.QPushButton(self.centralwidget)
        self.PLOT.setGeometry(QtCore.QRect(10, 350, 181, 23))
        self.PLOT.setObjectName("PLOT")
        self.PLOT.clicked.connect(self.btn_click)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 881, 561))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        StatsApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StatsApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 882, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        StatsApp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StatsApp)
        self.statusbar.setObjectName("statusbar")
        StatsApp.setStatusBar(self.statusbar)
        self.actionLoadData = QtWidgets.QAction(StatsApp)
        self.actionLoadData.setObjectName("actionLoadData")
        self.actionExit = QtWidgets.QAction(StatsApp)
        self.actionExit.setObjectName("actionExit")
        self.actionRemoveData = QtWidgets.QAction(StatsApp)
        self.actionRemoveData.setObjectName("actionRemoveData")
        self.actionSaveResults = QtWidgets.QAction(StatsApp)
        self.actionSaveResults.setObjectName("actionSaveResults")
        self.actionExit_2 = QtWidgets.QAction(StatsApp)
        self.actionExit_2.setObjectName("actionExit_2")
        self.menuFile.addAction(self.actionLoadData)
        self.menuFile.addAction(self.actionRemoveData)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSaveResults)
        self.menuFile.addAction(self.actionExit_2)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(StatsApp)
        QtCore.QMetaObject.connectSlotsByName(StatsApp)

    def btn_click(self):
        self.PLOT.addAction(mn.Graphical(mn.X,mn.Y))

    def retranslateUi(self, StatsApp):
        _translate = QtCore.QCoreApplication.translate
        StatsApp.setWindowTitle(_translate("StatsApp", "MainWindow"))
        self.SPIRMEN.setText(_translate("StatsApp", "CheckSpirmen"))
        self.label.setText(_translate("StatsApp", "NormalCheck"))
        self.PIRSON.setText(_translate("StatsApp", "CheckPirson"))
        self.ONEWAY.setText(_translate("StatsApp", "Check-1WAY"))
        self.label_2.setText(_translate("StatsApp", "Plots"))
        self.PLOT.setText(_translate("StatsApp", "Plot"))
        self.menuFile.setTitle(_translate("StatsApp", "File"))
        self.actionLoadData.setText(_translate("StatsApp", "LoadData"))
        self.actionExit.setText(_translate("StatsApp", "Exit"))
        self.actionRemoveData.setText(_translate("StatsApp", "RemoveData"))
        self.actionSaveResults.setText(_translate("StatsApp", "SaveResults"))
        self.actionExit_2.setText(_translate("StatsApp", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StatsApp = QtWidgets.QMainWindow()
    ui = Ui_StatsApp()
    ui.setupUi(StatsApp)
    StatsApp.show()
    sys.exit(app.exec_())

