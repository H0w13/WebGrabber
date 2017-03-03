import logging

from ..scheduler import Scheduler
from .threadpool import ThreadPool


class Engine(object):
    """core engine"""

    def __init__(self, tasktypes, settings):
        self.settings = settings
        self.scheduler = Scheduler(tasktypes)
        self.threadpool = {}
        for tasktype in tasktypes:
            count = 10
            if self.settings[tasktype.name + ".count"]:
                count = self.settings[tasktype.name + ".count"]
            self.threadpool[tasktype.name] = ThreadPool(tasktype, count, self.getTask)

    def run(self, initTasks):
        self.scheduler.addTask(initTasks)

    def getTask(self, tasktype):
        self.threadpool[tasktype].task_done()
        return self.threadpool[tasktype].getTask()

    def allFinished(self):
        isAllThreadIdle = True
        for pool in self.threadpool:
            isAllThreadIdle = isAllThreadIdle and pool.isAllThreadIdle()

        if self.scheduler.isPoolEmpty() and isAllThreadIdle:
            logging.warning(
                "Task queue is empty and all threads are idling. Complete the job")
            return True
        return False
