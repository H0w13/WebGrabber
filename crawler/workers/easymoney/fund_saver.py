from ...core.saver import Saver
import pymongo

class FundSaver(Saver):
    def __init__(self):
        Saver.__init__(self)
        return 

    def doWork(self, item):
        client = MongoClient('localhost', 27017)
        db = client['webgrabber']
        collection = db['easymoney_fund']        
        collection.insert_one(item)