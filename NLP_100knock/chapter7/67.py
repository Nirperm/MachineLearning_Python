"""
67. 複数のドキュメントの取得
特定の（指定した）別名を持つアーティストを検索せよ．
"""

import pymongo
import sys


def main():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.nlp
    col = db.artist

    data = col.find({'aliases.name': sys.argv[1]})
    if data:
        for doc in data:
            print(doc)
    else:
        print('Not Found')

if __name__ == '__main__':
    main()
