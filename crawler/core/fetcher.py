# -- coding: utf-8 --

import sys
import time
import random
import pycurl
import StringIO
from ..utilities import *

class Fetcher(object):

    def __init__(self):
        reload(sys)
        sys.setdefaultencoding('utf8') 
        self.max_repeat = 3
        self.sleep_time = 5
    
    def url_fetch(self,url, useProxy=False):
        c=pycurl.Curl()
        c.setopt(pycurl.URL,url)
        if useProxy:
            c.setopt(pycurl.PROXY, 'localhost')
            c.setopt(pycurl.PROXYPORT, 1090)
            c.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5)
        c.setopt(pycurl.FOLLOWLOCATION,1)
        c.setopt(pycurl.MAXREDIRS,5)

        b=StringIO.StringIO()
        c.setopt(pycurl.WRITEFUNCTION,b.write)
        c.setopt(pycurl.HTTPHEADER, self.build_header())

        c.perform()
        return b.getvalue()
    
    def build_header(self):
        headers = ["User-Agent:"+getRandomUserAgent(), "Accept-Encoding:gzip"]
        return headers

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
        