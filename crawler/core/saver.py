from pymongo import MongoClient

class Saver(object):
    def __init__(self):
        pass
    def doWork(self, task):
        raise NotImplementedError

class MongoSaver(Saver):
    def __init__(self):
        Saver.__init__(self)
        
    def doWork(self, task):
        raise NotImplementedError

    def saveItem(self, item):
        client = MongoClient('localhost', 27017)
        db = client['webgrabber']
        collection = db['easymoney_fund']        
        collection.insert_one(item)