from services.api import db

import datetime as dt

class Transaction(db.Model):
    __tablename__ = "transactions"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    transaction_type_id = db.Column(db.Integer, db.ForeignKey('transaction_types.id'), nullable=False)
    transaction_category_id = db.Column(db.Integer, db.ForeignKey('transaction_categories.id'), nullable=True)
    date = db.Column(db.DateTime, nullable=False)
    amount = db.Column(db.Integer, default=0)
    source = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    date_last_modified = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    def toDict(self):
        dic = {}

        for col in self.__table__.columns:
            dic[col.name] = getattr(self, col.name)

        return dic

    @classmethod
    def getColumnsMap(cls):
        columns = cls.__table__.cols
        print(columns)
        return columns

