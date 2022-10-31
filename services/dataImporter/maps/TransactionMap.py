from services.api.models.Transaction import Transaction
from services.api.models.TransactionType import TransactionType
from services.api.models.TransactionCategory import TransactionCategory

# ---- Transaction model columns ----
# id = db.Column(db.Integer, primary_key=True, autoincrement=True)
# transaction_type_id = db.Column(db.Integer, db.ForeignKey('transaction_types.id'), nullable=False)
# transaction_category_id = db.Column(db.Integer, db.ForeignKey('transaction_categories.id'), nullable=True)
# date = db.Column(db.DateTime, nullable=False)
# amount = db.Column(db.Integer, default=0)
# source = db.Column(db.String(50), nullable=False)
# description = db.Column(db.String(100), nullable=False)
# date_added = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
# date_last_modified = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

class TransactionMap:
    
    def __init__(self, data):
        self.data = data

    def getTransactionTypeId(self, transactionType):
        transactionType = TransactionType.query.filter_by(description=transactionType).first()
        transactionTypeId = transactionType.id
        return transactionTypeId

    def getTransactionType(self):
        pass

    def getTransactionCategoryId(self):
        return 1

    def getTransactionDate(self):
        pass

    def getTransactionAmount(self):
        pass

    def getTransactionSource(self):
        return self.data[-1]

    def getTransactionDescription(self):
        pass