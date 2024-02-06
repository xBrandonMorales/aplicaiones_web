import web

# Rutas de los controladores
urls = (
    '/(.*)', 'mvc.controllers.hello.Hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World_2'
        return 'Hola, ' + name + '!'

# Punto de entrada
if __name__ == "__main__":
    app.run()