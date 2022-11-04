from .BaseController import BaseController

from ..models.ImportLog import ImportLog

class LogController(BaseController):
    def __init__(self):
        self.model = ImportLog