import os
import cv2
import csv
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

p1 = 1
p2 = 'M'

path = './%s_IUV' % p1
files = os.listdir(path)
path2 = './%s' % p2

df = pd.DataFrame(columns=["檔案id", "體型", "檔案長寬", "腳長", "身長", "臀寬", "腰寬", "胸寬"])


# 計算肩臀寬
def user_cwn(p):

    need_point = {"1": "肩", "8": "臀"}
    ydex = []

    y8 = round(jt2['part_candidates'][0]['%s' % p][1])

    for j in range(json_point.shape[1]):

        ls = int(json_point[y8:y8 + 1][j])

        if ls == 2 or ls == 9 or ls == 10:
            ydex.append(j)

    c8 = ydex[-1] - ydex[0]

    print(need_point["%s" % p], "的輪廓 :", ydex)
    print(need_point["%s" % p], "寬 :", ydex[-1] - ydex[0], "像素距")

    return c8


def get_point(p, y):

    return round(jt2['part_candidates'][0]['%s' % p][y])


# 計算腰胸寬
def user_ew():

    need_point = {"26": "腰", "27": "胸"}

    ydex1 = []

    y26 = round(get_point(8, 1) - ((get_point(8, 1) - get_point(1, 1)) / 3))
    y27 = round(get_point(1, 1) + ((get_point(8, 1) - get_point(1, 1)) / 3))

    for j in range(json_point.shape[1]):

        if int(json_point[y26:y26 + 1][j]) == 2:
            ydex1.append(j)

    c26 = ydex1[-1] - ydex1[0]

    print(need_point["%s" % 26], "的輪廓 :", ydex1)
    print(need_point["%s" % 26], "寬 :", c26, "像素距")

    ydex2 = []

    for j in range(json_point.shape[1]):

        if int(json_point[y27:y27 + 1][j]) == 2:
            ydex2.append(j)

    c27 = ydex2[-1] - ydex2[0]

    print(need_point["%s" % 27], "的輪廓 :", ydex2)
    print(need_point["%s" % 27], "寬 :", c27, "像素距")
    return c26, c27


# 計算身長總長
def user_long():

    need_point = {"28": "腳長", "29": "總長"}

    y28 = int(round(np.sqrt(np.square(get_point(8, 0) - get_point(1, 0)) +
                            np.square(get_point(8, 1) - get_point(1, 1)))))

    y29 = int(round(np.sqrt(np.square(get_point(13, 0) - get_point(12, 0)) +
                            np.square(get_point(13, 1) - get_point(12, 1))) +
                    np.sqrt(np.square(get_point(14, 0) - get_point(13, 0)) +
                            np.square(get_point(14, 1) - get_point(13, 1)))
                    ))

    print(need_point["%s" % 28], ":", y28, "像素距")
    print(need_point["%s" % 29], ":", y29, "像素距")
    return y28, y29


err = []

for k in files:

    try:

        df.to_csv("test%s.csv" % p1, encoding="utf-8", index=False)

        IUV = cv2.imread(path + "/" + k)
        json_point = pd.DataFrame(IUV[:,:,0]/1)

        x = json_point.shape
        with open(path2 + "/" + k.rsplit("_", 1)[0] + "_keypoints.json", 'r') as load_f:
            jt2 = json.load(load_f)

        print("======%s start======" % k)

        data = {
            "檔案id": k,
            "體型": p2,
            "檔案長寬": x,
            "腳長": user_long()[1],
            "身長": user_long()[0],
            "臀寬": user_cwn(8),
            "腰寬": user_ew()[0],
            "胸寬": user_ew()[1]
        }

        print("======OK!======")

        df = df.append(data, ignore_index=True)

    except IndexError:
        err.append(k)

print(err)







