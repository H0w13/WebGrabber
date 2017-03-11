from ...parser import Parser
from ...core.itemdata import ItemData
from ...core.settings import settings
from ...core.request import Request
import re
import logging

class FundParser(Parser):
    def __init__(self):
        Parser.__init__(self)
        return

    def doWork(self, response):
        pattern = r"\<tr\>\<td\>(?P<date>[\d-]+)\</td\>\<td[^\>]*?\>(?P<value>[\d\.]+)\</td\>\<td[^\>]*?\>(?P<totalvalue>[\d\.]+)\</td\>"
        ptnCurPage = r"curpage:(?P<cur>\d+)"
        ptnTotalPage = r"pages:(?P<total>\d+)"
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
            #get current pages and add fetcher tasks for more pages
            p = re.compile(ptnCurPage)
            match = p.match(response.data)
            if match:
                curPage = match.group("cur")
                if int(curPage) == 1:
                    m = re.match(ptnTotalPage, response.data)
                    if m:
                        totalPage = int(m.group("total"))
                        for x in xrange(2, totalPage+1):
                            t = Request(response.tags["code"], "Fetcher")
                            t.build(settings["baseurl"] + response.tags["code"] + "&page=" + str(x))
                            t.addTags({"name": response.tags["name"]})
                            result.append(t)

            logging.warning("%s parsed content for %s", self.__class__.__name__, response.identifier)
        except Exception as excep:
            logging.error("%s.doWork() error: %s", self.__class__.__name__, excep)
            return []
        return result
