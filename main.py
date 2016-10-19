import queries
import cherrypy
from bottle import route, run, response


@route('/hello')
def hello():
    return "Hello World!"

@route('/')
def mainPage():
    response.set_header('Access-Control-Allow-Origin', '*')
    donuts = queries.getAll('donuts')
    return {'cats':['Austin', 'Tommy', 'Wes', 'Robby'], 'donuts': donuts};

@route('/<id>')
def oneThing(id):
    response.set_header('Access-Control-Allow-Origin', '*')
    donuts = queries.getWhere('donuts', 'id', id)
    return {'cats':['Austin', 'Tommy', 'Wes', 'Robby'], 'donuts': donuts};

run(host='localhost', port=8000, debug=True, reloader=True, server='cherrypy')
