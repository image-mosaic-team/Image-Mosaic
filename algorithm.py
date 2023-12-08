# -*- coding: utf-8 -*-
# @Author : Jiahao Zeng

import numpy as np
import cv2
import json

# achieve stitcher
class Stitcher:
    """
    初始化：
        需要传入参数文件

    两个主要的属性：
        1、result（首拼接的图片没有处理）
        2、cut_img（用户剪切后的图片）
    
    使用简介：
        初始后可以使用“def stitch(self, images, showMatches=False):”函数，使用时为了测试一般会把showMatches设置为true
        返回拼接后的图像和特征点匹配的效果图

        使用“def cut_handle(self):”对图片进行手动剪切，最后会保存在img_tmp中的result_crop.jpg中，如果想后续使用则需要使用
        stitch.cut_img访问该属性


    开发备注：
        还是拼接后的黑色区域需要改善，之前想着自动去除黑色，但是仅限图像输入完整，如果过于奇怪则效果巨差。
        所以现在使用的是手动裁剪后保存（如果有更好的机器学习想法可以提出）
        图像修复CSTGD感觉可以用，但是仅限机器学习的技术和实现复杂度就暂时不考虑）
    """
    def __init__(self, path='algo_para.json'):
        algo_para_json = open(path,'r',encoding='utf-8')
        algo_para_dict = json.load(algo_para_json)

        self.ratio = algo_para_dict["ratio"]
        self.reprojThresh = algo_para_dict["reprojThresh"]
        self.Homography_matrix = algo_para_dict["Homography_matrix"]

        self.point1 = 0
        self.point2 = 0

        self.result = None
        self.cut_img = None

    def stitch(self, images, showMatches=False):
        '''
        主函数

        :param images : 输入的一组图像
        :param showMatches : 是否返回结果（拼接结果和特征点匹配的结果）

        :return : 返回结果（拼接结果和特征点匹配的结果）
        '''
        (imageB, imageA) = images
        
        (kpsA, featuresA) = self.detectAndDescribe(imageA)
        (kpsB, featuresB) = self.detectAndDescribe(imageB)  # 检测A B特征关键点，并计算特征描述子

        M = self.matchKeypoints(kpsA, kpsB, featuresA, featuresB, self.ratio, self.reprojThresh, self.Homography_matrix)  # 匹配两张图片的所有特征点，返回匹配结果

        if M is None:
            return None

        (matches, H, status) = M
        # print("Status", status)
        result = cv2.warpPerspective(imageA, H, (imageA.shape[1] + imageB.shape[1], imageA.shape[0]))
        result[0:imageB.shape[0], 0:imageB.shape[1]] = imageB

        self.result = result  # save

        if showMatches:
            vis = self.drawMatches(imageA, imageB)
            return result, vis

    def detectAndDescribe(self, image):
        """
        检测关键点计算特征描述符

        :param iamge: 传入单个图像

        :return 计算关键点和特征描述符（特征）
        """
        # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        descripter = cv2.SIFT_create()
        (kps, features) = descripter.detectAndCompute(image, None)
        kps = np.float32([kp.pt for kp in kps])
        return (kps, features)

    def matchKeypoints(self, kpsA, kpsB, featuresA, featuresB, ratio, reprojThresh, Homography_matrix):
        """
        匹配该方法接受两组关键点和特征描述符，以及比值测试的阈值和R	ANSAC算法的阈值，然后找出匹配的关键点。

        :param kspA、kspB : 这两个参数是从两个输入图像中检测到的关键点的坐标。这些关键点是使用SIFT描述符检测到的。
        :param featuresA、featuresB : 这两个参数是从两个输入图像中计算出的特征描述符。特征描述符是使用SIFT描述符计算出的，它们描述了关键点周围的图像区域的外观。
        :param reatio : 参数是用于比值测试的阈值
        :param reprojThresh : 用于计算单应性矩阵的RANSAC算法的阈值。
        :param Homography_matrix : 需要匹配点的个数大于这个值才算能拼接
        :return : 返回匹配的关键点、单应性矩阵和状态值
        """
        matcher = cv2.BFMatcher()
        rawMatches = matcher.knnMatch(featuresA, featuresB, 2)
        matches = []
        for m in rawMatches:
            if len(m) == 2 and m[0].distance < m[1].distance * ratio:
            #  如果两个匹配都存在，并且第一个匹配的距离小于第二个匹配的距离乘以一个比率（这是一个阈值），那么我们认为这是一个好的匹配。
                matches.append((m[0].trainIdx, m[0].queryIdx))

        if len(matches) > Homography_matrix:  
        # 如果找到的匹配数大于一个阈值，那么我们将计算单应性矩阵。
            ptsA = np.float32([kpsA[i] for (_, i) in matches])
            ptsB = np.float32([kpsB[i] for (i, _) in matches])
            (H, status) = cv2.findHomography(ptsA, ptsB, cv2.RANSAC, reprojThresh)
            return (matches, H, status)


    def drawMatches(self, imageA, imageB):
        """
        该方法接受两个图像作为输入，然后显示匹配的特征点。

        :param imageA、imageB : 传入图像
        
        :return : 拼接好之后的图像
        """
        bf = cv2.BFMatcher()
        sift = cv2.SIFT_create()
        kp1, des1 = sift.detectAndCompute(imageA, None)
        kp2, des2 = sift.detectAndCompute(imageB, None)
        matches = bf.knnMatch(des1, des2, k=2)
        good = []
        for m,n in matches:
            if m.distance < 0.75 * n.distance:
                good.append([m])

        img3 = cv2.drawMatchesKnn(imageB, kp2, imageA, kp1, good, None, flags=2)
        return img3
    
    def on_mouse(self, event, x, y, flags, param):
        """
        鼠标点击函数，根据框出的矩形进行最后结果的保存
        """
        result_copy = self.result.copy()

        if event == cv2.EVENT_LBUTTONDOWN:  #左键点击
            self.point1 = (x,y)
            cv2.circle(result_copy, self.point1, 10, (0,255,0), 5)
            cv2.imshow('crop', result_copy)

        elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):  #按住左键拖曳
            cv2.rectangle(result_copy, self.point1, (x,y), (255,0,0), 5)
            cv2.imshow('crop', result_copy)

        elif event == cv2.EVENT_LBUTTONUP:  #左键释放
            self.point2 = (x,y)
            cv2.rectangle(result_copy, self.point1, self.point2, (0,0,255), 5)
            cv2.imshow('crop', result_copy)
            min_x = min(self.point1[0],self.point2[0])
            min_y = min(self.point1[1],self.point2[1])
            width = abs(self.point1[0] - self.point2[0])
            height = abs(self.point1[1] -self.point2[1])
            self.cut_img = self.result[min_y:min_y+height, min_x:min_x+width]

            """
            23/12/2 修改，不清楚什么时候会进入Exception
            """
            try:
                if len(self.cut_img) > 0:
                    cv2.imwrite('img_tmp/result_crop.jpg', self.cut_img)
                    print("save successful")
                else:
                    print("redraw")
            except Exception as e:
                print(self.cut_img)
                print("def on_mouse in algorithm.py error:", e)

    def cut_handle(self):
        """
        on_mouse函数的调用，设置窗口等
        """
        cv2.namedWindow('crop')
        cv2.setMouseCallback('crop', self.on_mouse)
        cv2.imshow('crop', self.result)
        cv2.waitKey(0)
 
# ----------------------------------------------------------------------------------------------


if __name__ == "__main__":

    # TODO:修改固定地址
    imageA = cv2.imread("test_img/image1.jpg")
    imageB = cv2.imread("test_img/image2.jpg")

    # TODO：考虑需不需要统一大小
    # x, y, c = imageA.shape  
    # imageB = cv2.resize(imageB, (y, x))
 
    # --------------------------------------

    # start stitcher
    stitcher = Stitcher()
    (result, vis) = stitcher.stitch([imageA, imageB],
                                    showMatches=True)

    stitcher.cut_handle()  # 裁剪
    
    # save TODO:修改固定地址
    # try:
    #     cv2.imwrite("img_tmp/result.jpg", result)
    #     cv2.imwrite("img_tmp/result_crop.jpg", stitcher.cut_img)
    # except:
    #     print("保存失败")
    # cv2.imwrite("vis", vis)


    # visual
    # cv2.imshow("Image A", imageA)
    # cv2.imshow("Image B", imageB)
    # cv2.imshow("Keypoint Matches", vis)
    # cv2.imshow("Result", result)
    # cv2.imshow("Result_Crop", stitcher.cut_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()