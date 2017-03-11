from ..core.tasktype import TaskType
from .taskpool import TaskPool
import logging

class Scheduler(object):
    def __init__(self, tasktypes):
        #init taskpool
        self.pools = {}
        for tasktype in tasktypes:
            self.pools[tasktype.name] = TaskPool()

    def addTask(self, tasks):
        for task in tasks:
            self.pools[task.typename].addTask(task)

    def getTask(self, tasktypename):
        if self.pools[tasktypename] != None:
            return self.pools[tasktypename].getTask()
        else:
            logging.error("Invalid task type " + tasktypename)
            return None

    def isPoolEmpty(self):
        isEmpty = True
        for pool in self.pools:
            isEmpty = isEmpty and self.pools[pool].isAllTaskDone()
        if isEmpty:
            logging.warning("Task queue is empty and all threads are idling. Complete the job")
            return True
        return False
