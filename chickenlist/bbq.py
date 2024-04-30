import requests as req
from bs4 import BeautifulSoup as bs
import json
def get_menu_data(url, base_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
    res = req.get(url, headers=headers)
    soup = bs(res.text, "lxml")
    menu = soup.select("")
    sub = soup.select("")
    menuimage = soup.select("")
    price = soup.select("")
    chart_data = []
    for menu, sub, menuimage in zip(menu, sub, menuimage, price):
        menuimage_url = menuimage['src'].strip()
        if menuimage_url.startswith('http'):
            menuimage_url = base_url + menuimage_url
            menuimage_url = menuimage_url.replace("http://", "https://")
        chart_data.append({
            'Menu': menu.text.strip(),
            'Sub': sub.text.strip(),
            'menuimage': menuimage_url,
            'price': price()
        })
    return chart_data
tab_urls = [
    "https://bbq.co.kr/categories/1",
    "https://bbq.co.kr/categories/14",
    "https://bbq.co.kr/categories/2",
    "https://bbq.co.kr/categories/3",
    "https://bbq.co.kr/categories/4",
    "https://bbq.co.kr/categories/5",
    "https://bbq.co.kr/categories/6",
    "https://bbq.co.kr/categories/7",
    "https://bbq.co.kr/categories/8",
    "https://bbq.co.kr/categories/9",
    "https://bbq.co.kr/categories/10",
]
base_url = "https://bbq.co.kr/"
all_tabs_data = []
for tab_url in tab_urls:
    chart_data = get_menu_data(tab_url, base_url)
    all_tabs_data.extend(chart_data)

# 데이터를 JSON 파일로 저장
with open("60chicken.json", "w", encoding='utf-8') as json_file:
    json.dump(all_tabs_data, json_file, ensure_ascii=False, indent=4)

# '\r\n' 제거 후 다시 JSON 파일로 저장
cleaned_data = []
for item in all_tabs_data:
    cleaned_item = {
        "Menu": item["Menu"],
        "Sub": item["Sub"].replace("\r\n", ""),
        "menuimage": item["menuimage"]
    }
    cleaned_data.append(cleaned_item)

# 수정된 JSON 파일로 저장
with open("60chicken.json", "w", encoding='utf-8') as json_file:
    json.dump(cleaned_data, json_file, ensure_ascii=False, indent=4)
