import enum

class TaskType(enum.Enum):
    URL_FETCH = "fetcher"
    HTM_PARSE = "parser" 
    ITEM_SAVE = "saver"