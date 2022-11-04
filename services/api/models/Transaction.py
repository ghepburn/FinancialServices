from services.api import db

import datetime as dt
from .BaseModel import BaseModel

class Transaction(BaseModel, db.Model):
    __tablename__ = "transactions"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text(), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    date_last_modified = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    type_id = db.Column(db.Integer, db.ForeignKey('transaction_types.id'), nullable=False)
    type = db.relationship('TransactionType', back_populates="transactions")

    category_id = db.Column(db.Integer, db.ForeignKey('transaction_categories.id'), nullable=True)
    category = db.relationship('TransactionCategory', back_populates="transactions")

    source_id = db.Column(db.Integer, db.ForeignKey('transaction_sources.id'), nullable=False)
    source = db.relationship('TransactionSource', back_populates="transactions")

    ref_num = db.Column(db.String, nullable=False)

    def setReferenceNumber(self):
        # transactionRefnum = str(self.type.id) + str(self.source.id) + str(self.date) + str(self.amount)
        # hashedTransactionRefnum = hash(transactionRefnum)

        # self.ref_num = hashedTransactionRefnum
        self.ref_num = self.date