from pymongo import MongoClient

class DataService(object):

    def __init__(self, server, port, db):
        client = MongoClient(server, port)
        self.db = client[db]

    def saveItem(self, collectionname, item):
        """insert item"""
        collection = self.db[collectionname]
        collection.insert_one(item)

    def upsertItem(self, collectionname, item, findQuery):
        """insert or update item"""
        collection = self.db[collectionname]
        collection.update(findQuery, item, upsert=True)

    def findItems(self, collectioname, findQuery):
        result = []
        collection = self.db[collectioname]
        items = collection.find(findQuery)
        for item in items:
            result.append(item)
        return result
