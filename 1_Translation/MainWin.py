import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtCore import QTranslator
from test_ui import *
class MyMainForm(QMainWindow,Ui_Form):
    def __init__(self,parent = None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        #定义翻译家
        self.trans = QTranslator()
        #将两个按钮链接到槽函数
        self.pushButton.clicked.connect(self._tigger_english)
        self.pushButton_2.clicked.connect(self._trigger_zh_cn)
    def _tigger_english(self):
        #加载语言包
        self.trans.load("en")
        #获取窗口实例
        app = QApplication.instance()
        #将翻译家安装到实例中
        app.installTranslator(self.trans)
        #翻译界面
        self.retranslateUi(self)
        pass
    def _trigger_zh_cn(self):
        #加载语言包
        self.trans.load("zh_CN")
        #获取窗口实例
        app = QApplication.instance()
        #将翻译家安装到实例中
        app.installTranslator(self.trans)
        self.retranslateUi(self)
        pass
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
