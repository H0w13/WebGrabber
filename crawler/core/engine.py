from ..scheduler import Scheduler
import logging


class Engine(object):
    """core engine"""

    def __init__(self, tasktypes, settings):
        self.settings = settings
        self.scheduler = Scheduler(tasktypes)

    def run(self, initTasks):
        self.scheduler.run(initTasks)

    def allFinished(self):
        if self.scheduler.tasks.isAllTaskDone() and self.scheduler.threads.isAllThreadIdle():
            logging.warning(
                "Task queue is empty and all threads are idling. Complete the job")
            return True
        return False
