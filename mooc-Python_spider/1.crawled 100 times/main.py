import requests
import time

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'ERROR'

if __name__ == '__main__':
    url = "https://www.baidu.com"
    start = time.clock()
    for i in range(100):
        print(i)
        getHTMLText(url)
    end = time.clock()
    length = end - start
    print('{} {}'.format(url, length))

