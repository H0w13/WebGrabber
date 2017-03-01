from ...core.parser import Parser
from ...core.task import Task 
from .tasktype import TaskType 
import re
import logging

class FundParser(Parser):
    def __init__(self):
        Parser.__init__(self)
        return  

    def doWork(self, task):
        pattern = "\<tr\>\<td\>(?P<date>[\d-]+)\</td\>\<td[^\>]*?\>(?P<value>[\d\.]+)\</td\>\<td[^\>]*?\>(?P<totalvalue>[\d\.]+)\</td\>"
        result = []
        groups = ["date", "value", "totalvalue"]
        try:
            p = re.compile(pattern)
            iterator = p.finditer(task.data["content"])
            for match in iterator:
                outputJSON = {"identifier": task.identifier, "name":task.data["name"]}
                for g in groups:
                    outputJSON[g] = match.group(g)
                result.append(outputJSON)
            logging.warning("%s parsed content for %s", self.__class__.__name__, task.identifier)
        except Exception as excep:
            logging.error("%s.doWork() error: %s", self.__class__.__name__, excep)
            return []
        return [Task(task.identifier, TaskType.ITEM_SAVE, r) for r in result]