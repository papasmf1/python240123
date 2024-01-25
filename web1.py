# web1.py 
#웹 크롤링 
from bs4 import BeautifulSoup

#페이지를 로딩(메서드나 함수를 연속으로 호출:메서드 체인) 
#네이버, 클리아(한페이지 2000줄)
page = open(r"c:\work\test01.html", "rt", encoding="utf-8").read() 

#검색이 용이한 객체 
soup = BeautifulSoup(page, "html.parser")

#전체 문서 보기 
#print(soup.prettify())
#<p> 전체를 검색 
# print(soup.find_all("p"))
#<p> 하나만 검색 
#print(soup.find("p"))
#<p class='outer-text'> 조건 
#print(soup.find_all("p", class_ ="outer-text"))
#최근 스타일: attrs 속성(Attributes)
#print(soup.find_all("p", attrs={"class":"outer-text"}))

#태그 안쪽에 컨텐츠만 가져오기: .text 
for tag in soup.find_all("p"):
    title = tag.text.strip() 
    print(title)

    
      


