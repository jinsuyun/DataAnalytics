from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify()) #보기 편하게 변환

print("a 태그")
tag = soup.a #a태그
print(tag)

print("태그 이름")
print(tag.name)

print("태그 Attribute")
print(tag.attrs)

print("태그 사이에 존재하는 텍스트")
print(tag.string)

print("태그에서 class라는 key값을 가져옴")
print(tag['class'])

print("타이틀 전체")
print(soup.title)

print("타이틀 태그 이름")
print(soup.title.name)

print("타이틀 태그 사이의 텍스트")
print(soup.title.string)


print(soup.title.parent.name) # parent 부모이름
print(soup.title.parent.title.string) # 타이틀 태그 사이의 텍스트
print(soup.head.contents[0].string) # contents :children as a list

print("p 태그")
print(soup.p)
print("p 태그에서 키가 class 값")
print(soup.p['class'])
print("a 태그")
print(soup.a)
print("a 태그 전체")
print(soup.find_all('a'))
print("id가 link3인 것")
print(soup.find(id='link3'))
print("id가 link3인 것의 태그 사이의 텍스트")
print(soup.find(id='link3').string)


for link in soup.find_all('a'): #a태그의 모든 것을 가져오겠다
    print(link.get('href')) #link의 attribute에서 키가 href인 것
    print(link['href']) #위의 동일한 값을 표할수 있다

print("\n태그사이의 모든 텍스트")
print(soup.get_text())