from thread import *
import copy

class ThreadPool(object):
    def __init__(self, tasktypes, count):
        self.threadList = []
        self.threadList += [BaseThread(str(tasktype)+"-"+str(i), copy.deepcopy(tasktypes[tasktype][0]), self.taskpool, tasktype) for i in xrange(count)]
       
    
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