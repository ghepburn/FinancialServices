import json


from .BaseController import BaseController

from ..models.Transaction import Transaction
from ..models.TransactionType import TransactionType

class TransactionController(BaseController):
    def __init__(self):
        self.model = Transaction

    def getDebitTransactions(self):
        debitTransactionType = TransactionType.query.filter_by(description="Debit").first()
        debitTransactions = Transaction.query.filter_by(transaction_type_id=debitTransactionType.id)
        return self.response(debitTransactions)

    def getCreditTransactions(self):
        creditTransactionType = TransactionType.query.filter_by(description="Credit").first()
        creditTransactions = Transaction.query.filter_by(transaction_type_id=creditTransactionType.id)
        return self.response(creditTransactions)

    def getDebitTransactionsForCategory(self, categoryExternalId):
        debitTransactionType = TransactionType.query.filter_by(description="Debit").first()
        debitTransactions = Transaction.query.filter_by(transaction_type_id=debitTransactionType.id, )
        return self.response(debitTransactions)

    def getCreditTransactionsForCategory(self, categoryExternalId):
        creditTransactionType = TransactionType.query.filter_by(description="Credit").first()
        categoryId = 1

        creditTransactions = Transaction.query.filter_by(transaction_category_id=categoryId)
        return self.response(creditTransactions)


