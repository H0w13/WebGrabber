import logging
import random
import time

from ...framework.core.response import Response
from ...framework.fetcher.sock5fetcher import Sock5Fetcher


class FundFetcher(Sock5Fetcher):

    def __init__(self):
        Sock5Fetcher.__init__(self)
        return

    def doWork(self, request):
        time.sleep(random.randint(0, self.sleep_time))
        try:
            content = self.url_fetch(request.url, False)
            logging.warning("%s downloaded content for %s",
                            self.__class__.__name__, request.identifier)
            logging.warning("page url is %s", request.url)
            response = Response(request.identifier, "Parser")
            response.addTags(request.tags)
            response.build(content)
            return [response]
        except Exception as excep:
            logging.error("FundFetcher.doWork() error: %s", excep)
            return []
