# -- coding: utf-8 --
import logging
import random
import time

from ..core.engine import Engine
from ..core.task import Task
from ..workers.easymoney.fund_fetcher import FundFetcher
from ..workers.easymoney.fund_parser import FundParser
from ..workers.easymoney.fund_saver import FundSaver
from ..workers.easymoney.tasktype import TaskType

from .fundapp_config import settings


def run():
    '''main function'''
    tasks = [Task(code["code"], TaskType.URL_FETCH, {"name": code[
        "name"], "url": settings["baseurl"] + code["code"]}) for code in settings["codelist"]]

    fetcher = FundFetcher()
    parser = FundParser()
    saver = FundSaver()

    tasktypes = {TaskType.URL_FETCH: (fetcher, 1),
                 TaskType.HTM_PARSE: (parser, 1),
                 TaskType.ITEM_SAVE: (saver, 1)}

    engine = Engine(tasktypes, settings)
    engine.run(tasks)
    while True:
        logging.warning("Check status")
        time.sleep(random.randint(0, 5))
        if engine.allFinished():
            break
    logging.warning("Job done")

if __name__ == "__main__":
    run()
