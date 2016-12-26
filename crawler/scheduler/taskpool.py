import Queue

class TaskPool(object):
    def __init__(self, types):
        self.pool = {}
        for name in types:
            self.pool[name] = Queue.PriorityQueue()
    
    def addTask(self, task):
        self.pool[task.type].put(task)

    def getTask(self, taskType):
        try:
            return self.pool[taskType].get(block=True, timeout=5)
        except Exception as excep:
            return None
    
    def task_done(self, taskType):
        self.pool[taskType].task_done()

    def isAllTaskDone(self):
        isEmpty = True
        for type in self.pool:
            isEmpty = isEmpty and self.pool[type].empty()
        return isEmpty
