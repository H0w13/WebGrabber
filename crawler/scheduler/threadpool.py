from thread import *
import copy

class ThreadPool(object):
    def __init__(self, fetcher, parser, saver, taskpool):
        self.threadList = []
        self.inst_fetcher = fetcher
        self.inst_parser = parser
        self.inst_saver = saver
        self.taskpool = taskpool
    
    def startWork(self, fetcher_num=10, parser_num=10, saver_num=10):
        self.threadList += [FetcherThread("fetcher-%d" % i, copy.deepcopy(self.inst_fetcher), self.taskpool) for i in range(fetcher_num)]
        self.threadList += [ParserThread("parser-%d" % i, copy.deepcopy(self.inst_parser), self.taskpool) for i in range(parser_num)]
        self.threadList += [SaverThread("saver-%d" % i, copy.deepcopy(self.inst_saver), self.taskpool) for i in range(saver_num)]

        for t in self.threadList:
            t.setDaemon(True)
            t.start()

        for t in self.threadList:
            if t.is_alive():
                t.join()

    def isAllThreadIdle(self):
        if len([t for t in self.threadList if t.status == ThreadStatus.IDLE or t.status is None]) == len(self.threadList):
            for t in self.threadList:
                t.terminated = True
            return True
        return False