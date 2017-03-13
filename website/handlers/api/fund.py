from tornado import ioloop,web
from ...services.dataservice import DataService

class FundApiHandler(web.RequestHandler):
    def __init__(self):
        web.RequestHandler.__init__(self)
        self.db = DataService()

	def get(self , story_id):
		# story = db.stories.find_one({"_id":ObjectId(str(story_id))})
		# self.set_header("Content-Type", "application/json")
		# self.write(json.dumps((story),default=json_util.default))
        pass
