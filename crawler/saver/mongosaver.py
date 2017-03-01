from pymongo import MongoClient
from . import Saver


class MongoSaver(Saver):

    def __init__(self, server, port, db):
        Saver.__init__(self)
        client = MongoClient(server, port)
        self.db = client[db]

    def doWork(self, task):
        raise NotImplementedError

    def saveItem(self, collectionname, item):
        """insert item"""
        collection = self.db[collectionname]
        collection.insert_one(item)

    def upsertItem(self, collectionname, item, findQuery):
        """insert or update item"""
        collection = self.db[collectionname]
        collection.update(findQuery, item, upsert=True)
