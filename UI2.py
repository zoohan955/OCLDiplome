# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
import mainNEW as mn
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(605, 600)
        self.Results = QtWidgets.QLabel(Form)
        self.Results.setGeometry(QtCore.QRect(210, 10, 511, 231))
        self.Results.setObjectName("Results")
        
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.btn_PEARSON)

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 80, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.btn_SPIRMEN)

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 110, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.Drawing_Plots = QtWidgets.QPushButton(Form)
        self.Drawing_Plots.setGeometry(QtCore.QRect(40, 250, 75, 23))
        self.Drawing_Plots.setObjectName("Drawing_Plots")
        self.Drawing_Plots.clicked.connect(mn.Graph)

        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(163, 0, 20, 491))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 210, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Load_Btn = QtWidgets.QPushButton(Form)
        self.Load_Btn.setGeometry(QtCore.QRect(180, 460, 75, 23))
        self.Load_Btn.setObjectName("Load_Btn")
        self.Remove_btn = QtWidgets.QPushButton(Form)
        self.Remove_btn.setGeometry(QtCore.QRect(260, 460, 91, 23))
        self.Remove_btn.setObjectName("Remove_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Results.setText(_translate("Form", "Results"))
        self.pushButton.setText(_translate("Form", "Pearson"))
        self.pushButton_2.setText(_translate("Form", "Spirmen"))
        self.pushButton_3.setText(_translate("Form", "1-way"))
        self.Drawing_Plots.setText(_translate("Form", "Draw_Plots"))
        self.label.setText(_translate("Form", "Normal Check"))
        self.label_2.setText(_translate("Form", "Plots"))
        self.Load_Btn.setText(_translate("Form", "Load_DATA"))
        self.Remove_btn.setText(_translate("Form", "Remove_Arrays"))

    def btn_SPIRMEN(self):
        #self.Results.setText(str(mn.Spirmen(mn.X,mn.Y)))
        self.Label_OUTPUT(mn.Spirmen(mn.X,mn.Y))
    def btn_PEARSON(self):
        self.Label_OUTPUT(mn.Pirson(mn.X,mn.Y))

    
    def Label_OUTPUT(self,f):
        self.Results.setText(self.Results.text()+'\n'+str(f))
    





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StatsApp = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(StatsApp)
    StatsApp.show()
    sys.exit(app.exec_())