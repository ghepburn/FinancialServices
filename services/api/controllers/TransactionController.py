import json


from .BaseController import BaseController

from ..models.Transaction import Transaction
from ..models.TransactionType import TransactionType
from ..models.TransactionSource import TransactionSource

class TransactionController(BaseController):
    def __init__(self):
        self.model = Transaction

    def setRefnum(self, data):
        transactionSource = TransactionSource.query.filter_by(id=data["source_id"])
        transactionType = TransactionType.query.filter_by(id=data["type_id"])
        transactionAmount = data["amount"]
        transactionDate = data["date"]

        transactionUniqueIdentifier = transactionSource + transactionType + transactionAmount + transactionDate
        hashedUniqueIdentifier = hash(transactionUniqueIdentifier)
        data["ref_num"] = hashedUniqueIdentifier
        
        return data
