
'''
import random
import cv2
import pandas as pd
import csv


# 讀取照片
image = cv2.imread('t1.png')
# 轉換成灰階
image_g = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 轉換成二進制
x = pd.DataFrame(image_g)

# 存成CSV檔
x.to_csv("tttttt")
'''
'''
from PIL import Image
new_im = Image.fromarray(x)
# ?示?片
new_im.show()
'''



'''
# -- 基礎
import cv2
import numpy as np
import pandas as pd
from PIL import Image

image = cv2.imread("t2.jpg")

# 灰階處理
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 高斯模糊
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
# 人型輪廓
canny = cv2.Canny(blurred, 100, 200)
print(canny[50])
# 三個願望一次滿足
result = np.hstack([gray, blurred, canny])

# 跳出視窗
cv2.imshow("Result:", canny)
cv2.imwrite('t2_output.jpg', canny)
# 固定視窗
cv2.waitKey(0)
'''

'''
# -- 滑動調參
import cv2
import numpy as np


def CannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(gray, (3, 3), 0)
    detected_edges = cv2.Canny(detected_edges, lowThreshold, lowThreshold * ratio, apertureSize=kernel_size)
    dst = cv2.bitwise_and(img, img, mask=detected_edges)
    cv2.imshow('canny demo', dst)


lowThreshold = 0
max_lowThreshold = 100
ratio = 2
kernel_size = 3

img = cv2.imread('t1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('canny demo')

cv2.createTrackbar('Min threshold', 'canny demo', lowThreshold, max_lowThreshold, CannyThreshold)

CannyThreshold(0)  # initialization
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
'''


# --輪廓
import cv2
import numpy as np
import pandas as pd


image = cv2.imread("n1_r.jpg")
image2 = cv2.imread("t2_pose.png")
# 灰階處理
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 高斯模糊
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
# 人型輪廓
canny = cv2.Canny(blurred, 50, 100)
print(canny)


print(len(canny[0]))
# 第一個參數是尋找輪廓的圖像；
#
# 第二個參數表示輪廓的檢索模式，有四種：
#     cv2.RETR_EXTERNAL表示只檢測外輪廓
#     cv2.RETR_LIST檢測的輪廓不建立等級關係
#     cv2.RETR_CCOMP建立兩個等級的輪廓，上面的一層為外邊界，
#     裡面的一層為內孔的邊界信息。如果內孔內還有一個連通物體，這個物體的邊界也在頂層。
#     cv2.RETR_TREE建立一個等級樹結構的輪廓。
#
# 第三個參數method為輪廓的近似辦法
#     cv2.CHAIN_APPROX_NONE存儲所有的輪廓點，相鄰的兩個點的像素位置差不超過1，
#     即max（abs（x1-x2），abs（y2-y1））==1
#     cv2.CHAIN_APPROX_SIMPLE壓縮水平方向，垂直方向，對角線方向的元素，
#     只保留該方向的終點坐標，例如一個矩形輪廓只需4個點來保存輪廓信息
#     cv2.CHAIN_APPROX_TC89_L1，CV_CHAIN_APPROX_TC89_KCOS使用teh-Chinl chain
#     近似算法
contours, hierarchy = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(image, contours, -1, (0, 0, 255), 1)


# cv2.imshow("img", image)
# cv2.waitKey(0)

result = np.hstack([gray, blurred, canny])

# 跳出視窗
cv2.imshow("Result:", canny)
cv2.imwrite('t2_output.jpg', canny)
# 固定視窗
cv2.waitKey(0)


'''
import cv2

imgfile = "t1.png"
img = cv2.imread(imgfile)
h, w, _ = img.shape

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 人型輪廓
canny = cv2.Canny(gray, 0, 0)

ret, thresh = cv2.threshold(canny, 127, 255, cv2.THRESH_BINARY)

# Find Contour
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# 需要搞一?list?cv2.drawContours()才行！！！！！
c_max = []
max_area = 0
max_cnt = 0
for i in range(len(contours)):
    cnt = contours[i]
    area = cv2.contourArea(cnt)
    # find max countour
    if (area > max_area):
        if (max_area != 0):
            c_min = []
            c_min.append(max_cnt)
            cv2.drawContours(img, c_min, -1, (0, 0, 0), cv2.FILLED)
        max_area = area
        max_cnt = cnt
    else:
        c_min = []
        c_min.append(cnt)
        cv2.drawContours(img, c_min, -1, (0, 0, 0), cv2.FILLED)

c_max.append(max_cnt)

cv2.drawContours(img, c_max, -1, (255, 255, 255), thickness=-1)

cv2.imwrite("mask.png", img)
cv2.imshow('mask', img)
cv2.waitKey(0)
'''

'''
import cv2

imgfile = "t1.png"
img = cv2.imread(imgfile)
h, w, _ = img.shape

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 0, 0)

ret, thresh = cv2.threshold(canny, 127, 255, cv2.THRESH_BINARY)

# Find Contour
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# 需要搞一?list?cv2.drawContours()才行！！！！！
c_max = []
for i in range(len(contours)):
    cnt = contours[i]
    area = cv2.contourArea(cnt)

    # ?理掉小的?廓?域，???域的大小自己定?。
    if (area < (h / 10 * w / 10)):
        c_min = []
        c_min.append(cnt)
        # thickness不?-1?，表示??廓?，thickness的值表示?的?度。
        cv2.drawContours(img, c_min, -1, (0, 0, 0), thickness=-1)
        continue
    #
    c_max.append(cnt)

cv2.drawContours(img, c_max, -1, (255, 255, 255), thickness=-1)

cv2.imwrite("mask.png", img)
cv2.imshow('mask', img)
cv2.waitKey(0)
'''










