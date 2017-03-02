import logging
import random
import threading
import time

import enum
from twisted.internet import reactor

class ThreadStatus(enum.Enum):
    RUNNING = "Running"
    IDLE = "Idle"


class BaseThread(threading.Thread):

    def __init__(self, name, tasktype, worker, callback):
        threading.Thread.__init__(self, name=name)

        def create_obj(cls_name):
            names = cls_name.split(".")
            cls = globals()[names[0]]
            for name in names[1:]:
                cls = getattr(cls, name)
            if isinstance(cls, type):
                return cls()
            else:
                raise Exception("no such class")

        self.worker = create_obj(worker)
        self.terminated = False
        self.status = ThreadStatus.IDLE
        self.tasktype = tasktype
        self.callback = callback
        return

    def run(self):
        logging.warning(
            "%s[%s] start", self.__class__.__name__, self.getName())
        while True:
            try:
                task = self.getTask()
                if task:
                    logging.warning("%s[%s] got a task.",
                                    self.__class__.__name__, self.getName())
                    self.status = ThreadStatus.RUNNING
                    self.work(task)
                else:
                    logging.warning(
                        "%s[%s] could not get task. idling", self.__class__.__name__, self.getName())
                    self.status = ThreadStatus.IDLE
                    if self.terminated:
                        break
                    time.sleep(random.randint(0, 5))
            except:
                self.status = ThreadStatus.IDLE
                break
        return

    def work(self, task):
        try:
            logging.warning("%s[%s] start working",
                            self.__class__.__name__, self.getName())
            tasks = self.worker.doWork(task)
            logging.warning("%s[%s] generates %s new tasks and add to task pool",
                            self.__class__.__name__, self.getName(), len(tasks))
            for t in tasks:
                self.pool.addTask(t)
            self.pool.task_done(self.tasktype)
        except Exception as excep:
            logging.error("%s.worker.doWork() error: %s",
                          self.__class__.__name__, excep)

    def getTask(self):
        logging.warning("%s[%s] try to get a task from %s queue",
                        self.__class__.__name__, self.getName(), self.tasktype)
        try:
            return self.pool.getTask(self.tasktype)
        except Exception as excep:
            return None