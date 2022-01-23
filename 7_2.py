#pip 패키지 설치
"https://pip.pypa.io/en/stable/user_guide/"

#BeautifulSoap모듈
"https://www.crummy.com/software/BeautifulSoup/bs4/doc/"

from bs4 import BeautifulSoup

from urllib import request

target = request.urlopen("https://www.naver.com/")
soup = BeautifulSoup(target, "html.parser")
for tag in soup.select("head"):
    print(tag.select_one("style"))

print()

