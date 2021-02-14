import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

# 코딩 시작

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    a_tag = movie.select_one('td.title>div>a')
    if a_tag is not None:
        rank = movie.select_one('td:nth-child(1)>img')['alt']
        title = a_tag.text
        star = movie.select_one('td.point').text
        doc = {
            'rank':rank,
            'title':title,
            'star':star
        }
        db.movies.insert_one(doc)
# 1번퀴즈
a1 = db.movies.find_one({'title': '매트릭스'})
print(a1['star'])

# 2번퀴즈
a2 = list(db.movies.find({'star':a1['star']},{'_id':False}))
for mv in a2:
    print(mv['title'])


# 3번퀴즈
db.movies.update_one({'title':'매트릭스'},{'$set':{'star':0}})


