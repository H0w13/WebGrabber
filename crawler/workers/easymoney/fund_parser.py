from ...parser import Parser
from ...core.itemdata import ItemData 
from .tasktype import TaskType 
import re
import logging

class FundParser(Parser):
    def __init__(self):
        Parser.__init__(self)
        return

    def doWork(self, response):
        pattern = r"\<tr\>\<td\>(?P<date>[\d-]+)\</td\>\<td[^\>]*?\>(?P<value>[\d\.]+)\</td\>\<td[^\>]*?\>(?P<totalvalue>[\d\.]+)\</td\>"
        result = []
        groups = ["date", "value", "totalvalue"]
        try:
            p = re.compile(pattern)
            iterator = p.finditer(response.data)
            for match in iterator:
                output = ItemData(response.identifier, "Saver")
                output.addTags(response.tags)
                content = {}
                for g in groups:
                    content[g] = match.group(g)
                output.build(content)
                result.append(output)
            logging.warning("%s parsed content for %s", self.__class__.__name__, response.identifier)
        except Exception as excep:
            logging.error("%s.doWork() error: %s", self.__class__.__name__, excep)
            return []
        return result
