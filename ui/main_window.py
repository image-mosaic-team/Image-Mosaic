# -*- coding: utf-8 -*-
# @Author : ltx


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os
from ui.more import more_Window
import cv2
# from testui import Ui_Dialog
from algorithm import Stitcher
import numpy as np

class Ui_MainWindow(object):
    # def __init__(self):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1062, 850)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 630, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(770, 640, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(470, 280, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(470, 370, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(470, 460, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lable1 = QtWidgets.QLabel(self.centralwidget)
        self.lable1.setGeometry(QtCore.QRect(10, 40, 441, 571))
        self.lable1.setStyleSheet("border-width: 1px;border-style: solid;border-color: rgb(255, 170, 0);")
        self.lable1.setObjectName("lable1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(600, 40, 441, 571))
        self.label_2.setStyleSheet("border-width: 1px;border-style: solid;border-color: rgb(255, 170, 0);")
        self.label_2.setObjectName("label_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(230, 630, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(890, 640, 93, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1062, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.more_window = None  # 在这里添加一个字段来保存more_Window的实例


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "upload"))
        self.pushButton_2.setText(_translate("MainWindow", "upload"))
        self.pushButton_3.setText(_translate("MainWindow", "start"))
        self.pushButton_4.setText(_translate("MainWindow", "clean up"))
        self.pushButton_5.setText(_translate("MainWindow", "more"))
        self.lable1.setText(_translate("MainWindow", "image1"))
        self.label_2.setText(_translate("MainWindow", "image2"))
        self.pushButton_6.setText(_translate("MainWindow", "revole"))
        self.pushButton_8.setText(_translate("MainWindow", "revole"))
        # 为按钮添加槽函数
        self.pushButton.clicked.connect(self.upload1ButtonClicked)
        self.pushButton_2.clicked.connect(self.upload2ButtonClicked)
        self.pushButton_3.clicked.connect(self.startButtonClicked)
        self.pushButton_4.clicked.connect(self.cleanupButtonClicked)
        self.pushButton_5.clicked.connect(self.moreButtonClicked)
        self.pushButton_6.clicked.connect(self.revole_1_ButtonClicked)
        self.pushButton_8.clicked.connect(self.revole_2_ButtonClicked)

    def upload1ButtonClicked(self):
        # pushButton 按钮的槽函数
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getOpenFileName(None, "select imageL:", "", "Images (*.png *.xpm *.jpg *.jpeg)", options=options)
        if file:
            save_dir = "img_tmp"  # 自定义文件夹路径
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            file_name = os.path.basename(file)
            save_path = os.path.join(save_dir, file_name)
            pixmap = QtGui.QPixmap(file)
            pixmap.save(save_path)
            scaled_pixmap = pixmap.scaled(self.lable1.size(), QtCore.Qt.KeepAspectRatio)
            self.lable1.setPixmap(scaled_pixmap)

    def upload2ButtonClicked(self):
        # pushButton_2 按钮的槽函数
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getOpenFileName(None, "选择图片", "", "Images (*.png *.xpm *.jpg *.jpeg)", options=options)
        if file:
            save_dir = "img_tmp/"  # 自定义文件夹路径
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            file_name = os.path.basename(file)
            save_path = os.path.join(save_dir, file_name)
            pixmap = QtGui.QPixmap(file)
            pixmap.save(save_path)
            scaled_pixmap = pixmap.scaled(self.label_2.size(), QtCore.Qt.KeepAspectRatio)
            self.label_2.setPixmap(scaled_pixmap)


    def startButtonClicked(self):
        print("-------------------------------")

        try:
            imageA = cv2.imread(r"img_tmp/image1.jpg")
            imageB = cv2.imread(r"img_tmp/image2.jpg")
            print("SHAPE:", imageA.shape, imageB.shape)
        except:
            print("没有图片")
            return

        try:
            stitcher = Stitcher()
            (result, vis) = stitcher.stitch([imageA, imageB],
                                        showMatches=True)
        except Exception as e:
            print("合成失败", e)
            return


        try:
            if result is not None:
                stitcher.cut_handle()  # 裁剪
            else:
                print("result 是None")
                return
        except:
            print("裁剪失败")


        try:
            cv2.imwrite(r"E:\git_test\Image-Mosaic\ui\image_result\result.jpg", result)
        except:
            print("result保存失败")



    def cleanupButtonClicked(self):
        # pushButton_4 按钮的槽函数
        self.lable1.clear()
        self.label_2.clear()

    def moreButtonClicked(self):
        self.more_window = more_Window()  # 使用self.more_window来保存more_Window的实例
        self.more_window.start()

    def revole_1_ButtonClicked(self):
        pixmap = self.lable1.pixmap()
        if pixmap:
            # 将QPixmap转换为OpenCV格式
            image = pixmap.toImage()
            ptr = image.bits()
            ptr.setsize(image.byteCount())
            arr = np.array(ptr).reshape(image.height(), image.width(), 4)  # Copies the data
            img = cv2.cvtColor(arr, cv2.COLOR_RGBA2BGR)

            # 使用OpenCV进行旋转
            (h, w) = img.shape[:2]
            center = (w / 2, h / 2)
            M = cv2.getRotationMatrix2D(center, 90, 1.0)
            rotated = cv2.warpAffine(img, M, (w, h))

            # 将旋转后的OpenCV图像转换回QPixmap
            rotated_pixmap = QtGui.QPixmap.fromImage(
                QtGui.QImage(rotated.data, rotated.shape[1], rotated.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped())
            self.lable1.setPixmap(rotated_pixmap)

            # 保存旋转后的图片
            save_dir = "img_tmp"  # 替换为你想保存图像的文件夹路径
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            file_name = "image1.jpg"  # 保存文件的名称
            save_path = os.path.join(save_dir, file_name)
            cv2.imwrite(save_path, rotated)
        # pushButton_5 按钮的槽函数
        #
        # pixmap = self.lable1.pixmap()
        # if pixmap:
        #     rotated_pixmap = pixmap.transformed(QtGui.QTransform().rotate(90))
        #     print(rotated_pixmap)
        #     self.lable1.setPixmap(rotated_pixmap)
        #
        #     # 保存旋转后的图片
        #     save_dir = "img_tmp"  # 替换为你想保存图像的文件夹路径
        #     if not os.path.exists(save_dir):
        #         os.makedirs(save_dir)
        #
        #     file_name = "image1.jpg"  # 保存文件的名称
        #     save_path = os.path.join(save_dir, file_name)
        #     rotated_pixmap.save(save_path)

    def revole_2_ButtonClicked(self):

        pixmap = self.label_2.pixmap()
        if pixmap:
            rotated_pixmap = pixmap.transformed(QtGui.QTransform().rotate(90))
            self.label_2.setPixmap(rotated_pixmap)

            # 保存旋转后的图片
            save_dir = "img_tmp"  # 替换为你想保存图像的文件夹路径
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            file_name = "image2.jpg"  # 保存文件的名称
            save_path = os.path.join(save_dir, file_name)
            rotated_pixmap.save(save_path)



import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# if __name__ == '__main__':
app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())