import cv2
import numpy as np

def enhance(img, brightness, constract, exposure, saturation):

    if brightness != 0:
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
    
    if constract != 1:
        img = cv2.convertScaleAbs(img, alpha=constract, beta=0)

    if exposure != 1:
        invGamma = 1.0 / exposure
        table = np.array([((i / 255.0) ** invGamma) * 255
            for i in np.arange(0, 256)]).astype("uint8")
        
        img = cv2.LUT(img, table)
    
    if saturation != 1:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        hsv[:,:,1] = hsv[:,:,1]*saturation

        hsv[:,:,1] = np.clip(hsv[:,:,1],0,255)

        img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    return img