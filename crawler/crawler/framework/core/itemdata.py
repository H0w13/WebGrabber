from .task import Task

class ItemData(Task):
    def __init__(self, identifier, tasktypename):
        Task.__init__(self, identifier, tasktypename)
        self.data = None
        return

    def build(self, data):
        self.data = data
