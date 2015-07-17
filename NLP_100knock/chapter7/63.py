"""
63. オブジェクトを値に格納したKVS
KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）のリストを
検索するためのデータベースを構築せよ．
さらに，ここで構築したデータベースを用い，アーティスト名からタグと被タグ数を検索せよ．
"""
import gzip
import json
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=1)
pipe = r.pipeline()

f = gzip.open('data/artist.json.gz', 'rt')
pipe.flushall()  # initialization
for line in f:
    data = json.loads(line)
    if 'tags' in data:
        pipe.hset(data['name'], 'name', data['tags'])
pipe.execute()

for name in r.keys():
    print(r.hvals(name))
