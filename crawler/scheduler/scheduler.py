from taskpool import *
from threadpool import *

class Scheduler(object):
    def __init__(self, tasktypes):
        #init taskpool
        self.tasks = TaskPool(tasktypes)
        #init threadpool
        self.threads = ThreadPool(tasktypes, self.tasks)

    def run(self, tasks):
        for task in tasks:
            self.tasks.addTask(task)
        self.threads.startWork()

    def allFinished(self):
        if self.tasks.isAllTaskDone() and self.threads.isAllThreadIdle():
            logging.warning("Task queue is empty and all threads are idling. Complete the job")
            return True
        return False
