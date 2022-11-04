from services.api import db
from .BaseModel import BaseModel

class TransactionType(BaseModel, db.Model):
    __tablename__ = "transaction_types"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.Text(), nullable=True)
    ref_num = db.Column(db.String(100), nullable=False)

    transactions = db.relationship("Transaction")