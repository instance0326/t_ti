
import os
import json

'''
path = './0_json'
files = os.listdir(path)

for k in files:
    # 讀取點位資訊
    with open(path + "/" + k, 'r') as load_f:
        jt2 = json.load(load_f)

    print(k)

    for l in range(25):

        if jt2['part_candidates'][0]['%s' %l] == []:

            print(l)
'''

'''
path = './0'
files = os.listdir(path)

for i in range(len(files)):

    oldname = path + "/" + files[i]
    newname = "./0_jpg/" + oldname.split(".")[0] + ".jpg"

    os.rename(oldname, newname)
'''
'''
path2 = './0'
files2 = os.listdir(path2)

for k in files2:
    fil_json = k.rsplit(".", 1)
    print(fil_json)
'''


'''
path = './0_IUV'
files = os.listdir(path)
print(files[0].rsplit("_", 1))
'''


import cv2
import matplotlib.pyplot as plt
import pandas as pd
IUV = cv2.imread('./2_IUV/L_0_IUV.png')
x = pd.DataFrame(IUV[:,:,0]/1)

with open("./L/L_0_keypoints.json", "r") as f:
    jt2 = json.load(f)
print(jt2['part_candidates'][0]['8'])

plt.imshow(IUV[:,:,0]/1)
plt.show()



'''
path = "./thin"
if not os.path.isdir(path):
    os.mkdir(path)

f = os.listdir(path)
print(f)
'''


'''
from operator import itemgetter

# 讀資料
with open("./M/M_12_keypoints.json", 'r') as load_f:
    jt2 = json.load(load_f)

print(jt2['part_candidates'][0])
print(len(jt2['part_candidates'][0]))

# 篩選出前3筆資料
for i in range(len(jt2['part_candidates'][0])):
    x = jt2['part_candidates'][0]['{}'.format(i)][0:3]

    print(x)
'''



'''
point = []

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
'''




