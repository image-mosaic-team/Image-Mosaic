# @Author : fxl
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import ParaSitting

class More_Windows(object):
    def MW_setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(610, 381)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 40, 171, 101))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 200, 171, 101))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 330, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(390, 330, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def MW_retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "参数设置"))
        self.pushButton_2.setText(_translate("Form", "制作人员"))
        self.label.setText(_translate("Form", "版本：1.0"))
        self.label_2.setText(_translate("Form", "源码地址："))


