import numpy as np
import cv2
import json

# achieve stitcher
class Stitcher:
    # 拼接函数
    def stitch(self, images, ratio=0.75, reprojThresh=4.0, Homography_matrix=4, showMatches=False):
        
        (imageB, imageA) = images
        
        (kpsA, featuresA) = self.detectAndDescribe(imageA)
        (kpsB, featuresB) = self.detectAndDescribe(imageB)  # 检测A B特征关键点，并计算特征描述子

        M = self.matchKeypoints(kpsA, kpsB, featuresA, featuresB, ratio, reprojThresh, Homography_matrix)  # 匹配两张图片的所有特征点，返回匹配结果

        if M is None:
            return None

        (matches, H, status) = M
        # print("Status", status)
        result = cv2.warpPerspective(imageA, H, (imageA.shape[1] + imageB.shape[1], imageA.shape[0]))
        result[0:imageB.shape[0], 0:imageB.shape[1]] = imageB
        if showMatches:
            vis = self.drawMatches(imageA, imageB)
            return result, vis

    def detectAndDescribe(self, image):
        # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        descripter = cv2.SIFT_create()
        (kps, features) = descripter.detectAndCompute(image, None)
        kps = np.float32([kp.pt for kp in kps])
        return (kps, features)

    def matchKeypoints(self, kpsA, kpsB, featuresA, featuresB, ratio, reprojThresh, Homography_matrix):
        matcher = cv2.BFMatcher()
        rawMatches = matcher.knnMatch(featuresA, featuresB, 2)
        matches = []
        for m in rawMatches:
            if len(m) == 2 and m[0].distance < m[1].distance * ratio:
                matches.append((m[0].trainIdx, m[0].queryIdx))

        if len(matches) > Homography_matrix:
            ptsA = np.float32([kpsA[i] for (_, i) in matches])
            ptsB = np.float32([kpsB[i] for (i, _) in matches])
            (H, status) = cv2.findHomography(ptsA, ptsB, cv2.RANSAC, reprojThresh)
            return (matches, H, status)


    def drawMatches(self, imageA, imageB):
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
    
# ----------------------------------------------------------------------------------------------

# ---- TODO：需要修改 -----
'''
删除多余黑色部分
2023.11.29 9:15 第二次修改，修改为使用二值化后找框来分界
'''
def delete_black(im):
    img = im.copy()
    img2 = im.copy()
    im = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
    # Read the image in grayscale

    thresh, im = cv2.threshold(im, 1, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(im, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img, contours, -1, (0,255,0), 2)

    max_x = -np.inf

    for contour in contours:

        x, y, w, h = cv2.boundingRect(contour)
        

        if x + w > max_x:
            max_x = x + w

    # print('最右上角的横坐标是：', max_x)
    max_x -= 10

    result = img2[:, :max_x]

    return result







if __name__ == "__main__":
    # load img and algp_para
    path='algo_para.json'
    algo_para_json = open(path,'r',encoding='utf-8')
    algo_para_dict = json.load(algo_para_json)

    ratio = algo_para_dict["ratio"]
    reprojThresh = algo_para_dict["reprojThresh"]
    Homography_matrix = algo_para_dict["Homography_matrix"]


    imageA = cv2.imread("test_img/16.png")
    imageB = cv2.imread("test_img/26.png")

    # x, y, c = imageA.shape  # TODO：需要修改 （好像又不需要修改了）
    # imageB = cv2.resize(imageB, (y, x))
 
    # --------------------------------------

    # start stitcher
    stitcher = Stitcher()
    (result, vis) = stitcher.stitch([imageA, imageB],
                                    ratio=ratio, 
                                    reprojThresh=reprojThresh,
                                    Homography_matrix=Homography_matrix, 
                                    showMatches=True)


    # save
    cv2.imwrite("img_tmp/result.jpg", result)
    change_result = delete_black(result)
    cv2.imwrite("img_tmp/result_delete_black.jpg", change_result)
    # cv2.imwrite("vis", vis)


    # visual
    # cv2.imshow("Image A", imageA)
    # cv2.imshow("Image B", imageB)
    # cv2.imshow("Keypoint Matches", vis)
    # cv2.imshow("Result", result)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()