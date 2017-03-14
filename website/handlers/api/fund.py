import json

from bson import json_util

from handlers.api.base import BaseApiHandler


class FundApiHandler(BaseApiHandler):

    def get(self, fundId):
        fund = self.dbService.findItems('fund', {"code": fundId})
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps((fund), default=json_util.default))
        self.finish()
