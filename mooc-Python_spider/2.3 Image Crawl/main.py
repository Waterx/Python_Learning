import requests
import os

url = "http://image.nationalgeographic.com.cn/2017/0828/20170828015807534.jpg"
path = url.split('/')[-1]
try:
    r = requests.get(url)
    r.raise_for_status()
    with open(path, 'wb') as f:
        f.write(r.content)
        f.close()
        print("The file saved successfully")

except:
    print("ERROR")


# The following code is example-------------------

url = "http://image.nationalgeographic.com.cn/2017/0828/20170828015807534.jpg"
root = "D://pics//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("The file saved successfully")
    else:
        print("The file has already exists")
except:
    print("ERROR")