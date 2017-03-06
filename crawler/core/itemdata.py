from .task import Task

class ItemData(Task):
    def __init__(self, identifier, tasktype):
        Task.__init__(self, identifier, tasktype)
        return
