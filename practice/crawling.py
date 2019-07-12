from selenium import webdriver
from bs4 import BeautifulSoup
############################################
#게임 url 및 게임 설명 크롤링
driver_path='../resources/chromedriver'
urls='https://play.google.com/store/apps/collection/cluster?clp=ChwKGgoUdG9wc2VsbGluZ19mcmVlX0dBTUUQBxgD:S:ANO1ljJH_B0&gsr=Ch4KHAoaChR0b3BzZWxsaW5nX2ZyZWVfR0FNRRAHGAM%3D:S:ANO1ljLEXvI'
browser=webdriver.Chrome(executable_path=driver_path)
browser.get(urls)

page=browser.page_source
soup=BeautifulSoup(page,'html.parser')
links=soup.find_all('div',{'class':'wXUyZd'})
googleStore_url='https://play.google.com'
for link in links: # div의 class wXUyZd의 여러개 태그중에서 a태그를 가져오기 위한 for문
    new_url=link.a['href']#여러 태그 중 a태그에서 href를 가져온다
    print(googleStore_url+new_url)
    browser.get(googleStore_url+new_url)
    description_page=browser.page_source
    soup=BeautifulSoup(description_page,'html.parser')
    game_description=soup.find('div',{'jsname':'sngebd'}).get_text() #get_text()로 태그 사이에 있는 텍스트를 전부 가지고 온다.
    print(game_description)

browser.quit()