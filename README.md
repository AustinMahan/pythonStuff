# Simple Python Server
## First you must install the dependencies(psycopg2,queries,cherrypy,bottle) using pip or pip3 if you have python3

1. import the dependencies
My main file:
```
import queries
import cherrypy
from bottle import get, post, route, run, response
```
My queries file(seperates the db related stuff):
`import psycopg2`
1. Connect to the postgres db:
```
try:
    conn = psycopg2.connect("dbname='kittens' user='Austin' host='localhost'")
    db = conn.cursor()
except:
    print("I am unable to connect to the database")
```
1. A simple route: 
```
@get('/')
def mainPage():
    response.set_header('Access-Control-Allow-Origin', '*')
    kittens = queries.getAll('kittens')
    kittens = queries.getComments('comments', kittens)
    return {'kittens': kittens}
```
1. A simple query:
```
def getAll(table):
    db.execute("SELECT * FROM {0}".format(table))
    out = db.fetchall()
    return out;
```
