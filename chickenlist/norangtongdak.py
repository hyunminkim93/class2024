import requests as req
from bs4 import BeautifulSoup as bs
import json
def get_menu_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
    res = req.get(url, headers=headers)
    res.encoding = 'UTF-8'
    soup = bs(res.text.encode('utf-8').decode('utf-8'), "lxml")
    menu = soup.select("span.lPzHi")
    sub = soup.select("div.kPogF")
    price = soup.select("div.GXS1X")
    chart_data = []
    for m, s, p in zip(menu, sub, price):
        chart_data.append({
            'Menu': m.text.strip(),
            'Sub': s.text.strip(),
            "Price": p.text.strip(),
        })
    return chart_data
# URL 정의
url = "https://m.place.naver.com/restaurant/37073264/menu/list"
chart_data = get_menu_data(url)
# 데이터를 JSON 파일로 저장
with open("norangtongdak.json", "w", encoding='UTF-8') as json_file:
    json.dump(chart_data, json_file, ensure_ascii=False, indent=4)
