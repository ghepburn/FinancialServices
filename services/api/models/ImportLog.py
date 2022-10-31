from services.api import db

class ImportLog(db.Model):
    __tablename__ = "import_logs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    source_id = db.Column(db.Integer, db.ForeignKey('transaction_sources.id'), nullable=True)
    message = db.Column(db.String(1000), nullable=False)

    def toDict(self):
        dic = {}

        for col in self.__table__.columns:
            dic[col.name] = getattr(self, col.name)

        return dic

