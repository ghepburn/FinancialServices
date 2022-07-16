from .BaseController import BaseController

from ..models.TransactionCategory import TransactionCategory

class TransactionCategoryController(BaseController):
    def __init__(self):
        self.model = TransactionCategory