from ...core.fetcher import Fetcher 
import time
import random

class FundFetcher(Fetcher):
    def __init__(self):
        Fetcher.__init__(self)
        return
         
    def doWork(self, url, repeat,useProxy):
        time.sleep(random.randint(0, self.sleep_time))
        try:
            content = self.url_fetch(url, useProxy)
        except Exception as excep:
            if repeat >= self.max_repeat:
                fetch_result, content = -1, None                
            else:
                fetch_result, content = 0, None
            return fetch_result, content
        return 1, content       