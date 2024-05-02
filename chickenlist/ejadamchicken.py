import requests as req
from bs4 import BeautifulSoup as bs
import json

def get_menu_data(url, base_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
    res = req.get(url, headers=headers)
    res.encoding = 'utf-8'
    soup = bs(res.text, "lxml")
    menu = soup.select("span.lPzHi")
    sub = soup.select("div.kPogF")
    menuimage = soup.select("div.place_thumb > .K0PDV")
    price = soup.select("div.GXS1X")
    chart_data = []
    for menu, sub, menuimage, price in zip(menu, sub, menuimage, price):
        menuimage_src = menuimage.find("img").get("src").strip() if menuimage.find("img") else ''
        if menuimage_src.startswith('/'):
            menuimage_src = base_url + menuimage_src
        chart_data.append({
            'Menu': menu.text.strip(),
            'Sub': sub.text.strip(),
            'menuimage': menuimage_src,
            "price": price.text.strip(),
        })
    return chart_data

base_url = "https://m.place.naver.com/restaurant/1340564962/menu/list"
all_tabs_data = []
for tab_url in base_url:
    chart_data = get_menu_data(base_url, base_url)
    all_tabs_data.extend(chart_data)

# 데이터를 JSON 파일로 저장
with open("ejadamchicken.json", "w", encoding='utf-8') as json_file:
    json.dump(all_tabs_data, json_file, ensure_ascii=False, indent=4)

# '\r\n' 제거 후 다시 JSON 파일로 저장
cleaned_data = []
for item in all_tabs_data:
    cleaned_item = {
        "Menu": item["Menu"],
        "Sub": item["Sub"].replace("\r\n", ""),
        "menuimage": item["menuimage"],
        "price": item["price"]
    }
    cleaned_data.append(cleaned_item)

# 수정된 JSON 파일로 저장
with open("ejadamchicken.json", "w", encoding='utf-8') as json_file:
    json.dump(cleaned_data, json_file, ensure_ascii=False, indent=4)