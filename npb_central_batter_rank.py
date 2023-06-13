import requests
from bs4 import BeautifulSoup

import json

url = "https://sports.news.naver.com/wbaseball/record/ajaxPlayerRecord"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# 데이터 전달
data = {'uCategory':'wbaseball','category':'npb', 'league':'CL', 'year':'2023','pFlag':'batter','order':'AVG'}

# post로 데이터 요청
response = requests.post(url, data=data, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
# print(response.status_code)
# print(soup.select('#_pitcherRecord'))
# print(soup.text)
dict_example = json.loads(soup.text)
# print(type(dict_example))
for i in dict_example:
    print(i['rank'], i['playerName'], '(',i['teamName'],')', ' | ', '타율 :', i['AVG'], ' | ', '홈런 :', i['HR'], ' | ', '타점 :', i['RBI'], ' | ', '도루 :', i['SB'], ' | ', '안타 :', i['H'], ' | ', 'OPS :', i['OPS'])