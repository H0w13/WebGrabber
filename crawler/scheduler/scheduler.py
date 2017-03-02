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
            self.pools[task.tasktype.name].addTask(task)

    def getTask(self, tasktype):
        if isinstance(tasktype, TaskType):
            return self.pools[tasktype.name].getTask()
        else:
            logging.error("Invalid task type")
            return None

    def isPoolEmpty(self):
        isEmpty = True
        for pool in self.pools:
            isEmpty = isEmpty and pool.isAllTaskDone()
        if isEmpty:
            logging.warning("Task queue is empty and all threads are idling. Complete the job")
            return True
        return False
