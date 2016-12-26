import threading
import logging
from taskpool import *
import enum
import time

class ThreadStatus(enum.Enum):
    RUNNING = "Running"
    IDLE = "Idle"

class BaseThread(threading.Thread):
    def __init__(self, name, worker, taskpool):       
        threading.Thread.__init__(self, name=name)
        self.worker = worker
        self.pool = taskpool
        self.terminated = False  
        self.status = ThreadStatus.IDLE      
        return
    def run(self):
        logging.warning("%s[%s] start", self.__class__.__name__, self.getName())       
        while True:
            try:
                task = self.getTask()
                if task:
                    self.status = ThreadStatus.RUNNING
                    self.work(task)                    
                else:
                    logging.warning("%s[%s] could not get task. idling", self.__class__.__name__, self.getName())
                    self.status = ThreadStatus.IDLE 
                    if self.terminated:
                        break
                    time.sleep(random.randint(0, 5))
            except:
                self.status = ThreadStatus.IDLE 
                break
        return

    def work(self, task):
        raise NotImplementedError

    def getTask(self):
        raise NotImplementedError

class FetcherThread(BaseThread):
    def __init__(self, name, worker, taskpool):
        BaseThread.__init__(self, name, worker, taskpool)
        self.maxTry = 3
        return

    def getTask(self):
        logging.warning("%s[%s] get a task from fetcher queue", self.__class__.__name__, self.getName())
        try:
            return self.pool.getTask(TaskType.URL_FETCH)
        except Exception as excep:
            return None

    def work(self, task):
        try:
            url, repeat = task
            if repeat > self.maxTry:
                logging.warning("Retied more than %s times for %s. Abort the task", self.maxTry, url)
                return
            logging.warning("%s[%s] start processing %s", self.__class__.__name__, self.getName(), url)    
            code, content = self.worker.doWork(url, repeat, False)
            self.pool.task_done(TaskType.URL_FETCH)
        except Exception as excep:
            code, content = -1, None
            logging.error("%s.worker.doWork() error: %s", self.__class__.__name__, excep)

        if code > 0:
            self.pool.addTask(TaskType.HTM_PARSE, (content))
        elif code == 0:
            self.pool.addTask(TaskType.URL_FETCH, (url, repeat+1))
        return

class ParserThread(BaseThread):
    def __init__(self, name, worker, taskpool):
        BaseThread.__init__(self, name, worker, taskpool)
        return
    
    def getTask(self):
        logging.warning("%s[%s] get a task from parser queue", self.__class__.__name__, self.getName())
        try:
            return self.pool.getTask(TaskType.HTM_PARSE)
        except Exception as excep:
            return None

    def work(self, task):
        content = task
        try:
            logging.warning("%s[%s] start parsing", self.__class__.__name__, self.getName())
            code, urlList, saveList = self.worker.doWork(content)
            self.pool.task_done(TaskType.HTM_PARSE)
        except Exception as excep:
            code, urlList, saveList = -1, [], []
            logging.error("%s.worker.doWork() error: %s", self.__class__.__name__, excep)
       
        if code > 0:
            for url in urlList:
                self.pool.addTask(TaskType.URL_FETCH, (url, 0))
            for item in saveList:
                self.pool.addTask(TaskType.ITEM_SAVE, item)
        return

class SaverThread(BaseThread):
    def __init__(self, name, worker, taskpool):
        BaseThread.__init__(self, name, worker, taskpool)
        return
    
    def getTask(self):
        logging.warning("%s[%s] get a task from saver queue", self.__class__.__name__, self.getName())
        try:
            return self.pool.getTask(TaskType.ITEM_SAVE)
        except Exception as excep:
            return None

    def work(self, task):
        item = task
        try:
            logging.warning("%s[%s] start saving", self.__class__.__name__, self.getName())
            code = self.worker.doWork(item)
            self.pool.task_done(TaskType.ITEM_SAVE)
        except Exception as excep:
            code = -1
            logging.error("%s.worker.doWork() error: %s", self.__class__.__name__, excep)
       
        if code != -1:
            logging.warning("%s[%s] saved successfully", self.__class__.__name__, self.getName())
        else:
            logging.warning("%s[%s] failed to save", self.__class__.__name__, self.getName())
        return