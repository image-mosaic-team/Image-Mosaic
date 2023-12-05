# @Author : fxl

from PyQt5 import QtCore, QtGui, QtWidgets


class Warning(object):
    def Warning_setupUi(self, Dialog):
        # 设置对话框的对象名和大小
        Dialog.setObjectName("Dialog")
        Dialog.resize(620, 265)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        # 创建一个标签并设置其位置和大小
        self.label = QtWidgets.QLabel(Dialog)
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
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 50, 161, 161))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        '''


        这里有一个三角形图像要插入进去

        
        '''

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def Warning_retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        # 设置对话框的标题
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        # 设置标签的文本内容
        self.label.setText(_translate("Dialog", "失    败"))