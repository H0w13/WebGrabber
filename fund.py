# -- coding: utf-8 --
from crawler.scheduler import *
from crawler.workers.easymoney import *
import time
import random
import logging

baseurl = "http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&page=1&per=10&code="
codelist = ["486002"]
sourcelist = [baseurl+code for code in codelist]

scheduler = Scheduler()
fetcher = FundFetcher()
parser = FundParser()
saver = FundSaver()

scheduler.initial(sourcelist, (fetcher, parser, saver))
scheduler.run((1,1,1))
while True:
    logging.warning("Check status")
    time.sleep(random.randint(0, 5))
    if scheduler.allFinished():
        break
logging.warning("Job done")