# @Author : fxl

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Warning(object):
    def Warning_setupUi(self, MainWindow):
        # 设置对话框的对象名和大小
        MainWindow.setObjectName("Dialog")
        MainWindow.resize(620, 265)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        # 创建一个标签并设置其位置和大小
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(270, 50, 271, 141))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setLineWidth(31)
        self.label.setMidLineWidth(1)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setIndent(41)
        self.label.setObjectName("label")
        # 创建另一个标签并设置其位置和大小
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(70, 50, 161, 161))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.setPixmap(QPixmap('R-C.jpg'))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Warning_retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # 设置对话框的标题
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # 设置标签的文本内容
        self.label.setText(_translate("MainWindow", "失    败"))

app = QtWidgets.QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Warning()
ui.Warning_setupUi(MainWindow)
ui.Warning_retranslateUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_()) 