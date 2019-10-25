import os
import json
import shutil

path = './2_json'
files = os.listdir(path)

path2 = './2'
files2 = os.listdir(path2)
need_point = [2, 1, 5, 9, 8, 12, 10, 13, 11, 14]

path3 = './L'
import time
time.sleep()
for k in files2:

    try:

        fil_json = k.rsplit(".", 1)[0] + "_keypoints.json"

        # 讀取點位資訊
        with open(path + "/" + fil_json, 'r') as load_f:
            jt2 = json.load(load_f)

        n = 0
        for l in need_point:

            if jt2['part_candidates'][0]['%s' % l] == []:

                shutil.copy(path + "/" + fil_json, path2 + "_import")
                shutil.copy(path2 + "/" + k, path2 + "_import")
                n = 1
                break

        if n == 1:
            continue

        # 判斷
        def get_point(x, y):

            return round(jt2['part_candidates'][0]['%s' % x][y])

        def body_down():

            bl = abs(get_point(9, 0) - get_point(8, 0) + 0.1) / abs(get_point(8, 0) - get_point(12, 0) + 0.1)
            h1 = abs(get_point(9, 1) - get_point(8, 1))
            h2 = abs(get_point(8, 1) - get_point(12, 1))

            if bl < 0.8 or bl > 1.2:
                return False
            elif h1 > 7 or h2 > 7:
                return False
            else:
                return True

        def body_up():

            bl = abs(get_point(2, 0) - get_point(1, 0)) / abs(get_point(1, 0) - get_point(5, 0))
            h1 = abs(get_point(2, 1) - get_point(1, 1))
            h2 = abs(get_point(1, 1) - get_point(5, 1))

            if bl < 0.8 or bl > 1.2:
                return False
            elif h1 > 7 or h2 > 7:
                return False
            else:
                return True

        if body_down() == True and body_up() == True:

            shutil.copy(path + "/" + fil_json, path3)
            shutil.copy(path2 + "/" + k, path3 + "/2_img")

        else:
            shutil.copy(path + "/" + fil_json, path2 + "_remove")
            shutil.copy(path2 + "/" + k, path2 + "_remove")

    except FileNotFoundError:

        print(k)
        shutil.copy(path2 + "/" + k, path2 + "_nofind")





