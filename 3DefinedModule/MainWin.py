import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction
from Ui_Form import *
class MainWin(QMainWindow,Win_Form):
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)
        self.setupUi(self)
        #将WinShow与WinHide连接到函数上
        self.label.WinShow.connect(self.BoxWinShow)
        self.label.WinHide.connect(self.BoxWinHide)
    def BoxWinShow(self):
        self.boxWin = BoxWin()
        self.boxWin.show()
    def BoxWinHide(self):
        self.boxWin = BoxWin()
        self.boxWin.hide()
class BoxWin(QMainWindow,Box_Form):
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)
        self.setupUi(self)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())