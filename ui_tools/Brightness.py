import cv2
import numpy as np

'''
23/11/29 10:10
@author:zjh
@introduce:
    亮度当brightness值大于0时，图像会变亮。
    当brightness值小于0时，图像会变暗。
    合理的范围内选择brightness值，比如-100到100。
'''

def modify_brightness(img, brightness=0):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # 将图像从BGR转换到HSV
    h, s, v = cv2.split(hsv) # 将HSV图像分解为H，S和V通道

    if brightness > 0:
        lim = 255 - brightness
        v[v > lim] = 255
        v[v <= lim] += brightness
    else:
        lim = np.absolute(brightness)
        v[v < lim] = 0
        v[v >= lim] -= np.absolute(brightness)

    final_hsv = cv2.merge((h, s, v)) # 合并H，S和V通道
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR) # 将图像从HSV转换回BGR
    return img

if __name__ == "__main__":
    img = cv2.imread('test_img/16.png')
    brightness = 100 

    result = modify_brightness(img, brightness=brightness)

    cv2.imwrite("test_img/modify_brightness.png", result)