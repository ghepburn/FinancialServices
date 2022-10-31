from services.dataImporter.maps.TransactionMap import TransactionMap
from services.api.models.TransactionType import TransactionType

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # transaction_type_id = db.Column(db.Integer, db.ForeignKey('transaction_types.id'), nullable=False)
    # transaction_category_id = db.Column(db.Integer, db.ForeignKey('transaction_categories.id'), nullable=True)
    # date = db.Column(db.DateTime, nullable=False)
    # amount = db.Column(db.Integer, default=0)
    # source = db.Column(db.String(50), nullable=False)
    # description = db.Column(db.String(100), nullable=False)
    # date_added = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    # date_last_modified = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

class bmoCreditCardTransactionMap(TransactionMap):
        
    def getTransactionType(self):
        amount = self.getTransactionAmount()

        transactionType = "Debit"
        isCredit = amount > 0

        if isCredit:
            transactionType = "Credit"

        return transactionType

    def getTransactionDate(self):
        return self.data[2]

    def getTransactionAmount(self):
        return self.data[4]

    def getTransactionDescription(self):
        return self.data[5]