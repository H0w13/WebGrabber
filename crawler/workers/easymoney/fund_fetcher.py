from ...core.fetcher import Fetcher 
from ...core.task import Task 
from .tasktype import TaskType
import time
import random
import logging

class FundFetcher(Fetcher):
    def __init__(self):
        Fetcher.__init__(self)
        return
         
    def doWork(self, task):
        time.sleep(random.randint(0, self.sleep_time))
        try:
            content = self.url_fetch(task.data["url"], False)            
            logging.warning("%s downloaded content for %s", self.__class__.__name__, task.identifier)
            return [Task(task.identifier, TaskType.HTM_PARSE, {"name": task.data["name"], "content":content})]
        except Exception as excep:
            logging.error("FundFetcher.doWork() error: %s", excep)
            return []        
         