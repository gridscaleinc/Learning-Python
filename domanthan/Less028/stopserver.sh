from werkzeug.serving import make_server

class ServerThread(threading.Thread):

    def __init__(self, app):
        threading.Thread.__init__(self)
        self.srv = make_server('127.0.0.1', 5000, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        log.info('starting server')
        self.srv.serve_forever()

    def shutdown(self):
        self.srv.shutdown()

def start_server():
    global server
    app = flask.Flask('myapp')
    ...
    server = ServerThread(app)
    server.start()
    log.info('server started')

def stop_server():
    global server
    server.shutdown()

stop_server()

