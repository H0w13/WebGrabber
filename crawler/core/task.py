class Task(object):
    def __init__(self, identifier, tasktype):
        self.identifier = identifier
        self.type = tasktype
        self.tags = {}

    def addTags(self, tags):
        for t in tags:
            self.tags[t] = tags[t]
