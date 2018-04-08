import tornado.web


class BaseHandler(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass


class MainHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.write('Hello, world')
