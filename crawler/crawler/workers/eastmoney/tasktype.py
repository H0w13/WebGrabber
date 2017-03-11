from ...framework.core.tasktype import TaskType
from .fund_fetcher import FundFetcher
from .fund_parser import FundParser
from .fund_saver import FundSaver

class FundTaskType(object):
    def __init__(self):
        pass

    def getTypes(self):
        types = []
        types.append(TaskType("Fetcher", FundFetcher()))
        types.append(TaskType("Saver", FundSaver()))
        types.append(TaskType("Parser", FundParser()))
        return types
