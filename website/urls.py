from handlers.foo import FooHandler
from handlers.fund import FundHandler
from handlers.api.fund import FundHandler

url_patterns = [
    (r"/foo", FooHandler),
    (r"/fund", FundHandler),
    #api
    (r"/api/fund/(.*)", FundHandler),
]
