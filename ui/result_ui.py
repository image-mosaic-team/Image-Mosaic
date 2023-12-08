# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap,QImage
from PyQt5.QtCore import Qt
from ui_tools.Brightness import modify_brightness
from ui_tools.Contrast import modify_constract
from ui_tools.Exposure import modify_exposure
from ui_tools.Saturation import modify_saturation
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import numpy as np
import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow
import cv2

class result_ui(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 840)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")



        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 951, 481))
        self.label.setStyleSheet("border-width: 1px;border-style: solid;border-color: rgb(255, 170, 0);")
        self.label.setObjectName("label")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 550, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 620, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(171, 540, 81, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 600, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 660, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(171, 720, 81, 20))
        self.label_5.setObjectName("label_5")

        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(280, 540, 441, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        # self.horizontalSlider.setTickInterval(5)
        self.horizontalSlider.setRange(-100, 100)
        self.horizontalSlider.setSingleStep(10)
        self.horizontalSlider.setObjectName("horizontalSlider")
        # 连接滑动条的 valueChanged 信号到槽函数
        self.horizontalSlider.valueChanged.connect(self.on_value_changed_brightness)

        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(280, 600, 441, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        # self.horizontalSlider_2.setTickInterval(20)
        self.horizontalSlider_2.setRange(0, 30)
        self.horizontalSlider_2.setSingleStep(1)
        self.horizontalSlider_2.setValue(10)  # 设置滑动条的初始值为10
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.valueChanged.connect(self.on_value_changed_constract)


        self.horizontalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(280, 660, 441, 22))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setTickPosition(QtWidgets.QSlider.TicksBelow)
        # self.horizontalSlider_3.setTickInterval(20)
        self.horizontalSlider_3.setRange(1, 100)
        self.horizontalSlider_3.setSingleStep(1)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalSlider_3.valueChanged.connect(self.on_value_changed_exposure)

        self.horizontalSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(280, 720, 441, 22))
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_4.setRange(1, 100)
        self.horizontalSlider_4.setSingleStep(1)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.horizontalSlider_4.valueChanged.connect(self.on_value_changed_saturation)


        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(260, 570, 31, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(700, 570, 72, 15))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(281, 630, 61, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(710, 630, 51, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(280, 690, 61, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(710, 690, 51, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(280, 750, 61, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(700, 750, 51, 20))
        self.label_13.setObjectName("label_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 加载图片
        pixmap = QPixmap(r'E:\git_test\Image-Mosaic\img_tmp\result_crop.jpg')
        # 将图片缩放到标签的大小，并保持图片的比例
        pixmap = pixmap.scaled(self.label.width(), self.label.height(), QtCore.Qt.KeepAspectRatio)
        # 在标签上显示图片
        self.label.setPixmap(pixmap)

        self.label.setAlignment(Qt.AlignCenter)
        self.image_modify = cv2.imread(r"E:\git_test\Image-Mosaic\img_tmp\result_crop.jpg")


        self.image_modify_prosess = np.copy( self.image_modify)

        print(self.image_modify_prosess[100][100])

        self.num = 0
        # self.img2 = None

        self.value_brightness = 0
        self.value_constract = 0
        self.value_exposure = 0
        self.value_saturation = 0


    def on_value_changed_brightness(self, value):
        print("value",value)
        print("before_value", self.value_brightness)
        value_now = value - self.value_brightness

        print("now_value", value_now)
        self.image_modify_prosess = modify_brightness(self.image_modify_prosess, value_now)

        self.value_brightness = value_now
        print(1)
        img2 = cv2.cvtColor(self.image_modify_prosess, cv2.COLOR_BGR2RGB)  # opencv读取的bgr格式图片转换成rgb格式
        print(2)
        _image = QtGui.QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3,
                              QtGui.QImage.Format_RGB888)  # pyqt5转换成自己能放的图片格式
        print(3)
        jpg_out = QtGui.QPixmap(_image).scaled(self.label.width(), self.label.height(),QtCore.Qt.KeepAspectRatio)  # 设置图片大小

        self.label.setPixmap(jpg_out)  # 设置图片显示
        self.label.setAlignment(Qt.AlignCenter)




    def on_value_changed_constract(self,value):


        value = value/10


        value_now = value - self.value_constract

        self.image_modify_prosess = modify_constract(self.image_modify_prosess, alpha=value_now)

        self.value_constract = value


        img2 = cv2.cvtColor(self.image_modify_prosess, cv2.COLOR_BGR2RGB)  # opencv读取的bgr格式图片转换成rgb格式


        _image = QtGui.QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3,
                              QtGui.QImage.Format_RGB888)  # pyqt5转换成自己能放的图片格式

        jpg_out = QtGui.QPixmap(_image).scaled(self.label.width(), self.label.height(),
                                               QtCore.Qt.KeepAspectRatio)  # 设置图片大小

        self.label.setPixmap(jpg_out)  # 设置图片显示
        self.label.setAlignment(Qt.AlignCenter)


    def on_value_changed_exposure(self,value):


        value = value/10

        value_now = value - self.value_exposure

        self.image_modify_prosess = modify_exposure(self.image_modify_prosess, value_now)
        self.value_exposure = value


        img2 = cv2.cvtColor(self.image_modify_prosess, cv2.COLOR_BGR2RGB)  # opencv读取的bgr格式图片转换成rgb格式

        _image = QtGui.QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3,
                              QtGui.QImage.Format_RGB888)  # pyqt5转换成自己能放的图片格式

        jpg_out = QtGui.QPixmap(_image).scaled(self.label.width(), self.label.height(),
                                               QtCore.Qt.KeepAspectRatio)  # 设置图片大小

        self.label.setPixmap(jpg_out)  # 设置图片显示
        self.label.setAlignment(Qt.AlignCenter)



    def on_value_changed_saturation(self,value):


        value = value / 10
        value_now = value - self.value_saturation


        self.image_modify_prosess = modify_saturation(self.image_modify_prosess, value_now)
        self.value_saturation = value


        img2 = cv2.cvtColor(self.image_modify_prosess, cv2.COLOR_BGR2RGB)  # opencv读取的bgr格式图片转换成rgb格式

        _image = QtGui.QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3,
                              QtGui.QImage.Format_RGB888)  # pyqt5转换成自己能放的图片格式

        jpg_out = QtGui.QPixmap(_image).scaled(self.label.width(), self.label.height(),
                                               QtCore.Qt.KeepAspectRatio)  # 设置图片大小

        self.label.setPixmap(jpg_out)  # 设置图片显示
        self.label.setAlignment(Qt.AlignCenter)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "result image"))
        self.pushButton.setText(_translate("MainWindow", "SAVE"))
        self.pushButton_2.setText(_translate("MainWindow", "EXIT"))
        self.label_2.setText(_translate("MainWindow", "brightness"))
        self.label_3.setText(_translate("MainWindow", "constract"))
        self.label_4.setText(_translate("MainWindow", "exposure"))
        self.label_5.setText(_translate("MainWindow", "saturation"))
        self.label_6.setText(_translate("MainWindow", "-100"))
        self.label_7.setText(_translate("MainWindow", "100"))
        self.label_8.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "3"))
        self.label_10.setText(_translate("MainWindow", "0.1"))
        self.label_11.setText(_translate("MainWindow", "10"))
        self.label_12.setText(_translate("MainWindow", "0.1"))
        self.label_13.setText(_translate("MainWindow", "10"))

        # 为按钮添加槽函数
        self.pushButton.clicked.connect(self.SAVEButtonClicked)
        self.pushButton_2.clicked.connect(self.EXITButtonClicked)


    def SAVEButtonClicked(self):
        # pushButton_2 按钮的槽函数
        options = QFileDialog.Options()
        # 打开保存文件对话框，让用户输入文件名
        image_save, _ = QFileDialog.getSaveFileName(None, "保存图片", "",
                                                    "所有文件 (*);;文本文件 (*.txt);;图片文件 (*.png *.jpg *.bmp)",
                                                    options=options)

        # 如果用户选择了文件路径，则保存图片
        if image_save:
            cv2.imwrite(image_save, self.image_modify_prosess)


    def EXITButtonClicked(self):
        self.MainWindow.close()


    def start(self):
        self.MainWindow = QMainWindow()  # 使用self.MainWindow来保存QMainWindow的实例
        self.setupUi(self.MainWindow)
        self.MainWindow.show()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     MainWindow = QMainWindow()
#     ui = result_ui()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
