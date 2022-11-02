from services.api import db

class TransactionCategory(db.Model):
    __tablename__ = "transaction_categories"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable = False)
    ref_num = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return self.ref_num
    
    def toDict(self):
        dic = {}

        for col in self.__table__.columns:
            dic[col.name] = getattr(self, col.name)

        return dic

