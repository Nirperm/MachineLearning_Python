import pymongo
from bottle import get, request
from bottle import run
from bottle import jinja2_template as template
from collections import OrderedDict


@get('/')
def form():
    return template('form_69')


@get('/search')
def search():
    name = request.query['name']
    aliases_name = request.query['aliases_name']
    tag = request.query['tag']

    if name is not '':
        query = OrderedDict([('name', name)])
    else:
        query = OrderedDict()

    if aliases_name is not '':
        query['aliases.name'] = aliases_name
    if tag is not '':
        query['tags'] = {'$elemMatch': {'value': tag}}

    client = pymongo.MongoClient('localhost', 27017)
    db = client.nlp
    col = db.artist

    result = []

    artists = col.find(query)
    for artist in artists:
        result.append(artist)
    result = sorted(filter(lambda r: 'rating' in r, result), key=lambda x: -x['rating']['count'])

    return template('result_69', result=result)


if __name__ == '__main__':
    run(host='0.0.0.0', port=3030, debug=True, reloader=False)
