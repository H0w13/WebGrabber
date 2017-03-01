# -- coding: utf-8 --

import random
import StringIO
import sys
import time

import pycurl

from ..utilities import useragents
from ..core.task import Task

from ..settings import settings


class Sock5Fetcher(object):

    def __init__(self):
        reload(sys)
        sys.setdefaultencoding('utf8')
        self.max_repeat = 3
        self.sleep_time = 5

    def url_fetch(self, url, useProxy=False):
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        if useProxy:
            c.setopt(c.PROXY, settings['proxy_server'])
            c.setopt(c.PROXYPORT, 1090)
            c.setopt(c.PROXYTYPE, c.PROXYTYPE_SOCKS5)
        c.setopt(c.FOLLOWLOCATION, 1)
        c.setopt(c.MAXREDIRS, 5)

        b = StringIO.StringIO()
        c.setopt(c.WRITEFUNCTION, b.write)
        c.setopt(c.HTTPHEADER, self.build_header())

        c.perform()
        return b.getvalue()

    def build_header(self):
        headers = ["User-Agent:" + useragents.getRandomUserAgent(),
                   "Accept-Encoding:gzip"]
        return headers

    def doWork(self, task):
        raise NotImplementedError
