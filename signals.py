import sys
from PyQt5 import QtWidgets,QtCore
import mainNEW as mn


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.a=QtWidgets.QPushButton('Check_PEARSON')
        
        self.c = QtWidgets.QPushButton('Check_SPIRMEN')

        self.d=QtWidgets.QPushButton('Check_1WAY')
        self.b = QtWidgets.QPushButton('PLOT')
        self.l = QtWidgets.QLabel('I have not been clicked yet')
       

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.b)
        v_box.addLayout(h_box)
        v_box.addWidget(self.c)

        self.setLayout(v_box)
        self.setWindowTitle('Stats App')

      #  self.b.clicked.connect(self.btn_PLOTS)
        self.c.clicked.connect(self.btn_SPIRMEN)
        self.b.clicked.connect(self.LBL)

        self.show()

    def btn_PLOTS(self):
        self.b.addAction(mn.Graph())
    def LBL(self):
        self.l.setText(str(mn.Pirson(mn.X,mn.Y)))
    
    def btn_SPIRMEN(self):
        self.c.addAction(mn.SpearmenGraph())
        a= self.c.addAction(mn.SpearmenGraph())
        #self.l.setText(scipy.stats.spearmanr(X,Y))


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())

