# -- coding: utf-8 --
import logging
import random
import time

from ..core.engine import Engine
from ..core.request import Request
from ..workers.easymoney.tasktype import FundTaskType

from .fundapp_config import settings

class FundApp(object):

    def run(self):
        '''main function'''
        tasks = []
        for code in settings["codelist"]:
            t = Request(code["code"], "Fetcher")
            t.build(settings["baseurl"] + code["code"])
            t.addTags({"name": code["name"]})
            tasks.append(t)

        fundTaskType = FundTaskType()

        engine = Engine(fundTaskType.getTypes(), settings)
        engine.run(tasks)
        while True:
            logging.warning("Check status")
            time.sleep(random.randint(0, 5))
            if engine.allFinished():
                break
        logging.warning("Job done")
