import requests
from bs4 import BeautifulSoup

url = "https://sports.news.naver.com/wbaseball/record/index?category=mlb&league=AL&year=2023"
response = requests.get(url)

# print(response.raise_for_status)
html = response.text

soup = BeautifulSoup(response.content, 'html.parser')

for tr_tag in soup.find(id='eastDivisionTeamRecordList_table').find_all('tr'):
    th_tag = tr_tag.find('td')
    strong_tag = th_tag.find('strong')
    lank = strong_tag.get_text()

    span_tag = tr_tag.findAll('span')
    team = span_tag[0].get_text()
    total = span_tag[1].get_text()
    win = span_tag[2].get_text()
    lose = span_tag[3].get_text()
    winper = span_tag[4].get_text()
    rate = span_tag[5].get_text()
    gab = span_tag[6].get_text()
    contin = span_tag[7].get_text()
    gobase = span_tag[8].get_text()
    longhit = span_tag[9].get_text()
    lately = span_tag[10].get_text()

    print("동부지구", lank, " ", team, " ",  total, "| 경기수 :", win, "| 승 :", lose, "| 패 :", winper, "| 승률 :", rate, "| 게임차 :", gab, "| 연속 :", contin, "| 출루율 :", gobase, "| 장타율 :", longhit, "| 최근10경기 :", lately)

for tr_tag in soup.find(id='centerDivisionTeamRecordList_table').find_all('tr'):
    th_tag = tr_tag.find('td')
    strong_tag = th_tag.find('strong')
    lank = strong_tag.get_text()

    span_tag = tr_tag.findAll('span')
    team = span_tag[0].get_text()
    total = span_tag[1].get_text()
    win = span_tag[2].get_text()
    lose = span_tag[3].get_text()
    winper = span_tag[4].get_text()
    rate = span_tag[5].get_text()
    gab = span_tag[6].get_text()
    contin = span_tag[7].get_text()
    gobase = span_tag[8].get_text()
    longhit = span_tag[9].get_text()
    lately = span_tag[10].get_text()
    print("중부지구", lank, " ", team, " ",  total, "| 경기수 :", win, "| 승 :", lose, "| 패 :", winper, "| 승률 :", rate, "| 게임차 :", gab, "| 연속 :", contin, "| 출루율 :", gobase, "| 장타율 :", longhit, "| 최근10경기 :", lately)

for tr_tag in soup.find(id='westDivisionTeamRecordList_table').find_all('tr'):
    th_tag = tr_tag.find('td')
    strong_tag = th_tag.find('strong')
    lank = strong_tag.get_text()

    span_tag = tr_tag.findAll('span')
    team = span_tag[0].get_text()
    total = span_tag[1].get_text()
    win = span_tag[2].get_text()
    lose = span_tag[3].get_text()
    winper = span_tag[4].get_text()
    rate = span_tag[5].get_text()
    gab = span_tag[6].get_text()
    contin = span_tag[7].get_text()
    gobase = span_tag[8].get_text()
    longhit = span_tag[9].get_text()
    lately = span_tag[10].get_text()
    print("서부지구", lank, " ", team, " ",  total, "| 경기수 :", win, "| 승 :", lose, "| 패 :", winper, "| 승률 :", rate, "| 게임차 :", gab, "| 연속 :", contin, "| 출루율 :", gobase, "| 장타율 :", longhit, "| 최근10경기 :", lately)

for tr_tag in soup.find(id='wildCardTeamRecordList_table').find_all('tr'):
    th_tag = tr_tag.find('td')
    strong_tag = th_tag.find('strong')
    lank = strong_tag.get_text()

    span_tag = tr_tag.findAll('span')
    team = span_tag[0].get_text()
    total = span_tag[1].get_text()
    win = span_tag[2].get_text()
    lose = span_tag[3].get_text()
    winper = span_tag[4].get_text()
    rate = span_tag[5].get_text()
    gab = span_tag[6].get_text()
    contin = span_tag[7].get_text()
    gobase = span_tag[8].get_text()
    longhit = span_tag[9].get_text()
    lately = span_tag[10].get_text()
    print("와일드카드", lank, " ", team, " ",  total, "| 경기수 :", win, "| 승 :", lose, "| 패 :", winper, "| 승률 :", rate, "| 게임차 :", gab, "| 연속 :", contin, "| 출루율 :", gobase, "| 장타율 :", longhit, "| 최근10경기 :", lately)
