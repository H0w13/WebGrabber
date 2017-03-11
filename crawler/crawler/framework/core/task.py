class Task(object):
    def __init__(self, identifier, tasktypename):
        self.identifier = identifier
        self.typename = tasktypename
        self.tags = {}

    def addTags(self, tags):
        for t in tags:
            self.tags[t] = tags[t]
