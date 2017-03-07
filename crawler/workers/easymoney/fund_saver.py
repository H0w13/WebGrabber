import logging

from ...saver.mongosaver import MongoSaver


class FundSaver(MongoSaver):

    def __init__(self):
        MongoSaver.__init__(self)
        return

    def doWork(self, itemdata):
        try:
            json = {}
            json["identifier"] = itemdata.identifier
            for t in itemdata.tags:
                json[t] = itemdata.tags[t]
            for c in itemdata.data:
                json[c] = itemdata.data[c]
            self.upsertItem("easyfund", json, {'date': itemdata.data[
                            "date"], 'identifier': itemdata.identifier})
            logging.warning("%s saved data to database for %s",
                            self.__class__.__name__, itemdata.identifier)
        except Exception as excep:
            logging.error("%s.doWork() error: %s",
                          self.__class__.__name__, excep)
        return []
