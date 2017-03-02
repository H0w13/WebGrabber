import Queue
import logging

class TaskPool(object):
    def __init__(self):
        self.pool = Queue.PriorityQueue()

    def addTask(self, task):
        self.pool.put(task)

    def getTask(self):
        try:
            return self.pool.get(block=True, timeout=5)
        except Exception as excep:
            logging.error("Retrieve task error. " + excep.message)
            return None

    def task_done(self):
        self.pool.task_done()

    def isAllTaskDone(self):
        return self.pool.empty()
