#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import web
import argparse
import psycopg2

## Arguments & help

ap = argparse.ArgumentParser(description='Run the web app and' +
                             'provide the PostGIS connection settings.')
ap.add_argument('-d', dest='db_name', default='appdb',
                help='PostgreSQL database.')
ap.add_argument('-U', dest='db_user', default='postgres',
                help='PostgreSQL user name.')
ap.add_argument('-H', dest='db_host', default='localhost',
                help='PostgreSQL host.')
ap.add_argument('-p', dest='db_port', default='5432',
                help='PostgreSQL port.')
args = ap.parse_args()

 ## Set up the DB connection with the given parameters

con = psycopg2.connect("dbname={0} user={1} host={2} port={3}".format(
    args.db_name, args.db_user, args.db_host, args.db_port))
cur = con.cursor()



 ## App

render = web.template.render('templates/')


# URL handling:
urls = (
'/', 'index',
'/add', 'add',
'/map', 'map'
)

# DB Connection:
db = web.database(dbn='postgres', user='postgres', pw='Velavsid', host='localhost', db='test_webapp')

class map:
    def GET(self):
        return render.map()

class index:
    def GET(self):
        todos = db.select('todo')
        return render.index(todos)

class add:
    def POST(self):
        i = web.input()
        n = db.insert('todo', title=i.title)
        raise web.seeother('/')

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run() 
