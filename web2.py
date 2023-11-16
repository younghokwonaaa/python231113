#web2.py
#웹 서버와 통신
import requests

#크롤링
from bs4 import BeautifulSoup

url = "https://www.daangn.com/fleamarket/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
posts = soup.find_all("div", attrs={"class":"card-desc"})

# 파일 생성
f=open("dangn.txt", "wt", encoding="utf-8")

for post in posts:
    title = post.find("h2", attrs={"class":"card-title"})    
    price = post.find("div", attrs={"class":"card-price"})    
    addr = post.find("div", attrs={"class":"card-region-name"})
    title1 = title.text.replace("\n","")
    price1 = price.text.replace("\n","")
    addr1 = addr.text.replace("\n","")
    print("{0}, {1}, {2}".format(title1, price1, addr1))
    print("{0}, {1}, {2}".format(title.text.strip(), price.text.strip(), addr.text.strip()))
    f.write(f"{title1}, {price1}, {addr1}\n")
    #f.write(f"{title.text.strip()}, {price.text.strip()}, {addr.text.strip()}\n")
    
f.close()
# <div class="card-desc">
#       <h2 class="card-title">삼성텔레비전65인치</h2>
#       <div class="card-price ">
#         150,000원
#       </div>
#       <div class="card-region-name">
#         서울 서초구 반포2동
#       </div>