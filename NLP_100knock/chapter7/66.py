"""
66. 検索件数の取得
MongoDBのインタラクティブシェルを用いて，
活動場所が「Japan」となっているアーティスト数を求めよ．
"""

import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.nlp
col = db.artist

print(col.find({'area': 'Japan'}).count())  # =>22821
