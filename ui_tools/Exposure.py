import cv2
import numpy as np

'''
23/11/19 9:41
@author:zjh
@introduce:
    曝光修改gamma，起始值为1，大于1变白，小于1变黑
    使用时直接调用就好
    范围在0.1-10(大概)
'''

def modify_exposure(image, gamma=1.0):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
        for i in np.arange(0, 256)]).astype("uint8")
    
    return cv2.LUT(image, table)


if __name__ == "__main__":
    img = cv2.imread("test_img/16.png")
    gamma = 2

    result = modify_exposure(img, gamma)

    cv2.imwrite("test_img/modify_exposure.png", result)