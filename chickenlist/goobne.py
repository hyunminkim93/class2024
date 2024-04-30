import requests as req
from bs4 import BeautifulSoup as bs
import json

def get_menu_data(url, base_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
    res = req.get(url, headers=headers)
    soup = bs(res.text, "lxml")
    menu = soup.select("dt.title")
    menuimage = soup.select("div.img.sale_img > img")
    price = soup.select(".dis-price > .l-num")
    chart_data = []
    for menu, menuimage, price in zip(menu, menuimage, price):
        menuimage = menuimage['src'].strip()
        if menuimage.startswith('/'):
            menuimage = base_url + menuimage
        chart_data.append({
            'Menu': menu.text.strip(),
            'menuimage': menuimage,
            "price": price.text.strip(),
        })
    return chart_data

tab_urls = [
    "https://www.goobne.co.kr/menu/menu_list?class_id=10",
    "https://www.goobne.co.kr/menu/menu_list?class_id=11&item_id=",
    "https://www.goobne.co.kr/menu/menu_list?class_id=12&item_id=",
]
base_url = "https://www.goobne.co.kr/index"
all_tabs_data = []

for tab_url in tab_urls:
    chart_data = get_menu_data(tab_url, base_url)
    all_tabs_data.extend(chart_data)

# 데이터를 JSON 파일로 저장
with open("goobne.json", "w", encoding='utf-8') as json_file:
    json.dump(all_tabs_data, json_file, ensure_ascii=False, indent=4)