from .thread import BaseThread
from .thread import ThreadStatus

class ThreadPool(object):
    def __init__(self, tasktype, count, getTask):
        self.threadList = []
        self.threadList += [BaseThread(str(tasktype)+"-"+str(i), tasktype, tasktype.handler, getTask) for i in xrange(count)]

    def startWork(self):
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

    def terminate(self):
        for t in self.threadList:
            t.terminated = True
