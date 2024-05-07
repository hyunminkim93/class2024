import requests as req
from bs4 import BeautifulSoup as bs
import json
import os

def get_menu_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
    res = req.get(url, headers=headers)
    res.encoding = 'UTF-8'
    soup = bs(res.text, "lxml")
    
    menu = soup.select("div.tit")
    sub = soup.select("div.detail")
    price = soup.select("div.price")
    menuimage = soup.select("span.img_box")

    chart_data = []
    for m, s, p, mi in zip(menu, sub, price, menuimage):
        # 이미지가 있는지 확인
        img_tag = mi.select_one("img")
        img_url = img_tag['src'] if img_tag else None

        chart_data.append({
            'Menu': m.text.strip(),
            'Sub': s.text.strip(),
            'Price': p.text.strip(),
            'MenuImage': img_url
        })
    return chart_data

# URL 정의
url = "https://m.booking.naver.com/order/bizes/827880/items/4824526?theme=place&refererCode=menutab&area=pll"
chart_data = get_menu_data(url)

# JSON 파일이 이미 존재하는지 확인
if os.path.exists("limschicken.json"):
    # 파일이 존재하는 경우에는 기존 파일을 열어서 내용을 읽음
    with open("limschicken.json", "r", encoding='UTF-8') as json_file:
        existing_data = json.load(json_file)
        # 기존 데이터에 새로운 데이터를 추가
        existing_data.extend(chart_data)
else:
    # 파일이 존재하지 않는 경우에는 새로운 파일을 생성하여 데이터를 저장
    existing_data = chart_data

# 데이터를 JSON 파일로 저장
with open("limschicken.json", "w", encoding='UTF-8') as json_file:
    json.dump(existing_data, json_file, ensure_ascii=False, indent=4)