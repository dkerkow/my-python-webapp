
import web

render = web.template.render('templates/')


# URL handling:
urls = (
'/', 'index',
'/add', 'add'
)

# DB Connection:
db = web.database(dbn='postgres', user='postgres', pw='Velavsid', host='localhost', db='test_webapp')



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
