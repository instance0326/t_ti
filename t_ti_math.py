
import csv
import cv2
import json

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
with open('./save/n1.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    cn1 = []

    for row in rows:
        cn1.append(row)

need_point = {"1": "肩", "8": "腰"}


# 計算輪廓寬度
def user_t_ti(p, x):

    ydex = []

    for j in range(1, len(cn1[x+1])):

        if cn1[x+1][j] == '255':

            ydex.append(j)

    print(need_point["%s" % p], "的輪廓 :", ydex)
    print(need_point["%s" % p], "寬 :", ydex[-1] - ydex[0], "像素距")


# 輸入需求點位並計算寬度
p = input("plz input need point : ")

user_t_ti(p, round(jt2['part_candidates'][0]['%s' % p][1]))
