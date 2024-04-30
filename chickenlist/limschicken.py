import requests as req
from bs4 import BeautifulSoup as bs
import json
def get_menu_data(url, base_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
    res = req.get(url, headers=headers)
    soup = bs(res.text, "lxml")
    menu = soup.select("a.gowun")
    sub = soup.select(".gall_tit > p")
    menuimage = soup.select("img.trans")
    chart_data = []
    for menu, sub, menuimage in zip(menu, sub, menuimage):
        menuimage = menuimage['src'].strip()
        if menuimage.startswith('/'):
            menuimage = base_url + menuimage
        chart_data.append({
            'Menu': menu.text.strip(),
            'Sub': sub.text.strip(),
            'menuimage': menuimage
        })
    return chart_data
tab_urls = [
    "https://www.limschicken.co.kr/menu/main",
    "https://www.limschicken.co.kr/menu/sub",
]
base_url = "https://www.limschicken.co.kr/"
all_tabs_data = []
for tab_url in tab_urls:
    chart_data = get_menu_data(tab_url, base_url)
    all_tabs_data.extend(chart_data)
# 데이터 추출 및 저장
all_tabs_data.extend(chart_data)
# JSON 파일로 저장

with open("limschicken.json", "r", encoding='utf-8') as json_file:
    loadedData = json.load(json_file)

# '\r\n' 제거 후 다시 JSON 파일로 저장
cleaned_data = []
for item in loadedData:
    cleaned_item = {
        "Menu": item["Menu"],
        "Sub": item["Sub"].replace("\r\n", ""),
        "menuimage": item["menuimage"]
    }
    cleaned_data.append(cleaned_item)

# 수정된 JSON 파일로 저장
with open("limschicken_cleaned.json", "w", encoding='utf-8') as json_file:
    json.dump(cleaned_data, json_file, ensure_ascii=False, indent=4)