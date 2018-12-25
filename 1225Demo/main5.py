from urllib.request import urlopen , urlretrieve
import json
import os
#MAC電腦
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


for m in range(12):
    print("正在處理:", m + 1, "月")
    url = "https://www.google.com/doodles/json/2018/" + str(m+1) + "?hl=zh_TW"
    response = urlopen(url)
    doodles = json.load(response) #轉成json格式
    #doodles -> list d -> dict
    for d in doodles:
        url = "https:" + d["url"]
        print(d["title"], url)
        dir = "doodles/" + str(m + 1) + "/"
        if not os.path.exists(dir):
            os.mkdir(dir)
        fname = dir + url.split("/")[-1]
        urlretrieve(url, fname)
