from .task import Task

class Request(Task):
    def __init__(self, identifier, tasktype):
        Task.__init__(self, identifier, tasktype)
        return
