from selenium import webdriver
#같은 파일에 있으면 안될 수 있으므로 task 패키지를 만들어서 실행
driver_path = '../resources/chromedriver' # driver path 드라이브 경로
url = 'https://play.google.com/store/apps/top/category/GAME' #url 경로
browser = webdriver.Chrome(executable_path=driver_path) # Chrome driver
browser.get(url)
browser.quit() #브라우저 닫기