from ...core.parser import Parser 
import re
import logging

class FundParser(Parser):
    def __init__(self):
        Parser.__init__(self)
        return  

    def doWork(self, content):
        pattern = "\<tr\>\<td\>(?P<date>[\d-]+)\</td\>\<td[^\>]*?\>(?P<value>[\d\.]+)\</td\>\<td[^\>]*?\>(?P<totalvalue>[\d\.]+)\</td\>"
        result = []
        groups = ["date", "value", "totalvalue"]
        try:
            p = re.compile(pattern)
            iterator = p.finditer(content)
            for match in iterator:
                outputJSON = {}
                for g in groups:
                    outputJSON[g] = match.group(g)
                result.append(outputJSON)
        except Exception as excep:
            logging.error("%s.doWork() error: %s", self.__class__.__name__, excep)
            return -1, [],[]
        return 1, [], result