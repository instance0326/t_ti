import os

p = 2
q = "L"

path = './{}/{}_img'.format(q, p)
files = os.listdir(path)

path2 = './%s' % q

for i in range(len(files)):

    oldname = path + "/" + files[i]
    newname = path + "/" + '%s_' % q + str(i) + ".jpg"

    os.rename(oldname, newname)

    json_old = files[i].rsplit(".", 1)[0] + "_keypoints.json"

    oldname1 = path2 + "/" + json_old
    newname1 = path2 + "/" + '%s_' % q + str(i) + "_keypoints.json"

    os.rename(oldname1, newname1)



