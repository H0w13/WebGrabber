from handlers.base import BaseHandler

import logging
logger = logging.getLogger('boilerplate.' + __name__)


class FundHandler(BaseHandler):
    def get(self):
        self.render("fund.html")