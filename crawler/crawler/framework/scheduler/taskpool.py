import Queue
import logging
import traceback

class TaskPool(object):
    def __init__(self):
        self.pool = Queue.Queue()

    def addTask(self, task):
        self.pool.put(task)
        #self.pool.task_done()

    def getTask(self):
        try:
            task = self.pool.get(block=True, timeout=5)
            return task
        except Exception as excep:
            # logging.error("Retrieve task error.")
            # logging.error(traceback.format_exc())
            return None

    def isAllTaskDone(self):
        return self.pool.empty()
