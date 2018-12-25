with open("d.txt", "r", encoding="utf-8") as f:
 article = f.read()

import jieba
jieba.load_userdict("dict.txt.big")
jieba.load_userdict("mydict.txt")
print(" ".join(jieba.cut(article)))

#import jieba.analyse
#print(jieba.analyse.extract_tags(article, 10))
#from jieba import analyse
#print(analyse.extract_tags(article, 10))
from jieba.analyse import extract_tags
print(extract_tags(article, 10))