import datetime as dt

from financialAnalysisApi import db
from financialAnalysisApi.models.TransactionType import TransactionType
from financialAnalysisApi.models.TransactionCategory import TransactionCategory
from financialAnalysisApi.models.Transaction import Transaction 

db.create_all()

transactionType1 = TransactionType(id=1, description="Debit")
transactionType2 = TransactionType(id=2, description="Credit")

transactionCategory1 = TransactionCategory(id=1, name="Restaurants")
transactionCategory2 = TransactionCategory(id=2, name="Grocery")
transactionCategory3 = TransactionCategory(id=3, name="Utillities")
transactionCategory4 = TransactionCategory(id=4, name="Income")

transaction1 = Transaction(id=1, transaction_type_id=1, transaction_category_id=1, date=dt.date(2022, 1, 1), source="BMOCreditCard", description="Restaurant Refund")
transaction2 = Transaction(id=2, transaction_type_id=1, transaction_category_id=4, date=dt.date(2022, 1, 1), source="BMOCreditCard", description="Job Pay")

transaction3 = Transaction(id=3, transaction_type_id=2, transaction_category_id=1, date=dt.date(2022, 1, 1), source="BMOCreditCard", description="KFC Baby")
transaction4 = Transaction(id=4, transaction_type_id=2, transaction_category_id=2, date=dt.date(2022, 1, 1), source="BMOCreditCard", description="NOFrills")

db.session.add(transactionType1)
db.session.add(transactionType2)

db.session.add(transactionCategory1)
db.session.add(transactionCategory2)
db.session.add(transactionCategory3)
db.session.add(transactionCategory4)

db.session.commit()

db.session.add(transaction1)
db.session.add(transaction2)
db.session.add(transaction3)
db.session.add(transaction4)

db.session.commit()

print('TRANSACTIONS')
print(Transaction.query.all())

print("TYPES")
print(TransactionType.query.all())

print('CATEGORIES')
print(TransactionCategory.query.all())