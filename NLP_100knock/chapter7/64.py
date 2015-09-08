"""
64. MongoDBの構築
アーティスト情報（artist.json.gz）をデータベースに登録せよ．
さらに，次のフィールドでインデックスを作成せよ: name, aliases.name, tags.value, rating.value
"""

import gzip
import json
import pymongo
from pymongo import ASCENDING


def main():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.nlp
    col = db.artists

    for line in gzip.open('data/artist.json.gz', 'rt'):
        data = json.loads(line)
        col.insert({'artist_info': data})

    col.create_index([('name', ASCENDING)])
    col.create_index([('aliases.name', ASCENDING)])
    col.create_index([('tags.value', ASCENDING)])
    col.create_index([('rating.value', ASCENDING)])

if __name__ == '__main__':
    main()
