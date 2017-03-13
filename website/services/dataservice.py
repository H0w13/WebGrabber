from pymongo import MongoClient
from ..settings import settings

class DataService(object):

    def __init__(self):
        client = MongoClient(settings['dbserver'], settings['dbport'])
        self.db = client[settings['dbname']]

    def saveItem(self, collectionname, item):
        """insert item"""
        collection = self.db[collectionname]
        collection.insert_one(item)

    def upsertItem(self, collectionname, item, findQuery):
        """insert or update item"""
        collection = self.db[collectionname]
        collection.update(findQuery, item, upsert=True)
