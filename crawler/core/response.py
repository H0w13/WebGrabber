from .task import Task

class Response(Task):
    def __init__(self, identifier, tasktype):
        Task.__init__(self, identifier, tasktype)
        return
