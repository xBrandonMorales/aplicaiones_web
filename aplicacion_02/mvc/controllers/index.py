import web

render = web.templete.render('mvc/views/')

class Index:
    def GET(self):
        return render.index()
        
