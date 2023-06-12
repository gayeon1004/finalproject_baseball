import requests
from bs4 import BeautifulSoup

html = requests.get("https://sports.news.naver.com/wbaseball/index")
soup = BeautifulSoup(html.content, "html.parser")

todaymatch = soup.find_all("div", id="_tab_box_mlb")[0]
todaymatchItems = todaymatch.find("div", class_="hmb_list").find_all("li", class_="hmb_list_items")

lftScore = ""
rgtScore = ""
for item in todaymatchItems : 
        lftItemBox = item.find(class_="vs_list vs_list1").find(class_="inner")
        
        if lftItemBox.find("div", calss_="score win") !=None:
                lftScore = lftItemBox.find("div", class_="score win").stripped_strings
        if lftItemBox.find("div", class_="score") !=None:
                lftScore = lftItemBox.find("div", class_="score").stripped_strings
                                   
        lftName = lftItemBox.find("span", class_="name").text
        lftPitcher = lftItemBox.find_all("span")[-1].text

        rgtItemBox = item.find(class_="vs_list vs_list2").find(class_="inner")

        if rgtItemBox.find("div", calss_="score win") !=None:
                rgtScore = rgtItemBox.find("div", class_="score win").stripped_strings
        if rgtItemBox.find("div", class_="score") !=None:
                rgtScore = rgtItemBox.find("div", class_="score").stripped_strings
                                   
        rgtName = rgtItemBox.find("span", class_="name").text
        rgtPitcher = rgtItemBox.find_all("span")[-1].text

        print ("(선발:"+lftPitcher+")\t"+ lftName + "\t"+("".join(lftScore)) + " vs " + ("".join(rgtScore))+"\t"+rgtName+""+"\t(선발:"+rgtPitcher+")")