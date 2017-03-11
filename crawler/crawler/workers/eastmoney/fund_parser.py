from ...framework.parser import Parser
from ...framework.core.itemdata import ItemData
from ...framework.core.settings import settings
from ...framework.core.request import Request
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
            iterator = p.finditer(response.responsedata)
            for match in iterator:
                output = ItemData(response.identifier, "Saver")
                output.addTags(response.tags)
                content = {}
                for g in groups:
                    content[g] = match.group(g)
                output.build(content)
                result.append(output)
            #get current pages and add fetcher tasks for more pages
            curMath = re.search(ptnCurPage, response.responsedata)
            if curMath:
                curPage = curMath.group("cur")
                if int(curPage) == 1:
                    logging.warning("got first page for " + response.tags["code"])
                    m = re.search(ptnTotalPage, response.responsedata)
                    if m:
                        totalPage = int(m.group("total"))
                        for x in xrange(2, totalPage+1):
                            t = Request(response.tags["code"], "Fetcher")
                            t.build(settings["baseurl"] + response.tags["code"] + "&page=" + str(x))
                            t.addTags({"name": response.tags["name"]})
                            result.append(t)
                        logging.warning("add %s page for %s", totalPage-1, response.tags["code"])

            logging.warning("%s parsed content for %s", self.__class__.__name__, response.identifier)
        except Exception as excep:
            logging.error("%s.doWork() error: %s", self.__class__.__name__, excep)
            return []
        return result
