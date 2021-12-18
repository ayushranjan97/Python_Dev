from test1 import *

import sys
import loadsql
class test11(Ui_Form):
    def __init__(self,window):
        self.setupUi(window)
        self.pushButton.clicked.connect(self.clickMe)

    def clickMe(self):
        loadsql.load_sql()


app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QMainWindow()

ui= test11(Form)

Form.show()
app.exec_()

