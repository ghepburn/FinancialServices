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

class bmoChequingsTransactionMap(TransactionMap):
        
    def getTransactionType(self):
        debit = self.data[4]
        credit = self.data[5]

        transactionType = "Debit"
        if credit is not None:
            transactionType = "Credit"

        transactionType = "Debit"

        return transactionType

    def getTransactionDate(self):
        return self.data[0]

    def getTransactionAmount(self):
        debit = self.data[4]
        credit = self.data[5]

        if int(credit) > 0:
            return credit
        else:
            return 0 - int(debit)

    def getTransactionDescription(self):
        return self.data[1]