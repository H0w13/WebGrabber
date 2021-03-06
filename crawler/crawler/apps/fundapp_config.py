# -- coding: utf-8 --
from ..framework.core.settings import settings

settings["baseurl"] = "http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&per=100&code="
settings["codelist"] = [{"code": "486002", "name": "工银全球精选"},
                        {"code": "040046", "name": "华安纳斯达克"},
                        {"code": "270025", "name": "广发行业领先"},
                        {"code": "217010", "name": "招商大盘蓝筹"},
                        {"code": "160505", "name": "博时主题行业"},
                        {"code": "460300", "name": "华泰博瑞沪深３００"},
                        {"code": "160119", "name": "南方中证５００"}]
# settings["codelist"] = [{"code": "486002", "name": "工银全球精选"}]
settings["Fetcher.count"] = 1
settings["Parser.count"] = 1
settings["Saver.count"] = 10
settings["Mongo.server"] = "localhost"
settings["Mongo.port"] = 27017
settings["Mongo.db"] = "eastmoney"
