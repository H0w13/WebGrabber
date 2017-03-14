from handlers.foo import FooHandler
from handlers.fund import FundHandler
from handlers.api.fund import FundApiHandler

url_patterns = [
    (r"/foo", FooHandler),
    (r"/fund", FundHandler),
    (r"/api/fund/(.*)", FundApiHandler),
]
