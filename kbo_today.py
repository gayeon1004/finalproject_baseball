import requests
from bs4 import BeautifulSoup

html = requests.get("https://sports.news.naver.com/kbaseball/index")
soup = BeautifulSoup(html.content, "html.parser")

todaymatch = soup.find_all("div", id="_tab_box_kbo")[0]
todaymatchItems = todaymatch.find("div", class_="hmb_list").find_all("li", class_="hmb_list_items")

for item in todaymatchItems : 
        lftItemBox = item.find(class_="vs_list vs_list1").find(class_="inner")
        lftScore = lftItemBox.find("div", class_="score").stripped_strings
        lftName = lftItemBox.find("span", class_="name").text
        lftPitcher = lftItemBox.find_all("span")[2].text

        rgtItemBox = item.find(class_="vs_list vs_list2").find(class_="inner")
        rgtScore = rgtItemBox.find("div", class_="score").stripped_strings
        rgtName = rgtItemBox.find("span", class_="name").text
        rgtPitcher = rgtItemBox.find_all("span")[2].text

        print ("(선발:"+lftPitcher+")\t"+ lftName + "\t"+("".join(lftScore)) + " vs " + ("".join(rgtScore))+"\t"+rgtName+""+"\t(선발:"+rgtPitcher+")" )