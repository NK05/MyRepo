import numpy as np
from main import mainRun
import sys
from PySide2 import QtGui
from PySide2.QtCore import QRect
from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QGridLayout, QGroupBox, QHBoxLayout, QDialog, QLabel, QLineEdit


class Form2(QWidget):

    def __init__(self, m, p):
        super().__init__()
        self.m = m
        assert isinstance(p, object)
        self.p = p

        self.title = "Group Technology"
        self.top = 100
        self.left = 100
        self.width = 500
        self.height = 400
        #self.setFixedHeight(400)
       # self.setFixedWidth(900)
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon8.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.Grpbx()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        self.show()

    def Grpbx(self):

        self.groupBox = QGroupBox("INPUT DATA")
        grid2 = QGridLayout()

        self.table = QTableWidget(self.m, self.p, self)
        self.table.setGeometry(QRect(50, 25, 400, 250))
        w = "Machines"
        alph = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "H", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z"]
        for x in range(self.m):
            if x == 0:
                self.table.setItem(x, 0, QTableWidgetItem("Machines"))
                for i in range((self.p) - 1):
                    self.table.setItem(x, i + 1, QTableWidgetItem("Part " + str(i + 1)))
            # elif x==7:
            #    for i in range(8):
            #       if i==0:
            #          self.table.setItem(x,"", QTableWidgetItem("Part " + str(i + 1)))
            else:
                for i in range(self.p):
                    if i == 0:
                        self.table.setItem(x, 0, QTableWidgetItem(alph[0]))
                        alph.pop(0)
                    else:
                        self.table.setItem(x, i, QTableWidgetItem("0"))

        self.table.move(0, 0)

        grid2.addWidget(self.table, 0, 0)

        button = QPushButton("Enter", self)
        button.setGeometry(QRect(150, 300, 111, 28))
        button.setToolTip("Press Enter to run iterations")
        button.clicked.connect(self.ClickMe2)
        grid2.addWidget(button, 1, 0)

        reset = QPushButton("Reset", self)
        reset.setGeometry(QRect(150, 300, 111, 28))
        reset.setToolTip("Press Enter Refresh")
        reset.clicked.connect(self.Reset)
        grid2.addWidget(reset, 1, 1)

        self.groupBox.setLayout(grid2)

    def Reset(self):
        w = "Machines"
        alph = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "H", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z"]
        for x in range(self.m):
            if x == 0:
                self.table.setItem(x, 0, QTableWidgetItem("Machines"))
                for i in range((self.m) - 1):
                    self.table.setItem(x, i + 1, QTableWidgetItem("Part " + str(i + 1)))
            # elif x==7:
            #    for i in range(8):
            #       if i==0:
            #          self.table.setItem(x,"", QTableWidgetItem("Part " + str(i + 1)))
            else:
                for i in range(self.p):
                    if i == 0:
                        self.table.setItem(x, 0, QTableWidgetItem(alph[0]))
                        alph.pop(0)
                    else:
                        self.table.setItem(x, i, QTableWidgetItem("0"))

        # self.table.move(0, 0)

    def ClickMe2(self):
        arry = []

        for x in range(self.m):
            lst = []
            for y in range(self.p):
                i = self.table.takeItem(x, y)
                print(i.text())
                lst.append(i.text())
            arry.append(lst)
        a = np.array(arry)
        col = a.shape[1]

        print(a)
        b = np.zeros((1, col), dtype=np.int16)
        a = np.append(a, b, axis=0)
        row = a.shape[0]
        c = np.zeros((row, 1), dtype=np.int16)
        a = np.append(a, c, axis=1)
        a[0][-1] = 999
        a[-1][0] = 999
        a[-1][-1] = 100

        print(a)
        fin = mainRun(a)
        x = 0

        for i in fin:
            y = 0
            for item in i[:-1]:
                self.table.setItem(x, y, QTableWidgetItem(item))
                y = y + 1
            x = x + 1
        print(fin)

        # print(a)


def secW(self, machines, parts):
    App2 = QMainWindow()
    window = Form2(machines, parts)
    sys.exit(App2.exec_())


class Form1(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "Manufacturing Systems"
        self.top = 200
        self.left = 200
        self.width = 500
        self.height = 100
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon8.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.Layout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        self.show()

    def Layout(self):
        self.groupBox = QGroupBox("Enter Number of Machines and Parts")
        grid = QGridLayout()

        labM = QLabel("Machines")
        labM.setMinimumHeight(40)
        grid.addWidget(labM, 0, 0)

        self.textM = QLineEdit(self)
        self.textM.setMinimumHeight(20)
        # textM.text()
        grid.addWidget(self.textM, 0, 1)

        labP = QLabel("Parts")
        labP.setMinimumHeight(40)
        grid.addWidget(labP, 0, 2)

        self.textP = QLineEdit()
        self.textP.setMinimumHeight(20)
        grid.addWidget(self.textP, 0, 3)

        button = QPushButton("Enter", self)
        button.setMinimumHeight(30)
        button.setMinimumWidth(100)
        # button.setToolTip("Press Enter to run iterations")

        button.clicked.connect(self.ClickMe)

        grid.addWidget(button, 1, 1)

        self.groupBox.setLayout(grid)

    def ClickMe(self):
        m = int(self.textM.text()) + 1
        p = int(self.textP.text()) + 1

        Form1.hide(self)
        secW(self, m, p)
        # sys.exit()


App = QApplication(sys.argv)
window = Form1()
# window2 = Form2()
# window2.hide()
sys.exit(App.exec_())