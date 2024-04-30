
import requests as req
from bs4 import BeautifulSoup as bs
import json
res = req.get("https://www.billboard.com/charts/hot-100/")
soup = bs(res.text, "lxml")
# 데이터 선택
ranking_elements = soup.select(r".u-letter-spacing-0080\@tablet")
title_elements = soup.select(".o-chart-results-list-row-container .lrv-u-width-100p  #title-of-a-story ")
artist_elements = soup.select(".a-truncate-ellipsis-2line")
image_elements = soup.select(".o-chart-results-list__item > .c-lazy-image > .lrv-a-crop-1x1 > img.c-lazy-image__img")
# 데이터 추출 및 저장
chart_data = []
for rank, title, artist, image in zip(ranking_elements, title_elements, artist_elements, image_elements):
    chart_data.append({
        'Ranking': rank.text.strip(),
        'Title': title.text.strip(),
        'Artist': artist.text.strip(),
        'Image': image['data-lazy-src'].strip() if 'data-lazy-src' in image.attrs else image['src'].strip()
    })
# JSON 파일로 저장
with open("billboard100.json", "w", encoding='utf-8') as json_file:
    json.dump(chart_data, json_file, ensure_ascii=False, indent=4)