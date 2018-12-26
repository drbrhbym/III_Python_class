# 使用內建的 urllib.request 裡的 urlopen 這個功能來送出網址
from urllib.request import urlopen, urlretrieve
from urllib.error import HTTPError
import time
from bs4 import BeautifulSoup
# 如果是 MAC 電腦, 請務必加入下面兩行, 因為 MAC 有視 htpps 的 ssl 證書無效的 bug
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import os

import warnings
warnings.filterwarnings('ignore')

# 準備空的 DataFrame, 先固定住 columns
import pandas as pd
from StyleFrame import StyleFrame

# 準備一個 Series, index 的欄位要跟 columns 對到
df = pd.DataFrame(columns=["餐廳美圖", "綜合評分", "晚間評分", "年間評分", "日文店名", "英文店名", "介紹網址"])

import glob
import openpyxl
from openpyxl import load_workbook
from openpyxl.drawing import image

page = 59
while True:
    url = "https://tabelog.com/tw/osaka/rstLst/" + str(page) + "/?SrtT=rt"
    print("處理頁面:", url)
    try:
        response = urlopen(url)
    except HTTPError:
        print("Completed")
        break
    html = BeautifulSoup(response)
    for r in html.find_all("li", class_="list-rst"):  # => find_all 必轉出 list
        ja = r.find("small", class_="list-rst__name-ja")
        en = r.find("a", class_="list-rst__name-main")
        scores = r.find_all("b", class_="c-rating__val")
        img = r.find("img", class_="c-img")
        fname = "tablelog/" + img["src"].split("/")[-1]
        urlretrieve(img["src"], fname)

        '''
        dir = "tablelog/" + str(page) + "/"
        if not os.path.exists(dir):
            os.mkdir(dir)
        fname = dir + img["src"].split("/")[-1]
        urlretrieve(img["src"], fname)
        '''

        # 準備Series和append進DataFrame
        s = pd.Series([scores[0].text, scores[1].text, scores[2].text, ja.text, en.text, en["href"]],
                      index=["綜合評分", "晚間評分", "年間評分", "日文店名", "英文店名", "介紹網址"])
        # 因為 Series 沒有橫列的標籤, 所以加進去的時候一定要 ignore_index=True
        df = df.append(s, ignore_index=True)


    page = page + 1



sf = StyleFrame(df)
#sf.set_column_width(columns=sf.columns, width=20)
#sf.set_row_height(rows=sf.row_indexes, height=25)


#sf = StyleFrame(df)
sf.set_column_width_dict(col_width_dict={
    ("餐廳美圖"): 25.5,
    ("綜合評分", "晚間評分", "年間評分", "日文店名", "英文店名") : 20,
    ("介紹網址"): 65.5
 })

all_rows = sf.row_indexes
sf.set_row_height_dict(row_height_dict={
    all_rows[1:]: 120
})

#ew = StyleFrame.ExcelWriter('tablelog.xlsx')


sf.to_excel('tablelog.xlsx',
            sheet_name='Sheet1',
            right_to_left=False,
            columns_and_rows_to_freeze='A1',
            row_to_add_filters=0).save()
            #allow_protection=True
#ew.save()

# 儲存成 csv, 不過列編號的數字不用存, 所以index=False
#df.to_excel("tablelog.xlsx", encoding="utf-8", index=False)

col = 0
wb = load_workbook('tablelog.xlsx')
ws = wb.worksheets[0]
searchedfiles = sorted(glob.glob("tablelog/*.jpg"), key=os.path.getmtime)
for fn in searchedfiles :
    img = openpyxl.drawing.image.Image(fn)
    c = str(col + 2)
    ws.add_image(img, 'A' + c)
    col = col + 1
wb.save('tablelog.xlsx')






