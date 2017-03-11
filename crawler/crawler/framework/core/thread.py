import logging
import random
import threading
import time
import traceback

import enum

class ThreadStatus(enum.Enum):
    RUNNING = "Running"
    IDLE = "Idle"


class BaseThread(threading.Thread):

    def __init__(self, name, tasktype, worker, eventHub):
        threading.Thread.__init__(self, name=name)

        # def create_obj(cls_name):
        #     names = cls_name.split(".")
        #     for key, value in globals().items():
        #         print key, value
        #     cls = globals()[names[0]]
        #     for name in names[1:]:
        #         cls = getattr(cls, name)
        #     if isinstance(cls, type):
        #         return cls()
        #     else:
        #         raise Exception("no such class")

        # self.worker = create_obj(worker)
        self.worker = worker
        self.terminated = False
        self.status = ThreadStatus.IDLE
        self.tasktype = tasktype
        self.eventHub = eventHub
        return

    def run(self):
        logging.warning(
            "%s[%s] start", self.__class__.__name__, self.getName())
        while True:
            try:
                task = self.eventHub.getGetTask()(self.tasktype.name)
                if task:
                    logging.warning("%s[%s] got a task.",
                                    self.__class__.__name__, self.getName())
                    self.status = ThreadStatus.RUNNING
                    nextTasks = self.work(task)
                    self.eventHub.getPutTask()(nextTasks)
                else:
                    logging.warning(
                        "%s[%s] could not get task. idling", self.__class__.__name__, self.getName())
                    self.status = ThreadStatus.IDLE
                    if self.terminated:
                        break
                    time.sleep(random.randint(0, 5))
            except Exception as exp:
                logging.error("thread %s[%s] error", self.__class__.__name__, self.getName())
                logging.error(traceback.format_exc())
                self.status = ThreadStatus.IDLE
                break
        return

    def work(self, task):
        try:
            logging.warning("%s[%s] start working",
                            self.__class__.__name__, self.getName())
            return self.worker.doWork(task)
        except Exception as excep:
            logging.error("%s.worker.doWork() error: %s",
                          self.__class__.__name__, excep)
