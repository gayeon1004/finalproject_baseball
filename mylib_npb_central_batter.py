import requests
from bs4 import BeautifulSoup

def npb_central_batter():
    m_list = []
    import json

    url = "https://sports.news.naver.com/wbaseball/record/ajaxPlayerRecord"
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    # 데이터 전달
    data = {'uCategory':'wbaseball','category':'npb', 'league':'CL', 'year':'2023','pFlag':'batter','order':'AVG'}

    # post로 데이터 요청
    response = requests.post(url, data=data, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    # print(response.status_code)

    dict_example = json.loads(soup.text)
    # print(type(dict_example))
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        rank = 1
        for i in dict_example:
            m_list.append((i['teamName'], i['playerName'], i['AVG'], i['HR'], i['RBI'], i['SB'], i['H'], i['OPS']))

    else:
            print(f"HTTP 요청 실패 코드: {response.status_code}")
    
    return m_list # 리스트 반환/