"""
68. ソート
"dance"というタグを付与されたアーティストの中で
レーティングの投票数が多いアーティスト・トップ10を求めよ．
"""

import pymongo


def main():
    conn = pymongo.MongoClient('localhost', 27017)
    db = conn.nlp
    col = db.artist

    data = col.find({'tags.value': 'dance'})

    if data:
        for i, doc in enumerate(sorted(filter(lambda d: 'rating' in d, data), key=lambda x: -x['rating']['count'])[:10]):
            print(i + 1)
            print(doc)
            print('\n')

if __name__ == '__main__':
    main()
