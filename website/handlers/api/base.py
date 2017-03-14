import tornado.web

class BaseApiHandler(tornado.web.RequestHandler):
    """A class to collect common handler methods - all other handlers should
    subclass this one.
    """

    @property
    def dbService(self):
        return self.application.dbService
