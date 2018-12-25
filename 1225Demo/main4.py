from urllib.request import urlopen , urlretrieve
import json
#MAC電腦
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.google.com/doodles/json/2018/12?hl=zh_TW"
response = urlopen(url)
doodles = json.load(response) #轉成json格式
#doodles -> list d -> dict
for d in doodles:
    url = "https:" + d["url"]
    print(d["title"], url)
    #print(url.split("/")[-1])
    fname = "doodles/"+ url.split("/")[-1]

    #response = urlopen(url)
    #img = response.read()

    #f = open(fname, "wb")
    #f.write(img)
    #f.close()

    urlretrieve(url, fname) #代替上面五行

