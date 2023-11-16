#web1.py
#웹 크롤링을 위한 선언
from bs4 import BeautifulSoup

#페이지 로딩(메서드 체인)
page = open("test01.html","rt", encoding="utf-8").read()
#print(page)
#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")

#전체 페이지 보기
#print(soup.prettify())
#<p>전체를 검색
#print(soup.find_all("p"))

#첫번째 <p>만 검색
#print(soup.find("p"))

#조건검색 : <p class="outer-text">
#class 키워드와 충돌
#print(soup.find_all("p", class_="outer-text"))
#attrs 속성을 많이 사용한다.
#print(soup.find_all("p", attrs={"class":"outer-text"}))
#<p id="first">
#print(soup.find_all("P", id="first"))
#태그 안쪽의 컨텐츠만 출력 : .text속성
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n", "")
    print(title)

