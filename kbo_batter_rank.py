import requests
from bs4 import BeautifulSoup

import json

url = "https://sports.news.naver.com/kbaseball/record/ajaxHtmlPlayerRecord.nhn?category=kbo&year=2023&type=batter&playerOrder=hra"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
# print(response.status_code)

dict_example = json.loads(soup.text)
# print(type(dict_example))
for i in dict_example:

    print(i['rank'], i['name'], '(',i['team'],')', ' | ', '타율 :', i['hra'], ' | ', '홈런 :', i['hr'], ' | ', '타점 :', i['rbi'], ' | ', '도루 :', i['sb'], ' | ', 'OPS :', i['ops'], ' | ', 'WAR :', i['war'])