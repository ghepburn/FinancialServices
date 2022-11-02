from services.api import db

class TransactionSource(db.Model):
    __tablename__ = "transaction_sources"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ref_num = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text(), nullable=True)

    def __repr__(self):
        return self.ref_num

    def toDict(self):
        dic = {}

        for col in self.__table__.columns:
            dic[col.name] = getattr(self, col.name)

        return dic