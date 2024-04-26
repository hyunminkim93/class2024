# 파이썬 설치     

````
    확장프로그램 python 설치   
````

설치된 목록보기   
````
    pip3 list   
````

파이선 결과보기
````
    print()   
````

## requests     
````
    pip3 install requests   
    이 명령어는 Requests 라이브러리를 설치합니다. Requests는 파이썬에서 HTTP 요청을 보내고 API와 작업하는 데 사용되는 인기 있는 HTTP 라이브러리입니다. HTTP 요청을 쉽게 보낼 수 있습니다.   

    pip3 install beautifulsoup4      
    이 명령어는 Beautiful Soup 라이브러리를 설치합니다. Beautiful Soup은 파이썬에서 웹 스크래핑에 사용됩니다. HTML 및 XML 문서를 구문 분석하고 구문 분석 트리를 탐색하며 데이터를 추출하는 도구를 제공합니다.   

    pip3 install lxml   
    이 명령어는 lxml 라이브러리를 설치합니다. lxml은 XML 및 HTML 문서를 처리하는 강력하고 효율적인 라이브러리입니다. XML 및 HTML 데이터를 처리하는 빠르고 유연한 방법을 제공합니다.   

    pip3 install pandas   
    이 명령어는 Pandas 라이브러리를 설치합니다. Pandas는 파이썬의 강력한 데이터 조작 및 분석 라이브러리입니다. 데이터 프레임, 시리즈 및 테이블과 같은 구조화된 데이터를 처리하고 작업하는 데 사용되는 데이터 구조 및 함수를 제공합니다.   

    pip3 install selenium   
    이 명령어는 Selenium 라이브러리를 설치합니다. Selenium은 웹 브라우저를 자동화하는 도구입니다. 웹 브라우저를 프로그래밍 방식으로 제어하고 버튼을 클릭하거나 양식을 작성하거나 웹 페이지를 탐색하는 등 사용자 상호 작용을 시뮬레이션할 수 있습니다.     
````

## python 파일 들어가기   
````
    cd python   
    홈페이지 데이터 가져오기 : python3 들어갈 주소.py     
    현재상태 확인방법 print(res.status_code)      
    안들어가지는 사이트 들어갈때 : head = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}   
    res = req.get("https://www.melon.com/chart/index.htm", headers=head)     
    가져온 데이터 보기 편하게 : from bs4 import BeautifulSoup as bs    
                          soup = bs(res.text, "lxml")   
                          print(soup)    
````

## 데이터 선택   
ranking = soup.select(".ranking > strong")   
title = soup.select(".title > a")   
artist = soup.select(".artist > a:nth-child(1)")   

print(len(ranking))   
print(len(title))   
print(len(artist))

## 데이터 저장   
rankingList = []   
titleList = []   
artistList = []   

for i in range(len(ranking)) :   
     rankingList.append(ranking[i].text)   
     titleList.append(title[i].text)   
     artistList.append(artist[i].text)

     rankingList = [ranking.text.strip() for rank in ranking]  위에거를 한번에 쓴거 strip은 여백없애는것.   

## 데이터 프레임 생성
chart_df = pd.DataFrame({   
    'Ranking' : rankingList,   
    'Title' : titleList,   
    'Artist' : artistList
})

## 저장된 데이터를 객체 형식으로 정리 
data = {"rank" : rankingList, "title" : titleList, "artist" : artistList }   
print(pd.DataFrame(data))

## json 파일로 만들기   
chart_df.to_json("bugsChart100.json", force_ascii=False, orient="records")   
