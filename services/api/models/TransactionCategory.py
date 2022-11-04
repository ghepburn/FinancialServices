from services.api import db
from .BaseModel import BaseModel

class TransactionCategory(BaseModel, db.Model):
    __tablename__ = "transaction_categories"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable = False)
    ref_num = db.Column(db.String(100), nullable=False)

    transactions = db.relationship("Transaction")

