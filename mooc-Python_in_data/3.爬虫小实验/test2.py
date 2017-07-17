import requests
from bs4 import BeautifulSoup
import re
import random
import time

item_num = 0
sum = 0
i = 0
while item_num < 50:
    i = i + 1
    url = "https://book.douban.com/subject/1082154/comments/hot?p={0:d}".format(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    pattern = soup.find_all('p', 'comment-content')
    for item in pattern:
        print(item_num)
        print(item.string, '\n')
        item_num = item_num + 1
        if item_num > 50:
            break
    pattern_s = re.compile('<span class="user-stars allstar(.*)rating"')
    p = re.findall(pattern_s, r.text)
    for star in p:
        sum += int(star)
    time.sleep(random.randint(1, 5))
ave = sum / 50
print("The average star:", ave)
