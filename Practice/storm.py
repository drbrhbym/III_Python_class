from urllib.request import urlopen
import ssl
from bs4 import BeautifulSoup
ssl._create_default_https_context = ssl._create_unverified_context
import warnings
warnings.filterwarnings('ignore')
import requests
import json
import jieba
import time
from jieba.analyse import extract_tags
jieba.load_userdict("dict.txt.big")
jieba.load_userdict("mydict.txt")


import logging
import logstash

def logban(fieldlog,error):

    logger = logging.getLogger(fieldlog)
    logger.setLevel(logging.INFO)
    host_demo = "10.120.14.204"
    logger.addHandler(logstash.TCPLogstashHandler(host_demo, 5000))
    logger.error(error)



def crab(class_):
    news_link = class_.find("a", class_="card_link")["href"]
    artical_number = news_link.split("/")[-1]
    id = "storm-politic-" + artical_number
    news_title = class_.find("h3", class_="card_title").text
    news_create_time = class_.find("span", class_="info_time").text

    response2 = urlopen(news_link)
    html2 = BeautifulSoup(response2)
    artical = html2.find("div", class_="article_content_inner")
    content = []
    for p in artical.find_all("p"):
        content.append(p.text)
    news_content = "".join(content)

    response3 = urlopen("https://service-pvapi.storm.mg/pvapi/get_pv/" + artical_number)
    html3 = BeautifulSoup(response3)
    #news_view = html3.text.split(":")[-1].replace("}", "")
    #print(news_view)
    news_tag = "politic"
    news_view = json.loads(html3.text)["total_count"]

    proxy = {"http": "140.227.199.211:60088"}
    try:
        fb_msg = requests.get('https://graph.facebook.com/?id={}'.format(news_link), proxies=proxy).json()['share']
        print("=============================")
        print(id), print(news_link), print(news_title), print(news_create_time),
        print(news_content), print("關鍵詞:", extract_tags(news_content, 10)),
        print(news_tag), print(news_view), print(fb_msg)
    except KeyError:
        logban("storm", "fxxk")



    #time.sleep(1.5)

page = 1
while True:
    url = "https://www.storm.mg/category/118/" + str(page)
    print("處理頁面:", url)

    response = urlopen(url)
    html = BeautifulSoup(response)

    for politic in html.find_all("div", class_="category_card"):
        crab(politic)

    page = page + 1
    if page == 70:
        break