import tornado.web


class BaseHandler(tornado.web.RequestHandler):

    def initialize(self, conn):
        self.conn = conn

    def data_received(self, chunk):
        pass


class MainHandler(BaseHandler):

    def get(self, *args, **kwargs):
        print(self.conn)
        self.write('Hello, world')
