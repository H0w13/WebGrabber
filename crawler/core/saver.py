class Saver(object):
    def __init__(self):
        pass
    def doWork(self, item):
        raise NotImplementedError

class MongoSaver(Saver):
    def __init__(self):
        Saver.__init__(self)
        
    def doWork(self, item):
        raise NotImplementedError