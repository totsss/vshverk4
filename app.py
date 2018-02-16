import json
from bottle import *

skra=open('bekkur.json','r',encoding='UTF-8')
l = json.load(skra)
print(skra)
@route('/')
def index():
    return template('tskra1.tpl', nem=l)

@route('/nemandi/<kt>')
def index(kt):
    for nemandi in l['nemendur']:
        if nemandi['kt']==kt:
            return template('nemandi.tpl',nemandi=nemandi)

#run(host='localhost', port=8080, debug=True)
run(host='0.0.0.0',port=os.environ.get('PORT'))
