from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

page = 1
while True:
    url = "https://tabelog.com/tw/osaka/rstLst/" + str(page) + "/?SrtT=rt"
    print("處理頁面:", url)
    try:
        response = urlopen(url)
    except HTTPError:
        print("Completed")
        break
    html = BeautifulSoup(response)
    #html.find_all("li", {"class":"list_rst"})
    for r in html.find_all("li", class_="list-rst"): #=> find_all 必轉出 list
        ja = r.find("small", class_="list-rst__name-ja")
        en = r.find("a", class_="list-rst__name-main")
        scores = r.find_all("b", class_="c-rating__val")
        print(scores[0].text, scores[1].text, scores[2].text, ja.text, en.text, en["href"])

    page = page + 1