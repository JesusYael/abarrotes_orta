import web

urls = (
    '/', 'mvc.controllers.bienvenida.index.Index'
)
app = web.application(urls, globals()) #aplicacion web

if __name__ == "__main__":
    app.run()
