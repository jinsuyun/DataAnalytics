from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlopen
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv
driver_path='../resources/chromedriver'

f = open('../crawling.csv', 'w',encoding="euc_kr",newline='')
wr=csv.writer(f)
wr.writerow(["NEWS_TITLE"])
for index in range(1,10):
    urls='https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230&page='
    page_idx=str(index)
    urls=urls+page_idx

    html=urlopen(urls)
    source=html.read()
    soup=BeautifulSoup(source,'html.parser')
    html.close()

    it_title_soup=soup.select('div.content > div > ul > li > dl > dt > a')

    for title in it_title_soup:
        wr.writerow([title.text.strip()])
        #print(title.text.strip())
        #hdline_news_title=soup.select('div.hdline_article_tit > a')[i].text.strip()
        #hdline_news_href=soup.select('div.hdline_article_tit > a')[i]['href']
        # gov_news_title=soup.select('div#section_politics > div > div > ul > li > a')[i].text.strip() # div.클래스 div.#아이디
        # eco_news_title=soup.select('div#section_economy > div > div > ul > li > a')[i].text.strip()
        # soc_news_title=soup.select('div#section_society > div > div > ul > li > a')[i].text.strip()
        # life_news_title=soup.select('div#section_life > div > div > ul > li > a')[i].text.strip()
        # world_news_title=soup.select('div#section_world > div > div > ul > li > a')[i].text.strip()
        # it_news_title=soup.select('div#section_it > div > div > ul > li > a')[i].text.strip()
        # f.write(hdline_news_title)
        # f.write(gov_news_title)
        # f.write(eco_news_title)
        # f.write(soc_news_title)
        # f.write(life_news_title)
        # f.write(world_news_title)
        # f.write(it_news_title)
        #article_address.append(urls+hdline_news_href)
    #browser.quit()

f.close()



from konlpy.tag import Hannanum
from collections import Counter
import pytagcloud # Add fonts supporting Korean

import simplejson


f = open("../crawling.txt", "r", encoding="utf-8")
description = f.read()

h = Hannanum()
nouns = h.nouns(description) #단어 단어 별로 리스트화
print("단어별 리스트")
print(nouns)
print("단어별 카운트")
count = Counter(nouns) #단어별로 카운트
print(count)

print("TAG")
tag = count.most_common(100) # 키값과 VALUE를 나타냄
print(tag)

print("TAG_LIST")
tag_list = pytagcloud.make_tags(tag, maxsize=50)
print(tag_list) # RGB값의 Color와 태크, 글씨 크기를 나타냄
pytagcloud.create_tag_image(tag_list, 'word_cloud.jpg', size=(900, 600), fontname='Korean',
rectangular=False)

import webbrowser
webbrowser.open('word_cloud.jpg')
