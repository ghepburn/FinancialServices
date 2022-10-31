from services.api import db

class TransactionSourceMap(db.Model):
    __tablename__ = "transaction_source_maps"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    source = db.Column(db.Integer, db.ForeignKey('transaction_sources.id'), nullable=False)
    transaction_date_column = db.Column(db.Integer, default=0)
    transaction_amount_column = db.Column(db.Integer, default=0)
    transaction_type_column = db.Column(db.Integer, default=0)
    transaction_description_column = db.Column(db.Integer, default=0)

    def toDict(self):
        dic = {}

        for col in self.__table__.columns:
            dic[col.name] = getattr(self, col.name)

        return dic

