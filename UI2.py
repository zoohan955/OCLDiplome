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
        Form.resize(1920, 500)
        self.DATA=self.DATA=''
        self.fname=self.fname=''
        self.Results=QtWidgets.QLabel(Form)
        self.Results.setGeometry(QtCore.QRect(190,50,1920,500))
        
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 50, 75, 23))
        self.pushButton.setObjectName("StatAnalysis")
        self.pushButton.clicked.connect(self.btn_Stat_Analysis)

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 80, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.btn_SPIRMEN)

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 110, 75, 23))
        self.pushButton_3.setObjectName("Pirson")
        self.pushButton_3.clicked.connect(self.btn_PEARSON)

        self.Kolmogorov=QtWidgets.QPushButton(Form)
        self.Kolmogorov.setGeometry(QtCore.QRect(50,140,75,23))
        self.Kolmogorov.setObjectName("Kolmogorov")
        self.Kolmogorov.clicked.connect(self.btn_KRUSKAL)

        self.Shapiro=QtWidgets.QPushButton(Form)
        self.Shapiro.setGeometry(QtCore.QRect(50,170,75,23))
        self.Shapiro.setObjectName("Shapiro")
        self.Shapiro.clicked.connect(self.btn_Shapiro)

        self.Apply_Button=QtWidgets.QPushButton(Form)
        self.Apply_Button.setGeometry(QtCore.QRect(50,470,75,23))
        self.Apply_Button.setObjectName("Apply")
        self.Apply_Button.clicked.connect(self.btn_Apply)


        self.Save_ResulsBtn=QtWidgets.QPushButton(Form)
        self.Save_ResulsBtn.setGeometry(QtCore.QRect(1500,470,91,23))
        self.Save_ResulsBtn.setObjectName("Save_Results")
        self.Save_ResulsBtn.clicked.connect(self.SAVING)

        self.Drawing_Plots = QtWidgets.QPushButton(Form)
        self.Drawing_Plots.setGeometry(QtCore.QRect(50, 270, 75, 23))
        self.Drawing_Plots.setObjectName("Drawing_Plots")
        self.Drawing_Plots.clicked.connect(self.Graph)

        self.Median_Btn=QtWidgets.QPushButton(Form)
        self.Median_Btn.setGeometry(QtCore.QRect(40,240,91,23))
        self.Median_Btn.setObjectName("Median_Btn")
        self.Median_Btn.clicked.connect(self.median_Output)

        self.X_column=QtWidgets.QLineEdit(Form)
        self.X_column.setGeometry(QtCore.QRect(30,410,113,20))
        self.X_column.setObjectName("X_column")

        self.Y_column=QtWidgets.QLineEdit(Form)
        self.Y_column.setGeometry(QtCore.QRect(30,440,113,20))
        self.Y_column.setObjectName("Y_column")

        
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(163, 0, 20, 491))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")


        self.line2=QtWidgets.QFrame(Form)
        self.line2.setGeometry(QtCore.QRect(170, 450, 1920, 20))
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")


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
        self.label4.setGeometry(QtCore.QRect(10,360,171,41))
        font1=QtGui.QFont()
        font1.setPointSize(15)
        self.label4.setFont(font1)
        self.label4.setObjectName("label_4")

        self.Load_Btn = QtWidgets.QPushButton(Form)
        self.Load_Btn.setGeometry(QtCore.QRect(180, 470, 101, 23))
        self.Load_Btn.setObjectName("Load_Btn")
        self.Load_Btn.clicked.connect(self.showDialog)



        self.Normilize_Btn=QtWidgets.QPushButton(Form)
        self.Normilize_Btn.setGeometry(QtCore.QRect(290, 470, 101, 23))
        self.Normilize_Btn.setObjectName("Normilize_Btn")
        self.Normilize_Btn.clicked.connect(self.btn_Normalize)




        self.Remove_btn = QtWidgets.QPushButton(Form)
        self.Remove_btn.setGeometry(QtCore.QRect(1400, 470, 91, 23))
        self.Remove_btn.setObjectName("Remove_btn")
        self.Remove_btn.clicked.connect(self.btn_REMOVE_ARRAYS)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        #self.Results.setText(_translate("Form", "Results"))
        self.pushButton.setText(_translate("Form", "Stat Analysis"))
        self.pushButton_2.setText(_translate("Form", "Spirmen"))
        self.pushButton_3.setText(_translate("Form", "Pirson"))
        self.Median_Btn.setText(_translate("Form","Median"))
        self.Kolmogorov.setText(_translate("Form","Kolmogorov"))
        self.Shapiro.setText(_translate("Form","Shapiro"))
        self.Drawing_Plots.setText(_translate("Form", "Draw_Plots"))
        self.label.setText(_translate("Form", "Stat Functions"))
        self.label_2.setText(_translate("Form", "Plots"))
        self.label4.setText(_translate("Form","Columns sellect"))
        self.Load_Btn.setText(_translate("Form", "Load_DATA"))
        self.Remove_btn.setText(_translate("Form", "Remove_Arrays"))
        self.Save_ResulsBtn.setText(_translate("Form","Save_RESULTS"))
        self.Normilize_Btn.setText(_translate("Form","Normalize Data"))
        self.X_column.setText(_translate("Form","A"))
        self.Y_column.setText(_translate("form","B"))

    
    def showDialog(self): #LOAD FILES
        self.fname = QtWidgets.QFileDialog.getOpenFileNames()
        self.dataOut()
        return(self.fname)

    def Graph(self):
        mn.Graphical(mn.DataSet.A,mn.DataSet.B)

    def btn_SPIRMEN(self):
        self.Label_OUTPUT(mn.Spirmen(mn.DataSet.A,mn.DataSet.B))
        
    def btn_PEARSON(self):
        self.Label_OUTPUT(mn.Pirson(mn.DataSet.A,mn.DataSet.B))

    def btn_Normalize(self):
        mn.miniMax(mn.X,mn.Y)

    def btn_Stat_Analysis(self):
       A=mn.descriptiveX(mn.DataSet.A)
       B=mn.descriptiveY(mn.DataSet.B)
       self.Label_OUTPUT("  ".join(A))
       self.Label_OUTPUT("  ".join(B))
       



    def btn_Shapiro(self):
        self.Label_OUTPUT(mn.Shapiro(mn.X,mn.Y))


    def btn_One_Way(self):
        mn.miniMax(mn.X,mn.Y)
        #mn.OCL_NORMALIZE()
    
    def btn_KRUSKAL(self):
        self.Label_OUTPUT(mn.KSSYMBOL(mn.X,mn.Y))

    def median_Output(self):
        self.Label_OUTPUT(mn.med())

    def btn_normalTest(self):
        self.Label_OUTPUT(mn.normalTest(mn.X))

    def btn_Apply(self):
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

    def STAT_OUTPUT(self,f):
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