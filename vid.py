import cv2
import json
import csv
import numpy as np

cap = cv2.VideoCapture(0)
flag = 1
num = 1

'''
# 讀取點位資訊
with open("./n1_keypoints.json", 'r') as load_f:
    jt2 = json.load(load_f)


# 判斷
def get_point(x, y):

    return round(jt2['part_candidates'][0]['%s' % x][y])


def body_down():

    if 0.8 < abs(get_point(9, 0) - get_point(8, 0)) / abs(get_point(8, 0) - get_point(12, 0)) < 1.2:

        print("下半身左右比例正確")

        if abs(get_point(9, 1) - get_point(8, 1)) < 5 and abs(get_point(8, 1) - get_point(12, 1)) < 5:

            print("左右腰高度一致")

            if abs(get_point(9, 0) - get_point(12, 0)) < abs(get_point(10, 0) - get_point(13, 0)):

                print("左右腳沒交叉")
                print("======down right======")

                return True


def body_up():

    if 0.8 < abs(get_point(2, 0) - get_point(1, 0)) / abs(get_point(1, 0) - get_point(5, 0)) < 1.2:

        print("上半身左右比例正確")

        if abs(get_point(2, 1) - get_point(1, 1)) < 5 and abs(get_point(1, 1) - get_point(5, 1)) < 5:

            print("左右肩高一致")

            if abs(get_point(4, 1) - get_point(3, 1)) < 5 and abs(get_point(3, 1) - get_point(2, 1)) < 5 :

                print("右臂高度一致")

                if 0.8 < abs(get_point(4, 0) - get_point(3, 0)) / abs(get_point(3, 0) - get_point(2, 0)) < 1.2:

                    print("右臂比例一致")

                    if abs(get_point(7, 1) - get_point(6, 1)) < 6 and abs(get_point(6, 1) - get_point(5, 1)) < 6:

                        print("左臂高度一致")

                        if 0.8 < abs(get_point(7, 0) - get_point(6, 0)) / abs(get_point(6, 0) - get_point(5, 0)) < 1.2:

                            print("左臂比例一致")
                            print("======up right======")

                            return True


if body_down() == True and body_up() == True:
    print("體態資訊已存入資料庫!")
'''


'''
point = []

# 有效點判斷
for i in range(len(jt2['part_candidates'][0])):

    keep = (round(jt2['part_candidates'][0]['%s' % i][0]), round(jt2['part_candidates'][0]['%s' % i][1]))
    point.append(keep)
'''

while True:

    ret_flag, Vshow = cap.read()

    k = cv2.waitKey(1) & 0xFF

    #for pt in point:
     #   cv2.circle(Vshow, pt, 3, (0, 255, 255), 3)

    cv2.imshow("Test", Vshow)

    if k == ord('s'):

        cv2.imwrite('C:/Users/User/PycharmProjects/opencv/show/' + str(num) + ".jpg", Vshow)

        print(cap.get(3))
        print(cap.get(4))
        print("success to save" + str(num) + ".jpg")
        print("====================================")
        num += 1

    elif k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()














