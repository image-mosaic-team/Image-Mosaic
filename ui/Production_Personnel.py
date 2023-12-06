# -*- coding: utf-8 -*-
# @Author : fxl

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class Production_Personnel(object):
    def PP_setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 400)
        self.textEdit = QtWidgets.QTextEdit(MainWindow)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 650, 400))
        self.textEdit.setObjectName("textEdit")

        # self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def PP_retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Form", "Form"))


    def start(self):
        self.MainWindow = QMainWindow()
        self.PP_setupUi(self.MainWindow)
        self.PP_retranslateUi(self.MainWindow)
        self.MainWindow.show()