from services.api import db
from .BaseModel import BaseModel

class TransactionSource(BaseModel, db.Model):
    __tablename__ = "transaction_sources"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ref_num = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text(), nullable=True)

    transactions = db.relationship("Transaction")