import requests as req
from bs4 import BeautifulSoup as bs
import json

def get_menu_data(url, base_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    res = req.get(url, headers=headers)
    soup = bs(res.text, "lxml")

    sub = soup.select("td.sub_price")
    menuimage = soup.select("img")
    price = soup.select(".main_price > b")

    chart_data = []
    for s, img, p in zip(sub, menuimage, price):
        menuimage_url = img['src'].strip()
        if menuimage_url.startswith('http'):
            menuimage_url = menuimage_url.replace("http://", "https://")
        else:
            menuimage_url = base_url + menuimage_url
        chart_data.append({
            'sub': s.text.strip(),
            'menuimage': menuimage_url,
            'price': p.text.strip()
        })
    return chart_data

base_url = "http://www.gcova.co.kr/"
all_tabs_data = []
chart_data = get_menu_data(base_url, base_url)
all_tabs_data.extend(chart_data)

# 데이터를 JSON 파일로 저장
with open("gcova.json", "w", encoding='utf-8') as json_file:
    json.dump(all_tabs_data, json_file, ensure_ascii=False, indent=4)

try:
    with open("gcova.json", "r", encoding='utf-8') as json_file:
        all_tabs_data = json.load(json_file)
    print("JSON 파일 불러오기 성공!")
except FileNotFoundError:
    print("JSON 파일을 찾을 수 없습니다.")
except Exception as e:
    print("JSON 파일을 불러오는 도중 오류가 발생했습니다:", e)