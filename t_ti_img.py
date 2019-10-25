# --輪廓
import cv2
import csv
import json
import numpy as np
import pandas as pd

# 讀取點位資訊
img_name = '1'

with open("./save/%s_keypoints.json" % img_name, 'r') as load_f:
    jt2 = json.load(load_f)

print(jt2['part_candidates'][0])

# 影像處理
image = cv2.imread("./save/n1-r.jpg")
image2 = cv2.imread("./save/n1_25.png")
# 灰階處理
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 高斯模糊
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
# 人型輪廓
canny = cv2.Canny(blurred, 0, 0)

# 把二為矩陣存成CSV檔
with open('./save/n1.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(canny)

# 在骨架圖上劃出輪廓，方便觀察
contours, hierarchy = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(image2, contours, -1, (0, 0, 255), 1)

# 跳出視窗
cv2.imshow("Result:", image2)
# 固定視窗
cv2.waitKey(0)

# 讀取點位資訊
with open("./save/n1_keypoints.json", 'r') as load_f:
    jt2 = json.load(load_f)

print(jt2)

'''
# 有效點判斷
point = []
for i in range(len(jt2['part_candidates'][0])):

    try:

        keep = (jt2['part_candidates'][0]['%s' % i][0], jt2['part_candidates'][0]['%s' % i][1])
        point.append(keep)
        print(jt2['part_candidates'][0]['%s' % i])

    except IndexError:

        point.append(())
        print("point %s noting" % i)

print(point)
'''


# 讀取人體輪廓二維資料
with open('./save/1.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    cn1 = []

    for row in rows:
        cn1.append(row)


def get_point(p, y):

    return round(jt2['part_candidates'][0]['%s' % p][y])


# 計算輪廓寬度
def user_cwn(p, x):

    need_point = {"1": "肩", "8": "臀"}
    ydex = []

    for j in range(1, len(cn1[x])):

        if cn1[x][j] == '255':

            ydex.append(j)

    print(need_point["%s" % p], "的輪廓 :", ydex)
    print(need_point["%s" % p], "寬 :", ydex[-1] - ydex[0], "像素距")


def user_ew():

    need_point = {"26": "腰", "27": "胸"}

    ydex = []

    y26 = round(get_point(8, 1) - ((get_point(8, 1) - get_point(1, 1)) / 3))
    y27 = round(get_point(1, 1) + ((get_point(8, 1) - get_point(1, 1)) / 3))

    for j in range(1, len(cn1[y26])):

        if cn1[y26][j] == '255':

            ydex.append(j)

    print(need_point["%s" % 26], "的輪廓 :", ydex)
    print(need_point["%s" % 26], "寬 :", ydex[-1] - ydex[0], "像素距")

    ydex = []

    for j in range(1, len(cn1[y27])):

        if cn1[y27][j] == '255':

            ydex.append(j)

    print(need_point["%s" % 27], "的輪廓 :", ydex)
    print(need_point["%s" % 27], "寬 :", ydex[-1] - ydex[0], "像素距")


def user_long():

    need_point = {"28": "身長", "29": "總長"}

    y28 = round(np.sqrt(np.square(get_point(8, 0) - get_point(1, 0)) + np.square(get_point(8, 1) - get_point(1, 1))))
    y29 = round(np.sqrt(np.square(get_point(13, 0) - get_point(12, 0)) +
                        np.square(get_point(13, 1) - get_point(12, 1))) +
                np.sqrt(np.square(get_point(14, 0) - get_point(13, 0)) +
                        np.square(get_point(14, 1) - get_point(13, 1)))
                )

    print(need_point["%s" % 28], ":", int(y28), "像素距")
    print(need_point["%s" % 29], ":", int(y29), "像素距")


# 輸入需求點位並計算寬度
user_cwn(8, round(jt2['part_candidates'][0]['%s' % 8][1]))
user_ew()
user_long()








