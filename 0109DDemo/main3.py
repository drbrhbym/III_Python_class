from bs4 import BeautifulSoup
import requests

url = "https://www.ptt.cc/bbs/Gossiping/M.1547006368.A.A6F.html"
session = requests.session()
session.cookies["over18"] = "1"
print(session.cookies)
response = session.get(url)
#response = session.get(url, cookies={"over18":"1"})

html = BeautifulSoup(response.text)
content = html.find("div", id = "main-content")
#print(content)
s = content.find_all("span", class_="article-meta-value")
#print("ID", s[0].text)
#print("看板", s[1].text)

metas = content.find_all("div", class_="article-metaline")
for m in metas:
    m.extract()
metas = content.find_all("div", class_="article-metaline-right")
for m in metas:
    m.extract()

ps = content.find_all("div", class_="push")
pos = []
neg = []
score = 0
for p in ps:
    tag = p.find("span", class_="push-tag").text
    if "推" in tag:
        score = score + 1
        pc = p.find("span", class_="push-content").text.replace(":","", 1)
        pos.append(pc)
    elif "噓" in tag:
        score = score - 1
        pc = p.find("span", class_="push-content").text.replace(":","", 1)
        neg.append(pc)
    p.extract()
print("總分:", score)
print("內文:", content.text)
print("推文:", pos)
print("噓文:", neg)
from jieba.analyse import extract_tags
print("關鍵詞:", extract_tags(content.text, 10))
