import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

import json
from collections import OrderedDict

# Chrome 옵션 설정
options = ChromeOptions()
options.add_argument("window-size=1920x1080")
options.add_argument("disable-gpu")
options.add_argument("lang=ko_KR")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)



# 사이트 접속
driver.get('https://music.apple.com/kr/playlist/%EC%98%A4%EB%8A%98%EC%9D%98-top-100-%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD/pl.d3d10c32fbc540b38e266367dc8cb00c')


time.sleep(2) 

search_box = driver.find_element(By.CLASS_NAME, 'svelte-1qeqonk')

rankings = search_box.find_elements(By.CLASS_NAME , 'songs-list-row__rank')
titles = search_box.find_elements(By.CLASS_NAME , 'songs-list-row__song-name')
artist = search_box.find_elements(By.CLASS_NAME ,  'songs-list-row__by-line')

rankList = [rank.text for rank in rankings]
titleList = [title.text for title in titles]
artistList = [art.find_element(By.TAG_NAME , 'span').text for art in artist]


# 데이터 프레임 생성
chart_df = pd.DataFrame({
    "Ranking" : rankList,
    "Title" : titleList , 
    "Artist" : artistList
})


chart_df.to_json("applemusicMusicChart.json", force_ascii=False , orient="records")