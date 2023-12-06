import cv2
import numpy as no


'''
23/11/19 10:35
@author:zjh
@introduce:
    alpha参数用于控制对比度。alpha的值可以是任何非负实数
    alpha的值越大，对比度越高；alpha的值越小，对比度越低。
    当alpha=1时，图像保持不变；当alpha<1时，对比度降低；当alpha>1时，对比度提高
'''

def modify_constract(image, alpha):
    return cv2.convertScaleAbs(image, alpha=alpha, beta=0)

if __name__ == "__main__":
    img = cv2.imread('/home/zjh/codeSpace/python/Image-Mosaic/Image-Mosaic/test_img/image1.jpg')
    alpha = 3

    result = modify_constract(img, alpha)

    cv2.imwrite("/home/zjh/codeSpace/python/Image-Mosaic/Image-Mosaic/test_img/modify_constract.png", result)
