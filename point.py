import json
import csv
import cv2


# 讀取點位資訊
with open("./save/1_keypoints.json", 'r') as load_f:
    jt2 = json.load(load_f)

print(jt2['part_candidates'][0])
print(len(jt2['part_candidates'][0]))

point = []

# 有效點判斷
for i in range(len(jt2['part_candidates'][0])):

    try:

        # if jt2['part_candidates'][0]['%s' % i][2] < 0.7:

        keep = (jt2['part_candidates'][0]['%s' % i][0], jt2['part_candidates'][0]['%s' % i][1])

        point.append(keep)
        print(jt2['part_candidates'][0]['%s' % i])

    except IndexError:

        point.append(())
        print("point %s noting" % i)

print(point)


print("肩中心點 :", jt2['part_candidates'][0]['9'])
print("腰中心點 :", jt2['part_candidates'][0]['8'])
print("腰中心點 :", jt2['part_candidates'][0]['12'])

print("肩中心點 :", jt2['part_candidates'][0]['1'])
print("肩中心點 :", jt2['part_candidates'][0]['8'])

# 讀取人體輪廓二維資料
with open('1.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)

    ct2 = []

    for row in rows:
        ct2.append(row)

need_point = {"1": "肩", "8": "腰"}


# 計算輪廓寬度
def user_t_ti(p, x):

    ydex = []

    for j in range(1, len(ct2[x+1])):

        if ct2[x+1][j] == '255':

            ydex.append(j)

    print(need_point["%s" % p], "的輪廓 :", ydex)
    print(need_point["%s" % p], "寬 :", ydex[-1] - ydex[0], "像素距")


# 輸入需求點位並計算寬度
p = input("plz input need point : ")

user_t_ti(p, round(jt2['part_candidates'][0]['%s' % p][1]))
