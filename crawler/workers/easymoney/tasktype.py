from ...core.tasktype import TaskType
from .fund_fetcher import FundFetcher
from .fund_parser import FundParser
from .fund_saver import FundSaver

class FundTaskType(object):
    def __init__(self):
        pass

    def getTypes(self):
        types = []
        types.append(TaskType("Fetcher", FundFetcher.__name__))
        types.append(TaskType("Saver", FundSaver.__name__))
        types.append(TaskType("Parser", FundParser.__name__))
