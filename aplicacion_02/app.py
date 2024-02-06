import web

# Rutas de los controladores
urls = (
    "/", "hello",
    "/pagina1", "pagina1",
    "/pagina2", "pagina2"  
)
app = web.application(urls, globals())

class hello:
    def GET(self, name=None):
        if not name:
            name = 'World'
        return 'Hola, ' + name + '!'

class pagina1:
    def GET(self):
        return "PAGINA 1"

class pagina2:  
    def GET(self):
        return "Hola, estás en la página 2. ¡Sientes mucha emoción!"

# Punto de entrada
if __name__ == "__main__":
    app.run()
