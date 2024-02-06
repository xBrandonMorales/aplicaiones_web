import web

class Hello:
    def GET(self, name):
        if not name:
            name = 'World_2'
        return 'Hola, ' + name + '!'