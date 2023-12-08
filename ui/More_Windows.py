# -*- coding: utf-8 -*-
# @Author : fxl
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from ui.ParaSitting import ParaSitting
from ui.Production_Personnel import Production_Personnel

class More_Windows(object):
    def MW_setupUi(self, MainWindow):
        MainWindow.setObjectName("MoreWindow")
        MainWindow.resize(610, 381)
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(210, 40, 171, 101))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 200, 171, 101))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(90, 330, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(390, 330, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        # MainWindow.setStatusBar(self.statusbar)

        # self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 在这里添加一个字段来保存more_window的实例
        # self.more_window = None
    

    def MW_retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "参数设置"))
        self.pushButton_2.setText(_translate("MainWindow", "制作人员"))
        self.label.setText(_translate("MainWindow", "版本：1.0"))
        self.label_2.setText(_translate("MainWindow", "源码地址："))
        # 为按钮添加槽函数
        self.pushButton.clicked.connect(self.PSsitButtonClicked)
        self.pushButton_2.clicked.connect(self.PPButtonClicked)
    

    def start(self):
        # app = QtWidgets.QApplication(sys.argv)
        # MainWindow = QMainWindow()
        # ui = More_Windows()
        # ui.MW_setupUi(MainWindow)
        # ui.MW_retranslateUi(MainWindow)
        # MainWindow.show()
        # sys.exit(app.exec_())
        self.MainWindow = QMainWindow()
        self.MW_setupUi(self.MainWindow)
        self.MW_retranslateUi(self.MainWindow)
        self.MainWindow.show()


    def PSsitButtonClicked(self):
        self.more_window = ParaSitting()
        self.more_window.start()


    def PPButtonClicked(self):
        self.more_window = Production_Personnel()
        self.more_window.start()


# m = More_Windows()
# m.start()