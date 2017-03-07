# -- coding: utf-8 --
import sys

from ..utilities.useragents import *


class Fetcher(object):

    def __init__(self):
        reload(sys)
        sys.setdefaultencoding('utf8')
        self.max_repeat = 3
        self.sleep_time = 5

    def build_header(self):
        headers = ["User-Agent:" + getRandomUserAgent(),
                   "Accept-Encoding:gzip"]
        return headers

    def doWork(self, task):
        raise NotImplementedError
