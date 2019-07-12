from selenium import webdriver
from bs4 import BeautifulSoup

driver_path = '../resources/chromedriver' # driver path
url = 'https://play.google.com/store/apps/top/category/GAME'

browser = webdriver.Chrome(executable_path=driver_path) # Chrome driver 크롬 드라이버의 실행
browser.get(url) #url 경로를 연결 시켜준다 (브라우저 실행)
page = browser.page_source # 경로에 있는 페이지 소스를 가져온다
browser.quit() # 브라우저 빠져나가기

soup = BeautifulSoup(page, "html.parser") #beautifulsoup로 html 소스를 긁어온다
print(soup.prettify()) #html 출력