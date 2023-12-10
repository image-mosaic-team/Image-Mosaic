# -*- coding: utf-8 -*-
# @Author : fxl

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import json


class ParaSitting(object):
    def PS_setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.PushButton = QtWidgets.QPushButton(MainWindow)
        self.PushButton.setGeometry(QtCore.QRect(450, 70, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PushButton.setFont(font)
        self.PushButton.setObjectName("PushButton")
        self.pushButton_2 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 270, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.line = QtWidgets.QFrame(MainWindow)
        self.line.setGeometry(QtCore.QRect(400, 0, 20, 400))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(50, 50, 72, 15))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(30, 180, 111, 15))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(10, 310, 141, 15))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(MainWindow)
        self.frame.setGeometry(QtCore.QRect(200, 20, 131, 81))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(40, 30, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEdit.setObjectName("textEdit")
        self.frame_2 = QtWidgets.QFrame(MainWindow)
        self.frame_2.setGeometry(QtCore.QRect(200, 150, 131, 81))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_2.setGeometry(QtCore.QRect(40, 30, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEdit_2.setObjectName("textEdit_2")
        self.frame_3 = QtWidgets.QFrame(MainWindow)
        self.frame_3.setGeometry(QtCore.QRect(200, 280, 131, 81))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit_3.setGeometry(QtCore.QRect(40, 30, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEdit_3.setObjectName("textEdit_3")
        # MainWindow.setStatusBar(self.statusbar)

        # self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def PS_retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PushButton.setText(_translate("MainWindow", "OK"))
        self.pushButton_2.setText(_translate("MainWindow", "EXIT"))
        self.label.setText(_translate("MainWindow", "Ratio"))
        self.label_2.setText(_translate("MainWindow", "Reprojthresh"))
        self.label_3.setText(_translate("MainWindow", "Homography_matrix"))

        # json文件读取
        f = open('algo_para.json','r')
        content = f.read()
        a = json.loads(content)
        f.close()


        self.textEdit.setPlainText(str(a["ratio"]))
        self.textEdit_2.setPlainText(str(a["reprojThresh"]))
        self.textEdit_3.setPlainText(str(a["Homography_matrix"]))
        # self.textEdit.setHtml('')
        # self.textEdit_2.setHtml('')
        # self.textEdit_3.setHtml('')
        self.PushButton.clicked.connect(self.JSButtonClicked)
        self.pushButton_2.clicked.connect(self.EXButtonClicked)

    def start(self):
        self.MainWindow = QMainWindow()
        self.PS_setupUi(self.MainWindow)
        self.PS_retranslateUi(self.MainWindow)
        self.MainWindow.show()

            
    def JSButtonClicked(self):
        k_1 = self.textEdit.toPlainText()
        k_2 = self.textEdit_2.toPlainText()
        k_3 = self.textEdit_3.toPlainText()
        dic = dict()
        for i in ("ratio","reprojThresh","Homography_matrix"):
            if i == "ratio":
                dic[i] = float(k_1)
            elif i == "reprojThresh":
                dic[i] = float(k_2)
            else:
                dic[i] = float(k_3)
        b = json.dumps(dic)
        f2 = open('algo_para.json','w')
        f2.write(b)
        f2.close()


    def EXButtonClicked(self):
        self.MainWindow.close()