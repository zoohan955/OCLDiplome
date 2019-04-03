# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
import mainNEW as mn
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(898, 490)
        self.DATA=self.DATA=''
        self.fname=self.fname=''
        self.Results=QtWidgets.QLabel(Form)
        self.Results.setGeometry(QtCore.QRect(180,40,701,401))
        
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
        self.pushButton_3.clicked.connect(self.btn_One_Way)

        self.KRUSKAL=QtWidgets.QPushButton(Form)
        self.KRUSKAL.setGeometry(QtCore.QRect(50,140,75,23))
        self.KRUSKAL.setObjectName("KRUSKAL")
        self.KRUSKAL.clicked.connect(self.btn_KRUSKAL)

        self.normalTest=QtWidgets.QPushButton(Form)
        self.normalTest.setGeometry(QtCore.QRect(50,170,75,23))
        self.normalTest.setObjectName("NormalTest")
        self.normalTest.clicked.connect(self.btn_normalTest)

        self.Apply_Button=QtWidgets.QPushButton(Form)
        self.Apply_Button.setGeometry(QtCore.QRect(50,410,75,23))
        self.Apply_Button.clicked.connect(self.btn_Apply)


        self.Save_ResulsBtn=QtWidgets.QPushButton(Form)
        self.Save_ResulsBtn.setGeometry(QtCore.QRect(350,460,91,23))
        self.Save_ResulsBtn.setObjectName("Save_Results")
        self.Save_ResulsBtn.clicked.connect(self.SAVING)

        self.Drawing_Plots = QtWidgets.QPushButton(Form)
        self.Drawing_Plots.setGeometry(QtCore.QRect(50, 270, 75, 23))
        self.Drawing_Plots.setObjectName("Drawing_Plots")
        self.Drawing_Plots.clicked.connect(mn.Graph)

        self.Median_Btn=QtWidgets.QPushButton(Form)
        self.Median_Btn.setGeometry(QtCore.QRect(40,240,91,23))
        self.Median_Btn.setObjectName("Median_Btn")
        self.Median_Btn.clicked.connect(self.median_Output)

        self.X_column=QtWidgets.QLineEdit(Form)
        self.X_column.setGeometry(QtCore.QRect(30,350,113,20))
        self.X_column.setObjectName("X_column")

        self.Y_column=QtWidgets.QLineEdit(Form)
        self.Y_column.setGeometry(QtCore.QRect(30,380,113,20))
        self.Y_column.setObjectName("Y_column")

        
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

        self.label4=QtWidgets.QLabel(Form)
        self.label4.setGeometry(QtCore.QRect(10,310,171,41))
        font1=QtGui.QFont()
        font1.setPointSize(15)
        self.label4.setFont(font1)
        self.label4.setObjectName("label_4")

        self.Load_Btn = QtWidgets.QPushButton(Form)
        self.Load_Btn.setGeometry(QtCore.QRect(180, 460, 75, 23))
        self.Load_Btn.setObjectName("Load_Btn")
        self.Load_Btn.clicked.connect(self.showDialog)

        self.Remove_btn = QtWidgets.QPushButton(Form)
        self.Remove_btn.setGeometry(QtCore.QRect(260, 460, 91, 23))
        self.Remove_btn.setObjectName("Remove_btn")
        self.Remove_btn.clicked.connect(self.btn_REMOVE_ARRAYS)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        #self.Results.setText(_translate("Form", "Results"))
        self.pushButton.setText(_translate("Form", "Pearson"))
        self.pushButton_2.setText(_translate("Form", "Spirmen"))
        self.pushButton_3.setText(_translate("Form", "1-way"))
        self.Median_Btn.setText(_translate("Form","Median"))
        self.KRUSKAL.setText(_translate("Form","KS-Test"))
        self.Drawing_Plots.setText(_translate("Form", "Draw_Plots"))
        self.label.setText(_translate("Form", "Normal Check"))
        self.label_2.setText(_translate("Form", "Plots"))
        self.label4.setText(_translate("Form","Columns sellect"))
        self.Load_Btn.setText(_translate("Form", "Load_DATA"))
        self.Remove_btn.setText(_translate("Form", "Remove_Arrays"))
        self.Save_ResulsBtn.setText(_translate("Form","Save_RESULTS"))
        self.X_column.setText(_translate("Form","A"))
        self.Y_column.setText(_translate("form","B"))

    
    def showDialog(self): #LOAD FILES
        self.fname = QtWidgets.QFileDialog.getOpenFileNames()
        self.dataOut()
        return(self.fname)
        #self.btn_Apply()
        #mn.reduceData(fname[0][0],fname[0][1])
    


    def btn_SPIRMEN(self):
        self.Label_OUTPUT(mn.Spirmen(mn.X,mn.Y))
    def btn_PEARSON(self):
        self.Label_OUTPUT(mn.Pirson(mn.X,mn.Y))

    def btn_One_Way(self):
        mn.OCL_NORMALIZE()
    
    def btn_KRUSKAL(self):
        self.Label_OUTPUT(mn.KSSYMBOL(mn.X,mn.Y))

    def median_Output(self):
        self.Label_OUTPUT(mn.med())

    def btn_normalTest(self):
        self.Label_OUTPUT(mn.normalTest(mn.X))

    def btn_Apply(self):
        #mn.OCL_NORMALIZE()
        mn.A=int(self.X_column.text())
        mn.B=int(self.Y_column.text())
        print(self.fname)
        mn.reduceData(self.fname[0][0],self.fname[0][1])
        
    def dataOut(self):
         PrevA=mn.dataPrieview(self.fname[0][0])
         PrevB=mn.dataPrieview(self.fname[0][1])
         self.Label_OUTPUT("\n".join(PrevA))
         self.Label_OUTPUT("\n".join(PrevB))
    

    def Label_OUTPUT(self,f):
        if(self.DATA==""):
            self.DATA=str(f)
        else:
            self.DATA+='\n'+str(f)
        self.Results.setText(self.DATA)


    def btn_REMOVE_ARRAYS(self):
        self.Results.clear()
        self.DATA=""
      
    
    def SAVING(self):
        f=open("out.int","w")
        f.write(self.DATA)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StatsApp = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(StatsApp)
    StatsApp.show()
    sys.exit(app.exec_())