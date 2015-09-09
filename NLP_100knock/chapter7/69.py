import pymongo
from bottle import run, template
from bottle import get, post, request


@get('/')
def form():
    return template('form_69')


@get('/do_process')
def do_process():
    _name = request.query['name']
    _aliases_name = request.query['aliases_name']
    _tag = request.query['tag']

    # TODO: show result next action & page
    return _name, _aliases_name, _tag

"""
def result():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.nlp
    col = db.artist
    artist_name = request.query.artist_name
    # artist_another_name = request.query['aliases']['name']
    # tag = request.query['tag']
    ans = list()
    for i in col.find({'name': artist_name}):
        if 'area' not in i.keys():
            i['area'] = 'NoWhere'
        ans.append({"name": i['name'], 'area': i['area']})
"""

if __name__ == '__main__':
    run(host='0.0.0.0', port=3030, debug=True, reloader=False)
