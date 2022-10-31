from .BaseController import BaseController

from ..models.TransactionSourceMap import TransactionSourceMap

class TransactionSourceMapController(BaseController):
    def __init__(self, transactionSourceId):
        self.trasactionSourceId = transactionSourceId
        self.model = TransactionSourceMap