
import requests
from bs4 import BeautifulSoup
import re
sum = 0

r = requests.get('https://book.douban.com/subject/1082154/comments/')
soup = BeautifulSoup(r.text, 'lxml')
pattern = soup.find_all('p', 'comment-content')
i = 0
for item in pattern:
    print(i+1)
    print(item.string, '\n')
    i = i + 1
pattern_s = re.compile('<span class="user-stars allstar(.*)rating"')
p = re.findall(pattern_s, r.text)
for star in p:
    sum += int(star)
print(sum)

