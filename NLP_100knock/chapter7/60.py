"""
60. KVSの構築
Key-Value-Store (KVS) を用い，
アーティスト名（name）から活動場所（area）を検索するためのデータベースを構築せよ．
"""

import gzip
import json
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
pipe = r.pipeline()

f = gzip.open('data/artist.json.gz', 'rt')
pipe.flushall()  # initialization
for i, line in enumerate(f):
    data = json.loads(line)
    pipe.hmset(i, data)
pipe.execute()
