"""
65. MongoDBの検索
MongoDBのインタラクティブシェルを用いて，
"Queen"というアーティストに関する情報を取得せよ．
さらに，これと同様の処理を行うプログラムを実装せよ．
"""

import pymongo


def main():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.nlp
    col = db.artist

    for data in col.find({'name': 'Queen'}):
        print(data)


if __name__ == '__main__':
    main()
