import jieba
from jieba.analyse import extract_tags
import glob

for fn in glob.glob("input/*.txt"):
    print("現在處理檔案:", fn)
    with open(fn, "r", encoding="utf-8") as f:
       article = f.read()

    jieba.load_userdict("dict.txt.big")
    jieba.load_userdict("mydict.txt")
    print("關鍵詞:", extract_tags(article, 10))