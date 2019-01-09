import requests
import json
import pandas as pd

df = pd.DataFrame(columns=["網址", "標題"])

for p in range(50):
    url = "https://crazy.ck101.com/category/more"
    post_data = {"id":1, "page":(p + 1)}
    print("第幾頁:", p + 1)
    response = requests.post(url, data=post_data)
    news = json.loads(response.text)
    for n in news:
        url = "https://crazy.ck101.com/post/" + str(n["id"])
        print(url, n["title"].strip(' '))
        s = pd.Series([url, n["title"].strip(' ')], index=["網址", "標題"])
        df = df.append(s, ignore_index=True)
df.to_csv("crazy.csv", encoding="utf-8", index=False)