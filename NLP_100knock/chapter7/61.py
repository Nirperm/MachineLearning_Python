"""
61. KVSの検索
60で構築したデータベースを用い，特定の（指定された）アーティストの活動場所を取得せよ．
"""

import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

for i in range(0, r.dbsize()):
    if None not in r.hmget(i, 'area'):
        print(r.hmget(i, 'area'))
