from services.api import db
from .BaseModel import BaseModel

class ImportLog(BaseModel, db.Model):
    __tablename__ = "import_logs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    source_id = db.Column(db.Integer, db.ForeignKey('transaction_sources.id'), nullable=True)
    message = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return __class__ + " - " + self.id
