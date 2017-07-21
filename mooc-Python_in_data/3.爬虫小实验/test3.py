
# import requests
# from bs4 import BeautifulSoup
# import re
# sum = 0
#
# r = requests.get('http://money.cnn.com/data/dow30/')
# soup = BeautifulSoup(r.text, 'lxml')
# pattern = soup.find_all('a', 'wsod_symbol')
# pattern2 = soup.find_all('tr')
# i = 0
# for item in pattern:
#     print(i+1)
#     print(item.string, '\n')
#     i = i + 1
# for item in pattern2:
#     print(item, '\n')
# # pattern_s = re.compile('<span class="user-stars allstar(.*)rating"')
# # p = re.findall(pattern_s, r.text)
# # for star in p:
# #     sum += int(star)
# # print(sum)

import requests
import re
def retrieve_dji_list():
    r = requests.get('http://money.cnn.com/data/dow30/')
    search_pattern =re.compile('''class="wsod_symbol">(.*)<\/a>.*<span.*">(.*?)<\/span>.*\n.*class="wsod_stream">(.*)<\/span>''')
    dji_list_in_text = re.findall(search_pattern, r.text)
    return dji_list_in_text
dji_list = retrieve_dji_list()
print(dji_list)
