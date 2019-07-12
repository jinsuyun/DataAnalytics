from selenium import webdriver
from bs4 import BeautifulSoup
driver_path = '../resources/chromedriver' # driver path
url = 'https://play.google.com/store/apps/top/category/GAME'
browser = webdriver.Chrome(executable_path=driver_path) # Chrome driver
browser.get(url)
page = browser.page_source
soup = BeautifulSoup(page, "html.parser")
links = soup.find_all('div', {'class': 'W9yFB'}) # find all links to rankings class : W9yFB는 '더보기' 값을 가져온 것
for link in links:
    new_url = link.a['href']
    browser.get(new_url)
    print(new_url)
browser.quit()