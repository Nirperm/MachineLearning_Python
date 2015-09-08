import gzip
import json
from pymongo import ASCENDING
from pymongo import Connection


def main():
    conn = Connection('localhost', 27017)
    if ('nlp' in conn.database_names()):
        print('Already nlp exists, Now cleanup!!!')
        conn.drop_database('nlp')
        db = conn.nlp
        coll = db.artist

    f = gzip.open('data/artist.json.gz', 'rt')
    for line in f:
        dic = json.loads(line)
        coll.insert(dic)
    f.close()

    coll.create_index([('name', ASCENDING)])
    coll.create_index([('aliases.name', ASCENDING)])
    coll.create_index([('tags.value', ASCENDING)])
    coll.create_index([('rating.value', ASCENDING)])


if __name__ == '__main__':
    main()
