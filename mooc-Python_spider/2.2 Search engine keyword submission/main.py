import requests
keyword = 'Python'
url = 'http://www.baidu.com/s'
try:
    kv = {'wd': keyword}
    r = requests.get(url, params=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print('Error')
