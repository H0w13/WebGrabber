import logging

from ..scheduler.scheduler import Scheduler
from .threadpool import ThreadPool
from .eventhub import EventHub


class Engine(object):
    """core engine"""

    def __init__(self, tasktypes, settings):
        self.settings = settings
        self.eventhub = EventHub()
        self.scheduler = Scheduler(tasktypes)
        self.threadpool = {}
        for tasktype in tasktypes:
            self.eventhub.registerGetTask(self.getTask)
            self.eventhub.registerPutTask(self.putTask)
            #Here we can add middleware
            #self.eventhub.registerPreWork(tasktype.name, None)
            #self.eventhub.registerPostWork(tasktype.name, None)
            count = 10
            if self.settings[tasktype.name + ".count"]:
                count = self.settings[tasktype.name + ".count"]
            self.threadpool[tasktype.name] = ThreadPool(tasktype, count, self.eventhub)

    def run(self, initTasks):
        self.scheduler.addTask(initTasks)
        for pool in self.threadpool:
            self.threadpool[pool].startWork()

    def getTask(self, tasktypename):
        return self.scheduler.getTask(tasktypename)

    def putTask(self, tasks):
        self.scheduler.addTask(tasks)

    def allFinished(self):
        isAllThreadIdle = True
        for pool in self.threadpool:
            isAllThreadIdle = isAllThreadIdle and self.threadpool[pool].isAllThreadIdle()

        if self.scheduler.isPoolEmpty() and isAllThreadIdle:
            logging.warning(
                "Task queue is empty and all threads are idling. Complete the job")
            return True
        return False
