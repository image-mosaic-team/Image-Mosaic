# -*- coding: utf-8 -*-
# @Author : ltx


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os
import cv2
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


from ui.More_Windows import More_Windows
from ui.result_ui import result_ui
from algorithm import Stitcher
from ui.Warning import Warning

class Ui_MainWindow(object):
    # def __init__(self):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1062, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 630, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(750, 630, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 220, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(480, 310, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(480, 400, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget) # 
        self.pushButton_9.setGeometry(QtCore.QRect(480, 480, 93, 28)) #
        self.pushButton_9.setObjectName("pushButton_9") #
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
        self.pushButton_8.setGeometry(QtCore.QRect(870, 630, 93, 28))
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
        self.result_window = None
        self.warning_window = None


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "upload"))
        self.pushButton_2.setText(_translate("MainWindow", "upload"))
        self.pushButton_3.setText(_translate("MainWindow", "start"))
        self.pushButton_4.setText(_translate("MainWindow", "clean up"))
        self.pushButton_5.setText(_translate("MainWindow", "more"))
        self.lable1.setText(_translate("MainWindow", ""))
        self.label_2.setText(_translate("MainWindow", ""))
        self.pushButton_6.setText(_translate("MainWindow", "revole"))
        self.pushButton_8.setText(_translate("MainWindow", "revole"))
        self.pushButton_9.setText(_translate("MainWindow", "exit"))
        # 为按钮添加槽函数
        self.pushButton.clicked.connect(self.upload1ButtonClicked)
        self.pushButton_2.clicked.connect(self.upload2ButtonClicked)
        self.pushButton_3.clicked.connect(self.startButtonClicked)
        self.pushButton_4.clicked.connect(self.cleanupButtonClicked)
        self.pushButton_5.clicked.connect(self.moreButtonClicked)
        self.pushButton_6.clicked.connect(self.revole_1_ButtonClicked)
        self.pushButton_8.clicked.connect(self.revole_2_ButtonClicked)
        self.pushButton_9.clicked.connect(self.clear_tmp)

    def upload1ButtonClicked(self):
        # pushButton 按钮的槽函数
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getOpenFileName(None, "select imageL:", "", "Images (*.png *.xpm *.jpg *.jpeg)", options=options)
        if file:
            save_dir = "img_tmp"  # 自定义文件夹路径
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            save_path = os.path.join(save_dir, 'image1.jpg')
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

            save_path = os.path.join(save_dir, 'image2.jpg')
            pixmap = QtGui.QPixmap(file)
            pixmap.save(save_path)
            scaled_pixmap = pixmap.scaled(self.label_2.size(), QtCore.Qt.KeepAspectRatio)
            self.label_2.setPixmap(scaled_pixmap)


    def startButtonClicked(self):
        try:
            imageA = cv2.imread(r"img_tmp/image1.jpg")
            imageB = cv2.imread(r"img_tmp/image2.jpg")
            print("SHAPE:", imageA.shape, imageB.shape)
        except Exception as e:
            self.warning_window = Warning()
            self.warning_window.start()
            print("startButtonClicked without load image error:", e)
            return

        try:
            stitcher = Stitcher()
            (result, vis) = stitcher.stitch([imageA, imageB],
                                        showMatches=True)
        except Exception as e:
            self.warning_window = Warning()
            self.warning_window.start()
            print("stitch failed, i dont know why, and the error:", e)
            return


        if result is not None:
            stitcher.cut_handle()  # 裁剪
        else:
            self.warning_window = Warning()
            self.warning_window.start()
            print("stitch result is None, cant crop")
            return

        try:
            cv2.imwrite(r"img_tmp\result.jpg", result)
        except Exception as e:
            self.warning_window = Warning()
            self.warning_window.start()
            print("save failed, the error :", e, "look by yourself")

        self.result_window = result_ui()  # 使用self.more_window来保存more_Window的实例
        self.result_window.start()

    def cleanupButtonClicked(self):
        # pushButton_4 按钮的槽函数
        self.lable1.clear()
        self.label_2.clear()

    def moreButtonClicked(self):
        self.more_window = More_Windows()  # 使用self.more_window来保存more_Window的实例

        self.more_window.start()

    def revole_1_ButtonClicked(self):
        try:
            img = cv2.imread("img_tmp/image1.jpg")


            # 使用OpenCV进行旋转
            trance_img = cv2.transpose(img)
            rotated = cv2.flip(trance_img,0)

            # 保存旋转后的图片
            cv2.imwrite("img_tmp/image1.jpg", rotated)

            # 加载图片
            pixmap = QPixmap(r'img_tmp/image1.jpg')
            # 将图片缩放到标签的大小，并保持图片的比例
            pixmap = pixmap.scaled(self.lable1.width(), self.lable1.height(), QtCore.Qt.KeepAspectRatio)
            # 在标签上显示图片
            self.lable1.setPixmap(pixmap)

        except Exception as e:
            self.warning_window = Warning()
            self.warning_window.start()
            print("revole_1_ButtonClicked error:", e)



    def revole_2_ButtonClicked(self):

        try:
            img = cv2.imread("img_tmp/image2.jpg")

            # 使用OpenCV进行旋转
            trance_img = cv2.transpose(img)
            rotated = cv2.flip(trance_img,0)

            # 保存旋转后的图片
            cv2.imwrite("img_tmp/image2.jpg", rotated)

            # 加载图片
            pixmap = QPixmap(r'img_tmp/image2.jpg')
            # 将图片缩放到标签的大小，并保持图片的比例
            pixmap = pixmap.scaled(self.label_2.width(), self.label_2.height(), QtCore.Qt.KeepAspectRatio)
            # 在标签上显示图片
            self.label_2.setPixmap(pixmap)

        except Exception as e:
            self.warning_window = Warning()
            self.warning_window.start()
            print("revole_2_ButtonClicked error:", e)

    def clear_tmp(self):
        all_tmp_file = os.listdir("img_tmp")
        if len(all_tmp_file) > 0:
            for tmp_name in all_tmp_file:
                os.remove(os.path.join("img_tmp", tmp_name))
                print("delete successful: ", os.path.join("img_tmp", tmp_name))

        self.MainWindow.close()

    def start(self):
        self.MainWindow = QMainWindow()  # 使用self.MainWindow来保存QMainWindow的实例
        self.setupUi(self.MainWindow)
        self.MainWindow.show()
