from .task import Task

class Request(Task):
    def __init__(self, identifier, tasktypename):
        Task.__init__(self, identifier, tasktypename)
        self.url = None
        return

    def build(self, url):
        self.url = url
