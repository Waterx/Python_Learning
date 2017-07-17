
import requests
from bs4 import BeautifulSoup
import re
sum = 0

r = requests.get('http://money.cnn.com/data/dow30/')
soup = BeautifulSoup(r.text, 'lxml')
pattern = soup.find_all('a', 'wsod_symbol')
pattern2 = soup.find_all('span')
i = 0
for item in pattern:
    print(i+1)
    print(item.string, '\n')
    i = i + 1
for item in pattern2:
    print(item.string, '\n')
# pattern_s = re.compile('<span class="user-stars allstar(.*)rating"')
# p = re.findall(pattern_s, r.text)
# for star in p:
#     sum += int(star)
# print(sum)

