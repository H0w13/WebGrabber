from taskpool import *
from threadpool import *

class Scheduler(object):
    def __init__(self):
        pass
    
    def initial(self, tasktypes, workers):
        #init taskpool
        self.tasks = TaskPool(tasktypes)
        #init threadpool
        fetcher, parser, saver = workers
        self.threads = ThreadPool(fetcher, parser, saver, self.tasks)
    
    def run(self, tasks, threadnum):
         for task in tasks:
            self.tasks.addTask(task)
        fetcher_num, parser_num, saver_num = threadnum
        self.threads.startWork(fetcher_num, parser_num, saver_num)

    def allFinished(self):
        if self.tasks.isAllTaskDone() and self.threads.isAllThreadIdle():
            logging.warning("Task queue is empty and all threads are idling. Complete the job") 
            return True
        return False