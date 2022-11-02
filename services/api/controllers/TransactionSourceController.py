from .BaseController import BaseController

from ..models.TransactionSource import TransactionSource

class TransactionSourceController(BaseController):
    def __init__(self):
        self.model = TransactionSource