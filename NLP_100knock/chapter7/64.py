"""
64. MongoDBの構築
アーティスト情報（artist.json.gz）をデータベースに登録せよ．
さらに，次のフィールドでインデックスを作成せよ: name, aliases.name, tags.value, rating.value
"""

import gzip
import json
import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.artist
col = db.artists

f = gzip.open('data/artist.json.gz', 'rt')
for line in f:
    data = json.loads(line)
    if 'aliases' in data:
        for i in range(len(data['aliases'])):
            data['aliases'][i]['name']
    if 'tags' in data:
        for i in range(len(data['tags'])):
            data['tags'][i]['value']
    if 'rating' in data:
        data['rating']['value']

    col.insert({'name': data['name'], 'aliases.name': '', 'tags.value': '', 'rating.value': '')
