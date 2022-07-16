from .BaseController import BaseController

from ..models.TransactionType import TransactionType

class TransactionTypeController(BaseController):
    def __init__(self):
        self.model = TransactionType