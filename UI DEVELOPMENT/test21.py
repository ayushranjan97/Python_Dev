from test2 import *

import sys

class test11(Ui_TEST):
    def __init__(self,window):
        self.setupUi(window)
        self.pushButton.clicked.connect(self.clickMe)
        self.pushButton_3.clicked.connect(self.clickMe1)
        self.pushButton_2.clicked.connect(self.clickMe2)
        self.pushButton_4.clicked.connect(self.exit)

    def clickMe(self):
        print("EXTRACT have been clicked")

    def clickMe1(self):
            print("TRANSFORM have been clicked")
    def clickMe2(self):
        print("LOAD have been clicked")
    def exit(self):
        sys.exit(app.exec_())


app = QtWidgets.QApplication(sys.argv)
TEST = QtWidgets.QMainWindow()

ui= test11(TEST)

TEST.show()
app.exec_()