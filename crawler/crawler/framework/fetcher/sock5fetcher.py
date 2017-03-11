# -- coding: utf-8 --

import random
import StringIO
import sys
import time

import pycurl

from . import Fetcher
from ..core.task import Task

from ..core.settings import settings


class Sock5Fetcher(Fetcher):

    def __init__(self):
        Fetcher.__init__(self)

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

    def doWork(self, task):
        raise NotImplementedError
