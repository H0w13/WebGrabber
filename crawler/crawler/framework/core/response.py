from .task import Task

class Response(Task):
    def __init__(self, identifier, tasktypename):
        Task.__init__(self, identifier, tasktypename)
        self.responsedata = None
        return

    def build(self, data):
        self.responsedata = data
