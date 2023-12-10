# -*- coding: utf-8 -*-
# @Author : fxl


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class Production_Personnel(object):
    def PP_setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 400)
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(0, 40, 650, 40))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(0, 120, 650, 40))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(0, 200, 650, 40))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(0, 280, 650, 40))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(0, 360, 650, 40))
        self.label_5.setObjectName("label_5")

        # self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def PP_retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦"))
        self.label_2.setText(_translate("MainWindow", "啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦"))
        self.label_3.setText(_translate("MainWindow", "啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦"))
        self.label_4.setText(_translate("MainWindow", "啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦"))
        self.label_5.setText(_translate("MainWindow", "啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦"))


    def start(self):
        self.MainWindow = QMainWindow()
        self.PP_setupUi(self.MainWindow)
        self.PP_retranslateUi(self.MainWindow)
        self.MainWindow.show()