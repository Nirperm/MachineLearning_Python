"""
62. KVS内の反復処理
60で構築したデータベースを用い，活動場所が「Japan」となっているアーティスト数を求めよ．
"""

import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
area_counter = 0
for i in range(0, r.dbsize()):
    if None not in r.hmget(i, 'area') and r.hmget(i, 'area')[0].decode('utf-8') == 'Japan':
        area_counter += 1

print(area_counter)
