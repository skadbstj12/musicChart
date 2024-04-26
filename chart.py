import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd

res = req.get("https://music.bugs.co.kr/chart")


soup = bs(res.text, "lxml")

# 데이터 선택
ranking = soup.select(".ranking > strong")
title = soup.select(".title > a")
artist = soup.select(".artist > a:nth-child(1)")




# 데이터 저장
rankingList = [rank.text.strip() for rank in ranking]
titleList = [t.text.strip() for t in title]
artistList = [a.text.strip() for a in artist]

print(rankingList)

# 데이터 프레임 생성    
chart_df = pd.DataFrame({
    'Ranking' : rankingList,
    'Title': titleList,
    'Artist': artistList
})

# JSON 파일로 저장
chart_df.to_json("bugsChart100.json", force_ascii=False, orient="records")
