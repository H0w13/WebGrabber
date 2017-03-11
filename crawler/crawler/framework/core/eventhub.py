class EventHub(object):
    def __init__(self):
        self.prework = {}
        self.postwork = {}
        self.getTask = None
        self.putTask = None

    def registerPreWork(self, tasktypename, handler):
        if tasktypename in self.prework:
            self.prework[tasktypename].append(handler)
        else:
            self.prework[tasktypename] = [handler]

    def registerPostWork(self, tasktypename, handler):
        if tasktypename in self.postwork:
            self.postwork[tasktypename].append(handler)
        else:
            self.postwork[tasktypename] = [handler]

    def getPreWork(self, tasktypename):
        return self.prework[tasktypename]

    def getPostWork(self, tasktypename):
        return self.postwork[tasktypename]

    def registerGetTask(self, handler):
        self.getTask = handler

    def registerPutTask(self, handler):
        self.putTask = handler

    def getGetTask(self):
        return self.getTask

    def getPutTask(self):
        return self.putTask
