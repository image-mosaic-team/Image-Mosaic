import cv2
import numpy as np

'''
23/11/29 10:10
@author:zjh
@introduce:
    饱和度saturation_scale值的范围没有严格的限制。它可以是任何正数：
    当saturation_scale值大于1时，图像的饱和度会增加。
    当saturation_scale值小于1时，图像的饱和度会降低。
    合理的范围内选择saturation_scale值，比如0.1到10。
'''
def modify_saturation(img, saturation_scale):

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hsv[:,:,1] = hsv[:,:,1]*saturation_scale

    hsv[:,:,1] = np.clip(hsv[:,:,1],0,255)

    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)


if __name__ == "__main__":
    img = cv2.imread('test_img/16.png')
    saturation_scale = 5

    result = modify_saturation(img, saturation_scale)

    cv2.imwrite("test_img/modify_saturation.png", result)
