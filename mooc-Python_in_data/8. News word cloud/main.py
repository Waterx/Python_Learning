import requests
import re
import jieba.posseg as pseg
from wordcloud import WordCloud
import pandas as pd
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt


def get_html_text(url):
    try:
        r = requests.get(url, headers={'user-agent': 'Mozilla/5.0'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("Failed to get html text")


def get_title(raw_text):
    # !the meaning of ?
    # raw_string = r'<a target="_blank" href="(http://news.sina.com.cn/\w/.*?)">(.*?)</a>'
    raw_string = '.shtml" target="_blank">(.*?)</a></span>(.*?)<span class="c_time">(.*)</span>'
    search_pattern = re.compile(raw_string)
    text = re.findall(search_pattern, raw_text)
    df = pd.DataFrame(text, columns=['title', 'time'])
    # df.to_excel('title.xlsx')
    return df

def title_seg(df):

    stop_words = set(line.strip() for line in open('stop_words.txt', encoding='utf-8'))
    title_list = df.title.values.tolist()
    # !string to list
    title_list_str = ''.join(title_list)
    print(title_list_str)
    word_list = pseg.cut(title_list_str)
    newslist = []
    for word, flag in word_list:
        if word not in stop_words and flag == 'n':
            newslist.append(word+' ')
            # print('{} {}'.format(word, flag))
    return newslist

def draw_cloud(newslist):
    content = ''.join(newslist)
    d = path.dirname(__file__)
    mask_image = imread(path.join(d, "girl.png"))
    wordcloud = WordCloud(font_path='yayuan.otf', background_color="white",
                         mask=mask_image, max_words=40).generate(content)

    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
url = 'http://roll.news.sina.com.cn'
raw_text = get_html_text(url)
df = get_title(raw_text)
newslist = title_seg(df)
draw_cloud(newslist)