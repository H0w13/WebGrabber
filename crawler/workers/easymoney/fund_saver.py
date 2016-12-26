from ...core.saver import MongoSaver
import pymongo
import logging

class FundSaver(MongoSaver):
    def __init__(self):
        MongoSaver.__init__(self)
        return 

    def doWork(self, task):
        try:
            self.saveItem(task.data)
            logging.warning("%s saved data to database for %s", self.__class__.__name__, task.identifier)
        except Exception as excep:
            logging.error("%s.doWork() error: %s", self.__class__.__name__, excep)
        return []