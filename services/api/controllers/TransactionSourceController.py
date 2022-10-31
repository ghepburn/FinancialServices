from .BaseController import BaseController

from ..models.TransactionSource import TransactionSource

class TransactionTypeController(BaseController):
    def __init__(self):
        self.model = TransactionSource