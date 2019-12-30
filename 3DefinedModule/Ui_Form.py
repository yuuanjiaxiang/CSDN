from PyQt5 import QtCore, QtGui, QtWidgets


class WatchLabel(QtWidgets.QLabel):#自定义组件WatchLabel，继承自QLabel
    def __init__(self,parent = None):
        super(WatchLabel, self).__init__(parent)
    WinShow = QtCore.pyqtSignal()#新建信号,到时候调用的方法就是WinShow，名字可以自己写
    WinHide = QtCore.pyqtSignal()#新建信号

    def enterEvent(self, *args, **kwargs):#定义鼠标移入事件，链接到WinShow信号
        self.WinShow.emit()
    def leaveEvent(self, *args, **kwargs):#定义鼠标移出事件，链接到WinHide信号
        self.WinHide.emit()

class Win_Form(object):#主窗口UI格式
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(453, 327)
        # 注意这里使用的是自定义的WatchLabel，而不是QtWidgets.QLabel,这样，这个Label就有了鼠标移入移出事件
        self.label = WatchLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 161, 51))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "这是一个组件，移入会有弹窗"))

class Box_Form(object):#弹窗窗口UI格式
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(354, 512)
        Form.setMinimumSize(QtCore.QSize(354, 512))
        Form.setMaximumSize(QtCore.QSize(354, 512))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 354, 512))
        self.label.setMinimumSize(QtCore.QSize(354, 512))
        self.label.setMaximumSize(QtCore.QSize(354, 512))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./弹窗.PNG"))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

