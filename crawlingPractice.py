# 패키지 설치할 때
# 경로 : cd C:\Users\김지혜\Desktop\sparta\pythonprac\venv\Scripts
# pip install (패키지 이름)

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작
# print(soup)
title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
print(title)

# 텍스트만 가져오고 싶어
# print(title.text)

# 태그의 속성을 가져오고 싶어
# print(title['href'])

# old_content > table > tbody > tr:nth-child(2)
# old_content > table > tbody > tr:nth-child(3)

# old_content > table > tbody > tr:nth-child(2) > td.title > div > a

trs = soup.select('#old_content > table > tbody > tr')
for tr in trs:
    # print(tr)
    a_tag = tr.select_one('td.title > div > a')
    # 왜 a_tag.text를 바로 프린트 하면 안되냐면 None이라는 무언가가 존재하기 때문!
    # 그렇기 때문에 none이 아니라는 전제 조건 하에 제목을 불러올 수 있어야 한다.
    if a_tag is not None:
       title = a_tag.text
       print(title)
